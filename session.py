from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,MetaData
import redis
from signalrcore.hub_connection_builder import HubConnectionBuilder

class sessions():

    def __init__(self):
        self.meta = MetaData()
        self.engine = create_engine('sqlite:///assetserver/employeedata.db', echo=True)
        
        self.meta.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

        self.redis_client=redis.Redis(host='localhost',port=6379,db=0)
        self.server_url = "wss://localhost:6001/chathub"
        self.hub_connection = HubConnectionBuilder() \
        .with_url(self.server_url, options={"verify_ssl": False}) \
        .with_automatic_reconnect({
            "repeat":False
        }
        ).build()



    def get_session(self):
        return self.Session()
    
    def start_redis(self):
        return self.redis_client
    
    def start_hub_connection(self):
        self.hub_connection.on_open(lambda: print("connection opened"))
        self.hub_connection.on_close(lambda: print("connection closed"))
        self.hub_connection.start()

        return self.hub_connection

    