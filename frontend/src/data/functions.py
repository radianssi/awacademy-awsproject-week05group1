from config import config
import psycopg2
import datetime

def insert_data():
    print("Welcome to Time Managament Tool!")

    while True:
        start_date = str(input("Enter start day (format: DD.MM.YYYY): "))
        try:
            if datetime.datetime.strptime(start_date, '%d.%m.%Y'):
                break
        except ValueError:
            print("Invalid date format, try again!")
            continue
    
    while True:
        start_time = str(input("Enter start time (format: HH.MM): "))
        try:
            if datetime.datetime.strptime(start_time, '%M.%S'):
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
            if datetime.datetime.strptime(end_time, '%M.%S'):
                if datetime.datetime.strptime(start_date, '%d.%m.%Y') == datetime.datetime.strptime(end_date, '%d.%m.%Y'):
                    if datetime.datetime.strptime(start_time, '%M.%S') < datetime.datetime.strptime(end_time, '%M.%S'):
                        break
                    else:
                        print("End time can't be earlier or same as start time, try again!")
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



    # date = "08.11.2022"
    # y = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # date2 = datetime.strptime(date, "%d.%m.%Y")
    # print(date2)

def push_data_to_database(start_time, end_time, project, project_desc):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = """
        INSERT INTO timetable (start_time, end_time, project, project_desc)
        VALUES (%s, %s, %s, %s);
        UPDATE 'timetable SET work_hours = %s -%s;
        """
        cursor.execute(SQL, (start_time, end_time, project, project_desc, end_time, start_time))
        con.commit()
        cursor.close()
        print("done")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()