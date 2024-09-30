import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog, Label, Button
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os


def calculate_rmssd(data):
    irradiance = data['PlaneOfArrayIrradiance']
    differences = np.diff(irradiance)
    rmssd = np.sqrt(np.mean(differences ** 2))
    return rmssd


def filter_data_between_hours(data):
    # Combine date and time columns into a datetime column
    data['Datetime'] = pd.to_datetime(data['TELEM DATE'].str.strip() + ' ' + data['TELEM TIME'].str.strip(),
                                      format='%d/%m/%Y %H:%M:%S', errors='coerce')

    # Filter for the times between 11:00 AM and 2:00 PM
    data = data[(data['Datetime'].dt.hour >= 11) & (data['Datetime'].dt.hour < 14)]

    return data


def calculate_daily_rmssd(data):
    # Filter data between 11am and 2pm
    filtered_data = filter_data_between_hours(data)

    # Group by 'TELEM DATE' and calculate RMSSD for each day
    daily_rmssd = filtered_data.groupby('TELEM DATE').apply(lambda x: calculate_rmssd(x))

    return daily_rmssd


def save_rmssd_to_file(daily_rmssd, input_file):
    # Extract the input file name (without the extension) for the output file name
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = f"RMSSD for {base_name}.csv"

    # Save the results to a CSV file
    df = pd.DataFrame(daily_rmssd, columns=['RMSSD'])
    df.reset_index(inplace=True)  # Reset index to make 'TELEM DATE' a column
    df.to_csv(output_file, index=False)

    return output_file


def graph_daily_rmssd(daily_rmssd):
    # Plot the daily RMSSD results
    plt.figure(figsize=(8, 6))
    plt.plot(daily_rmssd.index, daily_rmssd.values, marker='o', linestyle='-', label='Daily RMSSD')
    plt.title('Daily RMSSD Values')
    plt.xlabel('Date')
    plt.ylabel('RMSSD')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Show the plot in the GUI
    fig, ax = plt.subplots()
    ax.plot(daily_rmssd.index, daily_rmssd.values, marker='o', linestyle='-', label='Daily RMSSD')
    ax.set_title('Daily RMSSD Values')
    ax.set_xlabel('Date')
    ax.set_ylabel('RMSSD')
    plt.xticks(rotation=45)

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()


def open_file():
    global data
    filepath = filedialog.askopenfilename(filetypes=[("Excel and CSV files", "*.xlsx *.xls *.csv")])
    if not filepath:
        return
    try:
        # Detect file type and load the file
        if filepath.endswith('.csv'):
            data = pd.read_csv(filepath)
        else:
            data = pd.read_excel(filepath)

        # Calculate daily RMSSD
        daily_rmssd = calculate_daily_rmssd(data)

        # Save the results to a new file
        output_file = save_rmssd_to_file(daily_rmssd, filepath)
        output_label.config(text=f"RMSSD calculated and saved to {output_file}.")

        # Graph the daily RMSSD results
        graph_daily_rmssd(daily_rmssd)

    except Exception as e:
        output_label.config(text=f"Error: {e}")


# Set up the GUI
window = tk.Tk()
window.title("RMSSD Calculator")
window.geometry("800x600")

open_button = Button(window, text="Open Excel or CSV File", command=open_file)
open_button.pack()

output_label = Label(window, text="")
output_label.pack()

# Frame for the plot
plot_frame = tk.Frame(window)
plot_frame.pack(fill=tk.BOTH, expand=True)

window.mainloop()
