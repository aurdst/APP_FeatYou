FEAT YOU is an application of courses online, courses of coaching about fitness, yoga, running and more.

This application is a school project.

Praticipant : 

- Lep Alexandre : Web Marketing
- Catieau Naomi : Web Marketing
- Tuybens Valentin : Web 
- Delhaye Zoé : Web Designer
- Destailleur Aurélien : Web Développer

#14 march 2022
Start of developpement, the application run on FastApi with alembic for configuration of the database.

# Alembic 

To create project with alembic use :

- pip install alembic

now run : 

- alembic init alembic
- alemebic revivion --autogenerate -m "text here"
- alembic upgrade head

config : 

Bdd : postgresql://user:pass@127.0.0.1:5432/dbname

# Backend (Python / FastAPI):

# Delete existing env folder or add it in .gitignore file 

1 - to execute in terminal : 
    # Create your environement :
        -> python -m venv env
    # Access to env : 
        -> env\Scripts\activate 

    pip install fastapi uvicorn[standard] pydantic sqlalchemy fastapi-utils mysqlclient pymysql sqlalchemy

2 - start API :
    python -m uvicorn main:app --reload

# from sqlalchemy.exc import SQLAlchemyError

# Create requirements dependencies file
pip install pip-upgrader
pip freeze > requirements.txt

# Update requirements.txt
pip install pip-upgrader
pip-upgrade ./requirements.txt

# For start project in the new colaborator machine's
pip install -r requirements.txt

# For db
pip install databases
# For sqlite
pip install databases[sqlite]
# For mysql
pip install pymysql

# Alembic
pip install alembic 
alembic init alembic

# Feature to fix : System of mailing 

Into the file send_mail.py, the conf doesn't work because he can find the datas into the .env, i don't know why i have try : 

from dotenv import dotenv_values

credentials = dotenv_values(".env")

SMTP_MAIL = credentials['MAIL']


# Frontend (JavaScript / VueJS Vuetify) :

For run front project :

- npm install
- npm run serve

or 

- yarn install 
- yarn run serve