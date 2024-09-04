from dataclasses import dataclass

import pandas as pd
import pymysql
from settings.logs import logger
from sqlalchemy import create_engine


@dataclass
class MySqlConnection:
    host: str
    user: str
    pmysql: str
    database: str
    port: int = 3306
    connection = None

    def __enter__(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.pmysql,
                database=self.database,
                port=self.port,
                cursorclass=pymysql.cursors.DictCursor,
            )
            logger.info("Connection with MySql Succeeded")
            return self
        except pymysql.Error as e:
            logger.critical(f"Error to connect with MySql: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self, "connection"):
            self.connection.close()

    def execute_fetch(self, sql) -> pd.DataFrame:
        """
        Execute 'select query'.

        Args:
            sql (str): Query SQL

        Returns:
            pd.DataFrame
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                return pd.DataFrame(
                    result, columns=[col[0] for col in cursor.description]
                )
        except pymysql.Error as e:
            logger.critical(f"Error to fetch: {e}")
            return pd.DataFrame()

    def execute_dml(self, sql: str, data: dict | list = None) -> bool:
        """
        Execute any DML instruction: 'insert, update, delete, truncate, etc'.

        Args:
            sql (str): Query SQL
            data (dict| list): parameters of query

        Returns:
            bool: True to success False to some fail.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, data)
                self.connection.commit()
                return True
        except pymysql.Error as e:
            logger.critical(f"DML Error: {e}")
            self.connection.rollback()
            return False

    def insert_dataframe_in_mysql(
        self, df: pd.DataFrame, table_name: str, if_exists="append"
    ) -> bool:
        """
        Insert a dataframe using pandas.to_sql(). To use it is necessary install lib SQLAlchemy.

        Args:
            df (pd.DataFrame): Dataframe with data to be inserted
            table_name (str): Name of table in database, only table name, no database name with table name.

        Returns:
            bool: True to success False to some fail.
        """
        try:
            engine = create_engine(
                f"mysql+pymysql://{self.user}:{self.pmysql}@{self.host}:{self.port}/{self.database}?charset=utf8"
            )
            rows_affected = df.to_sql(
                table_name, engine, if_exists=if_exists, index=False
            )
            if rows_affected is not None and rows_affected > 0:
                return True
            return False
        except Exception as e:
            logger.critical(f"Insert Error: {e}")
            return False
