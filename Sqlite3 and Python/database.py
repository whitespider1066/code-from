# database.py
# Author: Darren Christie
# Last updated: 02/5/2023
# Description: class to access our sqlite3 database

import sqlite3

class Database:

    def __init__(self,database_name):
        # connect to our database
        self.con = sqlite3.connect(database_name)
        # create a cursor object to help execute sql queries
        self.cur = self.con.cursor()

    def getAllRegions(self):
        
        results = self.cur.execute(
            '''SELECT * FROM Regions''').fetchall()

        print(len(results))
        for row in results:
            print (row)

    def getAllCustomers(self):

        results = self.cur.execute(
            '''SELECT * FROM Customers''').fetchall()

        for row in results:
            print (row)

    def getAllSuppliers(self):

        results = self.cur.execute(
            '''SELECT * FROM Suppliers''').fetchall()

        for row in results:
            print (row)

    def closeDatabase(self):
        self.con.commit()
        self.con.close()
        
        
