# import Message_Que.find_parent
import json
from External_Infrastructure.Q_PUB_SUB_class import Q

class Insert_BackTesting_config_into_Q:
    def __init__(self):
        # initialise connections to the Q and the DB
        self.que_instance = Q()

    def Backtesting_Insert_config_into_q(self, config_array):
        # Assert Input

        # Construct Message
        dummy_config_array = {
            'Strategy':'dummy_data_strategy',
            'Parameter':0,
            'Assets': [
                {
                    "assetPair": {
                        "data_provider": "Kraken",
                        "id": 13191,
                        "ticker": "ACAEUR"
                    },
                    "candleSize": "1_Day"
                },
                {
                    "assetPair": {
                        "data_provider": "Kraken",
                        "id": 12191,
                        "ticker": "ADAEUR"
                    },
                    "candleSize": "1_Day"
                }
            ],
            'Candle_Size': '1_Day',
            'Start_Time': None,
            'End_Time': None,
            'Data_Set_Size': None
        }
        # Important to include Message_Group for the backtesting poll messages class
        Message_Group = 'Start_Simulation'
        message = json.dumps(dummy_config_array)
        # Insert Mesage
        self.que_instance.publish(message)
        