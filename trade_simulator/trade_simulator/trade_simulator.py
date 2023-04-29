import csv
import datetime
from .olhcv import OLHCV


class TradeSimulator:
    def __init__(self, input_path: str = None) -> None:
        if input_path is not None:
            with open(input_path) as f:
                reader = csv.reader(f)
                self.chart = [row for row in reader]

    def get_all_chart(self) -> list[list]:
        pass

    def _generate_OLHCV_from_cryptodatadownload_style_list(self, input: list) -> OLHCV:
        unix = int(input[0])
        format = "%Y-%m-%d %H:%M:%S"
        dt = datetime.datetime.strptime(input[1], format)
        open = int(input[3])
        high = int(input[4])
        low = int(input[5])
        close = int(input[6])
        volume = int(input[7])
        return OLHCV(unix, dt, input[2], open, high, low, close, volume)

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
