import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import exists, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import aliased

engine = sa.create_engine("mysql+mysqldb://root:903326@localhost:3306/sql_demo?charset=utf8", echo=True)
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {}

    id = sa.Column(u'id', Integer, primary_key=True, nullable=False)
    user_name = Column(u'user_name', String(length=30), nullable=True, default='')
    password = Column(u'password', String(length=30), nullable=True, default='')
    passed = Column(u'passed', Integer, nullable=True, default=0)
    forbidden = Column(u'forbidden', Integer, nullable=True, default=0)
    deleted = Column(u'deleted', Integer, nullable=True, default=0)


users = db_session.query(User).all()
for user in users:
    print user.user_name

my_user = db_session.query(User.user_name.label('username'), (User.passed * 10).label('user_passed')).filter(
    User.id == 3).first()
print my_user
print "~~~~~~~~~~~~~~~~~~~~~~~~~"
print db_session.query(exists().where(User.id == 3).label('exist_id')).scalar()
print db_session.query((db_session.query(User.id).filter(User.id == 3).exists().label('exist_id'))).scalar()

print db_session.query(func.count('*').label('count_id')).select_from(User).scalar()
print db_session.query(func.now().label('time_now')).scalar()
print db_session.query(User).filter(User.id == 3).scalar()

print db_session.execute(insert(User).from_select((User.user_name, User.password),
                                                  db_session.query(User.user_name, User.password).filter(User.id == 3)))
db_session.commit()
print db_session.execute(insert(User).from_select((User.user_name, User.password),
                                                  db_session.query('"xiaoqigui01"', User.password).filter(
                                                      User.id == 3)))
db_session.commit()

res_users = db_session.query(User.user_name, func.group_concat(User.user_name.op('SEPARATOR')(';'))).group_by(
    User.user_name).all()
print res_users

user_table = aliased(User, name='user_table')
print db_session.query(exists().where(user_table.id == 3).label('exist_id')).scalar()

print "~~~~~~~~~~~~~~~~~~~~~~~~~"

sub_query = db_session.query(User.user_name.label('user_name'), User.id.label('user_id')).filter(User.id == 3).subquery(
    'sub')
# columns¸úcÒ»Ñù
print db_session.query(User.user_name.label('user_name')).filter(User.id == sub_query.columns.user_id).all()


print "~~~~~~~~~~~~~~~~~~~~~~~~~"
