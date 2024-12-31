import mysql.connector
import streamlit as st


#connection
try:
    
    conn=mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        passwd="",
        db="my_streamlit"

    )

    c= conn.cursor()

    #fetch data

    def view_all_data():
        c.execute('SELECT * FROM customers order by id asc')
        data= c.fetchall()
        return data
except:
    st.write("Database Could not found")