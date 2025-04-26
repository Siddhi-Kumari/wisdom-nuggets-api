<<<<<<< HEAD
# Wisdom Nuggets API

The **Wisdom Nuggets API** is a simple Flask application to create, fetch, and delete inspirational quotes ("nuggets"). Built for a backend development assessment to demonstrate API design and basic database operations.

For a full project description, visit the [GitHub repository](https://github.com/your-repo-url).
=======
🧠 Wisdom Nuggets API
A simple Flask-based RESTful API to manage and serve "Wisdom Nuggets" — inspirational quotes — built for the SuperMorpheus assessment.

📋 Project Overview
This backend service allows users to:
>>>>>>> ceefa6adbda561da5ab9412a4e5f91c39efecb55

Retrieve all wisdom nuggets

<<<<<<< HEAD
## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
- [Troubleshooting](#troubleshooting)
- [Maintainers](#maintainers)
=======
Get a random nugget

Add a new nugget
>>>>>>> ceefa6adbda561da5ab9412a4e5f91c39efecb55

Delete a nugget

<<<<<<< HEAD
## Requirements

- Python 3.8+
- Flask
- SQLAlchemy

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url.git
   cd wisdom-nuggets-api

## Setup Instructions

### 1. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
# OR
source venv/bin/activate  # For Mac/Linux

2. Install dependencies:

 pip install -r requirements.txt


3. Run the application:
 python run.py
=======
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
>>>>>>> ceefa6adbda561da5ab9412a4e5f91c39efecb55
