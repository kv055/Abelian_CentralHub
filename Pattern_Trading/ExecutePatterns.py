import find_parent
import talib
from PriceData.Get_Price_Data_Class import ImportData

asset_dict =  {
    "data_provider": "Kraken",
    "id": 12191,
    "ticker": "ADAEUR"
    }

class Pattern_Screening:
    def __init__(self, asset_dict) -> None:
        self.asset_dict = asset_dict
        pricedata_instance = ImportData()
        self.ohlc_data_frame = pricedata_instance.return_ohlc_dataframe(asset_dict)
        self.available_patterns = talib.get_function_groups()['Pattern Recognition']

    def ta_lib_candlestick_Pattern_Screening(self):
        detected_matches_of_all_patterns = []
        

        for name_of_pattern in self.available_patterns:
            method_to_call = getattr(talib, name_of_pattern)
            frame_of_scanned_pattern = method_to_call(
                    self.ohlc_data_frame['Open'],
                    self.ohlc_data_frame['High'],
                    self.ohlc_data_frame['Low'],
                    self.ohlc_data_frame['Close']
            )
            non_0_frame = frame_of_scanned_pattern[frame_of_scanned_pattern != 0]
            non_0_frame_dict = non_0_frame.to_dict()

            if len(non_0_frame_dict) != 0:
                items = non_0_frame_dict.items()
                for key_val_pair in items:
                    
                    if key_val_pair[1] == 100:
                        match_direction = 'Long'
                    elif key_val_pair[1] == -100:
                        match_direction = 'Short'
                    
                    pattern_match_dict = {
                        'Pattern_Name': name_of_pattern,
                        'Time' : key_val_pair[0],
                        'Direction' : match_direction
                    }
                    
                    detected_matches_of_all_patterns.append(pattern_match_dict)
        
        # Sort all metches by timestamp in ascending order
        detected_matches_sorted_by_time = sorted(detected_matches_of_all_patterns, key=lambda d: d['Time']) 
          
        return detected_matches_sorted_by_time

lol = Pattern_Screening(asset_dict)
l= lol.ta_lib_candlestick_Pattern_Screening()
o=0