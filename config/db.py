from sqlalchemy import create_engine, MetaData

engine=create_engine("mariadb+pymysql://root:oreuglas1910@localhost:3306/ejemplo")

meta=MetaData()

conn=engine.connect()