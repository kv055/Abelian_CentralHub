# Dependencies
import json
from flask import Flask, request, session
from flask_cors import CORS
from flask_restful import Api

# General Infrastructure
from Abelian_Live_Trading.Q_for_Abelian_Live_Trading import Insert_config_rows_into_Q
from Indicators.Indicators_Class import Indicators
from PriceData.Get_Price_Data_Class import ImportData
# Abelian Repos
from Abelian_Frontend_Terminal.Selector_For_Visualisation_Class import Select_For_Terminal
from Abelian_Frontend_Terminal.Data_for_visualisation_Class import Plot_for_Terminal

from Abelian_Live_Trading.Abelian_Live_Trading_Inserts_Class import Abelian_Live_Trading_Insert
from Abelian_Backtesting.Q_for_Abelian_BackTesting import Insert_BackTesting_config_into_Q

app = Flask(__name__)
CORS(app)
api = Api(app)

app.secret_key = 'DeezNutz'

# Integration of the Frontend Abelian Terminal

@app.route('/Abelian_Terminal_get_selectors', methods = ['GET'])
def return_all_selectors():
    selector_instance = Select_For_Terminal()
    all_possible_selections = {
        # Fetching Price-data
        'all_OHLC_sources': selector_instance.return_all_OHLC_Sources(),
        # Fetching all Technical Indicators
        'all_technical_Indicators': selector_instance.return_all_technical_Indicators(),
        # Fetching all available Models
        'all_Models': selector_instance.return_all_Models(),
        # Fetching all available Strategies for Backtesting
        'all_Strategies': selector_instance.return_all_Strategies(),
    }
    return all_possible_selections

@app.route('/Abelian_Terminal_post_asset_selectors', methods = ['POST'])
def return_all_chosen_selectors():
    # Get selected Asset
    data = request.get_json()
    selected_data_source = data['DataSource']['data_provider']
    selector_instance = Select_For_Terminal()
    all_assets_by_datasource = selector_instance.return_assets_and_candleSizes(selected_data_source)
    return all_assets_by_datasource

@app.route('/Abelian_Terminal_post_ohlc_config_for_plotdata', methods = ['POST'])
def return_plotable_dataset():
    # save posted data
    asset_dict = request.get_json()

    OHLC_Instance = ImportData()
    OHLC_data_set_with_seperated_traces = OHLC_Instance.return_seperate_ohlc_traces(asset_dict)
    OHLC_data_set_in_json = json.dumps(OHLC_data_set_with_seperated_traces)
    return OHLC_data_set_in_json

@app.route('/Abelian_Terminal_post_Indicator_config_for_plotdata', methods = ['POST'])
def return_plotable_indicators_set():
    # save posted data
    data = request.get_json()
    Asset_dict = data['Asset_dict']
    Selected_Indicator = data['Selected_Indicator']

    Indicator_Instance = Indicators(Asset_dict)
    Indicator_Method = getattr(Indicator_Instance, Selected_Indicator['Name'])
    Indicator_Data =  Indicator_Method(Selected_Indicator['Range'])
    Indicator_data_in_json = json.dumps(Indicator_Data)
    return Indicator_data_in_json


# Integaratidefon of Abelian Clae

# Integration of Abelian Models

@app.route('/Abelian_Models_post_config', methods = ['POST'])
def return_plotable_model_dataset():
    pass

# Integration of Abelian Backtesting
@app.route('/Abelian_Backtesting_post_big_sim_config', methods = ['POST'])
def create_simulation_dataset():
    sim_config = request.get_json()
    Back_testing_instance = Insert_BackTesting_config_into_Q()
    Back_testing_instance.Backtesting_Insert_config_into_q(sim_config)

@app.route('/Abelian_Backtesting_get_list_all_sim_sets', methods = ['GET'])
def return_all_sim_sets_to_select():
    pass

@app.route('/Abelian_Backtesting_post_config', methods = ['POST'])
def return_sim_set():
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

# host='0.0.0.0'
# app.run(host='localhost',port=5001,debug=True)