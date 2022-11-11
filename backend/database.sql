CREATE DATABASE timemanagement;

CREATE TABLE timetable
(id SERIAL PRIMARY KEY,
start_time TIMESTAMP NOT NULL,
end_time TIMESTAMP NOT NULL,
work_hours INTERVAL,
project VARCHAR(255) NOT NULL,
project_desc VARCHAR (255) NOT NULL
);