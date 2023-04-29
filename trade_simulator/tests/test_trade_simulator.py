from trade_simulator.trade_simulator import TradeSimulator
from trade_simulator.olhcv import OLHCV
from datetime import datetime


def test_generate_collect_OLHCV():
    ut = 123456789
    t = datetime(year=1111, month=12, day=13, hour=14, minute=15, second=16)
    t_str = "1111-12-13 14:15:16"
    sym = "BBB/TTC"
    op = 1111
    lo = 1000
    hi = 2000
    cl = 1222
    vl = 101010

    collect = OLHCV(unix_time=ut, time=t, symbol=sym, open=op, low=lo, high=hi, close=cl, volume=vl)
    input = [str(ut), t_str, sym, str(op), str(lo), str(hi), str(cl), str(vl)]
    ts = TradeSimulator(None)

    assert ts._generate_OLHCV_from_cryptodatadownload_style_list(input) == collect
