from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS

from Abelian_LiveTrading.Abelian_LiveTrading_Inserts_Class import Abelian_Live_Trading_Insert

app = Flask(__name__)
CORS(app)
api = Api(app)

# Integration of the Frontend Abelian Terminal

# Integaration of Abelian Clae

# Integration of Abelian Models

# Integration of Abelian Backtesting

# Integration of Abelian LiveTrading

@app.route('/Insert_LiveTrading', methods = ['POST'])
def Insert_Setup_Into_DB():
    """Return an ex-parrot."""
    data = request.get_json()
    data_source = data['']
    db_instance = Abelian_Live_Trading_Insert()
    if data_source == 'Insert_User':
        db_instance.insert_user(data_source)
    elif data_source == 'Insert_API_Keys':
        db_instance.insert_api_keys(data_source)
    elif data_source == 'Insert_Config_Setup':
        db_instance.insert_config_live_trading(data_source)
    elif data_source == 'Delete_User':
        db_instance.insert_config_live_trading(data_source)
    elif data_source == 'Delete_API_Keys':
        db_instance.insert_config_live_trading(data_source)

    return {'Setup_Inserted'}