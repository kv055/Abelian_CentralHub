import find_parent
import Indicators.Indicator as Indicator
from Strategies.MAFormater import IndicatorsToFormate
import Indicators.Visualize_Indicators as VisIndicator


def InitSelectedIndicator(symbol,PriceData,Timeframe):
    # print(symbol,PriceData,Timeframe)
    
    # Overlap Studies
    # if(symbol == 'BBANDS'):
    #     formated = VisIndicator.visualize_BBANDS(PriceData,Timeframe)
    #     return formated
    if(symbol == 'DEMA'):
        formated = VisIndicator.visualize_DEMA(PriceData,Timeframe)
        return formated
    elif(symbol == 'EMA'):
        formated = VisIndicator.visualize_EMA(PriceData,Timeframe)
        return formated
    elif(symbol == 'HT_TRENDLINE'):
        formated = VisIndicator.visualize_HT_TRENDLINE(PriceData)
        return formated
    elif(symbol == 'KAMA'):
        formated = VisIndicator.visualize_KAMA(PriceData,Timeframe)
        return formated
    elif(symbol == 'MA'):
        formated = VisIndicator.visualize_MA(PriceData,Timeframe)
        return formated
    # elif(symbol == 'MAMA'):
    #     formated = VisIndicator.visualize_MAMA(PriceData,Timeframe)
    #     return formated
    # elif(symbol == 'MAVP'):
    #     formated = VisIndicator.visualize_MAVP(PriceData,Timeframe)
    #     return formated
    elif(symbol == 'MIDPOINT'):
        formated = VisIndicator.visualize_MIDPOINT(PriceData,Timeframe)
        return formated
    # elif(symbol == 'MIDPRICE'):
    #     formated = VisIndicator.visualize_MIDPRICE(PriceData,Timeframe)
    #     return formated
    # elif(symbol == 'SAR'):
    #     formated = VisIndicator.visualize_SAR(PriceData,Timeframe)
    #     return formated
    # elif(symbol == 'SAREXT'):
    #     formated = VisIndicator.visualize_SAREXT(PriceData,Timeframe)
    #     return formated
    elif(symbol == 'SMA'):
        formated = VisIndicator.visualize_SMA(PriceData,Timeframe)
        return formated
    elif(symbol == 'T3'):
        formated = VisIndicator.visualize_T3(PriceData,Timeframe)
        return formated
    elif(symbol == 'TEMA'):
        formated = VisIndicator.visualize_TEMA(PriceData,Timeframe)
        return formated
    elif(symbol == 'TRIMA'):
        formated = VisIndicator.visualize_TRIMA(PriceData,Timeframe)
        return formated
    elif(symbol == 'WMA'):
        formated = VisIndicator.visualize_WMA(PriceData,Timeframe)
        return formated

    # Momentum Indicators 
    elif(symbol == 'ADX'):
        formated = VisIndicator.visualize_ADX(PriceData,Timeframe)
        return formated
    elif(symbol == 'ADXR'):
        formated = VisIndicator.visualize_ADXR(PriceData,Timeframe)
        return formated
    elif(symbol == 'APO'):
        formated = VisIndicator.visualize_APO(PriceData,Timeframe)
        return formated
    elif(symbol == 'AROON'):
        formated = VisIndicator.visualize_AROON(PriceData,Timeframe)
        return formated
    elif(symbol == 'AROONOSC'):
        formated = VisIndicator.visualize_AROONOSC(PriceData,Timeframe)
        return formated
    elif(symbol == 'BOP'):
        formated = VisIndicator.visualize_BOP(PriceData,Timeframe)
        return formated
    elif(symbol == 'CCI'):
        formated = VisIndicator.visualize_CCI(PriceData,Timeframe)
        return formated
    elif(symbol == 'CMO'):
        formated = VisIndicator.visualize_CMO(PriceData,Timeframe)
        return formated
    elif(symbol == 'DX'):
        formated = VisIndicator.visualize_DX(PriceData,Timeframe)
        return formated
    elif(symbol == 'MACD'):
        formated = VisIndicator.visualize_MACD(PriceData,Timeframe)
        return formated
    elif(symbol == 'MACDEXT'):
        formated = VisIndicator.visualize_MACDEXT(PriceData,Timeframe)
        return formated
    elif(symbol == 'MACDFIX'):
        formated = VisIndicator.visualize_MACDFIX(PriceData,Timeframe)
        return formated
    elif(symbol == 'MFI'):
        formated = VisIndicator.visualize_MFI(PriceData,Timeframe)
        return formated
    elif(symbol == 'MINUS_DI'):
        formated = VisIndicator.visualize_MINUS_DI(PriceData,Timeframe)
        return formated
    elif(symbol == 'MINUS_DM'):
        formated = VisIndicator.visualize_MINUS_DM(PriceData,Timeframe)
        return formated
    elif(symbol == 'MOM'):
        formated = VisIndicator.visualize_MOM(PriceData,Timeframe)
        return formated
    elif(symbol == 'PLUS_DI'):
        formated = VisIndicator.visualize_PLUS_DI(PriceData,Timeframe)
        return formated
    elif(symbol == 'PLUS_DM'):
        formated = VisIndicator.visualize_PLUS_DM(PriceData,Timeframe)
        return formated
    elif(symbol == 'PPO'):
        formated = VisIndicator.visualize_PPO(PriceData,Timeframe)
        return formated
    elif(symbol == 'ROC'):
        formated = VisIndicator.visualize_ROC(PriceData,Timeframe)
        return formated
    elif(symbol == 'ROCP'):
        formated = VisIndicator.visualize_ROCP(PriceData,Timeframe)
        return formated
    elif(symbol == 'ROCR'):
        formated = VisIndicator.visualize_ROCR(PriceData,Timeframe)
        return formated
    elif(symbol == 'ROCR100'):
        formated = VisIndicator.visualize_ROCR100(PriceData,Timeframe)
        return formated
    elif(symbol == 'RSI'):
        formated = VisIndicator.visualize_RSI(PriceData,Timeframe)
        return formated
    elif(symbol == 'STOCH'):
        formated = VisIndicator.visualize_STOCH(PriceData,Timeframe)
        return formated
    elif(symbol == 'STOCHF'):
        formated = VisIndicator.visualize_STOCHF(PriceData,Timeframe)
        return formated
    elif(symbol == 'STOCHRSI'):
        formated = VisIndicator.visualize_STOCHRSI(PriceData,Timeframe)
        return formated
    elif(symbol == 'TRIX'):
        formated = VisIndicator.visualize_TRIX(PriceData,Timeframe)
        return formated
    elif(symbol == 'ULTOSC'):
        formated = VisIndicator.visualize_ULTOSC(PriceData,Timeframe)
        return formated
    elif(symbol == 'WILLR'):
        formated = VisIndicator.visualize_WILLR(PriceData,Timeframe)
        return formated
        
    # Volume Indicators
    # Volatility Indicators
    # Cycle Indicators
    # Statistic Functions
    # Math Transform
    # Math Operators

    # Pattern Recognition 
    elif(symbol == 'CDLALL'):
        formated = VisIndicator.visualize_CDLALL(PriceData)
        return formated
    # elif(symbol == 'CDL2CROWS'):
    #     formated = VisIndicator.visualize_CDL2CROWS(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDL3BLACKCROWS'):
    #     formated = VisIndicator.visualize_CDL3BLACKCROWS(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDL3INSIDE'):
    #     formated = VisIndicator.visualize_CDL3INSIDE(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDL3LINESTRIKE'):
    #     formated = VisIndicator.visualize_CDL3LINESTRIKE(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDL3OUTSIDE'):
    #     formated = VisIndicator.visualize_CDL3OUTSIDE(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDL3STARSINSOUTH'):
    #     formated = VisIndicator.visualize_CDL3STARSINSOUTH(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDL3WHITESOLDIERS'):
    #     formated = VisIndicator.visualize_CDL3WHITESOLDIERS(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLABANDONEDBABY'):
    #     formated = VisIndicator.visualize_CDLABANDONEDBABY(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLADVANCEBLOCK'):
    #     formated = VisIndicator.visualize_CDLADVANCEBLOCK(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLBELTHOLD'):
    #     formated = VisIndicator.visualize_CDLBELTHOLD(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLBREAKAWAY'):
    #     formated = VisIndicator.visualize_CDLBREAKAWAY(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLCLOSINGMARUBOZU'):
    #     formated = VisIndicator.visualize_CDLCLOSINGMARUBOZU(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLCONCEALBABYSWALL'):
    #     formated = VisIndicator.visualize_CDLCONCEALBABYSWALL(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLCOUNTERATTACK'):
    #     formated = VisIndicator.visualize_CDLCOUNTERATTACK(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLDARKCLOUDCOVER'):
    #     formated = VisIndicator.visualize_CDLDARKCLOUDCOVER(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLDOJI'):
    #     formated = VisIndicator.visualize_CDLDOJI(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLDOJISTAR'):
    #     formated = VisIndicator.visualize_CDLDOJISTAR(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLDRAGONFLYDOJI'):
    #     formated = VisIndicator.visualize_CDLDRAGONFLYDOJI(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLENGULFING'):
    #     formated = VisIndicator.visualize_CDLENGULFING(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLEVENINGDOJISTAR'):
    #     formated = VisIndicator.visualize_CDLEVENINGDOJISTAR(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLEVENINGSTAR'):
    #     formated = VisIndicator.visualize_CDLEVENINGSTAR(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLGAPSIDESIDEWHITE'):
    #     formated = VisIndicator.visualize_CDLGAPSIDESIDEWHITE(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLGRAVESTONEDOJI'):
    #     formated = VisIndicator.visualize_CDLGRAVESTONEDOJI(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLHAMMER'):
    #     formated = VisIndicator.visualize_CDLHAMMER(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLHANGINGMAN'):
    #     formated = VisIndicator.visualize_CDLHANGINGMAN(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLHARAMI'):
    #     formated = VisIndicator.visualize_CDLHARAMI(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLHARAMICROSS'):
    #     formated = VisIndicator.visualize_CDLHARAMICROSS(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLHIGHWAVE'):
    #     formated = VisIndicator.visualize_CDLHIGHWAVE(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLHIKKAKE'):
    #     formated = VisIndicator.visualize_CDLHIKKAKE(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLHIKKAKEMOD'):
    #     formated = VisIndicator.visualize_CDLHIKKAKEMOD(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLHOMINGPIGEON'):
    #     formated = VisIndicator.visualize_CDLHOMINGPIGEON(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLIDENTICAL3CROWS'):
    #     formated = VisIndicator.visualize_CDLIDENTICAL3CROWS(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLINNECK'):
    #     formated = VisIndicator.visualize_CDLINNECK(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLINVERTEDHAMMER'):
    #     formated = VisIndicator.visualize_CDLINVERTEDHAMMER(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLKICKING'):
    #     formated = VisIndicator.visualize_CDLKICKING(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLKICKINGBYLENGTH'):
    #     formated = VisIndicator.visualize_CDLKICKINGBYLENGTH(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLLADDERBOTTOM'):
    #     formated = VisIndicator.visualize_CDLLADDERBOTTOM(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLLONGLEGGEDDOJI'):
    #     formated = VisIndicator.visualize_CDLLONGLEGGEDDOJI(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLLONGLINE'):
    #     formated = VisIndicator.visualize_CDLLONGLINE(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLMARUBOZU'):
    #     formated = VisIndicator.visualize_CDLMARUBOZU(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLMATCHINGLOW'):
    #     formated = VisIndicator.visualize_CDLMATCHINGLOW(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLMATHOLD'):
    #     formated = VisIndicator.visualize_CDLMATHOLD(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLMORNINGDOJISTAR'):
    #     formated = VisIndicator.visualize_CDLMORNINGDOJISTAR(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLMORNINGSTAR'):
    #     formated = VisIndicator.visualize_CDLMORNINGSTAR(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLONNECK'):
    #     formated = VisIndicator.visualize_CDLONNECK(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLPIERCING'):
    #     formated = VisIndicator.visualize_CDLPIERCING(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLRICKSHAWMAN'):
    #     formated = VisIndicator.visualize_CDLRICKSHAWMAN(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLRISEFALL3METHODS'):
    #     formated = VisIndicator.visualize_CDLRISEFALL3METHODS(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLSEPARATINGLINES'):
    #     formated = VisIndicator.visualize_CDLSEPARATINGLINES(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLSHOOTINGSTAR'):
    #     formated = VisIndicator.visualize_CDLSHOOTINGSTAR(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLSHORTLINE'):
    #     formated = VisIndicator.visualize_CDLSHORTLINE(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLSPINNINGTOP'):
    #     formated = VisIndicator.visualize_CDLSPINNINGTOP(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLSTALLEDPATTERN'):
    #     formated = VisIndicator.visualize_CDLSTALLEDPATTERN(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLSTICKSANDWICH'):
    #     formated = VisIndicator.visualize_CDLSTICKSANDWICH(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLTAKURI'):
    #     formated = VisIndicator.visualize_CDLTAKURI(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLTASUKIGAP'):
    #     formated = VisIndicator.visualize_CDLTASUKIGAP(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLTHRUSTING'):
    #     formated = VisIndicator.visualize_CDLTHRUSTING(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLTRISTAR'):
    #     formated = VisIndicator.visualize_CDLTRISTAR(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLUNIQUE3RIVER'):
    #     formated = VisIndicator.visualize_CDLUNIQUE3RIVER(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLUPSIDEGAP2CROWS'):
    #     formated = VisIndicator.visualize_CDLUPSIDEGAP2CROWS(PriceData)
    #     return formated                                     
    # elif(symbol == 'CDLXSIDEGAP3MET'):
    #     formated = VisIndicator.visualize_CDLXSIDEGAP3METHODS(PriceData)
    #     return formated                                     