# ------------------Connect to MSSQl database------------------------------
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

import pyodbc  # to get this write in terminal : pip install pyodbc


def ConnectToSQL():
    server = 'DESKTOP-TL74A5V'
    database = 'Test'
    username = 'sa'
    password = 'sa123456'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    cursor.execute('SELECT * FROM HrmEmployee')

    for row in cursor:
        print(row)

    cursor.close()

    print("close")
