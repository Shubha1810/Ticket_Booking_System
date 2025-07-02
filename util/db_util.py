import mysql.connector


class DBUtil:
    @staticmethod
    def get_db_conn():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Shubha@2003",
            database="ticketbookingsystem"
        )
