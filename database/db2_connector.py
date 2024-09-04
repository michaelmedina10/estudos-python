from dataclasses import dataclass

import ibm_db
import pandas as pd
from ibm_db_dbi import Connection, OperationalError
from settings.logs import logger


@dataclass
class Db2Connection:
    conn_str: str
    connection = None
    db_api_connection = None

    def __enter__(self):
        try:
            self.connection = ibm_db.connect(self.conn_str, "", "")
            self.db_api_connection = Connection(self.connection)
            logger.info("Connection with DB2 Succeeded")
            return self
        except OperationalError as e:
            logger.critical(f"Error to connect with DB2: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if self.db_api_connection:
            self.db_api_connection.close()

    def execute_fetch(self, query: str) -> pd.DataFrame:
        """
        Execute select query.

        Args:
          query str: query to execute in database

        returns:
            pandas.DataFrame, DataFrame must be empty in case of Failure

        """

        try:
            df = pd.read_sql(query, self.db_api_connection)
            return df
        except (Exception, OperationalError) as e:
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
            with self.db_api_connection.cursor() as cursor:
                if data is not None:
                    cursor.execute(query, data)
                else:
                    cursor.execute(query)
                self.db_api_connection.commit()
                return True
        except (Exception, OperationalError) as e:
            logger.critical(f"DML Error: {e}")
            return False
