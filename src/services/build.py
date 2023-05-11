from services.connection import CONNECTION


def create_table(connection):

    connection.execute("""
    create table High_Scores (id INTEGER PRIMARY KEY, name TEXT, score INTEGER);    
    """)
    connection.commit()
    connection.close()


if __name__ == '__main__':
    create_table(CONNECTION)
