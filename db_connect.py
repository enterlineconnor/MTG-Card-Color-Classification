#!/usr/bin/python
import MySQLdb
from config import creds

def query_local(query):
    db = MySQLdb.connect(host=creds['host'],    
                        user=creds['username'],        
                        passwd=creds['password'],  
                        db=creds['db'])        

    cur = db.cursor()
    cur.execute(query)
    row = cur.fetchone()

    card_array = []
    while row is not None:
        card_array.append(row)
        row = cur.fetchone()

    return card_array