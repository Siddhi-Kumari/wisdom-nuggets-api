🧠 Wisdom Nuggets API
A simple Flask-based RESTful API to manage and serve "Wisdom Nuggets" — inspirational quotes — built for the SuperMorpheus assessment.

📋 Project Overview
This backend service allows users to:

Retrieve all wisdom nuggets

Get a random nugget

Add a new nugget

Delete a nugget

The application uses Flask for the backend and SQLite for database storage.

⚙️ Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/Siddhi-Kumari/wisdom-nuggets-api.git
cd wisdom-nuggets-api
2. Create a virtual environment
bash
Copy
Edit
python -m venv venv
3. Activate the environment
On Windows:

bash
Copy
Edit
venv\Scripts\activate
On Mac/Linux:

bash
Copy
Edit
source venv/bin/activate
4. Install project dependencies
bash
Copy
Edit
pip install -r requirements.txt
5. Run the application
bash
Copy
Edit
python run.py
➡️ The server will start running at: http://127.0.0.1:5000

🗃️ Database Setup
No manual database setup is required.

When the app runs for the first time, an SQLite database nuggets.db is automatically created.

You can populate it by using the API to add new nuggets.

🌐 Available API Endpoints

Method	URL	Description
GET	/nuggets	Get all wisdom nuggets
GET	/nuggets/random	Get a random wisdom nugget
POST	/nuggets	Add a new wisdom nugget
DELETE	/nuggets/<id>	Delete a wisdom nugget by ID
📬 Example Usage (via curl)
Fetch all nuggets
bash
Copy
Edit
curl http://127.0.0.1:5000/nuggets
Fetch a random nugget
bash
Copy
Edit
curl http://127.0.0.1:5000/nuggets/random
Add a new nugget
bash
Copy
Edit
curl -X POST http://127.0.0.1:5000/nuggets \
-H "Content-Type: application/json" \
-d '{"text": "Success is not final; failure is not fatal: It is the courage to continue that counts.", "author": "Winston Churchill"}'
Delete a nugget
bash
Copy
Edit
curl -X DELETE http://127.0.0.1:5000/nuggets/1
📂 Project Structure
arduino
Copy
Edit
wisdom-nuggets-api/
├── wisdom_nuggets/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── model.py
│   │   ├── routes.py
│   ├── config.py
├── run.py
├── requirements.txt
├── README.md
🛠️ Tech Stack
Python 3.10+

Flask

Flask-SQLAlchemy

SQLite
