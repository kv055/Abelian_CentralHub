from PriceData.Querry_Assets_OHLC_DB_Class import Querry_Assets_OHLC_from_DB
from Indicators.Indicators_Class import Indicators

class Plot_for_Terminal:
    def __init__(self,asset_dict) -> None:
        self.asset_dict = asset_dict
        self.ohlc_db = Querry_Assets_OHLC_from_DB()

    def return_OHLC_data(self, asset_dict):
        # Fetch Assets DB by ticker and data_provider
        self.ohlc_set = self.ohlc_db.return_historical_ohlc_from_db(asset_dict)
        return self.ohlc_set

    def return_Indicators_data(self, indicator_config_dict):
        # create indicators_instance
        self.indicator_instance = Indicators(self.ohlc_set)
        selected_indicator_method = getattr(self.indicator_instance, indicator_config_dict['Name'])
        Indicator = selected_indicator_method(indicator_config_dict['Range'])
        return Indicator
