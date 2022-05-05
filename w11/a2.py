import psycopg2

name=input()
number=input()

def check(name,number):
    config = psycopg2.connect(
        host='localhost', 
        database='postgres',
        port = '5432',
        user='postgres',
        password='alma45884'
    )
    current = config.cursor()


    postgres_select_query = """select username from phonebook where username = %s"""
    current.execute(postgres_select_query,(name,))
    result = current.fetchone()
    if result:
        postgres_update_query = """Update phonebook set number = %s where username = %s"""
        current.execute(postgres_update_query,(number,name))
    else:
        postgres_insert_query=''' INSERT INTO phonebook (username,number) VALUES (%s,%s)'''
        current.execute(postgres_insert_query,(name,number))
    config.commit()
    current.close()
    config.close()



check(name,number)