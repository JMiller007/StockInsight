# StockInsight

StockInsight is a web application that allows users to visualize historical stock prices using interactive charts. The application leverages Flask for the backend, Plotly for creating charts, and yfinance for fetching stock data. Additionally, it provides educational links to learn more about investing and stocks.

## Features

- **Interactive Visualizations**: Generate dynamic line charts to explore stock price trends over time.
- **Real-Time Data**: Fetches up-to-date stock data to ensure accurate visualizations.
- **User-Friendly Interface**: Simple and intuitive form for entering stock symbols and viewing results.
- **Educational Links**: Provides links to learn more about investing and stocks.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **Plotly**: An open-source graphing library that makes interactive, publication-quality graphs.
- **yfinance**: A library that allows easy access to stock market data from Yahoo Finance.
- **HTML/CSS**: For structuring and styling the user interface.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/JMiller007/StockInsight.git
   cd StockInsight
   ```

2. **Set Up a Virtual Environment**:

   On macOS and Linux:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install Flask plotly yfinance
   ```

## Usage

1. **Run the Application**:

   ```bash
   python app.py
   ```

2. **Access the Application**:
   Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to start using StockInsight.

3. **Using the Application**:
   - Enter a valid stock symbol (e.g., AAPL for Apple) in the input field.
   - Click on the "Fetch Data" button to generate the stock price visualization.
   - View the interactive line chart displaying the historical stock prices.
   - Click on the "Learn More" buttons to navigate to pages that teach you about investing and stocks.

## Project Structure

```
StockInsight/
├── templates/
│   ├── index.html
│   ├── investing.html
│   ├── stocks.html
├── app.py
├── README.md
└── venv/
```

- `templates/`: Contains the HTML templates for the application.
  - `index.html`: The main page of the application where users can input stock symbols and view visualizations.
  - `investing.html`: Page providing information about investing.
  - `stocks.html`: Page providing information about stocks.
- `app.py`: The main Flask application file.
- `README.md`: This README file.
- `venv/`: The virtual environment directory (not included in the repository, but created locally).

## License

This project is licensed under the MIT License.
