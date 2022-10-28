from PriceData.Querry_Assets_OHLC_DB_Class import Querry_Assets_OHLC_from_DB
from Indicators.Indicators_Class import Indicators

class Plot_for_Terminal:
    def __init__(self,asset_dict) -> None:
        self.asset_dict = asset_dict
        self.ohlc_db = Querry_Assets_OHLC_from_DB()

    def return_OHLC_data(self, ticker):
        # Fetch Assets DB by ticker and data_provider
        self.ohlc_set = self.ohlc_db.return_historical_ohlc_from_db(ticker)
        # create indicators_instance
        return self.ohlc_set

    def create_Indicators_instance(self):
        self.indicator_instance = Indicators(self.ohlc_set)
        pass
