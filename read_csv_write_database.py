# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:09:40 2016

@author: arthur gouveia

Reads a CSV file and imports it to a pandas Data Frame. Then it connects
to a MySQL database, creates a new table and inserts the data into that
table
"""

import mysql.connector as con
import pandas as pd

# Open database connection
db = con.connect(host="db4free.net",user="g2798774",\
                 password="~b~_^SD~2[mm+k4#",database="test_schema" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

data = pd.read_csv('C:\\Users\\arthu\\Desktop\\tb_income.csv',header=0)
print(data)

create_tb = (
    "CREATE TABLE `tb_income` ("
    "	`id` INT NOT NULL AUTO_INCREMENT,"
    "	`pclass` VARCHAR(5) NOT NULL DEFAULT '0',"
    "	`income` INT NOT NULL DEFAULT '0',"
    "	PRIMARY KEY (`id`)"
    ")"
    "COLLATE='utf8mb4_unicode_ci'"
    "ENGINE=InnoDB")
    
cursor.execute(create_tb)

db.commit()

for i in range(len(data)):
    insert = "INSERT INTO tb_income (id,pclass,income) VALUES (NULL,\"%s\",%d)"\
             %tuple(data.as_matrix()[i])
    cursor.execute(insert)

db.commit()
cursor.close()

db.close()
