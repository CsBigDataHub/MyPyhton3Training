#!/usr/bin/python3
# databases.py 



import sqlite3

def main():
    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row # to get dict object
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int)')
    db.execute('insert into test (t1,i1) values (?,?)',('one',1))
    db.execute('insert into test (t1,i1) values (?,?)',('two',2))
    db.execute('insert into test (t1,i1) values (?,?)',('three',3))
    db.execute('insert into test (t1,i1) values (?,?)',('four',4))
    db.commit()
    query = db.execute('select * from test order by t1')
    for rows in query:
       # print(rows)
        print(dict(rows))   # to get dict object
        print(rows['t1'],rows['i1']) # to get dict object segregared
    print('This is the databases.py file')

if __name__ == "__main__": main()
