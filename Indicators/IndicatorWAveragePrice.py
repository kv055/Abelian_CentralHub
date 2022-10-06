import talib
import numpy
# from Indicators.getRidofNan import delNan

def Price(Data):
    PriceMaker = numpy.array(Data[1])
    return PriceMaker

# Overlap Studies
# # Bollinger Bands
# def BBANDS(PriceDaten,Range):
#     _BBANDS = talib.BBANDS(Price(PriceDaten),Range)
#     Band1 = _BBANDS[0].tolist()
#     Band2 = _BBANDS[1].tolist()
#     Band3 = _BBANDS[2].tolist()
#     return[[Band1,Band2,Band3],PriceDaten[0],PriceDaten[1],Range]
# Double Exponential Moving Average
def DEMA(PriceDaten,Range):
    _DEMA = talib.DEMA(Price(PriceDaten),Range).tolist()
    return[_DEMA,PriceDaten[0],PriceDaten[1],Range]
# Exponential Moving Average
def EMA(PriceDaten,Range):
    _EMA = talib.EMA(Price(PriceDaten),Range).tolist()
    return[_EMA,PriceDaten[0],PriceDaten[1],Range]
# Hilbert Transform - Instantaneous Trendline
def HT_TRENDLINE(PriceDaten):
    _HT_TRENDLINE = talib.HT_TRENDLINE(Price(PriceDaten)).tolist()
    return[_HT_TRENDLINE,PriceDaten[0],PriceDaten[1]]
# Kaufman Adaptive Moving Average
def KAMA(PriceDaten,Range):
    _KAMA = talib.KAMA(Price(PriceDaten),Range).tolist()
    return[_KAMA,PriceDaten[0],PriceDaten[1],Range]
# Moving average
def MA(PriceDaten,Range):
    _MA = talib.MA(Price(PriceDaten),Range).tolist()
    return[_MA,PriceDaten[0],PriceDaten[1],Range]
# # MESA Adaptive Moving Average
# def MAMA(PriceDaten):
#     _MAMA = talib.MAMA(Price(PriceDaten))
#     Trace1 = _MAMA[0].tolist()
#     Trace2 = _MAMA[1].tolist()
#     return[[Trace1,Trace2],PriceDaten[0],PriceDaten[1]]
# # Moving average with variable period
# def MAVP(PriceDaten,Range):
#     _MAVP = talib.MAVP(Price(PriceDaten),Range).tolist()
#     return[_MAVP,PriceDaten[0],PriceDaten[1],Range]
# MidPoint over period
def MIDPOINT(PriceDaten,Range):
    _MIDPOINT = talib.MIDPOINT(Price(PriceDaten),Range).tolist()
    return[_MIDPOINT,PriceDaten[0],PriceDaten[1],Range]
# # Midpoint Price over period
# def MIDPRICE(PriceDaten,Range):
#     # Requires OHLC Data (high, low, Range)
#     _MIDPRICE= talib.MIDPRICE(Price(PriceDaten),Range).tolist()
#     return[_MIDPRICE,PriceDaten[0],PriceDaten[1],Range]
# # Parabolic SAR
# def SAR(PriceDaten,Range):
#     # Requires OHLC Data (high, low, Range)
#     _SAR = talib.SAR(Price(PriceDaten),Range).tolist()
#     return[_SAR,PriceDaten[0],PriceDaten[1],Range]
# # Parabolic SAR - Extended
# def SAREXT(PriceDaten,Range):
#     # Requires OHLC Data (high, low, Range)
#     _SAREXT= talib.SAREXT(Price(PriceDaten),Range).tolist()
#     return[_SAREXT,PriceDaten[0],PriceDaten[1],Range]
# Simple Moving Average
def SMA(PriceDaten,Range):
    _SMA = talib.SMA(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_SMA,PriceDaten[0],PriceDaten[1],Range] 
# Triple Exponential Moving Average (T3)
def T3(PriceDaten,Range):
    _T3 = talib.T3(Price(PriceDaten),Range).tolist()
    return[_T3,PriceDaten[0],PriceDaten[1],Range]
# Triple Exponential Moving Average
def TEMA(PriceDaten,Range):
    _TEMA = talib.TEMA(Price(PriceDaten),Range).tolist()
    return[_TEMA,PriceDaten[0],PriceDaten[1],Range]
# Triangular Moving Average
def TRIMA(PriceDaten,Range):
    _TRIMA = talib.TRIMA(Price(PriceDaten),Range).tolist()
    return[_TRIMA,PriceDaten[0],PriceDaten[1],Range]
# Weighted Moving Average
def WMA(PriceDaten,Range):
    _WMA = talib.WMA(Price(PriceDaten),Range).tolist()
    return[_WMA,PriceDaten[0],PriceDaten[1],Range]


    
#Momentum Indicators

def ADX(PriceDaten,Range):
    _ADX = talib.ADX(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ADX,PriceDaten[0],PriceDaten[1],Range] 
 
def ADXR(PriceDaten,Range):
    _ADXR = talib.ADXR(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ADXR,PriceDaten[0],PriceDaten[1],Range] 
 
def APO(PriceDaten,Range):
    _APO = talib.APO(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_APO,PriceDaten[0],PriceDaten[1],Range] 
 
def AROON(PriceDaten,Range):
    _AROON = talib.AROON(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_AROON,PriceDaten[0],PriceDaten[1],Range]
 
def AROONOSC(PriceDaten,Range):
    _AROONOSC = talib.AROONOSC(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_AROONOSC,PriceDaten[0],PriceDaten[1],Range] 
 
def BOP(PriceDaten,Range):
    _BOP = talib.BOP(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_BOP,PriceDaten[0],PriceDaten[1],Range] 
 
def CCI(PriceDaten,Range):
    _CCI = talib.CCI(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_CCI,PriceDaten[0],PriceDaten[1],Range] 
 
def CMO(PriceDaten,Range):
    _CMO = talib.CMO(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_CMO,PriceDaten[0],PriceDaten[1],Range] 
 
def DX(PriceDaten,Range):
    _DX = talib.DX(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_DX,PriceDaten[0],PriceDaten[1],Range] 

def MACD(PriceDaten,Range):
    _MACD = talib.MACD(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_MACD,PriceDaten[0],PriceDaten[1],Range] 
 
def MACDEXT(PriceDaten,Range):
    _MACDEXT = talib.MACDEXT(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_MACDEXT,PriceDaten[0],PriceDaten[1],Range] 
 
def MACDFIX(PriceDaten,Range):
    _MACDFIX = talib.MACDFIX(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_MACDFIX,PriceDaten[0],PriceDaten[1],Range] 
 
def MFI(PriceDaten,Range):
    _MFI = talib.MFI(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_MFI,PriceDaten[0],PriceDaten[1],Range] 
 
def MINUS_DI(PriceDaten,Range):
    _MINUS_DI = talib.MINUS_DI(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_MINUS_DI,PriceDaten[0],PriceDaten[1],Range] 
 
def MINUS_DM(PriceDaten,Range):
    _MINUS_DM = talib.MINUS_DM(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_MINUS_DM,PriceDaten[0],PriceDaten[1],Range] 
 
def MOM(PriceDaten,Range):
    _MOM = talib.MOM(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_MOM,PriceDaten[0],PriceDaten[1],Range] 
 
def PLUS_DI(PriceDaten,Range):
    _PLUS_DI = talib.PLUS_DI(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_PLUS_DI,PriceDaten[0],PriceDaten[1],Range] 
 
def PLUS_DM(PriceDaten,Range):
    _PLUS_DM = talib.PLUS_DM(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_PLUS_DM,PriceDaten[0],PriceDaten[1],Range] 
 
def PPO(PriceDaten,Range):
    _PPO = talib.PPO(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_PPO,PriceDaten[0],PriceDaten[1],Range] 
 
def ROC(PriceDaten,Range):
    _ROC = talib.ROC(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ROC,PriceDaten[0],PriceDaten[1],Range] 
 
def ROCP(PriceDaten,Range):
    _ROCP = talib.ROCP(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ROCP,PriceDaten[0],PriceDaten[1],Range] 
 
def ROCR(PriceDaten,Range):
    _ROCR = talib.ROCR(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ROCR,PriceDaten[0],PriceDaten[1],Range] 
 
def ROCR100(PriceDaten,Range):
    _ROCR100 = talib.ROCR100(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ROCR100,PriceDaten[0],PriceDaten[1],Range] 

def RSI(PriceDaten,Range):
    _RSI = talib.RSI(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_RSI,PriceDaten[0],PriceDaten[1],Range] 
 
def STOCH(PriceDaten,Range):
    _STOCH = talib.STOCH(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_STOCH,PriceDaten[0],PriceDaten[1],Range] 
 
def STOCHF(PriceDaten,Range):
    _STOCHF = talib.STOCHF(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_STOCHF,PriceDaten[0],PriceDaten[1],Range] 
 
def STOCHRSI(PriceDaten,Range):
    _STOCHRSI = talib.STOCHRSI(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_STOCHRSI,PriceDaten[0],PriceDaten[1],Range] 
 
def TRIX(PriceDaten,Range):
    _TRIX = talib.TRIX(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_TRIX,PriceDaten[0],PriceDaten[1],Range] 
 
def ULTOSC(PriceDaten,Range):
    _ULTOSC = talib.ULTOSC(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ULTOSC,PriceDaten[0],PriceDaten[1],Range] 
 
def WILLR(PriceDaten,Range):
    _WILLR = talib.WILLR(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_WILLR,PriceDaten[0],PriceDaten[1],Range] 



# Volume Indicators

def AD(PriceDaten,Range):
    _AD = talib.AD(Price(PriceDaten),Range).tolist()
    return[_AD,PriceDaten[0],PriceDaten[1],Range]

def ADOSC(PriceDaten,Range):
    _ADOSC = talib.ADOSC(Price(PriceDaten),Range).tolist()
    return[_ADOSC,PriceDaten[0],PriceDaten[1],Range]

def OBV(PriceDaten,Range):
    _OBV = talib.OBV(Price(PriceDaten),Range).tolist()
    return[_OBV,PriceDaten[0],PriceDaten[1],Range]



# Cycle Indicators

def HT_DCPERIOD(PriceDaten,Range):
    _HT_DCPERIOD = talib.HT_DCPERIOD(Price(PriceDaten),Range).tolist()
    return[_HT_DCPERIOD,PriceDaten[0],PriceDaten[1],Range]

def HT_DCPHASE(PriceDaten,Range):
    _HT_DCPHASE = talib.HT_DCPHASE(Price(PriceDaten),Range).tolist()
    return[_HT_DCPHASE,PriceDaten[0],PriceDaten[1],Range]

def HT_PHASOR(PriceDaten,Range):
    _HT_PHASOR = talib.HT_PHASOR(Price(PriceDaten),Range).tolist()
    return[_HT_PHASOR,PriceDaten[0],PriceDaten[1],Range]

def HT_SINE(PriceDaten,Range):
    _HT_SINE = talib.HT_SINE(Price(PriceDaten),Range).tolist()
    return[_HT_SINE,PriceDaten[0],PriceDaten[1],Range]

def HT_TRENDMODE(PriceDaten,Range):
    _HT_TRENDMODE = talib.HT_TRENDMODE(Price(PriceDaten),Range).tolist()
    return[_HT_TRENDMODE,PriceDaten[0],PriceDaten[1],Range]


#Volatility Indicators

def ATR(PriceDaten,Range):
    _ATR = talib.ATR(Price(PriceDaten),Range).tolist()  
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ATR,PriceDaten[0],PriceDaten[1],Range] 

def NATR(PriceDaten,Range):
    _NATR = talib.NATR(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_NATR,PriceDaten[0],PriceDaten[1],Range] 

def TRANGE(PriceDaten,Range):
    _TRANGE = talib.TRANGE(Price(PriceDaten),Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_TRANGE,PriceDaten[0],PriceDaten[1],Range]         



# Statistic Functions(PriceDaten,Range):

def BETA(PriceDaten,Range):
    _BETA = talib.BETA(Price(PriceDaten),Range).tolist()
    return [_BETA,PriceDaten[0],PriceDaten[1],Range]

# Beta
def CORREL(PriceDaten,Range):
    _CORREL = talib.CORREL(Price(PriceDaten),Range).tolist()
    return [_CORREL,PriceDaten[0],PriceDaten[1],Range]

# Pearson's Correlation Coefficient (r)
def LINEARREG(PriceDaten,Range):
    _LINEARREG = talib.LINEARREG(Price(PriceDaten),Range).tolist()
    return [_LINEARREG,PriceDaten[0],PriceDaten[1],Range]

# Linear Regression
def LINEARREG_ANGLE(PriceDaten,Range):
    _LINEARREG_ANGLE = talib.LINEARREG_ANGLE(Price(PriceDaten),Range).tolist()
    return [_LINEARREG_ANGLE,PriceDaten[0],PriceDaten[1],Range]

# Linear Regression Angle
def LINEARREG_INTERCEPT(PriceDaten,Range):
    _LINEARREG_INTERCEPT = talib.LINEARREG_INTERCEPT(Price(PriceDaten),Range).tolist()
    return [_LINEARREG_INTERCEPT,PriceDaten[0],PriceDaten[1],Range]

# Linear Regression Intercept
def LINEARREG_SLOPE(PriceDaten,Range):
    _LINEARREG_SLOPE = talib.LINEARREG_SLOPE(Price(PriceDaten),Range).tolist()
    return [_LINEARREG_SLOPE,PriceDaten[0],PriceDaten[1],Range]

# Linear Regression Slope
def STDDEV(PriceDaten,Range):
    _STDDEV = talib.STDDEV(Price(PriceDaten),Range).tolist()
    return [_STDDEV,PriceDaten[0],PriceDaten[1],Range]

# Standard Deviation
def TSF(PriceDaten,Range):
    _TSF = talib.TSF(Price(PriceDaten),Range).tolist()
    return [_TSF,PriceDaten[0],PriceDaten[1],Range]

# Time Series Forecast
def VAR(PriceDaten,Range):
    _VAR= talib.VAR(Price(PriceDaten),Range).tolist()
    return [_VAR,PriceDaten[0],PriceDaten[1],Range]  

# Variance


# Math Transform

def ACOS(PriceDaten,Range):
    _ACOS = talib.ACOS(Price(PriceDaten),Range).tolist()
    return [_ACOS,PriceDaten[0],PriceDaten[1],Range]

# Vector Trigonometric ACos
def ASIN(PriceDaten,Range):
    _ASIN = talib.ASIN(Price(PriceDaten),Range).tolist()
    return [_ASIN,PriceDaten[0],PriceDaten[1],Range]

# Vector Trigonometric ASin
def ATAN(PriceDaten,Range):
    _ATAN = talib.ATAN(Price(PriceDaten),Range).tolist()
    return [_ATAN,PriceDaten[0],PriceDaten[1],Range]

# Vector Trigonometric ATan
def CEIL(PriceDaten,Range):
    _CEIL = talib.CEIL(Price(PriceDaten),Range).tolist()
    return [_CEIL,PriceDaten[0],PriceDaten[1],Range]

# Vector Ceil
def COS(PriceDaten,Range):
    _COS = talib.COS(Price(PriceDaten),Range).tolist()
    return [_COS,PriceDaten[0],PriceDaten[1],Range]

# Vector Trigonometric Cos
def COSH(PriceDaten,Range):
    _COSH = talib.COSH(Price(PriceDaten),Range).tolist()
    return [_COSH,PriceDaten[0],PriceDaten[1],Range]

# Vector Trigonometric Cosh
def EXP(PriceDaten,Range):
    _EXP = talib.EXP(Price(PriceDaten),Range).tolist()
    return [_EXP,PriceDaten[0],PriceDaten[1],Range]

# Vector Arithmetic Exp
def FLOOR(PriceDaten,Range):
    _FLOOR = talib.FLOOR(Price(PriceDaten),Range).tolist()
    return [_FLOOR,PriceDaten[0],PriceDaten[1],Range]

# Vector Floor
def LN(PriceDaten,Range):
    _LN = talib.LN(Price(PriceDaten),Range).tolist()
    return [_LN,PriceDaten[0],PriceDaten[1],Range]

# Vector Log Natural
def LOG10(PriceDaten,Range):
    _LOG10 = talib.LOG10(Price(PriceDaten),Range).tolist()
    return [_LOG10,PriceDaten[0],PriceDaten[1],Range]

# Vector Log10
def SIN(PriceDaten,Range):
    _SIN = talib.SIN(Price(PriceDaten),Range).tolist()
    return [_SIN,PriceDaten[0],PriceDaten[1],Range]

# Vector Trigonometric Sin
def SINH(PriceDaten,Range):
    _SINH = talib.SINH(Price(PriceDaten),Range).tolist()
    return [_SINH,PriceDaten[0],PriceDaten[1],Range]

# Vector Trigonometric Sinh
def SQRT(PriceDaten,Range):
    _SQRT = talib.SQRT(Price(PriceDaten),Range).tolist()
    return [_SQRT,PriceDaten[0],PriceDaten[1],Range]

# Vector Square Root
def TAN(PriceDaten,Range):
    _TAN = talib.TAN(Price(PriceDaten),Range).tolist()
    return [_TAN,PriceDaten[0],PriceDaten[1],Range]

# Vector Trigonometric Tan
def TANH(PriceDaten,Range):
    _TANH = talib.TANH(Price(PriceDaten),Range).tolist()
    return [_TANH,PriceDaten[0],PriceDaten[1],Range]

# Vector Trigonometric Tanh



# Math Operators

def ADD(PriceDaten,Range):
    _ADD = talib.ADD(Price(PriceDaten),Range).tolist()
    return [_ADD,PriceDaten[0],PriceDaten[1],Range]
# Vector Arithmetic Add
def DIV(PriceDaten,Range):
    _DIV = talib.DIV(Price(PriceDaten),Range).tolist()
    return [_DIV,PriceDaten[0],PriceDaten[1],Range]
# Vector Arithmetic Div
def MAX(PriceDaten,Range):
    _MAX = talib.MAX(Price(PriceDaten),Range).tolist()
    return [_MAX,PriceDaten[0],PriceDaten[1],Range]
# Highest value over a specified period
def MAXINDEX(PriceDaten,Range):
    _MAXINDEX = talib.MAXINDEX(Price(PriceDaten),Range).tolist()
    return [_MAXINDEX,PriceDaten[0],PriceDaten[1],Range]
# Index of highest value over a specified period
def MIN(PriceDaten,Range):
    _MIN = talib.MIN(Price(PriceDaten),Range).tolist()
    return [_MIN,PriceDaten[0],PriceDaten[1],Range]
# Lowest value over a specified period
def MININDEX(PriceDaten,Range):
    _MININDEX = talib.MININDEX(Price(PriceDaten),Range).tolist()
    return [_MININDEX,PriceDaten[0],PriceDaten[1],Range]
# Index of lowest value over a specified period
def MINMAX(PriceDaten,Range):
    _MINMAX = talib.MINMAX(Price(PriceDaten),Range).tolist()
    return [_MINMAX,PriceDaten[0],PriceDaten[1],Range]
# Lowest and highest values over a specified period
def MINMAXINDEX(PriceDaten,Range):
    _MINMAXINDEX = talib.MINMAXINDEX(Price(PriceDaten),Range).tolist()
    return [_MINMAXINDEX,PriceDaten[0],PriceDaten[1],Range]
# Indexes of lowest and highest values over a specified period
def MULT(PriceDaten,Range):
    _MULT = talib.MULT(Price(PriceDaten),Range).tolist()
    return [_MULT,PriceDaten[0],PriceDaten[1],Range]
# Vector Arithmetic Mult
def SUB(PriceDaten,Range):
    _SUB = talib.SUB(Price(PriceDaten),Range).tolist()
    return [_SUB,PriceDaten[0],PriceDaten[1],Range]
# Vector Arithmetic Substraction
def SUM(PriceDaten,Range):
    _SUM = talib.SUM(Price(PriceDaten),Range).tolist()
    return [_SUM,PriceDaten[0],PriceDaten[1],Range]                  
# Summation