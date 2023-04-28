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

    def get_noise_count(self) -> dict[int, int]:
        noise = {}
        for line in self.chart:
            cnt = noise.get(len(line), 0)
            noise[len(line)] = cnt + 1

        return noise

    def get_chart_line_count(self) -> int:
        return len(self.chart)



