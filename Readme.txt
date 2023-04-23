Flask To-Do List Project
This project is a web application developed with Flask, which uses various Flask extensions, including Flask-Login, Flask-WTF, Flask-MySQL .

The app is a to-do list system, where each user can create and manage their own personal to-do list. The system also includes a user authentication system and the ability to remove users from the database.

Setting:
To run this project, you must first install the required dependencies, which are found in the requirements.txt file. You can install them using the following command:

Then you need to configure the MySQL database in the config.py file. You can modify the database configuration in this file.


Features:
authentication system
The application includes a user authentication system. Users can sign in or create a new account if they don't have one. Authentication is done using the Flask-Login extension.

User creation:
Users can create a new account in the app. User information is stored in the MySQL database using the Flask-MySQL extension.

Things to do:
Each user has their own to-do list. When a user logs in, they are redirected to their personal task list. Users can create new tasks, edit existing tasks, and delete tasks. The task list is stored in the MySQL database using the Flask-MySQL extension.

User removal:
Users can remove their account from the app. When you delete an account, all tasks associated with the account are also deleted.


Install necessary packages in the detailed versions, they are in requirements.txt

>> pip install -r requirements.txt
