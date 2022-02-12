import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='seu_usuario', passwd='suasenha', host='localhost', port=3306)
cursor = conn.cursor()
print(' -------------  Oleos:  -------------')
cursor.execute('select * from oleoteca.oleo order by corrente asc') #deixando em ordem alfabética
for jogo in cursor.fetchall():
    print(jogo)
conn.commit()
cursor.close()
