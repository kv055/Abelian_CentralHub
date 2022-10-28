import find_parent

from PriceData.Querry_Assets_OHLC_DB_Class import Querry_Assets_OHLC_from_DB

class Select_For_Terminal:
    def __init__(self) -> None:
        self.assets_db = Querry_Assets_OHLC_from_DB()

    def return_all_Strategies(self):
        all_Strategies = [
            {'name': 'Moving Average Crossings'}
        ]
        return all_Strategies

    def return_all_Models(self):
        all_Models = [
            {'name': 'Rates of Logarithmic Volatility'},
            {'name': 'Rates of Simple Volatility'},
            {'name': 'Rates of Return'},
            {'name': 'Rates of Deviation'},
            {'name': 'Rates of Corelation'}
        ]
        return all_Models

    def return_all_OHLC_Sources(self):
        OHLC_Sources = [
            {'name': 'Alpaca', 'mic': 'Alpaca'},
            {'name': 'Binance', 'mic': 'Binance'},
            {'name': 'Kraken', 'mic': 'Binance'}
        ]
        # Fetch Assets DB by Distinct data_provider
        
        return OHLC_Sources
    
    def return_assets(self,data_source):
        asset_dicts = self.assets_db.return_all_assets(data_source)
        return asset_dicts


    def return_all_IndicatorCategories(self):  
        IndicatorCategories = [
            'Overlap Studies',
            'Momentum Indicators',
            'Volume Indicators',
            'Volatility Indicators',
            'Price Transform',
            'Cycle Indicators',
            'Pattern Recognition',
            'Statistic Functions',
            'Math Transform',
            'Math Operators'
        ]
        return IndicatorCategories
    
    def return_all_TA_LIB_Overlap_Studies(self):
        Overlap_Studies = [
            # {'name':'Bollinger Bands','symbol':'BBANDS'}, Output is an Array instead of Single Variable      
            {'name':'Double Exponential Moving Average','symbol':'DEMA'},        
            {'name':'Exponential Moving Average','symbol':'EMA'},        
            # {'name':'Hilbert Transform         Instantaneous Trendline','symbol':'HT_TRENDLINE'},
            {'name':'Kaufman Adaptive Moving Average','symbol':'KAMA'},        
            {'name':'Moving average','symbol':'MA'},        
            # {'name':'MESA Adaptive Moving Average','symbol':'MAMA'}, Output is an Array instead of Single Variable     
            # {'name':'Moving average with variable period','symbol':'MAVP'},        
            {'name':'MidPoint over period','symbol':'MIDPOINT'},        
            # {'name':'Midpoint Price over period','symbol':'MIDPRICE'},        
            # {'name':'Parabolic SAR','symbol':'SAR'},        
            # {'name':'Parabolic SAR         Extended','symbol':'SAREXT'},        
            {'name':'Simple Moving Average','symbol':'SMA'},
            {'name':'Triple Exponential Moving Average (T3)','symbol':'T3'},        
            {'name':'Triple Exponential Moving Average','symbol':'TEMA'},        
            {'name':'Triangular Moving Average','symbol':'TRIMA'},        
            {'name':'Weighted Moving Average','symbol':'WMA'}
        ]
        return Overlap_Studies

    def return_all_TA_LIB_Momentum_Indicators(self):
        Momentum_Indicators = [
            {'name':'Average Directional Movement Index','symbol':'ADX'}, 
            {'name':'Average Directional Movement Index Rating','symbol':'ADXR'},
            # {'name':'Absolute Price Oscillator','symbol':'APO'},
            # {'name':'Aroon','symbol':'AROON'}, Output is an Array instead of Single Variable
            {'name':'Aroon Oscillator','symbol':'AROONOSC'},
            {'name':'Balance Of Power','symbol':'BOP'},
            {'name':'Commodity Channel Index','symbol':'CCI'},
            {'name':'Chande Momentum Oscillator','symbol':'CMO'},
            {'name':'Directional Movement Index','symbol':'DX'},
            # {'name':'Moving Average Convergence/Divergence','symbol':'MACD'},
            # {'name':'MACD with controllable MA type','symbol':'MACDEXT'},
            # {'name':'Moving Average Convergence/Divergence Fix 12/26','symbol':'MACDFIX'},
            # {'name':'Money Flow Index','symbol':'MFI'},
            {'name':'Minus Directional Indicator','symbol':'MINUS_DI'},
            {'name':'Minus Directional Movement','symbol':'MINUS_DM'},
            {'name':'Momentum','symbol':'MOM'},
            {'name':'Plus Directional Indicator','symbol':'PLUS_DI'},
            {'name':'Plus Directional Movement','symbol':'PLUS_DM'},
            {'name':'Percentage Price Oscillator','symbol':'PPO'},
            {'name':'Rate of change : ((price/prevPrice)-1)*1','symbol':'ROC'},
            {'name':'Rate of change Percentage: (price-prevPrice)/prevPrice','symbol':'ROCP'},
            {'name':'Rate of change ratio: (price/prevPrice)','symbol':'ROCR'},
            {'name':'Rate of change ratio 1'' scale: (price/prevPrice)*1','symbol':'ROCR1'''},
            {'name':'Relative Strength Index','symbol':'RSI'},
            # {'name':'Stochastic','symbol':'STOCH'},
            # {'name':'Stochastic Fast','symbol':'STOCHF'},
            # {'name':'Stochastic Relative Strength Index','symbol':'STOCHRSI'},
            {'name':'1-day Rate-Of-Change (ROC) of a Triple Smooth EMA','symbol':'TRIX'},
            # {'name':' Ultimate Oscillator','symbol':'ULTOSC'},
            {'name':'Williams R','symbol':'WILLR'}
        ]
        return Momentum_Indicators

    def return_all_TA_LIB_Volume_Indicators(self):
        Volume_Indicators = [
            {'name':'Chaikin A/D Line','symbol':'AD'},           
            {'name':'Chaikin A/D Oscillator','symbol':'ADOSC'},
            {'name':'On Balance Volume','symbol':'OBV'}
        ]
        return Volume_Indicators

    def return_all_TA_LIB_Volatility_Indicators(self):
        Volatility_Indicators = [      
            {'name':'Average True Range','symbol':'ATR'},
            {'name':'Normalized Average True Range','symbol':'NATR'},        
            {'name':'True Range','symbol':'TRANGE'}
        ]
        return Volatility_Indicators


    def return_all_TA_LIB_Price_Transform(self):
        pass

    def return_all_TA_LIB_Cycle_Indicators(self):
        Cycle_Indicators = [ 
            {'name':'Hilbert Transform  Dominant Cycle Period ','symbol':'HT_DCPERIOD '},       
            {'name':'Hilbert Transform  Dominant Cycle Phase','symbol':'HT_DCPHASE  '},
            {'name':'Hilbert Transform  Phasor Component','symbol':'HT_PHASOR   '},         
            {'name':'Hilbert Transform  SineWave','symbol':'HT_SINE'},
            {'name':'Hilbert Transform  Trend vs Cycle Mode','symbol':'HT_TRENDMODE'}
        ]
        return Cycle_Indicators

    def return_all_TA_LIB_Pattern_Recognition(self):
        Pattern_Recognition = [
            {'name':'Two Crows','symbol':'CDL2CROWS '},
            {'name':'Three Black Crows','symbol':'CDL3BLACKCROWS '},
            {'name':'Three Inside Up/Down','symbol':'CDL3INSIDE'},
            {'name':'Three-Line Strike','symbol':'CDL3LINESTRIKE '},
            {'name':'Three Outside Up/Down','symbol':'CDL3OUTSIDE '},
            {'name':'Three Stars In The South','symbol':'CDL3STARSINSOUTH'},
            {'name':'Three Advancing White Soldiers','symbol':'CDL3WHITESOLDIERS'},
            {'name':'Abandoned Baby','symbol':'CDLABANDONEDBABY'},
            {'name':'Advance Block','symbol':'CDLADVANCEBLOCK'},
            {'name':'Belt-hold','symbol':'CDLBELTHOLD '},
            {'name':'Breakaway','symbol':'CDLBREAKAWAY'},
            {'name':'Closing Marubozu','symbol':'CDLCLOSINGMARUBOZU '},
            {'name':'Concealing Baby Swallow','symbol':'CDLCONCEALBABYSWALL'},
            {'name':'Counterattack','symbol':'CDLCOUNTERATTACK'},
            {'name':'Dark Cloud Cover','symbol':'CDLDARKCLOUDCOVER'},
            {'name':'Doji','symbol':'CDLDOJI   '},
            {'name':'Doji Star','symbol':'CDLDOJISTAR '},
            {'name':'Dragonfly Doji','symbol':'CDLDRAGONFLYDOJI'},
            {'name':'Engulfing Pattern','symbol':'CDLENGULFING'},
            {'name':'Evening Doji Star','symbol':'CDLEVENINGDOJISTAR '},
            {'name':'Evening Star','symbol':'CDLEVENINGSTAR '},
            {'name':'Up/Down-gap side-by-side white lines','symbol':'CDLGAPSIDESIDEWHITE'},
            {'name':'Gravestone Doji','symbol':'CDLGRAVESTONEDOJI'},
            {'name':'Hammer','symbol':'CDLHAMMER '},
            {'name':'Hanging Man','symbol':'CDLHANGINGMAN'},
            {'name':'Harami Pattern','symbol':'CDLHARAMI '},
            {'name':'Harami Cross Pattern','symbol':'CDLHARAMICROSS '},
            {'name':'High-Wave Candle','symbol':'CDLHIGHWAVE '},
            {'name':'Hikkake Pattern','symbol':'CDLHIKKAKE'},
            {'name':'Modified Hikkake Pattern','symbol':'CDLHIKKAKEMOD'},
            {'name':'Homing Pigeon','symbol':'CDLHOMINGPIGEON'},
            {'name':'Identical Three Crows','symbol':'CDLIDENTICAL3CROWS '},
            {'name':'In-Neck Pattern','symbol':'CDLINNECK '},
            {'name':'Inverted Hammer','symbol':'CDLINVERTEDHAMMER'},
            {'name':'Kicking','symbol':'CDLKICKING'},
            {'name':'Kicking - bull/bear determined by the longer marubozu','symbol':'CDLKICKINGBYLENGTH '}, 
            {'name':'Ladder Bottom','symbol':'CDLLADDERBOTTOM'},
            {'name':'Long Legged Doji','symbol':'CDLLONGLEGGEDDOJI'},
            {'name':'Long Line Candle','symbol':'CDLLONGLINE '},
            {'name':'Marubozu','symbol':'CDLMARUBOZU '},
            {'name':'Matching Low','symbol':'CDLMATCHINGLOW '},
            {'name':'Mat Hold','symbol':'CDLMATHOLD'},
            {'name':'Morning Doji Star','symbol':'CDLMORNINGDOJISTAR '},
            {'name':'Morning Star','symbol':'CDLMORNINGSTAR '},
            {'name':'On-Neck Pattern','symbol':'CDLONNECK '},
            {'name':'Piercing Pattern','symbol':'CDLPIERCING '},
            {'name':'Rickshaw Man','symbol':'CDLRICKSHAWMAN '},
            {'name':'Rising/Falling Three Methods','symbol':'CDLRISEFALL3METHODS'},
            {'name':'Separating Lines','symbol':'CDLSEPARATINGLINES '},
            {'name':'Shooting Star','symbol':'CDLSHOOTINGSTAR'},
            {'name':'Short Line Candle','symbol':'CDLSHORTLINE'},
            {'name':'Spinning Top','symbol':'CDLSPINNINGTOP '},
            {'name':'Stalled Pattern','symbol':'CDLSTALLEDPATTERN'},
            {'name':'Stick Sandwich','symbol':'CDLSTICKSANDWICH'},
            {'name':'Takuri (Dragonfly Doji with very long lower shadow)','symbol':'CDLTAKURI '},
            {'name':'Tasuki Gap','symbol':'CDLTASUKIGAP'},
            {'name':'Thrusting Pattern','symbol':'CDLTHRUSTING'},
            {'name':'Tristar Pattern','symbol':'CDLTRISTAR'},
            {'name':'Unique 3 River','symbol':'CDLUNIQUE3RIVER'},
            {'name':'Upside Gap Two Crows','symbol':'CDLUPSIDEGAP2CROWS '},
            {'name':'Upside/Downside Gap Three Methods','symbol':'CDLXSIDEGAP3METHODS'},
            {'name':'Check for all ta-lib Candle Patterns','symbol':'CDLALL'}
        ]
        return Pattern_Recognition

    def return_all_TA_LIB_Statistic_Functions(self):
        Statistic_Functions = [     
            {'name':'Beta','symbol':'BETA'},
            {'name':'Pearsons Correlation Coefficient (r)','symbol':'CORREL'},
            {'name':'Linear Regression','symbol':'LINEARREG'},
            {'name':'Linear Regression Angle','symbol':'LINEARREG_ANGLE'},
            {'name':'Linear Regression Intercept','symbol':'LINEARREG_INTERCEPT'},
            {'name':'Linear Regression Slope','symbol':'LINEARREG_SLOPE'},
            {'name':'Standard Deviation','symbol':'STDDEV'},
            {'name':'Time Series Forecast','symbol':'TSF'},
            {'name':'Variance','symbol':'VAR'}
        ]
        return Statistic_Functions

    def return_all_TA_LIB_Math_Transform(self):
        Math_Transform = [
            {'name':'Vector Trigonometric ACos ','symbol':'ACOS'},            
            {'name':'Vector Trigonometric ASin','symbol':'ASIN'},            
            {'name':'Vector Trigonometric ATan ','symbol':'ATAN'},            
            {'name':'Vector Ceil','symbol':'CEIL'},
            {'name':'Vector Trigonometric Cos','symbol':'COS'},           
            {'name':'Vector Trigonometric Cosh ','symbol':'COSH'},            
            {'name':'Vector Arithmetic Exp ','symbol':'EXP'},        
            {'name':'Vector Floor','symbol':'FLOOR'},            
            {'name':'Vector Log Natural','symbol':'LN'},     
            {'name':'Vector Log10','symbol':'LOG10'},
            {'name':'Vector Trigonometric Sin ','symbol':'SIN'},           
            {'name':'Vector Trigonometric Sinh','symbol':'SINH'},            
            {'name':'Vector Square Root','symbol':'SQRT'},     
            {'name':'Vector Trigonometric Tan ','symbol':'TAN'},           
            {'name':'Vector Trigonometric Tanh','symbol':'TANH'}
        ]
        return Math_Transform

    def return_all_TA_LIB_Math_Operators(self):
        Math_Operators = [
            {'name':'Vector Arithmetic Add ','symbol':'ADD'},        
            {'name':'Vector Arithmetic Div ','symbol':'DIV'},        
            {'name':'Highest value over a specified period','symbol':'MAX'},
            {'name':'Index of highest value over ','symbol':'MAXINDEX'}, 
            {'name':'Lowest value over a specified period','symbol':'MIN'},
            {'name':'Index of lowest value over a specified period','symbol':'MININDEX'},  
            {'name':'Lowest and highest values over a specified period','symbol':'MINMAX'},
            {'name':'Indexes of lowest and highest values over a specified period','symbol':'MINMAXINDEX '},
            {'name':'Vector Arithmetic Mult ','symbol':'MULT'},         
            {'name':'Vector Arithmetic Substraction','symbol':'SUB'}, 
            {'name':'Summation','symbol':'SUM'}
        ]
        return Math_Operators