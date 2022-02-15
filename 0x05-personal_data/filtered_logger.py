#!/usr/bin/env python3
"""" Module named filtered_logger """

import mysql.connector
import re
from typing import List
import logging
import os


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Implement a function that returns a connector to the database """
    user = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.environ.get("PERSONAL_DATA_DB_NAME")

    myDB = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=db_name
    )

    return myDB


def get_logger() -> logging.Logger:
    """ Create logger

    Return: a logging.Logger object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)

    return logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Init constructor """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ Implement the format method to filter values in incoming log
        records using filter_datum()
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Function that returns the log message obfuscated

    Args:
        - fields: list of the strings. Represents all fields to obfuscate
        - redaction: string. Represents by what the field willbe obfuscated
        - message: string. Represents the log line
        - separator: string. Represents by which character is separating all
                     fields in the log line (message)

    Return: a string -> message
    """
    for f in fields:
        message = re.sub(rf'{f}=.+?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message
