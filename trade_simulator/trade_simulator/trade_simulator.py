import csv


class TradeSimulator:
    def __init__(self, input_path: str) -> None:
        with open(input_path) as f:
            reader = csv.reader(f)
            self.chart = [row for row in reader]

    def get_all_chart(self) -> list[list]:
        pass

    def get_chart_head(self, lines: int) -> list:
        return self.chart[:lines]

    def get_noise_count(self) -> int:
        pass

