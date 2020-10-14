import sqlite3

def getConn():
    conn = sqlite3.connect('d:/share/mydb.db')    # mydb.db 가 있으면 사용, 없으면 생성
    return conn    # 접속정보