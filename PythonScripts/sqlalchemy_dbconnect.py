#!/usr/bin/python3

from sqlalchemy import *
#from sqlalchemy.orm import sessionmaker


#username = input("What is the username to connect?")
#pwd = input("What is the password to use?")
engine = create_engine('mysql+mysqldb://root:''@localhost/john', pool_recycle=3600)
#Session = session.configure(bind=engine)
#session = Session()
#inspector = inspect(engine)
#dbtables = engine.execute('SHOW TABLES')

#available_tables = dbtables.fetchall()

#print(available_tables)

# Print table names

print(engine.table_names())
#name = select * from engine.table_names()

#select * from available_tables



#for instance in Session.query(john.EMPLOYEE).order_by(User.id):
#    print(instance.name, instance.fullname)
