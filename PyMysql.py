import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Ls825.com', db='mysql')
cur = conn.cursor()
cur.execute("USE scraping")

cur.execute("SELECT*FROM pages WHERE ID = 1")
print(cur.fetchone())

cur.close()
conn.close()