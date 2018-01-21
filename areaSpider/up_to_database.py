import pymysql
import datetime

with open('./oil_information.json','r') as f:
    fi=f.read()

list1=eval(fi)

now_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

db=pymysql.connect(host="101.132.44.182",user="oiluser",password="123456",db="oil_price",charset="utf8")
cursor = db.cursor()

for dic in list1:
    time_str = datetime.datetime.strptime(dic['updatetime'], '%Y年%m月%d日').strftime('%Y-%m-%d')
    sql_insert=r"insert into t_traffic_oil_price(prov,city,ct,p0,p89,p92,p95,create_time) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(dic['province'],dic['area'],time_str,dic['oil0'],dic['oil89'],dic['oil92'],dic['oil95'],now_time)
    sql_query=r"select 1 from t_traffic_oil_price where city='{0}' limit 1".format(dic['area'])
    sql_update=r"update t_traffic_oil_price set prov='{0}',ct='{2}',p0='{3}',p89='{4}',p92='{5}',p95='{6}',create_time='{7}' where city='{1}'".format(dic['province'],dic['area'],time_str,dic['oil0'],dic['oil89'],dic['oil92'],dic['oil95'],now_time)
    try:
        cursor.execute(sql_query)
        if cursor.rowcount==0:
            cursor.execute(sql_insert)
        else:
            cursor.execute(sql_update)
        db.commit()
    except:
        db.rollback()

db.close()