# Clock Your Work!
This is a "simple" tool to record your work tasks to PostgreSQL database in AWS RDS. You can also get email report for example daily.

# Architecture

![Architecture](https://i.imgur.com/Hjbybrg.png)

## How to use
* 1 Create virtual enviroment (Python 3.11 doesn't work atm) and install dependencies
```bash
py -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
* 2 Create your own VPC and networking infra to AWS with backend/cloudformation.yaml. You need to install AWS CLI before this. Run command in backend folder:
```bash
aws cloudformation deploy --template-file ./cloudformation.yaml --stack-name timemanagament-vpcstack
```

* 3 Create AWS RDS PostgreSQL 13.7 database with public internet access to your created VPC

* 4 Connect to database with command line and run commands from backend/database.sql

* 5 Create database.ini in frontend/src/data folder and fill values
```bash
[postgresql]
host= #AWS RDS public endpoint here
database=timemanagement
port=5432
user= #your username
password= #your password
```

* 6 Run main.py file from frontend/src/data folder
```bash
py main.py
```

* 7 (Optional) Get automatic reports via email. You need to setup your email to AWS SES. Next set up AWS Lambda with psycopg2.zip (pack psycopg2 folder files) and upload get_worked_hours.py + send_mail.py files to Lambda. You also have to upload database.ini with same information as in phase 5. Setup AWS EventBridge to schedule Lambda to run for example once per day.