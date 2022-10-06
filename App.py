"""Module for final execusion"""
# eat a dick
# from crypt import methods
# from Config.BinanceFetchFrontend import PriceDataFetch
# from flask_restful import Api Resource, reqparse, request

from copy import deepcopy
from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS

from Config.DataSourceFrontend import DataSources
from Config.AssetPairsFrontend import AssetPairs
from Config.OHLCDataFrontend import OHLCData
from Config.ListOfIndicatorsFrontend import IndicatorsToRender
from Config.ListOfStrategies import Strategies
# from PriceData.AveragePrices import getAveragePrice
# from PriceData.BinanceOHLCforIndicators import OHLCformated
from Indicators.Rendered_Indicators import InitSelectedIndicator
from Config.AllModelsFrontend import AllModels
# from Models.Models import Modelz
# from Models.SelectModels import ModelData
# from Patterns.ExecutePatterns import AllCandlePatterns
# from Patterns.SelectPatternTemplateFrontend import FrameTemplate
# from SimulationApi import RunSimulation

import find_parent

app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route('/DataSources', methods=['GET'])
def get_data_sources():
    """Return an ex-parrot."""
    return{'Metadata':DataSources()}


@app.route('/AssetPairs',methods = ['POST'])
def post_asset_pairs():
    """Return an ex-parrot."""
    data = request.get_json()
    selected_data_source = data['DataSource']
    return_asset_pairs = AssetPairs(selected_data_source)
    return {'AssetPairs': return_asset_pairs}

# Create Global Array in which all PriceData gets fetched

GlobalPriceData = []

# def append_global_pricedata(toAppend):
#     """Return an ex-parrot."""
#     price_data = deepcopy(getAveragePrice(toAppend))
#     # print('Average in App.py', PriceData)
#     GlobalPriceData.append({
#         'config':toAppend['config'],
#         'OHLC': toAppend['OHLC'],
#         'Average': price_data
#     })

# Price Data ---------------------

# @app.route('/OHLC', methods=['POST'])
# def ohlc():
#     """Return an ex-parrot."""
#     data = request.get_json()
#     ohlc_config = data['ohlcConfig']
#     return_ohlc_data = OHLCData(ohlc_config)
#     append_global_pricedata({'config':ohlc_config,'OHLC': return_ohlc_data})
#     return {'config':ohlc_config,'OHLC': return_ohlc_data}


# Indicators Data ---------------------

@app.route('/ListAllIndicators', methods=['GET'])
def list_indi():
    """Return an ex-parrot."""
    return {'IndicatorsToRender': IndicatorsToRender}

@app.route('/RenderIndicator', methods=['POST'])
def render_indi():
    """Return an ex-parrot."""
    data = request.get_json()
    indicator_config = data['config']
    if len(GlobalPriceData)>0:
        # Ze Übeltäter
        # ohlc_price = deepcopy(OHLCformated(GlobalPriceData[-1]['OHLC']))
        ohlc_price = deepcopy(GlobalPriceData[-1]['OHLC'])
        indicator_ready = InitSelectedIndicator(
            indicator_config['selectedIndicator']['symbol'],
            ohlc_price,
            int(indicator_config['selectedPeriod'])
        )
        return {
            'Indicator': indicator_ready,
            'config': indicator_config
        }

# Pattern Screener Data ------------------------

# @app.route('/PatternScreening', methods=['GET'])
# def pattern_screening():StatisticsPriceData
#     """Return an ex-parrot."""
#     if len(GlobalPriceData)>0:
#         data = request.get_json()
#         screening_config = data['config']
#         # Select Frame Template (Binance, Alpaca,... whatevaaa)
#         frame_template = FrameTemplate(screening_config)
#         ohlc_price = deepcopy(OHLCformated(GlobalPriceData[-1]['OHLC']))
#         patterns = AllCandlePatterns(ohlc_price, frame_template)
#         return {'AllPatterns': patterns}

# Statistics Data ---------------------

@app.route('/AllModels', methods=['GET'])
def get_all_models():
    """Return an ex-parrot."""
    return{'Metadata':AllModels()}

# @app.route('/Statistics', methods=['POST'])
# def statistics():
#     """Return an ex-parrot."""
#     data = request.get_json()
#     ohlc_config = data['OHLCConfig']
#     model_config = data['ModelConfig']
#     StatisticsPriceData = []
#     for config_set in ohlc_config:
#         return_ohlc_data = OHLCData(config_set)
#         price_data = deepcopy(getAveragePrice({'config':config_set,'OHLC': return_ohlc_data}))
#         StatisticsPriceData.append({
#             'config':config_set,
#             'OHLC': return_ohlc_data,
#             'Average': price_data
#         })
        
#     frame = Modelz(StatisticsPriceData)
#     rendered_model = ModelData(model_config,frame)
#     return {'Config': model_config, 'StatisticsModel': rendered_model}

# Simulation Data ---------------------

@app.route('/ListAllStrategies', methods=['GET'])
def list_strat():
    """Return an ex-parrot."""
    return {'Strategies': Strategies}

# # from PriceData.BinanceAveragePrice import AveragePrice
# @app.route('/Simulation', methods=['POST'])
# def sim():
#     """Return an ex-parrot."""
#     if len(GlobalPriceData)>0:
#         data = request.get_json()
#         simulation_config = data['config']
#         ohlc_price = deepcopy(OHLCformated(GlobalPriceData[-1]['OHLC']))
#         simulation = RunSimulation(ohlc_price,simulation_config)
#         return {
#             'Simulation': simulation,
#             'config': simulation_config
#         }

host='0.0.0.0'
app.run(host='localhost',port=5001,debug=True)