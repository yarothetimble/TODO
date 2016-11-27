#todo

Simple web application for managing user tasks

## Installation
Tested on Linux machine (Debian 8)    

Required packages:  
python 3.4 or higher  
postgresql (tested on version 9.4)  
django (tested on version 1.10)  
python3-psycopg2

After installing the above packages, make sure, the postgressql service is running on your local machine.  
Run script from the project directory 'create_db.sql' via postgres shell command (please make sure you have the right permissions for doing so):  
psql -d template1 < create_db.sql  
or as root:  
sudo -u postgres psql -d template1 < create_db.sql

Run these commands from the project directory:  
python3 manage.py migrate  
python3 manage.py runserver

Run your app by typing this url in your web browser:
http://127.0.0.1:8000/tasks/

Good to go!

## License

MIT
