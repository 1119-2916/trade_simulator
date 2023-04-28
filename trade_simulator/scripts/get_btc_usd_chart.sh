#!/bin/bash
cd `dirname $0`
# sed 未テスト
curl -L https://www.cryptodatadownload.com/cdd/Bitstamp_BTCUSD_2023_minute.csv | sed "1d" > ../lib/BTC_USD.csv
