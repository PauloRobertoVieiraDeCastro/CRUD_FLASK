import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='seu_usuario', passwd='suasenha', host='localhost', port=3306)

conn.cursor().execute("DROP DATABASE `oleoteca`;") #so execute se vc já tiver o banco com esse nome, do contrário, retire essa linha
conn.commit()#idem

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `oleoteca` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `oleoteca`;
    CREATE TABLE `oleo` (
      `ide` INT NOT NULL AUTO_INCREMENT,
      `Corrente` VARCHAR(50) COLLATE utf8_bin NOT NULL,
      `API` FLOAT NOT NULL,
      `Nafta` FLOAT NOT NULL,
      `Diesel` FLOAT NOT NULL,
      `Gasoleo` FLOAT NOT NULL,
      `Enxofre` FLOAT NOT NULL,
      `Nitrogenio` FLOAT NOT NULL,
      `TAN` FLOAT NOT NULL,
      PRIMARY KEY (`ide`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(criar_tabelas)
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO oleoteca.oleo (Corrente, API, Nafta, Diesel, Gasoleo, Enxofre, Nitrogenio, TAN) values (%s, %s, %s, %s, %s, %s, %s, %s)',
      [
            ('Alagoano','40.9','25.22','30.08','44.70','0.039','0.039','0.1')
      ])
print(' -------------  Oleos:  -------------')
cursor.execute('select * from oleoteca.oleo')
for jogo in cursor.fetchall():
    print(jogo) #vendo a cara do banco
conn.commit()
cursor.close()
