from dataclasses import dataclass

import ibm_db
from ibm_db_dbi import OperationalError

# Logger desenvolvido a partir da lib logging do python
from settings.logs import logger

import pandas as pd


@dataclass
class Db2Connection:
    conn_str: str
    connection = None
    cursor = None

    def __enter__(self):
        try:
            self.connection = ibm_db.connect(self.conn_str, "", "")
            logger.info("Connection with DB2 Succeeded")
            return self
        except OperationalError as e:
            logger.critical(f"Error to connect with DB2: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            ibm_db.close(self.connection)

    def execute_fetch(self, query: str) -> pd.DataFrame:
        """
        Execute select query.

        Args:
          query str: query to execute in database

        returns:
            pandas.DataFrame, DataFrame must be empty in case of Failure

        """

        try:
            stmt = ibm_db.exec_immediate(self.connection, query)
            columns = [column_name for column_name in ibm_db.fetch_assoc(stmt).keys()]
            rows = []
            row = ibm_db.fetch_assoc(stmt)  # return first line

            while row:
                rows.append(row)
                row = ibm_db.fetch_assoc(stmt)  # return next line

            df = pd.DataFrame(rows, columns=columns)
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
            if data is not None:
                ibm_db.exec_immediate(self.connection, query, data)
                ibm_db.commit(self.connection)
            self.connection.commit()
            return True
        except (Exception, OperationalError) as e:
            logger.critical(f"DML Error: {e}")
            return False
