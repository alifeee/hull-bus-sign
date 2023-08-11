import os
import matplotlib.pyplot as plt
import pandas
import numpy

FOLDER = "send-0x0e00_1-clock_2-data_0"
file_dir = os.path.dirname(__file__)

plt.style.use("dark_background")

if __name__ == "__main__":
    # import data with pandas csv
    ch1_filename = os.path.join(file_dir, FOLDER, "CH1.csv")
    ch2_filename = os.path.join(file_dir, FOLDER, "CH2.csv")
    ch1_df = pandas.read_csv(ch1_filename, header=None)
    ch2_df = pandas.read_csv(ch2_filename, header=None)

    # the settings are the top 19 rows and the first 2 columns
    ch1_settings_df = ch1_df.iloc[:19, :2]
    # make into dictionary with the first column as the key
    ch1_settings = dict(zip(ch1_settings_df.iloc[:, 0], ch1_settings_df.iloc[:, 1]))

    ch2_settings_df = ch2_df.iloc[:19, :2]
    ch2_settings = dict(zip(ch2_settings_df.iloc[:, 0], ch2_settings_df.iloc[:, 1]))

    # the data is the rest of the rows
    # the first column is the time
    # the second column is the voltage

    ch1_data_df = ch1_df.iloc[19:, -3:-1]
    ch2_data_df = ch2_df.iloc[19:, -3:-1]

    ch1_voltage = ch1_data_df.iloc[:, 1].to_numpy()
    TRIGGER_VAL_V = 1

    rising_edges_indices = (
        numpy.flatnonzero(
            (ch1_voltage[:-1] < TRIGGER_VAL_V) & (ch1_voltage[1:] > TRIGGER_VAL_V)
        )
        + 1
    )
    print(rising_edges_indices)

    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212, sharex=ax1, sharey=ax1)

    ax1.plot(ch1_data_df.iloc[:, 0], ch1_data_df.iloc[:, 1], color="yellow")
    ax2.plot(ch2_data_df.iloc[:, 0], ch2_data_df.iloc[:, 1], color="cyan")

    # plot grey vertical lines at the rising edges
    for index in rising_edges_indices:
        ax1.axvline(ch1_data_df.iloc[index, 0], color="grey", alpha=0.5)
        ax2.axvline(ch2_data_df.iloc[index, 0], color="grey", alpha=0.5)

    ax1.set_ylabel("Voltage (V)")
    ax2.set_ylabel("Voltage (V)")
    ax2.set_xlabel("Time (s)")

    plt.xlim(-2e-5, 2.4e-4)

    fig.savefig(os.path.join(file_dir, "single_message.png"), dpi=300)
    plt.show()
