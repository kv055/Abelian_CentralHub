# import find_parent
from Database_SQL.aws_sql_connect import SQL_Server


class Querry_Assets_OHLC_from_DB:
    def __init__(self) -> None:
        self.db_name = 'DummyData'
        self.db_connection = SQL_Server(self.db_name)

    def return_all_dataproviders(self):
        querry_all_dataproviders_Distinct_sql = f"""
            SELECT DISTINCT data_provider FROM {self.db_name}.assets
        """
        self.db_connection.cursor.execute(querry_all_dataproviders_Distinct_sql)
        table = self.db_connection.cursor.fetchall()
        return table
    
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

    def return_all_candle_sizes(self, data_provider=None):
        querry_all_candle_sizes_Distinct_sql = f"""
            SELECT DISTINCT Time_Frame FROM {self.db_name}.OHLC
        """
        querry_all_candle_sizes_by_data_provider_Distinct_sql = f"""
            SELECT DISTINCT Time_Frame FROM {self.db_name}.OHLC
            WHERE data_provider = '{data_provider}'
        """
        if data_provider == None:
            self.db_connection.cursor.execute(querry_all_candle_sizes_Distinct_sql)
            table = self.db_connection.cursor.fetchall()
        else:
            self.db_connection.cursor.execute(querry_all_candle_sizes_by_data_provider_Distinct_sql)
            table = self.db_connection.cursor.fetchall()

        return table

    def return_historical_ohlc_from_db(self, asset_dict):
        ticker = asset_dict['ticker']
        data_provider = asset_dict['data_provider']
        query = f"""
            SELECT 
                UNIX_TIMESTAMP(Date) AS Timestamp,Open,High,Low,Close
            FROM {self.db_name}.OHLC
            WHERE data_provider = '{data_provider}' and ticker = '{ticker}'
        """
        self.db_connection.cursor.execute(query)
        table = self.db_connection.cursor.fetchall()
        return table
    
        # def return_historical_ohlc_from_db(self, asset_dict):
        # ticker = asset_dict['ticker']
        # data_provider = asset_dict['data_provider']
        # query = f"""
        #     SELECT * FROM {self.db_name}.OHLC
        #     WHERE data_provider = '{data_provider}' and ticker = '{ticker}'
        # """
        # self.db_connection.cursor.execute(query)
        # table = self.db_connection.cursor.fetchall()
        # return table
