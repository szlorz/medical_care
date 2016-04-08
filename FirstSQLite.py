import sqlite3

def convert(value):
    if value.startswith('-'):
        return value.strip('-')
    if not value:
        value = '0'
    return float(value)

conn = sqlite3.connect('FirstSQLite.db')
curs = conn.cursor()

curs.execute('''
create table FirstSQlite(
id             TEXT          PRIMARY KEY ,
department     TEXT,
hospital       TEXT,
sex            TEXT,
age            INT,
description    TEXT
)
''')

query = 'INSERT INTO FirstSQLite VALUES (?,?,?,?,?,?)'

for line in open(ABBREV.txt)
    fields = line.split('^')
    vals = [convert(f) for f in fields[:field_count]]
    curs.execute(query.vals)s

conn.commit()
conn.close()