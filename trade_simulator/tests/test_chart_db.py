from datetime import datetime

from trade_simulator.chart_db import ChartDB
from trade_simulator.olhcv import OLHCV


def test_read_csv():
    target = ChartDB()
    target.read_csv("tests/fixture/btc_usd.csv")
    assert len(target.chart) == 9
    assert target.chart[0] == [
        "1682638980",
        "2023-04-27 23:43:00",
        "BTC/USD",
        "29422",
        "29422",
        "29415",
        "29415",
        "0.00120342",
        "35.3985993",
    ]


def test_get_olhcv():
    db = ChartDB()
    db.read_csv("tests/fixture/btc_usd.csv")
    format = "%Y-%m-%d %H:%M:%S"
    time = datetime.strptime("2023-04-27 23:39:00", format)
    target = db.get_OLHCV(time)

    assert target.unix_time == 1682638740


def test_get_olhcv_head():
    db = ChartDB()
    db.read_csv("tests/fixture/btc_usd.csv")
    target = db.get_olhcv_head(2)

    assert len(target) == 2
    assert target[0].unix_time == 1682638980
    format = "%Y-%m-%d %H:%M:%S"
    time = datetime.strptime("2023-04-27 23:42:00", format)
    assert target[1].time == time


def test_generate_collect_OLHCV():
    ut = 123456789
    t = datetime(year=1111, month=12, day=13, hour=14, minute=15, second=16)
    t_str = "1111-12-13 14:15:16"
    sym = "BBB/TTC"
    op = 1111
    lo = 1000
    hi = 2000
    cl = 1222
    vl = 10.1010

    collect = OLHCV(
        unix_time=ut, time=t, symbol=sym, open=op, low=lo, high=hi, close=cl, volume=vl
    )
    input = [str(ut), t_str, sym, str(op), str(lo), str(hi), str(cl), str(vl)]
    db = ChartDB()

    assert db.generate_OLHCV_from_cryptodatadownload_style_list(input) == collect
