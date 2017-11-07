#!/usr/bin/env python3
 
import psycopg2
from config import config
 
 
def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE shopping (
            shopping_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE daughter (
                daughter_id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE daughter_pics(
                daughter_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (daughter_id)
                REFERENCES daughter (daughter_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE shopping_data (
                shopping_id INTEGER NOT NULL,
                daughter_id INTEGER NOT NULL,
                PRIMARY KEY (shopping_id , daughter_id),
                FOREIGN KEY (shopping_id)
                    REFERENCES shopping (shopping_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (daughter_id)
                    REFERENCES daughter (daughter_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    create_tables()
