import pymysql
import json
import pandas as pd

class sql_server:

    @staticmethod
    def insert(insert_data):
        conn = pymysql.connect(host='localhost', port=3306, user='auint', password='pwpw', 
        db = 'mysql', charset='utf8')  # *6CC6A1C22CFFA93B23769CAE343636557E024D12

        try:
            # cur = conn.cursor()랑 같은 의미
            with conn.cursor() as cur:

                # DB에 쿼리로 데이터 추가
                col_list = list(insert_data.keys())
                col = ', '.join(col_list)

                #val = ','.join(map(str, insert_data.values())) <== 이렇게하면 문자열이 ''로 안둘려서 나옴
                val = ""
                for i in col_list:
                    col_data = insert_data[i]
                    if str(type(col_data)) == "<class 'str'>":  # str이면 '추가
                        val += "'"
                    val += str(col_data)
                    if str(type(col_data)) == "<class 'str'>":
                        val += "'"
                    val += ", "
                val = val[0:-2]

                query = "INSERT INTO mytable(%s) VALUSE(%s);" %(col, val)
                cur.execute(query)  # cur.execute(query, insert_data.values())

                conn.commit()
        finally:
            conn.close()

    @staticmethod
    def select(where_data):
        conn = pymysql.connect(host='localhost', port=3306, user='auint', password='pwpw', 
        db = 'mysql', charset='utf8')

        try:
            with conn.cursor() as cur:

                # 들어오는 명렁어 추가 해서 검색하기 
                add_query = ""
                if where_data is not None:
                    add_query = " WHERE "
                    add_query += where_data

                # 검색, 결과도출 
                query = "SELECT * FROM mytable" + add_query + ";"
                result_query = pd.read_sql(query, con = conn)
                
                # 전송을 위해 dataframe -> dict으로 변환
                df = df.to_dict('records')  # 형식: {time, plant..}, {time, plant...}
                # 받고나서 다시 dict -> dataframe로 변환 [df = pd.DataFrame(df)]

                print(df)  # 테스트

                ''' ex) WHERE
                plant='hub' // 식물이 허븬거 찾기
                plant LIKE 'temp%' // temp*인거 모두 ex) temp_plan, temp_abcdf...
                time BETWEEN '2021-06-22 14:00:00' AND '2021-06-22 14:40:00' // ~부터 ~까지 
                temperature < 7
                '''

                conn.commit()
        finally:
            conn.close()

    @staticmethod
    def delete(delete_data):
        conn = pymysql.connect(host='localhost', port=3306, user='auint', password='pwpw', 
        db = 'mysql', charset='utf8')

        try:
            with conn.cursor() as cur:

                



                conn.commit()
        finally:
            conn.close()

    @staticmethod
    def update(update_data):
        conn = pymysql.connect(host='localhost', port=3306, user='auint', password='pwpw', 
        db = 'mysql', charset='utf8')

        try:
            with conn.cursor() as cur:

                



                conn.commit()
        finally:
            conn.close()


# now test

dict_message = {
    'time' : '1111-22-33 44:55:66',
    'plant' : 'baechu',
    'temperature': 21,
    'humidity': 6,
    'illuminance': 24.13
}

sql_server.insert(dict_message)
print("----------1")

sql_server.select(None)
print("----------2")

sql_server.select()
print("----------3")

sql_server.select("")
print("----------4")

tempp = "plant = 'hub'"
sql_server.select(tempp)
print("----------5")





