from trade_simulator.trade_simulator import TradeSimulator


def main():
    path = "lib/BTC_USD.csv"
    ts = TradeSimulator(path)
    lines = ts.get_chart_head(10)
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
