import os, psycopg2

def get_connection():
    url = os.environ['DATABASE_URL']
    connection = psycopg2.connect(url)
    return connection

def select_all_books():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM book_manage"
    
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return rows

def insert_book(title, author, publisher, isbn):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO book_manage VALUES (default, %s, %s, %s, %s)"
    
    cursor.execute(sql, (title, author, publisher, isbn))
    
    connection.commit()
    cursor.close()
    connection.close()
    
def delete_book(id):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "DELETE FROM book_manage WHERE id = %s"
    
    cursor.execute(sql, (id,))
    
    connection.commit()
    cursor.close()
    connection.close()    
    
def search_book(keyword):
    connection = get_connection()
    cursor = connection.cursor()
    
    
    print('+++++ '+('%' + keyword + '%'))
    key = ('%' + keyword + '%')
    cursor.execute("SELECT * FROM book_manage WHERE name LIKE %s", (key,))
    #cursor.execute("SELECT * FROM book_manage WHERE name LIKE '%test%'")
    result = cursor.fetchall()

    cursor.close()
    connection.close()
    return result
 