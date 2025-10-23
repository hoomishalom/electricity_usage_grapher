import matplotlib.pyplot as plt
import pandas as pd
import sys

def main():
    if (len(sys.argv) != 2):
        print(f"Wrong amount of arguments, usage: 'python3 {__file__} filename.csv'")
        return

    df = pd.read_csv(sys.argv[1])
    consumption_mean_by_time = df.groupby("starting time")["consumption"].mean()
    x_labels = list(consumption_mean_by_time.index.to_numpy())

    fig_width = max(10, len(x_labels) * 0.2)

    consumption_mean_by_time.plot(figsize=(fig_width, 10))
    plt.ylabel("Mean consumption in KWh")
    plt.xlabel("Period starting time")

    plt.xticks(range(len(x_labels)), x_labels, rotation=90, size='small')
    plt.tight_layout()

    plt.savefig("output.png")

    
if __name__ == "__main__":
    main()
