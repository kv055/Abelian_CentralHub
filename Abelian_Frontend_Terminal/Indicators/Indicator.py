import talib
from copy import deepcopy

from PriceData.BinanceOHLCforIndicators import OHLCformated


# Overlap Studies

# # Bollinger Bands
# def BBANDS(PriceData,Range):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _BBANDS = talib.BBANDS(PriceData),Range)
#     Band1 = _BBANDS[0].tolist()
#     Band2 = _BBANDS[1].tolist()
#     Band3 = _BBANDS[2].tolist()
#     return[[Band1,Band2,Band3],ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Double Exponential Moving Average
def DEMA(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _DEMA = talib.DEMA(ohlc_price['close'],Range).tolist()
    return[_DEMA,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Exponential Moving Average
def EMA(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _EMA = talib.EMA(ohlc_price['close'],Range).tolist()
    return[_EMA,ohlc_price['date'],ohlc_price['close'].tolist(),Range]
# 
# # Hilbert Transform - Instantaneous Trendline
# def HT_TRENDLINE(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _HT_TRENDLINE = talib.HT_TRENDLINE(ohlc_price['close']).tolist()
#     return[_HT_TRENDLINE,ohlc_price['date'],ohlc_price['close'].tolist()]

# Kaufman Adaptive Moving Average
def KAMA(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _KAMA = talib.KAMA(ohlc_price['close'],Range).tolist()
    return[_KAMA,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Moving average
def MA(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _MA = talib.MA(ohlc_price['close'],Range).tolist()
    return[_MA,ohlc_price['date'],ohlc_price['close'].tolist(),Range]
# 
# # MESA Adaptive Moving Average
# def MAMA(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _MAMA = talib.MAMA(PriceData))
#     Trace1 = _MAMA[0].tolist()
#     Trace2 = _MAMA[1].tolist()
#     return[[Trace1,Trace2],ohlc_price['date'],ohlc_price['close'].tolist()]
# 
# # Moving average with variable period
# def MAVP(PriceData,Range):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _MAVP = talib.MAVP(ohlc_price['close'],Range).tolist()
#     return[_MAVP,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# MidPoint over period
def MIDPOINT(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _MIDPOINT = talib.MIDPOINT(ohlc_price['close'],Range).tolist()
    return[_MIDPOINT,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Midpoint over period
def MIDPRICE(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _MIDPRICE= talib.MIDPRICE(PriceData['high'],PriceData['low'],Range).tolist()
    return[_MIDPRICE,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Parabolic SAR
def SAR(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _SAR = talib.SAR(PriceData['high'],PriceData['low'],Range).tolist()
    return[_SAR,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Parabolic SAR - Extended
def SAREXT(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    # Requires OHLC Data (high, low, Range)
    _SAREXT= talib.SAREXT(PriceData['high'],PriceData['low'],Range).tolist()
    return[_SAREXT,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Simple Moving Average
def SMA(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _SMA = talib.SMA(ohlc_price['close'],Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_SMA,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

# Triple Exponential Moving Average (T3)
def T3(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _T3 = talib.T3(ohlc_price['close'],Range).tolist()
    return[_T3,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Triple Exponential Moving Average
def TEMA(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _TEMA = talib.TEMA(ohlc_price['close'],Range).tolist()
    return[_TEMA,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Triangular Moving Average
def TRIMA(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _TRIMA = talib.TRIMA(ohlc_price['close'],Range).tolist()
    return[_TRIMA,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Weighted Moving Average
def WMA(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _WMA = talib.WMA(ohlc_price['close'],Range).tolist()
    return[_WMA,ohlc_price['date'],ohlc_price['close'].tolist(),Range]


    
#Momentum Indicators

# Average Directional Movement Index
def ADX(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _ADX = talib.ADX(PriceData['high'],PriceData['low'],ohlc_price['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ADX,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

# Average Directional Movement Index Rating
def ADXR(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _ADXR = talib.ADXR(PriceData['high'],PriceData['low'],ohlc_price['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ADXR,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 
# 
# Absolute Price Oscillator 
# def APO(PriceData,Range):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _APO = talib.APO(ohlc_price['close'],Range).tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [_APO,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 
# 
#  Aroon
# def AROON(PriceData,Range):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _AROON = talib.AROON(PriceData['high'],PriceData['low'],Range)
#     aroondown = _AROON[0].tolist()
#     aroonup = _AROON[1].tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [[aroondown,aroonup],ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Aroon Oscillator
def AROONOSC(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _AROONOSC = talib.AROONOSC(PriceData['high'],PriceData['low'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_AROONOSC,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

# Balance Of Power
def BOP(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _BOP = talib.BOP(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_BOP,ohlc_price['date'],ohlc_price['close'].tolist()] 

# Commodity Channel Index
def CCI(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _CCI = talib.CCI(PriceData['high'],PriceData['low'],ohlc_price['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_CCI,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

#  Chande Momentum Oscillator
def CMO(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _CMO = talib.CMO(ohlc_price['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_CMO,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

#  Directional Movement Index
def DX(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _DX = talib.DX(PriceData['high'],PriceData['low'],ohlc_price['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_DX,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 
# 
# # Moving Average Convergence/Divergence
# def MACD(PriceData,Range):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _MACD = talib.MACD(ohlc_price['close'],Range).tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [_MACD,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 
# 
# # MACD with controllable MA type
# def MACDEXT(PriceData,Range):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _MACDEXT = talib.MACDEXT(ohlc_price['close'],Range).tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [_MACDEXT,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 
# 
# Moving Average Convergence/Divergence Fix 12/26
# def MACDFIX(PriceData,Range):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _MACDFIX = talib.MACDFIX(ohlc_price['close'],Range).tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [_MACDFIX,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 
# 
# # Money Flow Index 
# def MFI(PriceData,Range):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# # Indicator requires Volume
#     _MFI = talib.MFI(ohlc_price['close'],Range).tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [_MFI,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

# Minus Directional Indicator
def MINUS_DI(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _MINUS_DI = talib.MINUS_DI(PriceData['high'],PriceData['low'],ohlc_price['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_MINUS_DI,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

# Minus Directional Movement
def MINUS_DM(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _MINUS_DM = talib.MINUS_DM(PriceData['high'],PriceData['low'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_MINUS_DM,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

# Momentum
def MOM(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _MOM = talib.MOM(ohlc_price['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_MOM,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

# Plus Directional Indicator
def PLUS_DI(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _PLUS_DI = talib.PLUS_DI(PriceData['high'],PriceData['low'],ohlc_price['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_PLUS_DI,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

# Plus Directional Movement
def PLUS_DM(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _PLUS_DM = talib.PLUS_DM(PriceData['high'],PriceData['low'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_PLUS_DM,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

# Percentage Price Oscillator
def PPO(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _PPO = talib.PPO(ohlc_price['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_PPO,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

# Rate of change : ((price/prevPrice)-1)*100
def ROC(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _ROC = talib.ROC(ohlc_price['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ROC,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

# Rate of change Percentage: (price-prevPrice)/prevPrice
def ROCP(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _ROCP = talib.ROCP(ohlc_price['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ROCP,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

# Rate of change ratio: (price/prevPrice)
def ROCR(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _ROCR = talib.ROCR(ohlc_price['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ROCR,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

# Rate of change ratio 100 scale: (price/prevPrice)*100
def ROCR100(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _ROCR100 = talib.ROCR100(ohlc_price['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ROCR100,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

# Relative Strength Index
def RSI(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _RSI = talib.RSI(ohlc_price['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_RSI,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 
# 
# # Stochastic
# def STOCH(PriceData,Range):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _STOCH = talib.STOCH(ohlc_price['close'],Range).tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [_STOCH,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 
# 
# # Stochastic Fast
# def STOCHF(PriceData,Range):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _STOCHF = talib.STOCHF(ohlc_price['close'],Range).tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [_STOCHF,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 
# 
# Stochastic Relative Strength Index
# def STOCHRSI(PriceData,Range):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _STOCHRSI = talib.STOCHRSI(ohlc_price['close'],Range).tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [_STOCHRSI,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

#  1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
def TRIX(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _TRIX = talib.TRIX(ohlc_price['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_TRIX,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 
# 
# # Ultimate Oscillator
# def ULTOSC(PriceData,Range):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# # Indicator requires 3 Ranges
#     _ULTOSC = talib.ULTOSC(PriceData['high'],PriceData['low'],ohlc_price['close'],Range).tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [_ULTOSC,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 


def WILLR(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _WILLR = talib.WILLR(PriceData['high'],PriceData['low'],ohlc_price['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_WILLR,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

 
                 
# # Volume Indicators

# Chaikin A/D Line
# def AD(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _AD = talib.AD(PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return[_AD,ohlc_price['date'],ohlc_price['close'].tolist()]

# Chaikin A/D Oscillator
# def ADOSC(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _ADOSC = talib.ADOSC(PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return[_ADOSC,ohlc_price['date'],ohlc_price['close'].tolist()]

# On Balance Volume
# def OBV(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _OBV = talib.OBV(ohlc_price['close']).tolist()
#     return[_OBV,ohlc_price['date'],ohlc_price['close'].tolist()]



#Volatility Indicators

# Average True Range
def ATR(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _ATR = talib.ATR(PriceData['high'],PriceData['low'],ohlc_price['close'],Range).tolist()  
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ATR,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

# Normalized Average True Range
def NATR(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _NATR = talib.NATR(PriceData['high'],PriceData['low'],ohlc_price['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_NATR,ohlc_price['date'],ohlc_price['close'].tolist(),Range] 

# True Range
def TRANGE(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _TRANGE = talib.TRANGE(PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_TRANGE,ohlc_price['date'],ohlc_price['close'].tolist()]         


# Cycle Indicators

# Hilbert Transform - Dominant Cycle Period
def HT_DCPERIOD(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _HT_DCPERIOD = talib.HT_DCPERIOD(ohlc_price['close']).tolist()
    return[_HT_DCPERIOD,ohlc_price['date'],ohlc_price['close'].tolist()]

# Hilbert Transform - Dominant Cycle Phase
def HT_DCPHASE(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _HT_DCPHASE = talib.HT_DCPHASE(ohlc_price['close']).tolist()
    return[_HT_DCPHASE,ohlc_price['date'],ohlc_price['close'].tolist()]

# Hilbert Transform - Phasor Components
def HT_PHASOR(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _HT_PHASOR = talib.HT_PHASOR(ohlc_price['close']).tolist()
    return[_HT_PHASOR,ohlc_price['date'],ohlc_price['close'].tolist()]

# Hilbert Transform - SineWave
def HT_SINE(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _HT_SINE = talib.HT_SINE(ohlc_price['close']).tolist()
    return[_HT_SINE,ohlc_price['date'],ohlc_price['close'].tolist()]

# Hilbert Transform - Trend vs Cycle Mode
def HT_TRENDMODE(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _HT_TRENDMODE = talib.HT_TRENDMODE(ohlc_price['close']).tolist()
    return[_HT_TRENDMODE,ohlc_price['date'],ohlc_price['close'].tolist()]



# Statistic Functions:

# Beta
def BETA(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _BETA = talib.BETA(PriceData['high'],PriceData['low'],Range).tolist()
    return [_BETA,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Pearson's Correlation Coefficient (r)
def CORREL(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _CORREL = talib.CORREL(PriceData['high'],PriceData['low'],Range).tolist()
    return [_CORREL,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Linear Regression
def LINEARREG(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _LINEARREG = talib.LINEARREG(ohlc_price['close'],Range).tolist()
    return [_LINEARREG,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Linear Regression Angle
def LINEARREG_ANGLE(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _LINEARREG_ANGLE = talib.LINEARREG_ANGLE(ohlc_price['close'],Range).tolist()
    return [_LINEARREG_ANGLE,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Linear Regression Intercept
def LINEARREG_INTERCEPT(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _LINEARREG_INTERCEPT = talib.LINEARREG_INTERCEPT(ohlc_price['close'],Range).tolist()
    return [_LINEARREG_INTERCEPT,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Linear Regression Slope
def LINEARREG_SLOPE(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _LINEARREG_SLOPE = talib.LINEARREG_SLOPE(ohlc_price['close'],Range).tolist()
    return [_LINEARREG_SLOPE,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Standard Deviation
def STDDEV(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _STDDEV = talib.STDDEV(ohlc_price['close'],Range).tolist()
    return [_STDDEV,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Time Series Forecast
def TSF(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _TSF = talib.TSF(ohlc_price['close'],Range).tolist()
    return [_TSF,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Variance
def VAR(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _VAR= talib.VAR(ohlc_price['close'],Range).tolist()
    return [_VAR,ohlc_price['date'],ohlc_price['close'].tolist(),Range]  


# Math Transform

def ACOS(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _ACOS = talib.ACOS(ohlc_price['close']).tolist()
    return [_ACOS,ohlc_price['date'],ohlc_price['close'].tolist()]

# Vector Trigonometric ACos
def ASIN(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _ASIN = talib.ASIN(ohlc_price['close']).tolist()
    return [_ASIN,ohlc_price['date'],ohlc_price['close'].tolist()]

# Vector Trigonometric ASin
def ATAN(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _ATAN = talib.ATAN(ohlc_price['close']).tolist()
    return [_ATAN,ohlc_price['date'],ohlc_price['close'].tolist()]

# Vector Trigonometric ATan
def CEIL(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _CEIL = talib.CEIL(ohlc_price['close']).tolist()
    return [_CEIL,ohlc_price['date'],ohlc_price['close'].tolist()]

# Vector Ceil
def COS(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _COS = talib.COS(ohlc_price['close']).tolist()
    return [_COS,ohlc_price['date'],ohlc_price['close'].tolist()]

# Vector Trigonometric Cos
def COSH(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _COSH = talib.COSH(ohlc_price['close']).tolist()
    return [_COSH,ohlc_price['date'],ohlc_price['close'].tolist()]

# Vector Trigonometric Cosh
def EXP(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _EXP = talib.EXP(ohlc_price['close']).tolist()
    return [_EXP,ohlc_price['date'],ohlc_price['close'].tolist()]

# Vector Arithmetic Exp
def FLOOR(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _FLOOR = talib.FLOOR(ohlc_price['close']).tolist()
    return [_FLOOR,ohlc_price['date'],ohlc_price['close'].tolist()]

# Vector Floor
def LN(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _LN = talib.LN(ohlc_price['close']).tolist()
    return [_LN,ohlc_price['date'],ohlc_price['close'].tolist()]

# Vector Log Natural
def LOG10(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _LOG10 = talib.LOG10(ohlc_price['close']).tolist()
    return [_LOG10,ohlc_price['date'],ohlc_price['close'].tolist()]

# Vector Log10
def SIN(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _SIN = talib.SIN(ohlc_price['close']).tolist()
    return [_SIN,ohlc_price['date'],ohlc_price['close'].tolist()]

# Vector Trigonometric Sin
def SINH(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _SINH = talib.SINH(ohlc_price['close']).tolist()
    return [_SINH,ohlc_price['date'],ohlc_price['close'].tolist()]


# Vector Trigonometric Sinh
def SQRT(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _SQRT = talib.SQRT(ohlc_price['close']).tolist()
    return [_SQRT,ohlc_price['date'],ohlc_price['close'].tolist()]


# Vector Square Root
def TAN(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _TAN = talib.TAN(ohlc_price['close']).tolist()
    return [_TAN,ohlc_price['date'],ohlc_price['close'].tolist()]


# Vector Trigonometric Tan
def TANH(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _TANH = talib.TANH(ohlc_price['close']).tolist()
    return [_TANH,ohlc_price['date'],ohlc_price['close'].tolist()]

# Vector Trigonometric Tanh



# Math Operators


def ADD(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _ADD = talib.ADD(PriceData['high'],PriceData['low']).tolist()
    return [_ADD,ohlc_price['date'],ohlc_price['close'].tolist()]

# Vector Arithmetic Add
def DIV(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _DIV = talib.DIV(PriceData['high'],PriceData['low']).tolist()
    return [_DIV,ohlc_price['date'],ohlc_price['close'].tolist()]

# Vector Arithmetic Div
def MAX(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _MAX = talib.MAX(ohlc_price['close'],Range).tolist()
    return [_MAX,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Highest value over a specified period
def MAXINDEX(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _MAXINDEX = talib.MAXINDEX(ohlc_price['close'],Range).tolist()
    return [_MAXINDEX,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Index of highest value over a specified period
def MIN(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _MIN = talib.MIN(ohlc_price['close'],Range).tolist()
    return [_MIN,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Lowest value over a specified period
def MININDEX(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _MININDEX = talib.MININDEX(ohlc_price['close'],Range).tolist()
    return [_MININDEX,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Index of lowest value over a specified period
def MINMAX(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _MINMAX = talib.MINMAX(ohlc_price['close'],Range).tolist()
    return [_MINMAX,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Lowest and highest values over a specified period
def MINMAXINDEX(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _MINMAXINDEX = talib.MINMAXINDEX(ohlc_price['close'],Range).tolist()
    return [_MINMAXINDEX,ohlc_price['date'],ohlc_price['close'].tolist(),Range]

# Indexes of lowest and highest values over a specified period
def MULT(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _MULT = talib.MULT(PriceData['high'],PriceData['low']).tolist()
    return [_MULT,ohlc_price['date'],ohlc_price['close'].tolist()]

# Vector Arithmetic Mult
def SUB(PriceData):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _SUB = talib.SUB(PriceData['high'],PriceData['low']).tolist()
    return [_SUB,ohlc_price['date'],ohlc_price['close'].tolist()]

# Vector Arithmetic Substraction
def SUM(PriceData,Range):
    ohlc_price = deepcopy(OHLCformated(PriceData))
    _SUM = talib.SUM(ohlc_price['close'],Range).tolist()
    return [_SUM,ohlc_price['date'],ohlc_price['close'].tolist(),Range]                  
# Summation

from Patterns.ExecutePatterns import all_candle_patterns
# Candlestick Patterns
def CDLALL(PriceData):
    ohlc_price = deepcopy(PriceData)
    _CDLALL = all_candle_patterns(ohlc_price)
    return _CDLALL
    
# def CDL2CROWS(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDL2CROWS  = talib.CDL2CROWS(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDL2CROWS,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDL3BLACKCROWS(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDL3BLACKCROWS = talib.CDL3BLACKCROWS(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDL3BLACKCROWS,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                             
# def CDL3INSIDE(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDL3INSIDE = talib.CDL3INSIDE(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDL3INSIDE,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDL3LINESTRIKE(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDL3LINESTRIKE = talib.CDL3LINESTRIKE(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDL3LINESTRIKE,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                             
# def CDL3OUTSIDE(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDL3OUTSIDE= talib.CDL3OUTSIDE(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDL3OUTSIDE,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDL3STARSINSOUTH(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDL3STARSINSOUTH = talib.CDL3STARSINSOUTH(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDL3STARSINSOUTH,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDL3WHITESOLDIERS (PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDL3WHITESOLDIERS= talib.CDL3WHITESOLDIERS (PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDL3WHITESOLDIERS,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLABANDONEDBABY(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLABANDONEDBABY = talib.CDLABANDONEDBABY(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLABANDONEDBABY,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDLADVANCEBLOCK(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLADVANCEBLOCK= talib.CDLADVANCEBLOCK(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLADVANCEBLOCK,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                             
# def CDLBELTHOLD(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLBELTHOLD= talib.CDLBELTHOLD(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLBELTHOLD,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDLBREAKAWAY (PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLBREAKAWAY   = talib.CDLBREAKAWAY (PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLBREAKAWAY,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLCLOSINGMARUBOZU(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLCLOSINGMARUBOZU= talib.CDLCLOSINGMARUBOZU(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLCLOSINGMARUBOZU,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLCONCEALBABYSWALL(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLCONCEALBABYSWALL = talib.CDLCONCEALBABYSWALL(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLCONCEALBABYSWALL,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLCOUNTERATTACK(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLCOUNTERATTACK = talib.CDLCOUNTERATTACK(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLCOUNTERATTACK,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLDARKCLOUDCOVER (PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLDARKCLOUDCOVER= talib.CDLDARKCLOUDCOVER (PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLDARKCLOUDCOVER,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                         
# def CDLDOJI(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLDOJI    = talib.CDLDOJI(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLDOJI,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                             
# def CDLDOJISTAR(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLDOJISTAR= talib.CDLDOJISTAR(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLDOJISTAR,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLDRAGONFLYDOJI(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLDRAGONFLYDOJI = talib.CDLDRAGONFLYDOJI(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLDRAGONFLYDOJI,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDLENGULFING (PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLENGULFING   = talib.CDLENGULFING (PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLENGULFING,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLEVENINGDOJISTAR(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLEVENINGDOJISTAR= talib.CDLEVENINGDOJISTAR(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLEVENINGDOJISTAR,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDLEVENINGSTAR(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLEVENINGSTAR = talib.CDLEVENINGSTAR(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLEVENINGSTAR,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLGAPSIDESIDEWHITE(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLGAPSIDESIDEWHITE = talib.CDLGAPSIDESIDEWHITE(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLGAPSIDESIDEWHITE,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLGRAVESTONEDOJI (PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLGRAVESTONEDOJI= talib.CDLGRAVESTONEDOJI (PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLGRAVESTONEDOJI,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                             
# def CDLHAMMER(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLHAMMER  = talib.CDLHAMMER(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLHAMMER,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDLHANGINGMAN(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLHANGINGMAN  = talib.CDLHANGINGMAN(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLHANGINGMAN,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                             
# def CDLHARAMI(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLHARAMI  = talib.CDLHARAMI(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLHARAMI,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDLHARAMICROSS(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLHARAMICROSS = talib.CDLHARAMICROSS(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLHARAMICROSS,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                             
# def CDLHIGHWAVE(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLHIGHWAVE= talib.CDLHIGHWAVE(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLHIGHWAVE,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                             
# def CDLHIKKAKE(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLHIKKAKE = talib.CDLHIKKAKE(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLHIKKAKE,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDLHIKKAKEMOD(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLHIKKAKEMOD  = talib.CDLHIKKAKEMOD(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLHIKKAKEMOD,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDLHOMINGPIGEON(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLHOMINGPIGEON= talib.CDLHOMINGPIGEON(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLHOMINGPIGEON,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLIDENTICAL3CROWS(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLIDENTICAL3CROWS= talib.CDLIDENTICAL3CROWS(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLIDENTICAL3CROWS,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                             
# def CDLINNECK(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLINNECK  = talib.CDLINNECK(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLINNECK,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLINVERTEDHAMMER (PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLINVERTEDHAMMER= talib.CDLINVERTEDHAMMER (PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLINVERTEDHAMMER,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                             
# def CDLKICKING(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLKICKING = talib.CDLKICKING(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLKICKING,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLKICKINGBYLENGTH(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLKICKINGBYLENGTH= talib.CDLKICKINGBYLENGTH(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLKICKINGBYLENGTH,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDLLADDERBOTTOM(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLLADDERBOTTOM= talib.CDLLADDERBOTTOM(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLLADDERBOTTOM,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLLONGLEGGEDDOJI (PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLLONGLEGGEDDOJI= talib.CDLLONGLEGGEDDOJI (PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLLONGLEGGEDDOJI,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                             
# def CDLLONGLINE(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLLONGLINE= talib.CDLLONGLINE(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLLONGLINE,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                             
# def CDLMARUBOZU(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLMARUBOZU= talib.CDLMARUBOZU(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLMARUBOZU,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDLMATCHINGLOW(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLMATCHINGLOW = talib.CDLMATCHINGLOW(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLMATCHINGLOW,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                             
# def CDLMATHOLD(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLMATHOLD = talib.CDLMATHOLD(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLMATHOLD,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLMORNINGDOJISTAR(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLMORNINGDOJISTAR= talib.CDLMORNINGDOJISTAR(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLMORNINGDOJISTAR,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDLMORNINGSTAR(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLMORNINGSTAR = talib.CDLMORNINGSTAR(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLMORNINGSTAR,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                             
# def CDLONNECK(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLONNECK  = talib.CDLONNECK(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLONNECK,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                             
# def CDLPIERCING(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLPIERCING= talib.CDLPIERCING(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLPIERCING,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDLRICKSHAWMAN(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLRICKSHAWMAN = talib.CDLRICKSHAWMAN(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLRICKSHAWMAN,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLRISEFALL3METHODS(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLRISEFALL3METHODS = talib.CDLRISEFALL3METHODS(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLRISEFALL3METHODS,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLSEPARATINGLINES(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLSEPARATINGLINES= talib.CDLSEPARATINGLINES(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLSEPARATINGLINES,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDLSHOOTINGSTAR(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLSHOOTINGSTAR= talib.CDLSHOOTINGSTAR(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLSHOOTINGSTAR,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDLSHORTLINE (PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLSHORTLINE   = talib.CDLSHORTLINE (PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLSHORTLINE,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDLSPINNINGTOP(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLSPINNINGTOP = talib.CDLSPINNINGTOP(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLSPINNINGTOP,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLSTALLEDPATTERN (PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLSTALLEDPATTERN= talib.CDLSTALLEDPATTERN (PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLSTALLEDPATTERN,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLSTICKSANDWICH(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLSTICKSANDWICH = talib.CDLSTICKSANDWICH(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLSTICKSANDWICH,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                             
# def CDLTAKURI(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLTAKURI  = talib.CDLTAKURI(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLTAKURI,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDLTASUKIGAP (PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLTASUKIGAP   = talib.CDLTASUKIGAP (PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLTASUKIGAP,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDLTHRUSTING (PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLTHRUSTING   = talib.CDLTHRUSTING (PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLTHRUSTING,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                             
# def CDLTRISTAR(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLTRISTAR = talib.CDLTRISTAR(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLTRISTAR,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                 
# def CDLUNIQUE3RIVER(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLUNIQUE3RIVER= talib.CDLUNIQUE3RIVER(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLUNIQUE3RIVER,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLUPSIDEGAP2CROWS(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLUPSIDEGAP2CROWS= talib.CDLUPSIDEGAP2CROWS(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLUPSIDEGAP2CROWS,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
                                     
# def CDLXSIDEGAP3METHODS(PriceData):
#   ohlc_price = deepcopy(OHLCformated(PriceData))    
# _CDLXSIDEGAP3METHODS = talib.CDLXSIDEGAP3METHODS(PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close']).tolist()
#     return [_CDLXSIDEGAP3METHODS,ohlc_price['date'],PriceData['open'],PriceData['high'],PriceData['low'],ohlc_price['close'].tolist()] 
