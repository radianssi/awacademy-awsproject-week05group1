from config import config
import psycopg2
import datetime

def insert_data():

    #Asks user to input start and end dates and times and validates them.
    
    while True:
        start_date = str(input("Enter start day (format: DD.MM.YYYY): "))
        try:
            if datetime.datetime.strptime(start_date, '%d.%m.%Y'):
                if datetime.datetime.strptime(start_date, '%d.%m.%Y') < datetime.datetime.now():
                    break
                else:
                    print("Start date can't be in the future!")
                    
        except ValueError:
            print("Invalid date format, try again!")
            continue
    
    while True:
        start_time = str(input("Enter start time (format: HH.MM): "))
        try:
            if datetime.datetime.strptime(start_time, '%H.%M'):
                break
        except ValueError:
            print("Invalid time format, try again!")
            continue

    while True:
        end_date = str(input("Enter end day (format: DD.MM.YYYY): "))
        try:
            if datetime.datetime.strptime(end_date, '%d.%m.%Y'):
                if datetime.datetime.strptime(start_date, '%d.%m.%Y') <= datetime.datetime.strptime(end_date, '%d.%m.%Y'):
                    break
                else:
                    print("End date can't be before start date, try again!")
                    continue
        except ValueError:
            print("Invalid date format, try again!")
            continue
    
    while True:
        end_time = str(input("Enter end time (format: HH.MM): "))
        try:
            if datetime.datetime.strptime(end_time, '%H.%M'):
                if datetime.datetime.strptime(start_date, '%d.%m.%Y') == datetime.datetime.strptime(end_date, '%d.%m.%Y'):
                    if datetime.datetime.strptime(start_time, '%H.%M') < datetime.datetime.strptime(end_time, '%H.%M'):
                        break
                    else:
                        print("End time can't be earlier or same as start time, try again!")
                else:
                    break
        except ValueError:
            print("Invalid time format, try again!")
            continue
    
    while True:
        project_name = str(input("Give name of the project: "))
        if project_name == "":
            print("Project name can't be empty, try again!")
            continue
        break

    while True:
        project_desc = str(input("Give description of the project: "))
        if project_desc == "":
            print("Project description can't be empty, try again!")
            continue
        break
    
    # Combine date and time and convert it to a datetime. Also validates they are legit.
    try:
        start_datetime = datetime.datetime.strptime(start_date + "." + start_time, '%d.%m.%Y.%H.%M')
    except ValueError:
        print("Something went wrong when creating start_datetime.")
    try:
        end_datetime = datetime.datetime.strptime(end_date + "." + end_time, '%d.%m.%Y.%H.%M')
    except ValueError:
        print("Something went wrong when creating end_datetime.")

    # Return values
    return (start_datetime, end_datetime, project_name, project_desc)

def push_data_to_database(start_time, end_time, project, project_desc):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = "INSERT INTO timetable (start_time, end_time, project, project_desc) VALUES (%s, %s, %s, %s) RETURNING id;"
        cursor.execute(SQL, (start_time, end_time, project, project_desc))
        id = cursor.fetchone()

        SQL2 = "UPDATE timetable SET work_hours = end_time - start_time WHERE id = %s;"
        cursor.execute(SQL2, (id,))
        con.commit()
        cursor.close()
        print("Information uploaded to database")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()