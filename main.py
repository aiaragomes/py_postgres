# -*- coding: utf-8 -*-

"""
Inserting data to postgres
"""

from src.manage_db import ManageDB


if __name__ == '__main__':

    # Database params
    # TODO: this info should be retrieved from env vars or a file that is not
    #  commited to git
    dbname = 'data'
    host = 'localhost'
    port = 5431
    user = 'postgres'
    password = 'postgres'

    # Connect to database
    postgres = ManageDB(
        dbname=dbname, host=host, port=port, user=user, password=password
    )
    postgres.connect()

    # Create new table
    table = 'data'
    columns = {
        'id': 'text PRIMARY KEY',
        't': 'text',
        'n': 'text',
        'm': 'text',
        'stage': 'text',
        'date_of_diagnosis': 'text',
        'date_of_fu': 'text',
        'vital_status': 'text'
    }
    postgres.create_table(table=table, columns=columns)

    # Prepare data
    file_path = 'data/sample_data.csv'
    df = postgres.prepare_data(file_path=file_path, columns=columns.keys())

    # Insert data to table
    postgres.insert_data(table=table, columns=columns.keys(), df=df)
    print('All worked out')

    # Display table
    postgres.show_table(table=table)

    # Close database
    postgres.close()

