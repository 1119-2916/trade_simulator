import csv
from datetime import datetime, timedelta

from .olhcv import OLHCV


class ChartDB:
    def __init__(self, input_path: str = None, olhcv_list: list[OLHCV] = None) -> None:
        # csv 読み込みと olhcv リスト注入だと後者が優先される
        self.olhcvs = None
        self.chart = None
        if input_path is not None:  # test fixture 導入までは引数 None を認める
            self.read_csv(input_path=input_path)
        if olhcv_list is not None:
            self.set_OLHCV_list(olhcvs=olhcv_list)

    def read_csv(self, input_path: str) -> None:
        with open(input_path) as f:
            reader = csv.reader(f)
            self.chart = [row for row in reader]
            self.chart.pop(0)  # 先頭行はカラム名なので除去

    def set_OLHCV_list(self, olhcvs: list[OLHCV]) -> None:
        self.olhcvs = olhcvs

    def get_all_chart(self) -> list[list]:
        return self.chart

    def get_OLHCV(self, target_datetime: datetime) -> OLHCV:
        if self.olhcvs is None:
            self._generate_OLHCV_list()
        for i in self.olhcvs:
            diff: timedelta = i.time - target_datetime
            if abs(diff.total_seconds()) < 30.0:  # 1分足で取得することを想定している
                return i
        return None

    @staticmethod
    def generate_OLHCV_from_cryptodatadownload_style_list(input: list) -> OLHCV:
        """
        cryptodatadownload のサイトで取得できる csv を
        読み込んだ list から OLHCV オブジェクトリストを生成する
        """

        unix = int(input[0])
        format = "%Y-%m-%d %H:%M:%S"
        dt = datetime.strptime(input[1], format)
        open = int(input[3])
        high = int(input[4])
        low = int(input[5])
        close = int(input[6])
        volume = float(input[7])
        return OLHCV(unix, dt, input[2], open, high, low, close, volume)

    def get_all_OLHCV(self) -> list[OLHCV]:
        return self.olhcvs

    def get_chart_head(self, lines: int) -> list:
        return self.chart[:lines]

    def get_noise_count(self) -> dict[int, int]:
        noise = {}
        for line in self.chart:
            cnt = noise.get(len(line), 0)
            noise[len(line)] = cnt + 1

        return noise

    def get_chart_line_count(self) -> int:
        return len(self.chart)

    def _generate_OLHCV_list(self) -> None:
        self.olhcvs: list[OLHCV] = [
            self.generate_OLHCV_from_cryptodatadownload_style_list(i)
            for i in self.chart
        ]
