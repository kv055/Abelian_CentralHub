import find_parent
from Database_SQL.aws_sql_connect import SQL_Server


class Querry_Assets_OHLC_from_DB:
    def __init__(self) -> None:
        self.db_name = 'DummyData'
        self.db_connection = SQL_Server(self.db_name)

    def return_all_assets(self, data_provider=None):
        query_all_assets_sql = f"""
            SELECT * FROM {self.db_name}.assets
        """
        query_all_assets_by_data_provider_sql = f"""
            SELECT * FROM {self.db_name}.assets
            WHERE data_provider = '{data_provider}'
        """
        if data_provider == None:
            self.db_connection.cursor.execute(query_all_assets_sql)
            table = self.db_connection.cursor.fetchall()
        else:
            self.db_connection.cursor.execute(query_all_assets_by_data_provider_sql)
            table = self.db_connection.cursor.fetchall()

        return table

    def return_historical_ohlc_from_db(self, asset_dict):
        ticker = asset_dict['ticker']
        data_provider = asset_dict['data_provider']
        query = f"""
            SELECT * FROM {self.db_name}.OHLC
            WHERE data_provider = '{data_provider}' and ticker = '{ticker}'
        """
        self.db_connection.cursor.execute(query)
        table = self.db_connection.cursor.fetchall()
        return table
    
    # def return_binance_asset_URLs(self):
    #     # Connection
    #     urls_to_fetch = []
    #     query =  f"SELECT * from {self.db_connection.DBNAME}.binance_assets"
    #     self.db_connection.cursor.execute(query)
    #     table = self.db_connection.cursor.fetchall()
    #     for row in table:
    #         urls_to_fetch.append({
    #                 'URL':row[2],
    #                 'Ticker': row[1],
    #                 'Data_Provider': 'Binance'
    #             })
    #     return urls_to_fetch


# test = Querry_Assets_OHLC_from_DB()
# asset = test.return_all_assets()
# ohlc = test.return_historical_ohlc_from_db(asset[0])
# l = 0