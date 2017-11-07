#!/usr/bin/python
import psycopg2
from config import config

def read_blob(daughter_id, path_to_dir):
    """ read BLOB data from a table """
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgresQL database
        conn = psycopg2.connect(**params)
        # create a new cursor object
        cur = conn.cursor()
        # execute the SELECT statement
        cur.execute(""" SELECT name, file_extension, drawing_data
                        FROM daughter_pics
                        INNER JOIN daughter on daughter.daughter_id = daughter_pics.daughter_id
                        WHERE daughter.daughter_id = %s """,
                    (daughter_id,))
 
        blob = cur.fetchone()
        open(path_to_dir + blob[0] + '.' + blob[1], 'wb').write(blob[2])
        # close the communication with the PostgresQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    read_blob(1, 'photosr/')
    read_blob(2, 'photosr/')
