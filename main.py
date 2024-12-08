from fastapi import FastAPI,Depends,Body,WebSocket, WebSocketDisconnect
from db import engine
from models import users as models
from auth import user as auth_router
from fastapi.middleware.cors import CORSMiddleware
from Schemas.users import CreateUserSchema, UserSchema
from sqlalchemy.orm import Session
from db import get_db
from models import users as user_model
from Manager import data as managers
from services.db.user import create_user
from fastapi.responses import HTMLResponse

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, change to specific origins in production
    allow_credentials=True,  # Allows cookies to be included
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
app.include_router(managers.router, prefix="/manager", tags=["manager"])
app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])

connections = []
sms_data = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)
    try:
        while True:
            # Wait for a response from the Android client
            data = await websocket.receive_text()
            sms_data.append(data)

            print(f"Received from client: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")
        connections.remove(websocket)


@app.get("/")
async def home():
    return HTMLResponse(
        """
        <html>
            <head>
                <title>SMS Viewer</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 20px;
                        line-height: 1.6;
                    }
                    table {
                        border-collapse: collapse;
                        width: 100%;
                        margin-top: 20px;
                    }
                    th, td {
                        border: 1px solid #ddd;
                        padding: 8px;
                        text-align: left;
                    }
                    th {
                        background-color: #f4f4f4;
                    }
                    tr:nth-child(even) {
                        background-color: #f9f9f9;
                    }
                    tr:hover {
                        background-color: #f1f1f1;
                    }
                    button {
                        padding: 10px 20px;
                        margin: 10px;
                        font-size: 16px;
                        cursor: pointer;
                        background-color: #4CAF50;
                        color: white;
                        border: none;
                        border-radius: 5px;
                    }
                    button:hover {
                        background-color: #45a049;
                    }
                </style>
            </head>
            <body>
                <h1>SMS Viewer</h1>
                <p>Real-time view of SMS messages sent from the Android app.</p>

                <!-- Buttons for HTTP Requests -->
                <button onclick="sendMessage()">Send Message</button>
                <button onclick="fetchSMSData()">Fetch SMS Data</button>

                <table id="smsTable">
                    <thead>
                        <tr>
                            <th>Sender</th>
                            <th>Message</th>
                            <th>Date</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- SMS data will be injected here -->
                    </tbody>
                </table>

                <script>
                 

                    // Function to send message
                    function sendMessage() {
                        fetch('http://127.0.0.1:8000/send-message/?message=ss', {
                            method: 'GET',
                        })
                        .then(response => response.json())
                        .then(data => {
                            console.log('Message sent:', data);
                        })
                        .catch(error => {
                            console.error('Error sending message:', error);
                        });
                    }

                    // Function to fetch SMS data
                   function fetchSMSData() {
    fetch('http://127.0.0.1:8000/sms', {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        console.log('SMS Data:', data);
        // Parse the SMS data from the array of strings
        const smsData = JSON.parse(data.sms[0]); // Assuming 'sms' is an array with one stringified object
        const tableBody = document.getElementById("smsTable").querySelector("tbody");

        // Clear the table
        tableBody.innerHTML = "";

        // Populate the table with fetched data
        for (const [sender, messages] of Object.entries(smsData)) {
            messages.forEach(message => {
                const row = document.createElement("tr");

                const senderCell = document.createElement("td");
                senderCell.textContent = sender;

                const bodyCell = document.createElement("td");
                bodyCell.textContent = message.body;

                const dateCell = document.createElement("td");
                dateCell.textContent = new Date(message.date).toLocaleString();

                row.appendChild(senderCell);
                row.appendChild(bodyCell);
                row.appendChild(dateCell);

                tableBody.appendChild(row);
            });
        }
    })
    .catch(error => {
        console.error('Error fetching SMS data:', error);
    });
}

                </script>
            </body>
        </html>
        """
    )




@app.post("/send-message/")
async def send_message(message: str):
    # Broadcast a message to all connected clients
    for connection in connections:
        await connection.send_text(message)
    return {"message": "Message sent to all clients"}


@app.get("/sms")
def get_sms():
    """
    HTTP endpoint to fetch the SMS data.
    """
    return {"sms": sms_data}

