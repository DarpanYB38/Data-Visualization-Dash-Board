
# Data Visualization Dashboard

## Overview

This project is a Data Visualization Dashboard built using Flask. It allows users to view and analyze sales, expenses, and profit data through interactive charts. The dashboard is dynamically generated based on the selected month, and users can also export the data to a CSV file.

## Features

- **Dynamic Charts**: Visualize sales, expenses, and profit data with interactive charts.
- **Month Selection**: Filter data by month to see specific trends.
- **Export Data**: Download the data as a CSV file.
- **Responsive Design**: A user-friendly interface with a clean layout.

## Technologies Used

- **Flask**: Web framework for Python.
- **Matplotlib**: Plotting library for generating charts.
- **Pandas**: Data manipulation and analysis library.
- **HTML/CSS**: For structuring and styling the web pages.

## Installation

1. **Clone the Repository**

   ```bash
     git clone https://github.com/yourusername/your-repository-name.git
   ```
## Navigate to the Project Directory
```
  cd DarpanYB38
```
## Install Required Packages
```
  pip install -r requirements.txt
```
## Generate Sample Data
If sales_data.csv does not already exist, create it using the provided data.py script:
```
  python data.py
```
## Run the Flask Application
```
  python app.py
```
### Open your browser and go to http://127.0.0.1:5000/ to view the dashboard.
## Usage
1. Viewing the Dashboard

- Navigate to the home page to see the dashboard.
- Select a month from the dropdown menu to filter the data.
- View interactive charts for Sales, Expenses, and Profit.
  
2. Exporting Data
- Click the "Export Data" button to download the data as a CSV file.
  
## Project Structure
your-repository-name/
│
├── static/
│   └── images/
│       ├── image1.jpg
│       └── image2.png
│
├── templates/
│   ├── index.html
│   └── dashboard.html
│
├── app.py
├── data.py
├── requirements.txt
└── README.md
## Requirements
- Python 3.x
- Flask
- Matplotlib
- Pandas

## License
This project is licensed under the MIT License - see the LICENSE file for details.
