{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Our goal is to build a dashboard to compare performance difference between DCA investing and a Lump Sum investing in any crypto of your choice."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Modules & Libraries\n",
    "import pandas as pd \n",
    "from binance.client import Client\n",
    "import streamlit as st\n",
    "import ccxt\n",
    "\n",
    "# Instantiating the binance client\n",
    "client = Client()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "# List of coins of interest\n",
    "\n",
    "tickers = ['BTCUSDT','XRPUSDT', 'TRXUSDT', 'WAVESUSDT', 'ZILUSDT', 'ONEUSDT', 'COTIUSDT', 'SOLUSDT', 'EGLDUSDT', 'AVAXUSDT', \n",
    "            'NEARUSDT', 'FILUSDT', 'AXSUSDT', 'ROSEUSDT', 'ARUSDT', 'MBOXUSDT',  'YGGUSDT',\n",
    "            'BETAUSDT', 'PEOPLEUSDT', 'EOSUSDT', 'ATOMUSDT', 'FTMUSDT', 'DUSKUSDT', 'IOTXUSDT', 'OGNUSDT',\n",
    "            'CHRUSDT', 'MANAUSDT', 'XEMUSDT', 'SKLUSDT', 'ICPUSDT', 'FLOWUSDT', 'WAXPUSDT', 'FIDAUSDT',\n",
    "            'ENSUSDT', 'SPELLUSDT', 'LTCUSDT', 'IOTAUSDT', 'LINKUSDT', 'XMRUSDT', 'DASHUSDT', 'MATICUSDT',\n",
    "            'ALGOUSDT',  'ANKRUSDT', 'COSUSDT', 'KEYUSDT', 'XTZUSDT', 'RENUSDT', 'RVNUSDT', 'HBARUSDT',\n",
    "            'BCHUSDT', 'COMPUSDT', 'ZENUSDT', 'SNXUSDT', 'SXPUSDT', 'SRMUSDT', 'SANDUSDT', 'SUSHIUSDT',\n",
    "            'YFIIUSDT', 'KSMUSDT',  'DIAUSDT', 'RUNEUSDT', 'AAVEUSDT', '1INCHUSDT', 'ALICEUSDT', 'FARMUSDT',\n",
    "            'REQUSDT', 'GALAUSDT', 'POWRUSDT', 'OMGUSDT', 'DOGEUSDT', 'SCUSDT', 'XVSUSDT', 'ASRUSDT',\n",
    "            'CELOUSDT', 'RAREUSDT', 'ADXUSDT', 'CVXUSDT', 'WINUSDT', 'C98USDT', 'FLUXUSDT', 'ENJUSDT',\n",
    "            'FUNUSDT', 'KP3RUSDT', 'ALCXUSDT', 'ETCUSDT', 'THETAUSDT', 'CVCUSDT', 'STXUSDT', 'CRVUSDT',\n",
    "            'MDXUSDT', 'DYDXUSDT', 'OOKIUSDT', 'CELRUSDT', 'RSRUSDT', 'ATMUSDT', 'LINAUSDT', 'POLSUSDT',\n",
    "            'ATAUSDT', 'RNDRUSDT', 'NEOUSDT', 'ALPHAUSDT', 'XVGUSDT', 'KLAYUSDT', 'DFUSDT', 'VOXELUSDT',\n",
    "            'LSKUSDT', 'KNCUSDT', 'NMRUSDT', 'MOVRUSDT', 'PYRUSDT', 'ZECUSDT', 'CAKEUSDT', 'HIVEUSDT',\n",
    "            'UNIUSDT', 'SYSUSDT', 'BNXUSDT', 'GLMRUSDT', 'LOKAUSDT', 'CTSIUSDT', 'REEFUSDT', 'AGLDUSDT',\n",
    "            'MCUSDT', 'ICXUSDT', 'TLMUSDT', 'MASKUSDT', 'IMXUSDT', 'XLMUSDT', 'BELUSDT', 'HARDUSDT',\n",
    "            'NULSUSDT', 'TOMOUSDT', 'NKNUSDT', 'BTSUSDT', 'LTOUSDT', 'STORJUSDT', 'ERNUSDT', 'XECUSDT',\n",
    "            'ILVUSDT', 'JOEUSDT', 'SUNUSDT', 'ACHUSDT', 'TROYUSDT', 'YFIUSDT', 'CTKUSDT',\n",
    "            'BANDUSDT', 'RLCUSDT', 'TRUUSDT', 'MITHUSDT', 'AIONUSDT', 'ORNUSDT', 'WRXUSDT', 'WANUSDT',\n",
    "            'CHZUSDT', 'ARPAUSDT', 'LRCUSDT', 'IRISUSDT', 'UTKUSDT', 'QTUMUSDT', 'GTOUSDT', 'MTLUSDT',\n",
    "            'KAVAUSDT', 'DREPUSDT', 'OCEANUSDT', 'UMAUSDT', 'FLMUSDT', 'UNFIUSDT', 'BADGERUSDT', 'PONDUSDT',\n",
    "            'PERPUSDT', 'TKOUSDT', 'GTCUSDT', 'TVKUSDT','MINAUSDT', 'RAYUSDT', 'LAZIOUSDT', 'AMPUSDT',\n",
    "            'BICOUSDT', 'CTXCUSDT', 'FISUSDT', 'BTGUSDT','TRIBEUSDT', 'QIUSDT', 'PORTOUSDT', 'DATAUSDT',\n",
    "            'NBSUSDT', 'EPSUSDT', 'TFUELUSDT', 'BEAMUSDT','REPUSDT', 'PSGUSDT', 'WTCUSDT', 'FORTHUSDT',\n",
    "            'BONDUSDT', 'ZRXUSDT', 'FIROUSDT', 'SFPUSDT', 'VTHOUSDT', 'FIOUSDT', 'PERLUSDT', 'WINGUSDT','AKROUSDT', 'BAKEUSDT',\n",
    "            'ALPACAUSDT', 'FORUSDT', 'IDEXUSDT', 'PLAUSDT', 'VITEUSDT', 'DEGOUSDT', 'XNOUSDT', 'STMXUSDT', 'JUVUSDT', 'STRAXUSDT',\n",
    "            'CITYUSDT', 'JASMYUSDT', 'DEXEUSDT', 'OMUSDT', 'MKRUSDT','FXSUSDT', 'ETHUSDT', 'ADAUSDT','BNBUSDT','SHIBUSDT']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "dropdown = st.selectbox('Pick the crypto/coin of interest!', tickers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Date picker\n",
    "\n",
    "start = st.date_input('Start', value = pd.to_datetime('2021-10-31'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Input DCA monthly investment\n",
    "\n",
    "investment = st.number_input('Choose amount invested monthly')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Time</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2018-01-01</th>\n",
       "      <td>13715.65</td>\n",
       "      <td>13818.55</td>\n",
       "      <td>12750.00</td>\n",
       "      <td>13380.00</td>\n",
       "      <td>8609.915844</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-01-02</th>\n",
       "      <td>13382.16</td>\n",
       "      <td>15473.49</td>\n",
       "      <td>12890.02</td>\n",
       "      <td>14675.11</td>\n",
       "      <td>20078.092111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-01-03</th>\n",
       "      <td>14690.00</td>\n",
       "      <td>15307.56</td>\n",
       "      <td>14150.00</td>\n",
       "      <td>14919.51</td>\n",
       "      <td>15905.667639</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-01-04</th>\n",
       "      <td>14919.51</td>\n",
       "      <td>15280.00</td>\n",
       "      <td>13918.04</td>\n",
       "      <td>15059.54</td>\n",
       "      <td>21329.649574</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-01-05</th>\n",
       "      <td>15059.56</td>\n",
       "      <td>17176.24</td>\n",
       "      <td>14600.00</td>\n",
       "      <td>16960.39</td>\n",
       "      <td>23251.491125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-12-06</th>\n",
       "      <td>16966.35</td>\n",
       "      <td>17107.01</td>\n",
       "      <td>16906.37</td>\n",
       "      <td>17088.96</td>\n",
       "      <td>218730.768830</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-12-07</th>\n",
       "      <td>17088.96</td>\n",
       "      <td>17142.21</td>\n",
       "      <td>16678.83</td>\n",
       "      <td>16836.64</td>\n",
       "      <td>220657.413340</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-12-08</th>\n",
       "      <td>16836.64</td>\n",
       "      <td>17299.00</td>\n",
       "      <td>16733.49</td>\n",
       "      <td>17224.10</td>\n",
       "      <td>236417.978040</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-12-09</th>\n",
       "      <td>17224.10</td>\n",
       "      <td>17360.00</td>\n",
       "      <td>17058.21</td>\n",
       "      <td>17128.56</td>\n",
       "      <td>238422.064650</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-12-10</th>\n",
       "      <td>17128.56</td>\n",
       "      <td>17227.72</td>\n",
       "      <td>17112.52</td>\n",
       "      <td>17174.18</td>\n",
       "      <td>121951.905450</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1805 rows × 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                Open      High       Low     Close         Volume\n",
       "Time                                                             \n",
       "2018-01-01  13715.65  13818.55  12750.00  13380.00    8609.915844\n",
       "2018-01-02  13382.16  15473.49  12890.02  14675.11   20078.092111\n",
       "2018-01-03  14690.00  15307.56  14150.00  14919.51   15905.667639\n",
       "2018-01-04  14919.51  15280.00  13918.04  15059.54   21329.649574\n",
       "2018-01-05  15059.56  17176.24  14600.00  16960.39   23251.491125\n",
       "...              ...       ...       ...       ...            ...\n",
       "2022-12-06  16966.35  17107.01  16906.37  17088.96  218730.768830\n",
       "2022-12-07  17088.96  17142.21  16678.83  16836.64  220657.413340\n",
       "2022-12-08  16836.64  17299.00  16733.49  17224.10  236417.978040\n",
       "2022-12-09  17224.10  17360.00  17058.21  17128.56  238422.064650\n",
       "2022-12-10  17128.56  17227.72  17112.52  17174.18  121951.905450\n",
       "\n",
       "[1805 rows x 5 columns]"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def getdata(symbol, start):\n",
    "\n",
    "    frame = pd.DataFrame(client.get_historical_klines(symbol, '1d', start))\n",
    "    frame = frame.iloc[:,:6]\n",
    "    frame.columns =['Time', 'Open', 'High', 'Low', 'Close', 'Volume']\n",
    "    frame.set_index('Time', inplace = True)\n",
    "    frame.index = pd.to_datetime(frame.index, unit = 'ms')\n",
    "    #CAST Column values as float to ensure that all values are float \n",
    "    df = frame.astype(float)\n",
    "    return df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "Input type must be str",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[23], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m df \u001b[39m=\u001b[39m getdata(dropdown, start)\n",
      "Cell \u001b[1;32mIn[22], line 2\u001b[0m, in \u001b[0;36mgetdata\u001b[1;34m(symbol, start)\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[39mdef\u001b[39;00m \u001b[39mgetdata\u001b[39m(symbol, start):\n\u001b[1;32m----> 2\u001b[0m     frame \u001b[39m=\u001b[39m pd\u001b[39m.\u001b[39mDataFrame(client\u001b[39m.\u001b[39;49mget_historical_klines(symbol, \u001b[39m'\u001b[39;49m\u001b[39m1d\u001b[39;49m\u001b[39m'\u001b[39;49m, start))\n\u001b[0;32m      3\u001b[0m     frame \u001b[39m=\u001b[39m frame\u001b[39m.\u001b[39miloc[:,:\u001b[39m6\u001b[39m]\n\u001b[0;32m      4\u001b[0m     frame\u001b[39m.\u001b[39mcolumns \u001b[39m=\u001b[39m[\u001b[39m'\u001b[39m\u001b[39mTime\u001b[39m\u001b[39m'\u001b[39m, \u001b[39m'\u001b[39m\u001b[39mOpen\u001b[39m\u001b[39m'\u001b[39m, \u001b[39m'\u001b[39m\u001b[39mHigh\u001b[39m\u001b[39m'\u001b[39m, \u001b[39m'\u001b[39m\u001b[39mLow\u001b[39m\u001b[39m'\u001b[39m, \u001b[39m'\u001b[39m\u001b[39mClose\u001b[39m\u001b[39m'\u001b[39m, \u001b[39m'\u001b[39m\u001b[39mVolume\u001b[39m\u001b[39m'\u001b[39m]\n",
      "File \u001b[1;32mc:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\binance\\client.py:934\u001b[0m, in \u001b[0;36mClient.get_historical_klines\u001b[1;34m(self, symbol, interval, start_str, end_str, limit, klines_type)\u001b[0m\n\u001b[0;32m    914\u001b[0m \u001b[39mdef\u001b[39;00m \u001b[39mget_historical_klines\u001b[39m(\u001b[39mself\u001b[39m, symbol, interval, start_str\u001b[39m=\u001b[39m\u001b[39mNone\u001b[39;00m, end_str\u001b[39m=\u001b[39m\u001b[39mNone\u001b[39;00m, limit\u001b[39m=\u001b[39m\u001b[39m1000\u001b[39m,\n\u001b[0;32m    915\u001b[0m                           klines_type: HistoricalKlinesType \u001b[39m=\u001b[39m HistoricalKlinesType\u001b[39m.\u001b[39mSPOT):\n\u001b[0;32m    916\u001b[0m     \u001b[39m\"\"\"Get Historical Klines from Binance\u001b[39;00m\n\u001b[0;32m    917\u001b[0m \n\u001b[0;32m    918\u001b[0m \u001b[39m    :param symbol: Name of symbol pair e.g BNBBTC\u001b[39;00m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    932\u001b[0m \n\u001b[0;32m    933\u001b[0m \u001b[39m    \"\"\"\u001b[39;00m\n\u001b[1;32m--> 934\u001b[0m     \u001b[39mreturn\u001b[39;00m \u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49m_historical_klines(\n\u001b[0;32m    935\u001b[0m         symbol, interval, start_str\u001b[39m=\u001b[39;49mstart_str, end_str\u001b[39m=\u001b[39;49mend_str, limit\u001b[39m=\u001b[39;49mlimit, klines_type\u001b[39m=\u001b[39;49mklines_type\n\u001b[0;32m    936\u001b[0m     )\n",
      "File \u001b[1;32mc:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\binance\\client.py:969\u001b[0m, in \u001b[0;36mClient._historical_klines\u001b[1;34m(self, symbol, interval, start_str, end_str, limit, klines_type)\u001b[0m\n\u001b[0;32m    966\u001b[0m timeframe \u001b[39m=\u001b[39m interval_to_milliseconds(interval)\n\u001b[0;32m    968\u001b[0m \u001b[39m# if a start time was passed convert it\u001b[39;00m\n\u001b[1;32m--> 969\u001b[0m start_ts \u001b[39m=\u001b[39m convert_ts_str(start_str)\n\u001b[0;32m    971\u001b[0m \u001b[39m# establish first available start timestamp\u001b[39;00m\n\u001b[0;32m    972\u001b[0m \u001b[39mif\u001b[39;00m start_ts \u001b[39mis\u001b[39;00m \u001b[39mnot\u001b[39;00m \u001b[39mNone\u001b[39;00m:\n",
      "File \u001b[1;32mc:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\binance\\helpers.py:76\u001b[0m, in \u001b[0;36mconvert_ts_str\u001b[1;34m(ts_str)\u001b[0m\n\u001b[0;32m     74\u001b[0m \u001b[39mif\u001b[39;00m \u001b[39mtype\u001b[39m(ts_str) \u001b[39m==\u001b[39m \u001b[39mint\u001b[39m:\n\u001b[0;32m     75\u001b[0m     \u001b[39mreturn\u001b[39;00m ts_str\n\u001b[1;32m---> 76\u001b[0m \u001b[39mreturn\u001b[39;00m date_to_milliseconds(ts_str)\n",
      "File \u001b[1;32mc:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\binance\\helpers.py:24\u001b[0m, in \u001b[0;36mdate_to_milliseconds\u001b[1;34m(date_str)\u001b[0m\n\u001b[0;32m     22\u001b[0m epoch: datetime \u001b[39m=\u001b[39m datetime\u001b[39m.\u001b[39mutcfromtimestamp(\u001b[39m0\u001b[39m)\u001b[39m.\u001b[39mreplace(tzinfo\u001b[39m=\u001b[39mpytz\u001b[39m.\u001b[39mutc)\n\u001b[0;32m     23\u001b[0m \u001b[39m# parse our date string\u001b[39;00m\n\u001b[1;32m---> 24\u001b[0m d: Optional[datetime] \u001b[39m=\u001b[39m dateparser\u001b[39m.\u001b[39;49mparse(date_str, settings\u001b[39m=\u001b[39;49m{\u001b[39m'\u001b[39;49m\u001b[39mTIMEZONE\u001b[39;49m\u001b[39m'\u001b[39;49m: \u001b[39m\"\u001b[39;49m\u001b[39mUTC\u001b[39;49m\u001b[39m\"\u001b[39;49m})\n\u001b[0;32m     25\u001b[0m \u001b[39mif\u001b[39;00m \u001b[39mnot\u001b[39;00m d:\n\u001b[0;32m     26\u001b[0m     \u001b[39mraise\u001b[39;00m UnknownDateFormat(date_str)\n",
      "File \u001b[1;32mc:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\dateparser\\conf.py:92\u001b[0m, in \u001b[0;36mapply_settings.<locals>.wrapper\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m     89\u001b[0m \u001b[39mif\u001b[39;00m \u001b[39mnot\u001b[39;00m \u001b[39misinstance\u001b[39m(kwargs[\u001b[39m'\u001b[39m\u001b[39msettings\u001b[39m\u001b[39m'\u001b[39m], Settings):\n\u001b[0;32m     90\u001b[0m     \u001b[39mraise\u001b[39;00m \u001b[39mTypeError\u001b[39;00m(\u001b[39m\"\u001b[39m\u001b[39msettings can only be either dict or instance of Settings class\u001b[39m\u001b[39m\"\u001b[39m)\n\u001b[1;32m---> 92\u001b[0m \u001b[39mreturn\u001b[39;00m f(\u001b[39m*\u001b[39margs, \u001b[39m*\u001b[39m\u001b[39m*\u001b[39mkwargs)\n",
      "File \u001b[1;32mc:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\dateparser\\__init__.py:61\u001b[0m, in \u001b[0;36mparse\u001b[1;34m(date_string, date_formats, languages, locales, region, settings, detect_languages_function)\u001b[0m\n\u001b[0;32m     57\u001b[0m \u001b[39mif\u001b[39;00m languages \u001b[39mor\u001b[39;00m locales \u001b[39mor\u001b[39;00m region \u001b[39mor\u001b[39;00m detect_languages_function \u001b[39mor\u001b[39;00m \u001b[39mnot\u001b[39;00m settings\u001b[39m.\u001b[39m_default:\n\u001b[0;32m     58\u001b[0m     parser \u001b[39m=\u001b[39m DateDataParser(languages\u001b[39m=\u001b[39mlanguages, locales\u001b[39m=\u001b[39mlocales,\n\u001b[0;32m     59\u001b[0m                             region\u001b[39m=\u001b[39mregion, settings\u001b[39m=\u001b[39msettings, detect_languages_function\u001b[39m=\u001b[39mdetect_languages_function)\n\u001b[1;32m---> 61\u001b[0m data \u001b[39m=\u001b[39m parser\u001b[39m.\u001b[39;49mget_date_data(date_string, date_formats)\n\u001b[0;32m     63\u001b[0m \u001b[39mif\u001b[39;00m data:\n\u001b[0;32m     64\u001b[0m     \u001b[39mreturn\u001b[39;00m data[\u001b[39m'\u001b[39m\u001b[39mdate_obj\u001b[39m\u001b[39m'\u001b[39m]\n",
      "File \u001b[1;32mc:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\dateparser\\date.py:442\u001b[0m, in \u001b[0;36mDateDataParser.get_date_data\u001b[1;34m(self, date_string, date_formats)\u001b[0m\n\u001b[0;32m    399\u001b[0m \u001b[39m\"\"\"\u001b[39;00m\n\u001b[0;32m    400\u001b[0m \u001b[39mParse string representing date and/or time in recognizable localized formats.\u001b[39;00m\n\u001b[0;32m    401\u001b[0m \u001b[39mSupports parsing multiple languages and timezones.\u001b[39;00m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    439\u001b[0m \n\u001b[0;32m    440\u001b[0m \u001b[39m\"\"\"\u001b[39;00m\n\u001b[0;32m    441\u001b[0m \u001b[39mif\u001b[39;00m \u001b[39mnot\u001b[39;00m \u001b[39misinstance\u001b[39m(date_string, \u001b[39mstr\u001b[39m):\n\u001b[1;32m--> 442\u001b[0m     \u001b[39mraise\u001b[39;00m \u001b[39mTypeError\u001b[39;00m(\u001b[39m'\u001b[39m\u001b[39mInput type must be str\u001b[39m\u001b[39m'\u001b[39m)\n\u001b[0;32m    444\u001b[0m res \u001b[39m=\u001b[39m parse_with_formats(date_string, date_formats \u001b[39mor\u001b[39;00m [], \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m_settings)\n\u001b[0;32m    445\u001b[0m \u001b[39mif\u001b[39;00m res[\u001b[39m'\u001b[39m\u001b[39mdate_obj\u001b[39m\u001b[39m'\u001b[39m]:\n",
      "\u001b[1;31mTypeError\u001b[0m: Input type must be str"
     ]
    }
   ],
   "source": [
    "df = getdata(dropdown, start)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Before our DCA calculations, we define a buydates array with the range of our fetched dataframe\n",
    "buydates = pd.date_range(df.index[0], df.index[-1], freq = '1M')\n",
    "\n",
    "# Buyprices array\n",
    "buyprices = df[df.index.isin(buydates)].Close"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "coin_amt = investment/buyprices\n",
    "coin_amt_LumpSum = investment * len(buyprices) / buyprices[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "coin_amt_sum = coin_amt.cumsum()\n",
    "coin_amt_sum.name = 'coin_amt_DCA'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_tog = pd.concat([coin_amt_sum,df], axis = 1).ffill()\n",
    "df_tog['coin_amt_LumpSum'] = coin_amt_LumpSum\n",
    "df_tog['Portfolio_DCA_Strategy'] = df_tog.coin_amt_DCA * df_tog.Close\n",
    "df_tog['Portfolio_Lump_Sum_Strategy'] = df_tog.coin_amt_LumpSum * df_tog.Close"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\hp\\AppData\\Local\\Temp\\ipykernel_11244\\4274000957.py:3: RuntimeWarning: invalid value encountered in double_scalars\n",
      "  performance_DCA = (df_tog['Portfolio_DCA_Strategy'][-1] / (investment * len(buyprices))) - 1\n",
      "C:\\Users\\hp\\AppData\\Local\\Temp\\ipykernel_11244\\4274000957.py:4: RuntimeWarning: invalid value encountered in double_scalars\n",
      "  performance_Lump_Sum = (df_tog['Portfolio_Lump_Sum_Strategy'][-1] / (investment *  len(buyprices))) -1\n"
     ]
    }
   ],
   "source": [
    "# Performance Calculations\n",
    "\n",
    "performance_DCA = (df_tog['Portfolio_DCA_Strategy'][-1] / (investment * len(buyprices))) - 1\n",
    "performance_Lump_Sum = (df_tog['Portfolio_Lump_Sum_Strategy'][-1] / (investment *  len(buyprices))) -1 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "st.line_chart(df_tog['Portfolio_Lump_Sum_Strategy'])\n",
    "st.write('Lump Sum Performance: ' + str(round(performance_Lump_Sum * 100, 2)) + ' %')\n",
    "\n",
    "st.line_chart(df_tog['Portfolio_DCA_Strategy'])\n",
    "st.write('DCA Performance: ' + str(round(performance_DCA * 100, 2)) + ' %')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.0 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "63963b3f4c440940f0b94a3100916033a226cb4f45979123153792d60aa56d6a"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
