import json
import pyodbc


def write_json_from_sql_server(server_name, database_name, table_name):

    # Connect to SQL Server
    conn_str = f"DRIVER={{SQL Server}};SERVER={server_name};DATABASE={database_name};Trusted_Connection=yes;"
    conn = pyodbc.connect(conn_str)

    cursor = conn.cursor()

    item = cursor.execute(
        f"SELECT * FROM {table_name}")

    columns = [column[0] for column in cursor.description]
    data = [dict(zip(columns, row)) for row in cursor.fetchall()]

    json_data = json.dumps(data, indent=4)

    with open('data.json', 'w') as json_file:
        json_file.write(json_data)


server_name = "DESKTOP-5NABLM8"
database_name = "pizza_DB"
table_name = "pizza_sales"

write_json_from_sql_server(server_name, database_name, table_name)
