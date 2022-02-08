import pymysql
conn = pymysql.connect(host="localhost", user="root", password="root", database="studentdb")
cursor = conn.cursor()
sql="""
CREATE TABLE subject (
  subID int NOT NULL,
  subName varchar(50) NOT NULL,
  PRIMARY KEY (subID)
) ENGINE = MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
"""
cursor.execute(sql)
cursor.close()
conn.commit()
conn.close()
