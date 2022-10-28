# Dependencies
from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api

# General Infrastructure
from Message_Que.insert_config_rows_DB import Insert_config_rows_into_Q

# Abelian Repos
from Abelian_Frontend_Terminal.Selector_For_Visualisation_Class import Select_For_Terminal
from Abelian_Frontend_Terminal.Data_for_visualisation_Class import Plot_for_Terminal

from Abelian_LiveTrading.Abelian_LiveTrading_Inserts_Class import Abelian_Live_Trading_Insert


app = Flask(__name__)
CORS(app)
api = Api(app)

# Integration of the Frontend Abelian Terminal

@app.route('/Abelian_Terminal_get_selectors', methods = ['GET'])
def return_all_selectors():
    pass

@app.route('/Abelian_Terminal_post_config_for_plotdata', methods = ['POST'])
def return_plotable_dataset():
    pass

# Integaration of Abelian Clae

# Integration of Abelian Models

@app.route('/Abelian_Models_post_config', methods = ['POST'])
def return_plotable_model_dataset():
    pass

# Integration of Abelian Backtesting

@app.route('/Abelian_Backtesting_post_config', methods = ['POST'])
def return_simulation_dataset():
    pass

# Integration of Abelian LiveTrading

@app.route('/Abelian_LiveTrading_post_db_entries', methods = ['POST'])
def Insert_Setup_Into_DB():
    """Return an ex-parrot."""
    test = Insert_config_rows_into_Q()
    db_instance = Abelian_Live_Trading_Insert()
    data = request.get_json()
    data_source = data['']
    
    if data_source == 'Insert_User':
        db_instance.insert_user(data_source)
        
    elif data_source == 'Insert_API_Keys':
        db_instance.insert_api_keys(data_source)

    elif data_source == 'Insert_Config_Setup':
        db_instance.insert_config_live_trading(data_source)
        
        test.fetch_config_rows()
        test.insert_deploy_messages_into_q()

    elif data_source == 'Delete_User':
        db_instance.insert_config_live_trading(data_source)

    elif data_source == 'Delete_API_Keys':
        db_instance.insert_config_live_trading(data_source)

    elif data_source == 'Deactivate_Config_Setup':

        test.fetch_config_rows()
        test.insert_stop_trading_messages_into_q()
        pass
    
    return {'Setup_Inserted'}