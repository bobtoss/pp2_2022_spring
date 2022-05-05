import psycopg2

s=input()

def delete(s):
    config = psycopg2.connect(
        host='localhost', 
        database='postgres',
        port = '5432',
        user='postgres',
        password='alma45884'
    )
    current = config.cursor()

    if s.isdigit():
        postgres_delete_query = """Delete from phonebook where number = %s"""
        current.execute(postgres_delete_query,(s,))
    else:
        postgres_delete_query = """Delete from phonebook where username = %s"""
        current.execute(postgres_delete_query,(s,))
    config.commit()

    current.close()
    config.close()

delete(s)