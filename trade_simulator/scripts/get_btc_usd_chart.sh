#!/bin/bash
cd `dirname $0`
curl -L https://www.cryptodatadownload.com/cdd/Bitstamp_BTCUSD_2023_minute.csv -o ../lib/BTC_USD.csv
