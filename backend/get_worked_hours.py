import psycopg2
from config import config
import json




con = psycopg2.connect(**config())

def get_db():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = '''select * from timetable where start_time > (now() - interval '24 hours');'''
        SQL2 = '''select date(start_time), sum(work_hours) as hours_worked from timetable group by date(start_time) order by date(start_time) desc limit 1;'''
        cursor.execute(SQL)
        response = cursor.fetchall()
        data = json.dumps(response, default = str)
        cursor.execute(SQL2)
        response = cursor.fetchall()
        data2 = json.dumps(response, default = str)
        return [data, data2]
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()


if __name__ == '__main__':
    get_db()

