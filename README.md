# Irradiance-Analysis-Tool
Description
This tool is designed to calculate the Root Mean Square of Successive Differences (RMSSD) for irradiance data, specifically for solar energy systems. It features a graphical user interface (GUI) built with Tkinter, allowing users to upload irradiance data files (either CSV or Excel), extract the RMSSD for each day between 11 AM and 2 PM, and save the results in a new CSV file. Additionally, the tool graphs daily RMSSD results for further analysis.

Features
Data Input: Accepts CSV or Excel files containing irradiance data.
RMSSD Calculation: Extracts daily irradiance data from 11 AM to 2 PM and calculates the RMSSD for each day.
Graphing: Displays a graph of the RMSSD values for easy visualization.
CSV Export: Saves the daily RMSSD values to a new CSV file named RMSSD for [input file name].csv for further use.

Installation
To run this project, you’ll need to have Python installed. You also need the following Python libraries:
Tkinter (for the GUI)
matplotlib (for graphing)
pandas (for handling data files)
openpyxl (for handling Excel files, if needed)

Installation steps:

1. Clone the repository:
git clone https://github.com/YOUR_USERNAME/Irradiance-Analysis-Tool.git

2. Navigate to the project directory:
cd Irradiance-Analysis-Tool

3. Install the required libraries:
pip install pandas matplotlib openpyxl

Usage
1. Run the GUI by executing the Python script:
python irr_analysis_gui.py
2. In the GUI window, upload a CSV or Excel file containing irradiance data.
3. The tool will automatically extract the irradiance values between 11 AM and 2 PM for each day and calculate the daily RMSSD.
4. The results will be plotted in the GUI and can be saved to a new CSV file by clicking the "Save" button.
5. The output file will be saved with the name format RMSSD for [input file name].csv in the same directory.

Example Input File
Your input file should have irradiance data with at least these columns:
Date/Time: Timestamp of the data entry
Irradiance: Plane of array irradiance values
Ensure that the data includes timestamps covering the time range from 11 AM to 2 PM for accurate RMSSD calculations.

Output
A CSV file with daily RMSSD values.
A plot displaying RMSSD values for easy analysis.

Contributors
Lynette Mojica: Developer and designer of the tool
Connect with me on LinkedIn
