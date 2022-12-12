import pandas as pd 
from binance.client import Client
import streamlit as st
import ccxt

client = Client()

# List of coins of interest

tickers = ['BTCUSDT','XRPUSDT', 'TRXUSDT', 'WAVESUSDT', 'ZILUSDT', 'ONEUSDT', 'COTIUSDT', 'SOLUSDT', 'EGLDUSDT', 'AVAXUSDT', 
            'NEARUSDT', 'FILUSDT', 'AXSUSDT', 'ROSEUSDT', 'ARUSDT', 'MBOXUSDT',  'YGGUSDT',
            'BETAUSDT', 'PEOPLEUSDT', 'EOSUSDT', 'ATOMUSDT', 'FTMUSDT', 'DUSKUSDT', 'IOTXUSDT', 'OGNUSDT',
            'CHRUSDT', 'MANAUSDT', 'XEMUSDT', 'SKLUSDT', 'ICPUSDT', 'FLOWUSDT', 'WAXPUSDT', 'FIDAUSDT',
            'ENSUSDT', 'SPELLUSDT', 'LTCUSDT', 'IOTAUSDT', 'LINKUSDT', 'XMRUSDT', 'DASHUSDT', 'MATICUSDT',
            'ALGOUSDT',  'ANKRUSDT', 'COSUSDT', 'KEYUSDT', 'XTZUSDT', 'RENUSDT', 'RVNUSDT', 'HBARUSDT',
            'BCHUSDT', 'COMPUSDT', 'ZENUSDT', 'SNXUSDT', 'SXPUSDT', 'SRMUSDT', 'SANDUSDT', 'SUSHIUSDT',
            'YFIIUSDT', 'KSMUSDT',  'DIAUSDT', 'RUNEUSDT', 'AAVEUSDT', '1INCHUSDT', 'ALICEUSDT', 'FARMUSDT',
            'REQUSDT', 'GALAUSDT', 'POWRUSDT', 'OMGUSDT', 'DOGEUSDT', 'SCUSDT', 'XVSUSDT', 'ASRUSDT',
            'CELOUSDT', 'RAREUSDT', 'ADXUSDT', 'CVXUSDT', 'WINUSDT', 'C98USDT', 'FLUXUSDT', 'ENJUSDT',
            'FUNUSDT', 'KP3RUSDT', 'ALCXUSDT', 'ETCUSDT', 'THETAUSDT', 'CVCUSDT', 'STXUSDT', 'CRVUSDT',
            'MDXUSDT', 'DYDXUSDT', 'OOKIUSDT', 'CELRUSDT', 'RSRUSDT', 'ATMUSDT', 'LINAUSDT', 'POLSUSDT',
            'ATAUSDT', 'RNDRUSDT', 'NEOUSDT', 'ALPHAUSDT', 'XVGUSDT', 'KLAYUSDT', 'DFUSDT', 'VOXELUSDT',
            'LSKUSDT', 'KNCUSDT', 'NMRUSDT', 'MOVRUSDT', 'PYRUSDT', 'ZECUSDT', 'CAKEUSDT', 'HIVEUSDT',
            'UNIUSDT', 'SYSUSDT', 'BNXUSDT', 'GLMRUSDT', 'LOKAUSDT', 'CTSIUSDT', 'REEFUSDT', 'AGLDUSDT',
            'MCUSDT', 'ICXUSDT', 'TLMUSDT', 'MASKUSDT', 'IMXUSDT', 'XLMUSDT', 'BELUSDT', 'HARDUSDT',
            'NULSUSDT', 'TOMOUSDT', 'NKNUSDT', 'BTSUSDT', 'LTOUSDT', 'STORJUSDT', 'ERNUSDT', 'XECUSDT',
            'ILVUSDT', 'JOEUSDT', 'SUNUSDT', 'ACHUSDT', 'TROYUSDT', 'YFIUSDT', 'CTKUSDT',
            'BANDUSDT', 'RLCUSDT', 'TRUUSDT', 'MITHUSDT', 'AIONUSDT', 'ORNUSDT', 'WRXUSDT', 'WANUSDT',
            'CHZUSDT', 'ARPAUSDT', 'LRCUSDT', 'IRISUSDT', 'UTKUSDT', 'QTUMUSDT', 'GTOUSDT', 'MTLUSDT',
            'KAVAUSDT', 'DREPUSDT', 'OCEANUSDT', 'UMAUSDT', 'FLMUSDT', 'UNFIUSDT', 'BADGERUSDT', 'PONDUSDT',
            'PERPUSDT', 'TKOUSDT', 'GTCUSDT', 'TVKUSDT','MINAUSDT', 'RAYUSDT', 'LAZIOUSDT', 'AMPUSDT',
            'BICOUSDT', 'CTXCUSDT', 'FISUSDT', 'BTGUSDT','TRIBEUSDT', 'QIUSDT', 'PORTOUSDT', 'DATAUSDT',
            'NBSUSDT', 'EPSUSDT', 'TFUELUSDT', 'BEAMUSDT','REPUSDT', 'PSGUSDT', 'WTCUSDT', 'FORTHUSDT',
            'BONDUSDT', 'ZRXUSDT', 'FIROUSDT', 'SFPUSDT', 'VTHOUSDT', 'FIOUSDT', 'PERLUSDT', 'WINGUSDT','AKROUSDT', 'BAKEUSDT',
            'ALPACAUSDT', 'FORUSDT', 'IDEXUSDT', 'PLAUSDT', 'VITEUSDT', 'DEGOUSDT', 'XNOUSDT', 'STMXUSDT', 'JUVUSDT', 'STRAXUSDT',
            'CITYUSDT', 'JASMYUSDT', 'DEXEUSDT', 'OMUSDT', 'MKRUSDT','FXSUSDT', 'ETHUSDT', 'ADAUSDT','BNBUSDT','SHIBUSDT']


dropdown = st.selectbox('Pick the crypto/coin of interest!', tickers)

start = st.date_input('Start', value = pd.to_datetime('2021-10-31'))

investment = st.number_input('Choose amount invested monthly')

def getdata(symbol, start):
    start = str(start)
    frame = pd.DataFrame(client.get_historical_klines(symbol, '1d', start))
    frame = frame.iloc[:,:6]
    frame.columns =['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame.set_index('Time', inplace = True)
    frame.index = pd.to_datetime(frame.index, unit = 'ms')
    #CAST Column values as float to ensure that all values are float 
    frame = frame.astype(float)
    return frame

df = getdata(dropdown, start)

buydates = pd.date_range(df.index[0], df.index[-1], freq = '1M')
buyprices = df[df.index.isin(buydates)].Close

coin_amt = investment / buyprices
coin_amt_LumpSum = investment * len(buyprices) / buyprices[0]

coin_amt_sum = coin_amt.cumsum()
coin_amt_sum.name = 'coin_amt_DCA'

df_tog = pd.concat([coin_amt_sum,df], axis = 1).ffill()
df_tog['coin_amt_LumpSum'] = coin_amt_LumpSum
df_tog['Portfolio_DCA_Strategy'] = df_tog.coin_amt_DCA * df_tog.Close
df_tog['Portfolio_Lump_Sum_Strategy'] = df_tog.coin_amt_LumpSum * df_tog.Close

performance_DCA = (df_tog['Portfolio_DCA_Strategy'][-1] / (investment * len(buyprices))) - 1
performance_Lump_Sum = (df_tog['Portfolio_Lump_Sum_Strategy'][-1] / (investment *  len(buyprices))) -1 

st.line_chart(df_tog['Portfolio_Lump_Sum_Strategy'])
st.write('Lump Sum Performance: ' + str(round(performance_Lump_Sum * 100, 2)) + ' %')

st.line_chart(df_tog['Portfolio_DCA_Strategy'])
st.write('DCA Performance: ' + str(round(performance_DCA * 100, 2)) + ' %')