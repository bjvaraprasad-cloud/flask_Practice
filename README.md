# Student Registration System

A simple **Flask** web application to manage student records with **MongoDB** as the backend database. Users can **add, view, update, and delete** student details.

---

## Features

* List all students on the home page
* Add a new student
* Update existing student details
* Delete a student with confirmation
* Simple and responsive UI using Bootstrap

---

## Tech Stack

* **Backend:** Python, Flask
* **Database:** MongoDB (via Flask-PyMongo)
* **Frontend:** HTML, Jinja2 templates, Bootstrap 5
* **Environment Variables:** Managed via `.env` file

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/bjvaraprasad-cloud/flask_Practice.git
Cloning into 'flask_Practice'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (3/3), done.

<img width="940" height="173" alt="image" src="https://github.com/user-attachments/assets/4223c701-3c87-4d52-82db-7a558982a0c1" />

<img width="940" height="718" alt="image" src="https://github.com/user-attachments/assets/411d3550-4b65-4728-b14c-a5a66e6c3638" />



### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Activate venv
# Windows:
venv\Scripts\activate
# Linux / Mac:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt` example:**

```
Flask
Flask-PyMongo
python-dotenv
bson
```
<img width="864" height="364" alt="image" src="https://github.com/user-attachments/assets/aa00051a-19cc-444c-953f-eab1be2b948b" />
<img width="940" height="410" alt="image" src="https://github.com/user-attachments/assets/e32626cf-ca99-453b-aada-8010d1c2f571" />

<img width="940" height="716" alt="image" src="https://github.com/user-attachments/assets/afb050ba-ccc4-4265-9522-1e6789a9c549" />

### 4. Configure environment variables

Create a `.env` file in the project root:

```
MONGO_URI=mongodb+srv://bjvaraprasad_db_user:*******@vara.axctbzu.mongodb.net/?appName=vara
SECRET_KEY=******
```

### 5. Run the application

```bash
python app.py
```

Open your browser at: [http://localhost:8000](http://localhost:8000)

---

## Project Structure

```
project/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_student.html
│   ├── update_student.html
│
├── app.py
├── requirements.txt
└── .env
```

---

## Screenshots

**Home Page**
Lists all students with Edit/Delete buttons.
- <img width="1902" height="607" alt="image" src="https://github.com/user-attachments/assets/a58a6a6d-4978-4769-8074-232e4d31e69d" />


**Add Student**
Form to add a new student.
- <img width="1897" height="801" alt="image" src="https://github.com/user-attachments/assets/d65d25c3-ebb5-410a-adb1-e130ad7c5878" />


**Update Student**
Form pre-filled with student details.
- <img width="1905" height="897" alt="image" src="https://github.com/user-attachments/assets/04febf01-879f-431f-ab07-abcfb993acf1" />


<img width="611" height="263" alt="image" src="https://github.com/user-attachments/assets/5b95a07e-32bb-4003-b65d-3cd129ca2768" />


<img width="634" height="282" alt="image" src="https://github.com/user-attachments/assets/ad3c465f-48dd-49f1-be56-bfd7f3fb8414" />

---

## Notes

* Make sure MongoDB is running and accessible via the URI in `.env`
* Delete action includes a confirmation page to prevent accidental deletion
* Uses `ObjectId` from `bson` to work with MongoDB document IDs
* If you use MongoDB Atlas on macOS, install dependencies again (`pip install -r requirements.txt`). This project now uses `certifi` CA bundle explicitly to avoid common TLS certificate verification failures with `pymongo`.

---

## License

MIT License

---



