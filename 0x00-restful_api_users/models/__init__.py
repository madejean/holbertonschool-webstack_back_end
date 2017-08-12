from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from models.base_model import Base
from models.user import User

host = os.environ.get('HBNB_YELP_MYSQL_HOST')
user = os.environ.get('HBNB_YELP_MYSQL_USER')
password = os.environ.get('HBNB_YELP_MYSQL_PWD')
db = os.environ.get('HBNB_YELP_MYSQL_DB')

db_engine = create_engine(
    'mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, db)
    )

if os.environ.get('HBNB_MYSQL_ENV') == 'test':
    User.metadata.drop_all()

User.metadata.create_all(db_engine)
db_session = scoped_session(
    sessionmaker(bind=db_engine, expire_on_commit=False)
    )
