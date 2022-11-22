import talib as talib

#   Two Crows
def CDL2CROWS(OHLC):
    _CDL2CROWS = talib.CDL2CROWS(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDL2CROWS]

#   Three Black Crows    
def CDL3BLACKCROWS(OHLC):
    _CDL3BLACKCROWS = talib.CDL3BLACKCROWS(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDL3BLACKCROWS]
    
#   Three Inside Up/Down    
def CDL3INSIDE(OHLC):
    _CDL3INSIDE = talib.CDL3INSIDE(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDL3INSIDE]
    
#   Three-Line Strike    
def CDL3LINESTRIKE(OHLC):
    _CDL3LINESTRIKE = talib.CDL3LINESTRIKE(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDL3LINESTRIKE]
    
#   Three Outside Up/Down    
def CDL3OUTSIDE(OHLC):
    _CDL3OUTSIDE = talib.CDL3OUTSIDE(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDL3OUTSIDE]
    
#   Three Stars In The South    
def CDL3STARSINSOUTH(OHLC):
    _CDL3STARSINSOUTH = talib.CDL3STARSINSOUTH(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDL3STARSINSOUTH]
    
#   Three Advancing White Soldiers    
def CDL3WHITESOLDIERS(OHLC):
    _CDL3WHITESOLDIERS = talib.CDL3WHITESOLDIERS(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDL3WHITESOLDIERS]
    
#   Abandoned Baby
def CDLABANDONEDBABY(OHLC):
    _CDLABANDONEDBABY = talib.CDLABANDONEDBABY(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLABANDONEDBABY]
    
#   Advance Block    
def CDLADVANCEBLOCK(OHLC):
    _CDLADVANCEBLOCK = talib.CDLADVANCEBLOCK(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLADVANCEBLOCK]
    
#   Belt-hold    
def CDLBELTHOLD(OHLC):
    _CDLBELTHOLD = talib.CDLBELTHOLD(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLBELTHOLD]
    
#   Breakaway    
def CDLBREAKAWAY(OHLC):
    _CDLBREAKAWAY = talib.CDLBREAKAWAY(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLBREAKAWAY]
    
#   Closing Marubozu    
def CDLCLOSINGMARUBOZU (OHLC):
    _CDLCLOSINGMARUBOZU = talib.CDLCLOSINGMARUBOZU(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLCLOSINGMARUBOZU]

#   Concealing Baby Swallow    
def CDLCONCEALBABYSWALL(OHLC):
    _CDLCONCEALBABYSWALL = talib.CDLCONCEALBABYSWALL(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLCONCEALBABYSWALL]

#   Counterattack
def CDLCOUNTERATTACK(OHLC):
    _CDLCOUNTERATTACK = talib.CDLCOUNTERATTACK(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLCOUNTERATTACK]

#   Dark Cloud Cover
def CDLDARKCLOUDCOVER(OHLC):
    _CDLDARKCLOUDCOVER = talib.CDLDARKCLOUDCOVER(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLDARKCLOUDCOVER]
    
#   Doji    
def CDLDOJI(OHLC):
    _CDLDOJI = talib.CDLDOJI(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLDOJI]

#   Doji Star    
def CDLDOJISTAR(OHLC):
    _CDLDOJISTAR = talib.CDLDOJISTAR(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLDOJISTAR]
    
#   Dragonfly Doji    
def CDLDRAGONFLYDOJI(OHLC):
    _CDLDRAGONFLYDOJI = talib.CDLDRAGONFLYDOJI(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLDRAGONFLYDOJI]
    
#   Engulfing Pattern    
def CDLENGULFING(OHLC):
    _CDLENGULFING = talib.CDLENGULFING(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLENGULFING]
    
#   Evening Doji Star    
def CDLEVENINGDOJISTAR(OHLC):
    _CDLEVENINGDOJISTAR = talib.CDLEVENINGDOJISTAR(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLEVENINGDOJISTAR]
    
#   Evening Star    
def CDLEVENINGSTAR(OHLC):
    _CDLEVENINGSTAR = talib.CDLEVENINGSTAR(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLEVENINGSTAR]
    
#   Up/Down-gap side-by-side white lines    
def CDLGAPSIDESIDEWHITE(OHLC):
    _CDLGAPSIDESIDEWHITE = talib.CDLGAPSIDESIDEWHITE(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLGAPSIDESIDEWHITE]
    
#   Gravestone Doji    
def CDLGRAVESTONEDOJI(OHLC):
    _CDLGRAVESTONEDOJI = talib.CDLGRAVESTONEDOJI(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLGRAVESTONEDOJI]
    
#   Hammer    
def CDLHAMMER(OHLC):
    _CDLHAMMER = talib.CDLHAMMER(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLHAMMER]
    
#   Hanging Man    
def CDLHANGINGMAN(OHLC):
    _CDLHANGINGMAN = talib.CDLHANGINGMAN(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLHANGINGMAN]
    
#   Harami Pattern    
def CDLHARAMI(OHLC):
    _CDLHARAMI = talib.CDLHARAMI(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLHARAMI]
    
#   Harami Cross Pattern
def CDLHARAMICROSS(OHLC):
    _CDLHARAMICROSS = talib.CDLHARAMICROSS(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLHARAMICROSS]
    
#   High-Wave Candle    
def CDLHIGHWAVE(OHLC):
    _CDLHIGHWAVE = talib.CDLHIGHWAVE(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLHIGHWAVE]
    
#   Hikkake Pattern    
def CDLHIKKAKE(OHLC):
    _CDLHIKKAKE = talib.CDLHIKKAKE(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLHIKKAKE]
    
#   Modified Hikkake Pattern    
def CDLHIKKAKEMOD(OHLC):
    _CDLHIKKAKEMOD = talib.CDLHIKKAKEMOD(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLHIKKAKEMOD]
    
#   Homing Pigeon    
def CDLHOMINGPIGEON(OHLC):
    _CDLHOMINGPIGEON = talib.CDLHOMINGPIGEON(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLHOMINGPIGEON]
    
#   Identical Three Crows    
def CDLIDENTICAL3CROWS(OHLC):
    _CDLIDENTICAL3CROWS = talib.CDLIDENTICAL3CROWS(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLIDENTICAL3CROWS]
    
#   In-Neck Pattern    
def CDLINNECK(OHLC):
    _CDLINNECK = talib.CDLINNECK(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLINNECK]
    
#   Inverted Hammer    
def CDLINVERTEDHAMMER(OHLC):
    _CDLINVERTEDHAMMER = talib.CDLINVERTEDHAMMER(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLINVERTEDHAMMER]
    
#   Kicking    
def CDLKICKING(OHLC):
    _CDLKICKING = talib.CDLKICKING(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLKICKING]
    
#   Kicking - bull/bear determined by the longer marubozu    
def CDLKICKINGBYLENGTH(OHLC):
    _CDLKICKINGBYLENGTH = talib.CDLKICKINGBYLENGTH(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLKICKINGBYLENGTH]
    
#   Ladder Bottom    
def CDLLADDERBOTTOM(OHLC):
    _CDLLADDERBOTTOM = talib.CDLLADDERBOTTOM(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLLADDERBOTTOM]
    
#   Long Legged Doji    
def CDLLONGLEGGEDDOJI(OHLC):
    _CDLLONGLEGGEDDOJI = talib.CDLLONGLEGGEDDOJI(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLLONGLEGGEDDOJI]
    
#   Long Line Candle    
def CDLLONGLINE(OHLC):
    _CDLLONGLINE = talib.CDLLONGLINE(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLLONGLINE]
    
#   Marubozu    
def CDLMARUBOZU(OHLC):
    _CDLMARUBOZU = talib.CDLMARUBOZU(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLMARUBOZU]
    
#   Matching Low    
def CDLMATCHINGLOW(OHLC):
    _CDLMATCHINGLOW = talib.CDLMATCHINGLOW(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLMATCHINGLOW]

#   Mat Hold    
def CDLMATHOLD(OHLC):
    _CDLMATHOLD = talib.CDLMATHOLD(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLMATHOLD]

#   Morning Doji Star   
# def CDLMORNINGDOJISTAR(OHLC):
#     _CDLMORNINGDOJISTAR = talib.CDLMORNINGDOJISTAR(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
#     return[_CDLMORNINGDOJISTAR]

#   Morning Star
# def CDLMORNINGSTAR(OHLC):
#     _CDLMORNINGSTAR = talib.CDLMORNINGSTAR(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
#     return[_CDLMORNINGSTAR]

#   On-Neck Pattern     
def CDLONNECK(OHLC):
    _CDLONNECK = talib.CDLONNECK(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLONNECK]
    
#   Piercing Pattern
def CDLPIERCING(OHLC):
    _CDLPIERCING = talib.CDLPIERCING(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLPIERCING]
    
#   Rickshaw Man    
def CDLRICKSHAWMAN(OHLC):
    _CDLRICKSHAWMAN = talib.CDLRICKSHAWMAN(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLRICKSHAWMAN]
    
#   Rising/Falling Three Methods    
def CDLRISEFALL3METHODS(OHLC):
    _CDLRISEFALL3METHODS = talib.CDLRISEFALL3METHODS(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLRISEFALL3METHODS]
    
#   Separating Lines    
def CDLSEPARATINGLINES(OHLC):
    _CDLSEPARATINGLINES = talib.CDLSEPARATINGLINES(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLSEPARATINGLINES]

#   Shooting Star
def CDLSHOOTINGSTAR(OHLC):
    _CDLSHOOTINGSTAR = talib.CDLSHOOTINGSTAR(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLSHOOTINGSTAR]

#   Short Line Candle
def CDLSHORTLINE(OHLC):
    _CDLSHORTLINE = talib.CDLSHORTLINE(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLSHORTLINE]
    
#   Spinning Top
def CDLSPINNINGTOP(OHLC):
    _CDLSPINNINGTOP = talib.CDLSPINNINGTOP(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLSPINNINGTOP]
    
#   Stalled Pattern
def CDLSTALLEDPATTERN(OHLC):
    _CDLSTALLEDPATTERN = talib.CDLSTALLEDPATTERN(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLSTALLEDPATTERN]
    
#   Stick Sandwich
def CDLSTICKSANDWICH(OHLC):
    _CDLSTICKSANDWICH = talib.CDLSTICKSANDWICH(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLSTICKSANDWICH]
    
#   Takuri (Dragonfly Doji with very long lower shadow)
def CDLTAKURI(OHLC):
    _CDLTAKURI = talib.CDLTAKURI(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLTAKURI]
    
#   Tasuki Gap
def CDLTASUKIGAP(OHLC):
    _CDLTASUKIGAP = talib.CDLTASUKIGAP(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLTASUKIGAP]
    
#   Thrusting Pattern
def CDLTHRUSTING(OHLC):
    _CDLTHRUSTING = talib.CDLTHRUSTING(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLTHRUSTING]
    
#   Tristar Pattern
def CDLTRISTAR(OHLC):
    _CDLTRISTAR = talib.CDLTRISTAR(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLTRISTAR]
    
#   Unique 3 River
def CDLUNIQUE3RIVER(OHLC):
    _CDLUNIQUE3RIVER = talib.CDLUNIQUE3RIVER(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLUNIQUE3RIVER]
    
#   Upside Gap Two Crows
def CDLUPSIDEGAP2CROWS(OHLC):
    _CDLUPSIDEGAP2CROWS = talib.CDLUPSIDEGAP2CROWS(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLUPSIDEGAP2CROWS]
    
#   Upside/Downside Gap Three Methods
def CDLXSIDEGAP3METHODS(OHLC):
    _CDLXSIDEGAP3METHODS = talib.CDLXSIDEGAP3METHODS(OHLC['open'],OHLC['high'],OHLC['low'],OHLC['close'])
    return[_CDLXSIDEGAP3METHODS]
    

# pattern_recognition = [
        
#         CDL2CROWS,

#         CDL3BLACKCROWS,

#         CDL3INSIDE,

#         CDL3LINESTRIKE,

#         CDL3OUTSIDE,

#         CDL3STARSINSOUTH,

#         CDL3WHITESOLDIERS,

#         CDLABANDONEDBABY,

#         CDLADVANCEBLOCK,

#         CDLBELTHOLD,

#         CDLBREAKAWAY,

#         CDLCLOSINGMARUBOZU,

#         CDLCONCEALBABYSWALL,

#         CDLCOUNTERATTACK,

#         CDLDARKCLOUDCOVER,

#         CDLDOJI,

#         CDLDOJISTAR,

#         CDLDRAGONFLYDOJI,

#         CDLENGULFING,

#         CDLEVENINGDOJISTAR,

#         CDLEVENINGSTAR,

#         CDLGAPSIDESIDEWHITE,

#         CDLGRAVESTONEDOJI,

#         CDLHAMMER,

#         CDLHANGINGMAN,

#         CDLHARAMI,

#         CDLHARAMICROSS,

#         CDLHIGHWAVE,

#         CDLHIKKAKE,

#         CDLHIKKAKEMOD,

#         CDLHOMINGPIGEON,

#         CDLIDENTICAL3CROWS,

#         CDLINNECK,

#         CDLINVERTEDHAMMER,

#         CDLKICKING,

#         CDLKICKINGBYLENGTH,

#         CDLLADDERBOTTOM,

#         CDLLONGLEGGEDDOJI,

#         CDLLONGLINE,

#         CDLMARUBOZU,

#         CDLMATCHINGLOW,

#         CDLMATHOLD,

#         # CDLMORNINGDOJISTAR,

#         # CDLMORNINGSTAR,

#         CDLONNECK,

#         CDLPIERCING,

#         CDLRICKSHAWMAN,

#         CDLRISEFALL3METHODS,

#         CDLSEPARATINGLINES,

#         CDLSHOOTINGSTAR,

#         CDLSHORTLINE,

#         CDLSPINNINGTOP,

#         CDLSTALLEDPATTERN,

#         CDLSTICKSANDWICH,

#         CDLTAKURI,

#         CDLTASUKIGAP,

#         CDLTHRUSTING,

#         CDLTRISTAR,

#         CDLUNIQUE3RIVER,

#         CDLUPSIDEGAP2CROWS,

#         CDLXSIDEGAP3METHODS
# ]                       
    



# df['candlestick_pattern'] = np.nan
# df['candlestick_match_count'] = np.nan
# for index, row in df.iterrows():

#     # no pattern found
#     if len(row[candle_names]) - sum(row[candle_names] == 0) == 0:
#         df.loc[index,'candlestick_pattern'] = "NO_PATTERN"
#         df.loc[index, 'candlestick_match_count'] = 0
#     # single pattern found
#     elif len(row[candle_names]) - sum(row[candle_names] == 0) == 1:
#         # bull pattern 100 or 200
#         if any(row[candle_names].values > 0):
#             pattern = list(compress(row[candle_names].keys(), row[candle_names].values != 0))[0] + '_Bull'
#             df.loc[index, 'candlestick_pattern'] = pattern
#             df.loc[index, 'candlestick_match_count'] = 1
#         # bear pattern -100 or -200
#         else:
#             pattern = list(compress(row[candle_names].keys(), row[candle_names].values != 0))[0] + '_Bear'
#             df.loc[index, 'candlestick_pattern'] = pattern
#             df.loc[index, 'candlestick_match_count'] = 1
#     # multiple patterns matched -- select best performance
#     else:
#         # filter out pattern names from bool list of values
#         patterns = list(compress(row[candle_names].keys(), row[candle_names].values != 0))
#         container = []
#         for pattern in patterns:
#             if row[pattern] > 0:
#                 container.append(pattern + '_Bull')
#             else:
#                 container.append(pattern + '_Bear')
#         rank_list = [candle_rankings[p] for p in container]
#         if len(rank_list) == len(container):
#             rank_index_best = rank_list.index(min(rank_list))
#             df.loc[index, 'candlestick_pattern'] = container[rank_index_best]
#             df.loc[index, 'candlestick_match_count'] = len(container)
#     # clean up candle columns
#     df.drop(candle_names, axis = 1, inplace = True)