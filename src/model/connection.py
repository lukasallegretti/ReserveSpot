import loguru
from psycopg2 import connect


def get_connection():
    try:
        connection = connect(
            host="postgres",
            database="postgres",
            user="postgres",
            password="postgres",
            port="5432",
        )
        return connection
    except Exception as error:
        loguru.logger.error(error)
        return None
