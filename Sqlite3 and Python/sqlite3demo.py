# sqlite3demo.py
# Author: Darren Christie
# Last updated: 02/5/2023
# Description: demo program to show how to connect to an sqlite3 database

import database

def main():
    db = database.Database('northwind.db')
    db.getAllRegions()
    db.getAllCustomers()
    db.getAllSuppliers()
    db.closeDatabase()

if __name__ == '__main__':
    main()
