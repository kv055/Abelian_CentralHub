import math
import talib
from copy import deepcopy
import Indicators.find_parent

from PriceData.Get_Price_Data_Class import ImportData

class Indicators:
    def __init__(self, asset_dict):
        price_data_instance = ImportData()
        self.ohlc_as_numpy_array = price_data_instance.return_ohlc_numpy_array(asset_dict)
    
    def delNan(self,list):
        #function that deletes NaN values from a list that is filled with indicator data
        new_list = [item for item in list if not(math.isnan(item)) == True]
        return new_list
    
    def IndicatorsToFormate(self,dataSet):
        formatedIndicators = []
        # If the check is passed continue
        self.DataIntegrityCheck(dataSet)
        # Delete NaN Values from Indicators
        # For Every indicator Dataset we take the firs array and delete the nan Values
        IndicatorDataSetWithoutNaN = self.delNan(dataSet[0])
        
        Period = deepcopy(dataSet[3] - 1)
        #For Every element in the Date List we delete
        TimeCopy = deepcopy(dataSet[1])
        for element in TimeCopy:
            if TimeCopy.index(element) < Period:
                TimeCopy.remove(element)

        #For Every element in the AssetValue List we delete
        AssetValueCopy = deepcopy(dataSet[2])
        for element in AssetValueCopy:
            if AssetValueCopy.index(element) <= Period:
                AssetValueCopy.remove(element)
        
        formatedIndicators = {
            'value': IndicatorDataSetWithoutNaN,
            'time': TimeCopy,
            'assetValue': AssetValueCopy,
            'range': dataSet[3]
        }   
        return formatedIndicators 

    def DataIntegrityCheck(Indicat0r):
        # dataIntegrityCheck checks if all lists have the same lenght to prevent serious bugs in other modules
        # If this one fails it means that the Indicator module is not providing enough Datapoints in any of the Lists
        # Lists must have the same lengths to pass this Check
        dataIntegrityCheck = []

        for element in Indicat0r:
            if type(element) is list:
                length = len(element)
                dataIntegrityCheck.append(length)

        # Uisng all()method
        result = all(element == dataIntegrityCheck[0] for element in dataIntegrityCheck)
        if result == True:
            print("Passed dataIntegrityCheck at ", Indicat0r[3], dataIntegrityCheck) 
        elif result == False:
            print("Failed dataIntegrityCheck at ", Indicat0r[3], dataIntegrityCheck)

        return result


    # Overlap Studies

    # # Bollinger Bands
    # def BBANDS(self,Range):
    #       
    # _BBANDS = talib.BBANDS(self,PriceData),Range)
    #     Band1 = _BBANDS[0].tolist()
    #     Band2 = _BBANDS[1].tolist()
    #     Band3 = _BBANDS[2].tolist()
    #     return[[Band1,Band2,Band3],self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Double Exponential Moving Average
    def DEMA(self,Range):
        
        _DEMA = talib.DEMA(self.ohlc_pricedata['close'],Range).tolist()
        return[_DEMA,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Exponential Moving Average
    def EMA(self,Range):
        Indicator_Object = talib.EMA(self.ohlc_as_numpy_array['np_Close'],Range)
        Indicator_as_list = list(Indicator_Object)
        Indicator_without_NAN = self.delNan(Indicator_as_list)
        return {
            "Indicator_Values": Indicator_without_NAN,
            "Time_Values": [],
            "Indicator_Config": 'Penis'
        }
    # 
    # # Hilbert Transform - Instantaneous Trendline
    # def HT_TRENDLINE(self,PriceData):
    #       
    # _HT_TRENDLINE = talib.HT_TRENDLINE(self.ohlc_pricedata['close']).tolist()
    #     return[_HT_TRENDLINE,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Kaufman Adaptive Moving Average
    def KAMA(self,Range):
        
        _KAMA = talib.KAMA(self.ohlc_pricedata['close'],Range).tolist()
        return[_KAMA,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Moving average
    def MA(self,Range):
        
        _MA = talib.MA(self.ohlc_pricedata['close'],Range).tolist()
        return[_MA,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]
    # 
    # # MESA Adaptive Moving Average
    # def MAMA(self,PriceData):
    #       
    # _MAMA = talib.MAMA(self,PriceData))
    #     Trace1 = _MAMA[0].tolist()
    #     Trace2 = _MAMA[1].tolist()
    #     return[[Trace1,Trace2],self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]
    # 
    # # Moving average with variable period
    # def MAVP(self,Range):
    #       
    # _MAVP = talib.MAVP(self.ohlc_pricedata['close'],Range).tolist()
    #     return[_MAVP,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # MidPoint over period
    def MIDPOINT(self,Range):
        
        _MIDPOINT = talib.MIDPOINT(self.ohlc_pricedata['close'],Range).tolist()
        return[_MIDPOINT,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Midpoint over period
    def MIDPRICE(self,Range):
        
        _MIDPRICE= talib.MIDPRICE(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],Range).tolist()
        return[_MIDPRICE,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Parabolic SAR
    def SAR(self,Range):
        
        _SAR = talib.SAR(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],Range).tolist()
        return[_SAR,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Parabolic SAR - Extended
    def SAREXT(self,Range):
        
        # Requires OHLC Data (high, low, Range)
        _SAREXT= talib.SAREXT(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],Range).tolist()
        return[_SAREXT,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Simple Moving Average
    def SMA(self,Range):
        
        _SMA = talib.SMA(self.ohlc_pricedata['close'],Range).tolist()
        #return Indicator Value, Date, the AssetPrice, and the Range
        return [_SMA,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    # Triple Exponential Moving Average (T3)
    def T3(self,Range):
        
        _T3 = talib.T3(self.ohlc_pricedata['close'],Range).tolist()
        return[_T3,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Triple Exponential Moving Average
    def TEMA(self,Range):
        
        _TEMA = talib.TEMA(self.ohlc_pricedata['close'],Range).tolist()
        return[_TEMA,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Triangular Moving Average
    def TRIMA(self,Range):
        
        _TRIMA = talib.TRIMA(self.ohlc_pricedata['close'],Range).tolist()
        return[_TRIMA,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Weighted Moving Average
    def WMA(self,Range):
        
        _WMA = talib.WMA(self.ohlc_pricedata['close'],Range).tolist()
        return[_WMA,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]


        
    #Momentum Indicators

    # Average Directional Movement Index
    def ADX(self,Range):
        
        _ADX = talib.ADX(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_ADX,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    # Average Directional Movement Index Rating
    def ADXR(self,Range):
        
        _ADXR = talib.ADXR(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_ADXR,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 
    # 
    # Absolute Price Oscillator 
    # def APO(self,Range):
    #       
    # _APO = talib.APO(self.ohlc_pricedata['close'],Range).tolist()
    #     ##return Indicator Value, Date, the AssetPrice, and the Range
    #     return [_APO,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 
    # 
    #  Aroon
    # def AROON(self,Range):
    #       
    # _AROON = talib.AROON(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],Range)
    #     aroondown = _AROON[0].tolist()
    #     aroonup = _AROON[1].tolist()
    #     ##return Indicator Value, Date, the AssetPrice, and the Range
    #     return [[aroondown,aroonup],self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Aroon Oscillator
    def AROONOSC(self,Range):
        
        _AROONOSC = talib.AROONOSC(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_AROONOSC,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    # Balance Of Power
    def BOP(self,PriceData):
        
        _BOP = talib.BOP(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_BOP,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()] 

    # Commodity Channel Index
    def CCI(self,Range):
        
        _CCI = talib.CCI(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_CCI,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    #  Chande Momentum Oscillator
    def CMO(self,Range):
        
        _CMO = talib.CMO(self.ohlc_pricedata['close'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_CMO,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    #  Directional Movement Index
    def DX(self,Range):
        
        _DX = talib.DX(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_DX,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 
    # 
    # # Moving Average Convergence/Divergence
    # def MACD(self,Range):
    #       
    # _MACD = talib.MACD(self.ohlc_pricedata['close'],Range).tolist()
    #     ##return Indicator Value, Date, the AssetPrice, and the Range
    #     return [_MACD,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 
    # 
    # # MACD with controllable MA type
    # def MACDEXT(self,Range):
    #       
    # _MACDEXT = talib.MACDEXT(self.ohlc_pricedata['close'],Range).tolist()
    #     ##return Indicator Value, Date, the AssetPrice, and the Range
    #     return [_MACDEXT,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 
    # 
    # Moving Average Convergence/Divergence Fix 12/26
    # def MACDFIX(self,Range):
    #       
    # _MACDFIX = talib.MACDFIX(self.ohlc_pricedata['close'],Range).tolist()
    #     ##return Indicator Value, Date, the AssetPrice, and the Range
    #     return [_MACDFIX,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 
    # 
    # # Money Flow Index 
    # def MFI(self,Range):
    #       
    # # Indicator requires Volume
    #     _MFI = talib.MFI(self.ohlc_pricedata['close'],Range).tolist()
    #     ##return Indicator Value, Date, the AssetPrice, and the Range
    #     return [_MFI,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    # Minus Directional Indicator
    def MINUS_DI(self,Range):
        
        _MINUS_DI = talib.MINUS_DI(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_MINUS_DI,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    # Minus Directional Movement
    def MINUS_DM(self,Range):
        
        _MINUS_DM = talib.MINUS_DM(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_MINUS_DM,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    # Momentum
    def MOM(self,Range):
        
        _MOM = talib.MOM(self.ohlc_pricedata['close'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_MOM,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    # Plus Directional Indicator
    def PLUS_DI(self,Range):
        
        _PLUS_DI = talib.PLUS_DI(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_PLUS_DI,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    # Plus Directional Movement
    def PLUS_DM(self,Range):
        
        _PLUS_DM = talib.PLUS_DM(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_PLUS_DM,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    # Percentage Price Oscillator
    def PPO(self,Range):
        
        _PPO = talib.PPO(self.ohlc_pricedata['close'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_PPO,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    # Rate of change : ((price/prevPrice)-1)*100
    def ROC(self,Range):
        
        _ROC = talib.ROC(self.ohlc_pricedata['close'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_ROC,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    # Rate of change Percentage: (price-prevPrice)/prevPrice
    def ROCP(self,Range):
        
        _ROCP = talib.ROCP(self.ohlc_pricedata['close'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_ROCP,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    # Rate of change ratio: (price/prevPrice)
    def ROCR(self,Range):
        
        _ROCR = talib.ROCR(self.ohlc_pricedata['close'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_ROCR,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    # Rate of change ratio 100 scale: (price/prevPrice)*100
    def ROCR100(self,Range):
        
        _ROCR100 = talib.ROCR100(self.ohlc_pricedata['close'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_ROCR100,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    # Relative Strength Index
    def RSI(self,Range):
        
        _RSI = talib.RSI(self.ohlc_pricedata['close'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_RSI,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 
    # 
    # # Stochastic
    # def STOCH(self,Range):
    #       
    # _STOCH = talib.STOCH(self.ohlc_pricedata['close'],Range).tolist()
    #     ##return Indicator Value, Date, the AssetPrice, and the Range
    #     return [_STOCH,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 
    # 
    # # Stochastic Fast
    # def STOCHF(self,Range):
    #       
    # _STOCHF = talib.STOCHF(self.ohlc_pricedata['close'],Range).tolist()
    #     ##return Indicator Value, Date, the AssetPrice, and the Range
    #     return [_STOCHF,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 
    # 
    # Stochastic Relative Strength Index
    # def STOCHRSI(self,Range):
    #       
    # _STOCHRSI = talib.STOCHRSI(self.ohlc_pricedata['close'],Range).tolist()
    #     ##return Indicator Value, Date, the AssetPrice, and the Range
    #     return [_STOCHRSI,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    #  1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
    def TRIX(self,Range):
        
        _TRIX = talib.TRIX(self.ohlc_pricedata['close'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_TRIX,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 
    # 
    # # Ultimate Oscillator
    # def ULTOSC(self,Range):
    #       
    # # Indicator requires 3 Ranges
    #     _ULTOSC = talib.ULTOSC(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'],Range).tolist()
    #     ##return Indicator Value, Date, the AssetPrice, and the Range
    #     return [_ULTOSC,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 


    def WILLR(self,Range):
        
        _WILLR = talib.WILLR(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_WILLR,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    
                    
    # # Volume Indicators

    # Chaikin A/D Line
    # def AD(self,PriceData):
    #       
    # _AD = talib.AD(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return[_AD,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Chaikin A/D Oscillator
    # def ADOSC(self,PriceData):
    #       
    # _ADOSC = talib.ADOSC(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return[_ADOSC,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # On Balance Volume
    # def OBV(self,PriceData):
    #       
    # _OBV = talib.OBV(self.ohlc_pricedata['close']).tolist()
    #     return[_OBV,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]



    #Volatility Indicators

    # Average True Range
    def ATR(self,Range):
        
        _ATR = talib.ATR(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'],Range).tolist()  
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_ATR,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    # Normalized Average True Range
    def NATR(self,Range):
        
        _NATR = talib.NATR(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'],Range).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_NATR,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range] 

    # True Range
    def TRANGE(self,Range):
        
        _TRANGE = talib.TRANGE(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
        ##return Indicator Value, Date, the AssetPrice, and the Range
        return [_TRANGE,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]         


    # Cycle Indicators

    # Hilbert Transform - Dominant Cycle Period
    def HT_DCPERIOD(self,PriceData):
        
        _HT_DCPERIOD = talib.HT_DCPERIOD(self.ohlc_pricedata['close']).tolist()
        return[_HT_DCPERIOD,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Hilbert Transform - Dominant Cycle Phase
    def HT_DCPHASE(self,PriceData):
        
        _HT_DCPHASE = talib.HT_DCPHASE(self.ohlc_pricedata['close']).tolist()
        return[_HT_DCPHASE,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Hilbert Transform - Phasor Components
    def HT_PHASOR(self,PriceData):
        
        _HT_PHASOR = talib.HT_PHASOR(self.ohlc_pricedata['close']).tolist()
        return[_HT_PHASOR,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Hilbert Transform - SineWave
    def HT_SINE(self,PriceData):
        
        _HT_SINE = talib.HT_SINE(self.ohlc_pricedata['close']).tolist()
        return[_HT_SINE,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Hilbert Transform - Trend vs Cycle Mode
    def HT_TRENDMODE(self,PriceData):
        
        _HT_TRENDMODE = talib.HT_TRENDMODE(self.ohlc_pricedata['close']).tolist()
        return[_HT_TRENDMODE,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]



    # Statistic Functions:

    # Beta
    def BETA(self,Range):
        
        _BETA = talib.BETA(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],Range).tolist()
        return [_BETA,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Pearson's Correlation Coefficient (r)
    def CORREL(self,Range):
        
        _CORREL = talib.CORREL(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],Range).tolist()
        return [_CORREL,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Linear Regression
    def LINEARREG(self,Range):
        
        _LINEARREG = talib.LINEARREG(self.ohlc_pricedata['close'],Range).tolist()
        return [_LINEARREG,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Linear Regression Angle
    def LINEARREG_ANGLE(self,Range):
        
        _LINEARREG_ANGLE = talib.LINEARREG_ANGLE(self.ohlc_pricedata['close'],Range).tolist()
        return [_LINEARREG_ANGLE,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Linear Regression Intercept
    def LINEARREG_INTERCEPT(self,Range):
        
        _LINEARREG_INTERCEPT = talib.LINEARREG_INTERCEPT(self.ohlc_pricedata['close'],Range).tolist()
        return [_LINEARREG_INTERCEPT,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Linear Regression Slope
    def LINEARREG_SLOPE(self,Range):
        
        _LINEARREG_SLOPE = talib.LINEARREG_SLOPE(self.ohlc_pricedata['close'],Range).tolist()
        return [_LINEARREG_SLOPE,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Standard Deviation
    def STDDEV(self,Range):
        
        _STDDEV = talib.STDDEV(self.ohlc_pricedata['close'],Range).tolist()
        return [_STDDEV,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Time Series Forecast
    def TSF(self,Range):
        
        _TSF = talib.TSF(self.ohlc_pricedata['close'],Range).tolist()
        return [_TSF,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Variance
    def VAR(self,Range):
        
        _VAR= talib.VAR(self.ohlc_pricedata['close'],Range).tolist()
        return [_VAR,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]  


    # Math Transform

    def ACOS(self,PriceData):
        
        _ACOS = talib.ACOS(self.ohlc_pricedata['close']).tolist()
        return [_ACOS,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Vector Trigonometric ACos
    def ASIN(self,PriceData):
        
        _ASIN = talib.ASIN(self.ohlc_pricedata['close']).tolist()
        return [_ASIN,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Vector Trigonometric ASin
    def ATAN(self,PriceData):
        
        _ATAN = talib.ATAN(self.ohlc_pricedata['close']).tolist()
        return [_ATAN,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Vector Trigonometric ATan
    def CEIL(self,PriceData):
        
        _CEIL = talib.CEIL(self.ohlc_pricedata['close']).tolist()
        return [_CEIL,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Vector Ceil
    def COS(self,PriceData):
        
        _COS = talib.COS(self.ohlc_pricedata['close']).tolist()
        return [_COS,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Vector Trigonometric Cos
    def COSH(self,PriceData):
        
        _COSH = talib.COSH(self.ohlc_pricedata['close']).tolist()
        return [_COSH,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Vector Trigonometric Cosh
    def EXP(self,PriceData):
        
        _EXP = talib.EXP(self.ohlc_pricedata['close']).tolist()
        return [_EXP,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Vector Arithmetic Exp
    def FLOOR(self,PriceData):
        
        _FLOOR = talib.FLOOR(self.ohlc_pricedata['close']).tolist()
        return [_FLOOR,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Vector Floor
    def LN(self,PriceData):
        
        _LN = talib.LN(self.ohlc_pricedata['close']).tolist()
        return [_LN,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Vector Log Natural
    def LOG10(self,PriceData):
        
        _LOG10 = talib.LOG10(self.ohlc_pricedata['close']).tolist()
        return [_LOG10,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Vector Log10
    def SIN(self,PriceData):
        
        _SIN = talib.SIN(self.ohlc_pricedata['close']).tolist()
        return [_SIN,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Vector Trigonometric Sin
    def SINH(self,PriceData):
        
        _SINH = talib.SINH(self.ohlc_pricedata['close']).tolist()
        return [_SINH,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]


    # Vector Trigonometric Sinh
    def SQRT(self,PriceData):
        
        _SQRT = talib.SQRT(self.ohlc_pricedata['close']).tolist()
        return [_SQRT,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]


    # Vector Square Root
    def TAN(self,PriceData):
        
        _TAN = talib.TAN(self.ohlc_pricedata['close']).tolist()
        return [_TAN,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]


    # Vector Trigonometric Tan
    def TANH(self,PriceData):
        
        _TANH = talib.TANH(self.ohlc_pricedata['close']).tolist()
        return [_TANH,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Vector Trigonometric Tanh



    # Math Operators


    def ADD(self,PriceData):
        
        _ADD = talib.ADD(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low']).tolist()
        return [_ADD,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Vector Arithmetic Add
    def DIV(self,PriceData):
        
        _DIV = talib.DIV(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low']).tolist()
        return [_DIV,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Vector Arithmetic Div
    def MAX(self,Range):
        
        _MAX = talib.MAX(self.ohlc_pricedata['close'],Range).tolist()
        return [_MAX,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Highest value over a specified period
    def MAXINDEX(self,Range):
        
        _MAXINDEX = talib.MAXINDEX(self.ohlc_pricedata['close'],Range).tolist()
        return [_MAXINDEX,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Index of highest value over a specified period
    def MIN(self,Range):
        
        _MIN = talib.MIN(self.ohlc_pricedata['close'],Range).tolist()
        return [_MIN,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Lowest value over a specified period
    def MININDEX(self,Range):
        
        _MININDEX = talib.MININDEX(self.ohlc_pricedata['close'],Range).tolist()
        return [_MININDEX,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Index of lowest value over a specified period
    def MINMAX(self,Range):
        
        _MINMAX = talib.MINMAX(self.ohlc_pricedata['close'],Range).tolist()
        return [_MINMAX,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Lowest and highest values over a specified period
    def MINMAXINDEX(self,Range):
        
        _MINMAXINDEX = talib.MINMAXINDEX(self.ohlc_pricedata['close'],Range).tolist()
        return [_MINMAXINDEX,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]

    # Indexes of lowest and highest values over a specified period
    def MULT(self,PriceData):
        
        _MULT = talib.MULT(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low']).tolist()
        return [_MULT,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Vector Arithmetic Mult
    def SUB(self,PriceData):
        
        _SUB = talib.SUB(self,self.ohlc_pricedata['high'],self.ohlc_pricedata['low']).tolist()
        return [_SUB,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist()]

    # Vector Arithmetic Substraction
    def SUM(self,Range):
        
        _SUM = talib.SUM(self.ohlc_pricedata['close'],Range).tolist()
        return [_SUM,self.ohlc_pricedata['date'],self.ohlc_pricedata['close'].tolist(),Range]                  
    # Summation
    ######################################################
    # from Patterns.ExecutePatterns import all_candle_patterns
    # # Candlestick Patterns
    # def CDLALL(self,PriceData):
    #     _CDLALL = all_candle_patterns(self,PriceData)
    #     return [_CDLALL,self.ohlc_pricedata['date']]
    ######################################################   
    # def CDL2CROWS(self,PriceData):
    #       
    # _CDL2CROWS  = talib.CDL2CROWS(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDL2CROWS,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDL3BLACKCROWS(self,PriceData):
    #       
    # _CDL3BLACKCROWS = talib.CDL3BLACKCROWS(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDL3BLACKCROWS,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                
    # def CDL3INSIDE(self,PriceData):
    #       
    # _CDL3INSIDE = talib.CDL3INSIDE(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDL3INSIDE,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDL3LINESTRIKE(self,PriceData):
    #       
    # _CDL3LINESTRIKE = talib.CDL3LINESTRIKE(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDL3LINESTRIKE,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                
    # def CDL3OUTSIDE(self,PriceData):
    #       
    # _CDL3OUTSIDE= talib.CDL3OUTSIDE(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDL3OUTSIDE,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDL3STARSINSOUTH(self,PriceData):
    #       
    # _CDL3STARSINSOUTH = talib.CDL3STARSINSOUTH(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDL3STARSINSOUTH,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDL3WHITESOLDIERS (self,PriceData):
    #       
    # _CDL3WHITESOLDIERS= talib.CDL3WHITESOLDIERS (self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDL3WHITESOLDIERS,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLABANDONEDBABY(self,PriceData):
    #       
    # _CDLABANDONEDBABY = talib.CDLABANDONEDBABY(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLABANDONEDBABY,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDLADVANCEBLOCK(self,PriceData):
    #       
    # _CDLADVANCEBLOCK= talib.CDLADVANCEBLOCK(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLADVANCEBLOCK,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                
    # def CDLBELTHOLD(self,PriceData):
    #       
    # _CDLBELTHOLD= talib.CDLBELTHOLD(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLBELTHOLD,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDLBREAKAWAY (self,PriceData):
    #       
    # _CDLBREAKAWAY   = talib.CDLBREAKAWAY (self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLBREAKAWAY,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLCLOSINGMARUBOZU(self,PriceData):
    #       
    # _CDLCLOSINGMARUBOZU= talib.CDLCLOSINGMARUBOZU(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLCLOSINGMARUBOZU,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLCONCEALBABYSWALL(self,PriceData):
    #       
    # _CDLCONCEALBABYSWALL = talib.CDLCONCEALBABYSWALL(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLCONCEALBABYSWALL,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLCOUNTERATTACK(self,PriceData):
    #       
    # _CDLCOUNTERATTACK = talib.CDLCOUNTERATTACK(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLCOUNTERATTACK,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLDARKCLOUDCOVER (self,PriceData):
    #       
    # _CDLDARKCLOUDCOVER= talib.CDLDARKCLOUDCOVER (self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLDARKCLOUDCOVER,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                            
    # def CDLDOJI(self,PriceData):
    #       
    # _CDLDOJI    = talib.CDLDOJI(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLDOJI,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                
    # def CDLDOJISTAR(self,PriceData):
    #       
    # _CDLDOJISTAR= talib.CDLDOJISTAR(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLDOJISTAR,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLDRAGONFLYDOJI(self,PriceData):
    #       
    # _CDLDRAGONFLYDOJI = talib.CDLDRAGONFLYDOJI(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLDRAGONFLYDOJI,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDLENGULFING (self,PriceData):
    #       
    # _CDLENGULFING   = talib.CDLENGULFING (self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLENGULFING,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLEVENINGDOJISTAR(self,PriceData):
    #       
    # _CDLEVENINGDOJISTAR= talib.CDLEVENINGDOJISTAR(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLEVENINGDOJISTAR,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDLEVENINGSTAR(self,PriceData):
    #       
    # _CDLEVENINGSTAR = talib.CDLEVENINGSTAR(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLEVENINGSTAR,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLGAPSIDESIDEWHITE(self,PriceData):
    #       
    # _CDLGAPSIDESIDEWHITE = talib.CDLGAPSIDESIDEWHITE(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLGAPSIDESIDEWHITE,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLGRAVESTONEDOJI (self,PriceData):
    #       
    # _CDLGRAVESTONEDOJI= talib.CDLGRAVESTONEDOJI (self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLGRAVESTONEDOJI,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                
    # def CDLHAMMER(self,PriceData):
    #       
    # _CDLHAMMER  = talib.CDLHAMMER(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLHAMMER,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDLHANGINGMAN(self,PriceData):
    #       
    # _CDLHANGINGMAN  = talib.CDLHANGINGMAN(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLHANGINGMAN,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                
    # def CDLHARAMI(self,PriceData):
    #       
    # _CDLHARAMI  = talib.CDLHARAMI(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLHARAMI,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDLHARAMICROSS(self,PriceData):
    #       
    # _CDLHARAMICROSS = talib.CDLHARAMICROSS(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLHARAMICROSS,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                
    # def CDLHIGHWAVE(self,PriceData):
    #       
    # _CDLHIGHWAVE= talib.CDLHIGHWAVE(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLHIGHWAVE,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                
    # def CDLHIKKAKE(self,PriceData):
    #       
    # _CDLHIKKAKE = talib.CDLHIKKAKE(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLHIKKAKE,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDLHIKKAKEMOD(self,PriceData):
    #       
    # _CDLHIKKAKEMOD  = talib.CDLHIKKAKEMOD(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLHIKKAKEMOD,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDLHOMINGPIGEON(self,PriceData):
    #       
    # _CDLHOMINGPIGEON= talib.CDLHOMINGPIGEON(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLHOMINGPIGEON,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLIDENTICAL3CROWS(self,PriceData):
    #       
    # _CDLIDENTICAL3CROWS= talib.CDLIDENTICAL3CROWS(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLIDENTICAL3CROWS,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                
    # def CDLINNECK(self,PriceData):
    #       
    # _CDLINNECK  = talib.CDLINNECK(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLINNECK,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLINVERTEDHAMMER (self,PriceData):
    #       
    # _CDLINVERTEDHAMMER= talib.CDLINVERTEDHAMMER (self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLINVERTEDHAMMER,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                
    # def CDLKICKING(self,PriceData):
    #       
    # _CDLKICKING = talib.CDLKICKING(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLKICKING,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLKICKINGBYLENGTH(self,PriceData):
    #       
    # _CDLKICKINGBYLENGTH= talib.CDLKICKINGBYLENGTH(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLKICKINGBYLENGTH,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDLLADDERBOTTOM(self,PriceData):
    #       
    # _CDLLADDERBOTTOM= talib.CDLLADDERBOTTOM(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLLADDERBOTTOM,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLLONGLEGGEDDOJI (self,PriceData):
    #       
    # _CDLLONGLEGGEDDOJI= talib.CDLLONGLEGGEDDOJI (self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLLONGLEGGEDDOJI,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                
    # def CDLLONGLINE(self,PriceData):
    #       
    # _CDLLONGLINE= talib.CDLLONGLINE(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLLONGLINE,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                
    # def CDLMARUBOZU(self,PriceData):
    #       
    # _CDLMARUBOZU= talib.CDLMARUBOZU(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLMARUBOZU,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDLMATCHINGLOW(self,PriceData):
    #       
    # _CDLMATCHINGLOW = talib.CDLMATCHINGLOW(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLMATCHINGLOW,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                
    # def CDLMATHOLD(self,PriceData):
    #       
    # _CDLMATHOLD = talib.CDLMATHOLD(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLMATHOLD,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLMORNINGDOJISTAR(self,PriceData):
    #       
    # _CDLMORNINGDOJISTAR= talib.CDLMORNINGDOJISTAR(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLMORNINGDOJISTAR,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDLMORNINGSTAR(self,PriceData):
    #       
    # _CDLMORNINGSTAR = talib.CDLMORNINGSTAR(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLMORNINGSTAR,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                
    # def CDLONNECK(self,PriceData):
    #       
    # _CDLONNECK  = talib.CDLONNECK(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLONNECK,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                
    # def CDLPIERCING(self,PriceData):
    #       
    # _CDLPIERCING= talib.CDLPIERCING(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLPIERCING,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDLRICKSHAWMAN(self,PriceData):
    #       
    # _CDLRICKSHAWMAN = talib.CDLRICKSHAWMAN(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLRICKSHAWMAN,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLRISEFALL3METHODS(self,PriceData):
    #       
    # _CDLRISEFALL3METHODS = talib.CDLRISEFALL3METHODS(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLRISEFALL3METHODS,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLSEPARATINGLINES(self,PriceData):
    #       
    # _CDLSEPARATINGLINES= talib.CDLSEPARATINGLINES(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLSEPARATINGLINES,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDLSHOOTINGSTAR(self,PriceData):
    #       
    # _CDLSHOOTINGSTAR= talib.CDLSHOOTINGSTAR(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLSHOOTINGSTAR,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDLSHORTLINE (self,PriceData):
    #       
    # _CDLSHORTLINE   = talib.CDLSHORTLINE (self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLSHORTLINE,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDLSPINNINGTOP(self,PriceData):
    #       
    # _CDLSPINNINGTOP = talib.CDLSPINNINGTOP(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLSPINNINGTOP,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLSTALLEDPATTERN (self,PriceData):
    #       
    # _CDLSTALLEDPATTERN= talib.CDLSTALLEDPATTERN (self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLSTALLEDPATTERN,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLSTICKSANDWICH(self,PriceData):
    #       
    # _CDLSTICKSANDWICH = talib.CDLSTICKSANDWICH(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLSTICKSANDWICH,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                
    # def CDLTAKURI(self,PriceData):
    #       
    # _CDLTAKURI  = talib.CDLTAKURI(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLTAKURI,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDLTASUKIGAP (self,PriceData):
    #       
    # _CDLTASUKIGAP   = talib.CDLTASUKIGAP (self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLTASUKIGAP,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDLTHRUSTING (self,PriceData):
    #       
    # _CDLTHRUSTING   = talib.CDLTHRUSTING (self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLTHRUSTING,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                
    # def CDLTRISTAR(self,PriceData):
    #       
    # _CDLTRISTAR = talib.CDLTRISTAR(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLTRISTAR,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                    
    # def CDLUNIQUE3RIVER(self,PriceData):
    #       
    # _CDLUNIQUE3RIVER= talib.CDLUNIQUE3RIVER(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLUNIQUE3RIVER,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLUPSIDEGAP2CROWS(self,PriceData):
    #       
    # _CDLUPSIDEGAP2CROWS= talib.CDLUPSIDEGAP2CROWS(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLUPSIDEGAP2CROWS,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
                                        
    # def CDLXSIDEGAP3METHODS(self,PriceData):
    #       
    # _CDLXSIDEGAP3METHODS = talib.CDLXSIDEGAP3METHODS(self,self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close']).tolist()
    #     return [_CDLXSIDEGAP3METHODS,self.ohlc_pricedata['date'],self.ohlc_pricedata['open'],self.ohlc_pricedata['high'],self.ohlc_pricedata['low'],self.ohlc_pricedata['close'].tolist()] 
