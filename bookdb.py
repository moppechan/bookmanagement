import os, psycopg2, hashlib, string, random

def get_connection():
    url = os.environ['DATABASE_URL']
    connection = psycopg2.connect(url)
    return connection

def select_all_books():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT title, author, publisher FROM book_manage"
    
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return rows

def insert_book(title, author, publisher, isbn):
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'INSERT INTO book_manage VALUES (default, %s, %s, %s, %s)'
    
    cursor.execute(sql, (title, author, publisher, isbn))
    
    connection.commit()
    cursor.close()
    connection.close()