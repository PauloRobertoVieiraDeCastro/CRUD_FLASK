import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='cimento1', host='localhost', port=3306)
cursor = conn.cursor()
print(' -------------  Oleos:  -------------')
cursor.execute('select * from oleoteca.oleo order by corrente asc')
for jogo in cursor.fetchall():
    print(jogo)
conn.commit()
cursor.close()
