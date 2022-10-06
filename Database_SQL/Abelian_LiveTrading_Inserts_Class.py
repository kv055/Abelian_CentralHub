from Database_SQL.aws_sql_connect import SQL_Server

# Data
user = {
    'first_name': 'Kilian',
    'last_name': 'Voss',
    'e_mail': 'kilian96@live.de'
}

keys = {
    'user_id': 69,
    'exchange_id': 69,
    'exchange_name': 69,
    'pub_key': 420,
    'priv_key': 420
}

config = {
    'user_id': 7,
    'strategy_id': 1,
    'asset_id': 69
}

class Abelian_Live_Trading_Insert:
    def __init__(self):
        self.connector = SQL_Server('DummyData') 

    def insert_user(self, user_data):
        ins = f"""INSERT INTO users (first_name, last_name, e_mail) VALUES (%s,%s,%s)"""
        val = (user['first_name'],user['last_name'],user['e_mail'])
        self.connector.cursor.execute(ins, val)
        self.connector.connection.commit()
        # implement error handling or any feedback from db


    def insert_api_keys(self, api_keys):
        ins = f"""INSERT INTO exchange_keys 
        (user_id, exchange_id,exchange_name,pub_key,priv_key) VALUES (%s,%s,%s,%s,%s)"""
        val = (keys['user_id'],keys['exchange_id'],keys['exchange_name'],keys['pub_key'],keys['priv_key'])
        self.connector.cursor.execute(ins,val)
        self.connector.connection.commit()


    def insert_config_live_trading(self, config_live_trading):
        ins = f"""INSERT INTO config_live_trading (user_id, strategy_id,asset_id) VALUES (%s,%s,%s)"""
        val = (config['user_id'],config['strategy_id'],config['asset_id'])
        self.connector.cursor.execute(ins,val)
        self.connector.connection.commit()


