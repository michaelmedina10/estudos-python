from dataclasses import dataclass

import oracledb

import pandas as pd


@dataclass
class OracleDBConnection:
    user: str
    passw: str
    dsn: str
    connection = None
    cursor = None

    def __enter__(self):
        self.connect()
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def connect(self):
        """
        Start connection with database
        :return None
        """
        try:
            self.connection = oracledb.connect(
                user=self.user, password=self.passw, dsn=self.dsn
            )
        except oracledb.DatabaseError as e:
            print(f"Database error: {e}")
            raise

    def execute_fetch(self, query: str) -> pd.DataFrame | None:
        """
        Execute select query.

        :param query: str

        :return pandas.DataFrame to success or None to Fail
        """

        try:
            self.cursor.execute(query)
            columns = [col[0] for col in self.cursor.description]
            rows = self.cursor.fetchall()
            data = [dict(zip(columns, row)) for row in rows]
            df = pd.DataFrame(data)
            return df
        except oracledb.DatabaseError as e:
            print(f"Error to execute query: {e}")
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
        except oracledb.DatabaseError as e:
            print(f"DML Error: {e}")
            return False
            return False
