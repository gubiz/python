# STEP 1
import pymysql

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='localhost', user='web', password='web@!',
                      db='pymysql', charset='utf8')  # 한글처리 (charset = 'utf8')

# STEP 3: Connection 으로부터 Cursor 생성
cur = con.cursor()

# STEP 4: SQL문 실행 및 Fetch
sql = "SELECT player, birth FROM baseball"
cur.execute(sql)

# 데이타 Fetch
rows = cur.fetchall()
print(rows)  # 전체 rows

# STEP 5: DB 연결 종료
con.close()