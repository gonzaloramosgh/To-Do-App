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



/////// VERSION EN ESPAÑOL   ////////////////////////


Proyecto Flask To-Do List
Este proyecto es una aplicación web desarrollada con Flask, que utiliza varias extensiones de Flask, incluyendo Flask-Login, Flask-WTF, Flask-MySQL .

La aplicación es un sistema de lista de tareas por hacer, donde cada usuario puede crear y administrar su propia lista personal de tareas. El sistema también incluye un sistema de autenticación de usuarios y la capacidad de eliminar usuarios de la base de datos.

Configuración:
Para ejecutar este proyecto, primero debe instalar las dependencias requeridas, que se encuentran en el archivo requirements.txt. Puede instalarlos usando el siguiente comando:

Luego, debe configurar la base de datos MySQL en el archivo config.py. Puede modificar la configuración de la base de datos en este archivo.


Funcionalidades:
Sistema de autenticación
La aplicación incluye un sistema de autenticación de usuarios. Los usuarios pueden iniciar sesión o crear una nueva cuenta si no tienen una. La autenticación se realiza utilizando la extensión Flask-Login.

Creación de usuarios:
Los usuarios pueden crear una nueva cuenta en la aplicación. La información del usuario se almacena en la base de datos MySQL utilizando la extensión Flask-MySQL.

Lista de tareas:
Cada usuario tiene su propia lista de tareas por hacer. Cuando un usuario inicia sesión, se le redirige a su lista de tareas personal. Los usuarios pueden crear nuevas tareas, editar tareas existentes y eliminar tareas. La lista de tareas se almacena en la base de datos MySQL utilizando la extensión Flask-MySQL.

Eliminación de usuarios:
Los usuarios pueden eliminar su cuenta de la aplicación. Al eliminar una cuenta, también se eliminan todas las tareas asociadas con la cuenta.


Las librerias necesarias para ejecutar correctamente la app se encuentran en requirements.txt
Instalarlas ejecutando el siguiente comando.

>> pip install -r requirements.txt


