from dataclasses import dataclass

import oracledb
import pandas as pd
from settings.logs import logger


@dataclass
class OracleDBConnection:
    user: str
    poracle: str
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
                user=self.user, password=self.poracle, dsn=self.dsn
            )
            logger.info("Connection with Oracle Succeeded")
        except oracledb.DatabaseError as e:
            logger.critical(f"Error to connect with Oracle: {e}")
            raise

    def execute_fetch(self, query: str) -> pd.DataFrame:
        """
        Execute select query.

        Args:
          query str: query to execute in database

        returns:
            pandas.DataFrame, DataFrame must be empty in case of Failure

        """

        try:
            self.cursor.execute(query)
            columns = [col[0] for col in self.cursor.description]
            rows = self.cursor.fetchall()
            data = [dict(zip(columns, row)) for row in rows]
            df = pd.DataFrame(data)
            return df
        except oracledb.DatabaseError as e:
            logger.critical(f"Error to execute query: {e}")
            return pd.DataFrame()

    def execute_dml(self, query: str, data: dict | list = None) -> bool:
        """
        Execute operations of type 'insert', 'update' and 'delete'

        Args:
            query str: Query to execute in database
            data dict | list: Optional parameters to use in the query

        Returns:
            bool 1 to success 0 to Fail
        """
        try:
            if data is not None:
                self.cursor.execute(query, data)
            else:
                self.cursor.execute(query)

            self.connection.commit()
            return True
        except oracledb.DatabaseError as e:
            logger.critical(f"DML Error: {e}")
            return False
