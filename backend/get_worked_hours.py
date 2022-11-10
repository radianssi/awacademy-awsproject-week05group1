import psycopg2
from config import config
import pandas as pd




def read_db():
    con = None
    SQL = 'select date(start_time), sum(work_hours) as hours_worked from timetable group by date(start_time) order by date(start_time) desc LIMIT 1;'
    try:
        con = psycopg2.connect(**config())
        dataframe = pd.read_sql(SQL, con)   
        print(dataframe)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()




def get_worked_hours():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = 'select date(start_time), sum(work_hours) as hours_worked from timetable group by date(start_time) order by date(start_time) desc limit 1;'
        cursor.execute(SQL)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()


if __name__ == '__main__':
    read_db()

