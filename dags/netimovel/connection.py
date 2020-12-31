import psycopg2
from airflow.models import Variable


def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]

    return get_class


@singleton
class Connection:
    _instance = None
    __conn = None

    def __init__(self):
        dsn = 'dbname={dbname} ' \
              'user={user} ' \
              'password={password} ' \
              'port={port} ' \
              'host={host} '.format(dbname= Variable.get('DATABASE_NAME'),
                                    user= Variable.get('DATABASE_USER'),
                                    password= Variable.get('DATABASE_PASSWORD'),
                                    port= Variable.get('DATABASE_PORT'),
                                    host= Variable.get('DATABASE_HOST'))
        self.__conn = psycopg2.connect(dsn)
        self.__conn.set_session(autocommit=True)

    def get_connection(self):
        return self.__conn

    def close(self) -> None:
        self.__conn.close()
