# Betking Betting Scraper

The **Betking Betting Scraper** automates the process of extracting betting data from the Betking platform. This script captures live odds for various football matches, offering valuable insights for bettors.

## 📌 Features

- **Real-Time Data Extraction**: Retrieves live betting data for today's football matches on Betking.
- **Clear Code Structure**: The code is organized and easy for developers to read and modify.
- **CSV Output**: Outputs the extracted data in a structured CSV format for easy analysis.
- **Data Deduplication**: Automatically removes duplicate entries to maintain clean data storage.

## 🚀 How It Works

1. **Initialization**: The script initializes the Selenium WebDriver to open the Betking website.
2. **Waiting for Elements**: It waits for specific elements on the page to load, ensuring data accuracy.
3. **Data Extraction**: The script captures the match time, home team, away team, and odds for each match.
4. **Output**: The results are saved in a CSV file for further analysis.

### Key Components:

- **Web Scraping**: Utilizes Selenium for navigating the website and extracting data.
- **Data Structuring**: Organizes the scraped data into a dictionary format for easy saving.
- **CSV File Management**: Handles the creation and management of CSV files for output.

## 🛠️ Requirements

Before running the script, ensure the following packages are installed:

- **Python 3.x**
- **Selenium**
- **Pandas**

Install the required packages using pip:
```bash
pip install selenium pandas
```

## 🏃 How to Run the Script

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ezee-Kits/Betking-Betting-Scraper.git
   ```

2. **Set up ChromeDriver**:  
   Download and install [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for your browser. Ensure the ChromeDriver is in your system path.

3. **Run the Python Script**:
   ```bash
   python betking_scraper.py
   ```

4. **View Results**:  
   The scraped data will be saved in a CSV file located at the specified path.

## 📁 Output

The output CSV file will contain the following fields:
- **TIME**: The scheduled time of the match.
- **HOME TEAM**: The name of the home team.
- **AWAY TEAM**: The name of the away team.
- **HOME ODD**: Odds for the home team to win.
- **DRAW ODD**: Odds for a draw.
- **AWAY ODD**: Odds for the away team to win.
- **BOOKMAKER**: The name of the bookmaker (in this case, Betking).

## 🔧 Future Improvements

- **Error Handling**: Implement more robust error handling to manage unexpected changes in the website structure.
- **Enhanced Data Analysis**: Integrate data analysis tools for better insights into betting patterns.
- **User Interface**: Develop a graphical user interface (GUI) for easier user interaction.
- **Mobile Compatibility**: Adapt the script for mobile devices to facilitate on-the-go data extraction.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🤝 Contributing

Feel free to contribute by opening issues, suggesting improvements, or submitting pull requests. All feedback is welcome!
