1.	Start Your Backend Server
Make sure your backend is running:
node index.js
If it's set up correctly, it should say:
Server running on port 5000
MongoDB connected

2. Use Postman to Test the Backend
BASE URL:
http://localhost:5000/api

Step 1: Register a New User (Admin or User)
POST /auth/register
In Postman:
•	Method: POST
•	URL: http://localhost:5000/api/auth/register
•	Body: Select raw > JSON:
{
  "email": "admin@example.com",
  "password": "admin123",
  "role": "admin"
}
Press Send
You should see:
{ "message": "User created" }
Step 2: Login
POST /auth/login
•	URL: http://localhost:5000/api/auth/login
•	Body (JSON):
{
  "email": "admin@example.com",
  "password": "admin123"
}
Press Send
You’ll get:
{ "token": "xxx.yyy.zzz", "role": "admin" }
Copy this token – you’ll use it for protected requests.

Step 3: Upload a Flight (with Logo)
POST /flights (admin only)
•	URL: http://localhost:5000/api/flights
•	Method: POST
•	Authorization tab:
o	Type: Bearer Token
o	Paste the token you got from login
 
•	Body: form-data (not raw):
o	flightNumber: ABC123
o	departure: New York
o	arrival: London
o	time: 2025-05-10 15:00
o	logo: (type = File, choose an image)
 
press Send
Response should return the new flight object with logo path.

Step 4: Get All Flights (Public Route)
GET /flights
•	URL: http://localhost:5000/api/flights
•	Method: GET
No token needed Returns list of flights with their details and logo URLs.
 

Step 5: Edit a Flight
PUT /flights/:id
•	First, copy a flight _id from /flights response.
•	URL: http://localhost:5000/api/flights/<flight_id>
•	Method: PUT
•	Authorization: Bearer Token (admin)
•	Body: form-data
o	Only include fields you want to change (e.g. new departure)
o	Include logo only if you're uploading a new one
Hit Send, flight gets updated.

Step 6: Delete a Flight
DELETE /flights/:id
•	URL: http://localhost:5000/api/flights/<flight_id>
•	Method: DELETE
•	Authorization: Bearer Token (admin)
Flight will be deleted.

