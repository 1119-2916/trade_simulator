from trade_simulator.chart_DB import ChartDB


def main():
    path = "lib/BTC_USD.csv"
    ts = ChartDB(path)
    noise_dict = ts.get_noise_count()
    for k, v in noise_dict.items():
        print(f"len = {k}, cnt = {v}")


if __name__ == "__main__":
    main()
