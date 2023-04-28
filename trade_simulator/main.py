from trade_simulator.trade_simulator import TradeSimulator


def main():
    path = "lib/BTC_USD.csv"
    ts = TradeSimulator(path)
    noise_dict = ts.get_noise_count()
    for k, v in noise_dict.items():
        print(f"len = {k}, cnt = {v}")


def noise_check(ts: TradeSimulator):
    noise_dict = ts.get_noise_count()
    for k, v in noise_dict.items():
        print(f"len = {k}, cnt = {v}")


if __name__ == "__main__":
    main()
