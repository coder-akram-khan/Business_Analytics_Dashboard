# Business Analytics Dashboard

## Description

The Business Analytics Dashboard is a Streamlit application designed to visualize and analyze employee data. 
It offers flexibility in data loading, allowing you to import data from a local MySQL database or a CSV file. 
The application empowers users to gain insights into employee metrics like salary, department distribution, and more, 
through various visualizations like charts, tables, and key performance indicators (KPIs).

### Features

- **Data Loading:** Load data from a local MySQL database or a CSV file.
- **Interactive Filters:** Filter data by department, country, and business unit to focus on specific areas.
- **Visualizations:** Gain insights through various charts, including pie charts, bar charts, heatmaps, and treemaps.
- **Downloadable Data:** Export filtered data as a CSV file for further analysis in other tools.
- **Responsive Design:** The dashboard is user-friendly and adapts to different screen sizes.

## File Structure

    .
    ├── database/SQL.sql  (Database schema definition)
    ├── export_to_csv.py  (Script for exporting data to CSV)
    ├── mysql_con.py  (Module for connecting to MySQL database)
    ├── requirements.txt  (List of required Python packages)
    ├── dataset.csv  (Sample employee data CSV file)
    ├── Main.py  (Main script for running the Streamlit application)
    ├── pycache  (Automatically generated cache files)
    ├── style.css  (Optional CSS file for styling the dashboard)
    └── config.toml  (Optional configuration file for the application)


## Installation

1. **Clone the repository:**

   ```bash
   https://github.com/coder-akram-khan/Business_Analytics_Dashboard.git
   cd Business_Analytics_Dashboard/  

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt

3. **Set up your MySQL database (if using MySQL):**

    Create a database named my_streamlit.
    Import the database/SQL.sql file into the created database to set up the necessary tables and data.

2. **Run the application:**
   ```bash
   streamlit run Main.py

Usage

    Use the sidebar to filter the data based on department, country, and business unit.
    View various visualizations and metrics on the dashboard to gain insights.
    Download the filtered data as a CSV file using the provided button for further analysis in other tools.


