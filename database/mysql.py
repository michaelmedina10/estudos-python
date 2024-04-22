from dataclasses import dataclass

import mysql.connector
import pandas as pd


@dataclass
class MySqlConnection:
    host: str
    user: str
    password: str
    database: str
    port: int = 3306
    connection = None
    cursor = None

    def __enter__(self):
        self.connect()
        self.cursor = self.connection.cursor(dictionary=True)

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.connection.is_connected():
            self.connection.close()

    def connect(self):
        """
        Start connection with database
        :return None
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.database,
            )
            print("Connection Succeeded")
        except mysql.connector.Error as e:
            print(f"Error to connect: {e}")

    def execute_fetch(self, query: str) -> pd.DataFrame | None:
        """
        Execute select query.

        :param query: str

        :return pandas.DataFrame to success or None to Fail
        """
        try:
            self.cursor.execute(query)
            columns = self.cursor.column_names
            rows = self.cursor.fetchall()
            df = pd.DataFrame(rows, columns=columns)
            return df
        except mysql.connector.Error as e:
            print(f"Error to fetch: {e}")
            return None

    def execute_dml(self, query: str, data: dict | list) -> bool:
        """
        Execute operations of type 'insert', 'update' and 'delete'

        :param query: str
        :param data: dict | list

        :return bool 1 to success 0 to Fail
        """
        try:
            if data:
                self.cursor.execute(query, data)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return True
        except mysql.connector.Error as e:
            print(f"DML Error: {e}")
            return False
