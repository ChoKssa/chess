
# Server Startup Guide

**Chess.OO Startup Guide**

## Prerequisites

Before starting, ensure you have Python installed and the required dependencies. Run the following command in your terminal to install them:

```bash
pip install -r requirements.txt
```

## Steps to Launch the Server

1. **Create Migrations for the Database**

   Run this command to create migration files for the database schema:

   ```bash
   python manage.py makemigrations
   ```

2. **Apply the Migrations**

   Apply the migrations to set up your database:

   ```bash
   python manage.py migrate
   ```

3. **Run the Webserver**

   Start the server with the following command:

   ```bash
   python manage.py runserver
   ```

4. **Run the WebSocket Server**

    Start the server with the following command:

   ```bash
   daphne a_core.asgi:application -p 8001
   ```

5. **Create Your Account**

   Open your browser and visit this URL to create your account:

   [http://127.0.0.1:8000/signup/](http://127.0.0.1:8000/signup/)

6. **Access the Game**

   Once signed up, you can access the game here:

   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

