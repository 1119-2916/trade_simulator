from datetime import datetime, timedelta

from trade_simulator.chart_db import ChartDB
from trade_simulator.olhcv import OLHCV


class Simulator:
    def __init__(self) -> None:
        self.setup_db()
        self.setup_user_status()

    def setup_db(self, input_path: str = "lib/BTC_USD.csv") -> None:
        self.db = ChartDB(input_path=input_path)

    def setup_user_status(
        self,
        usd: float = 1000.00,
        btc: float = 0.00,
        start_datetime: datetime = None,
        end_datetime: datetime = None,
    ) -> None:
        self.user_usd = usd
        self.user_btc = btc
        if end_datetime is None:
            latest: OLHCV = self.db.get_chart_head(1)
            self.end_time = latest[0].time
        else:
            self.end_time = end_datetime
        if start_datetime is None:
            start = self.end_time - timedelta(days=365)
            self.next_time = start
        else:
            self.next_time = start_datetime

    def reset(self) -> None:
        self.db = None

    def next(self) -> OLHCV:
        pass
