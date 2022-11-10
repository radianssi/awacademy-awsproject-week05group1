# Clock Your Work!
This is a "simple" tool to record your work tasks to PostgreSQL database in AWS RDS. You can also get email report for example daily.

# Architecture

![Architecture](https://imgur.com/a/ZcFV77Y)

## How to use
* 1. Create virtual enviroment (Python 3.11 doesn't work atm) and install dependencies
```bash
py -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
* 2. Creat your own VPC and networking infra to AWS with backend/cloudformation.yaml. You need to install AWS CLI before this. Run command in backend folder:
```bash
aws cloudformation deploy --template-file ./cloudformation.yaml --stack-name timemanagament-vpcstack
```

* 3. Create AWS RDS PostgreSQL 13.7 database with public internet access to your created VPC

* 4. Connect to database with command line and run commands from backend/database.sql

* 5. Create database.ini in frontend/src/data folder and fill values
```bash
[postgresql]
host= #AWS RDS public endpoint here
database=timemanagement
port=5432
user= #your username
password= #your password
```

* 6. Run main.py file from frontend/src/data folder
```bash
py main.py
```

* 7. (Optional) Get automatic reports via email. 