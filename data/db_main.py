import psycopg2
from config import host, user, password, db

class DBWorker:
    def __init__(self):
        self.connection = psycopg2.connect(host=host, user=user, password=password, database=db)

    # Template
    def template(self):
        with self.connection.cursor() as cursor:
            cursor.execute('something')