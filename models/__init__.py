from mongoengine import connect

from engine.config import MONGODB_PORT, MONGODB_USE_AUTH, MONGODB_HOST, MONGODB_DBNAME, MONGODB_PASSWORD, \
    MONGODB_USERNAME

if MONGODB_USE_AUTH:
    connection = connect(db=MONGODB_DBNAME, host=MONGODB_HOST, port=MONGODB_PORT,
                         username=MONGODB_USERNAME, password=MONGODB_PASSWORD, authentication_source='admin', connect=False)
else:
    connection = connect(db=MONGODB_DBNAME, host=MONGODB_HOST, port=MONGODB_PORT,  connect=False)
