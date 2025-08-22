import psycopg2
from psycopg2.extras import DictCursor #Use select data like dict
from dotenv import load_dotenv
import os

load_dotenv()
connection = psycopg2.connect(
    host=os.getenv('POSTGRES_HOST'),
    port=os.getenv('POSTGRES_PORT'),
    database=os.getenv('POSTGRES_DB'),
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD')
)

if connection:
    print("Connected to PostgreSQL")

#Access to change DB
connection.autocommit = True

cursor = connection.cursor(cursor_factory=DictCursor)
cursor.execute(
    """select c.company_name, c.status, s.service_name
        from companies c 
        join services s
        on s.company_id = c.company_id
        where c.status in (1, 2);"""
)
companies = cursor.fetchall()

for company in companies:
    print(f'Company {company["company_name"]} has service {company["service_name"]}')

#Close connection
cursor.close()
connection.close()
print("Connection closed")