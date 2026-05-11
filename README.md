# Forex Exchange Using API

A simple Python-based Forex Currency Converter application that fetches real-time exchange rates using an external API.


# Features

- Real-time currency conversion
- Supports different international currencies
- User-friendly command-line interface
- API integration using Python requests
- Error handling for invalid currency codes


# Technologies Used

- Python
- Requests Library
- ExchangeRate API


# How It Works

The program:

1. Takes base currency input from the user
2. Takes target currency input
3. Takes amount to convert
4. Fetches live exchange rates from the API
5. Calculates and displays converted amount


# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/forex-exchange-api.git
```


## Navigate to Project Folder

```bash
cd forex-exchange-api
```



## Install Required Package

```bash
pip install requests
```


# Run the Program

```bash
python main.py
```


# Example Output

```text
Enter the base currency: USD
Enter the target currency: NPR
Enter the amount: 100

Conversion Result
100 USD = 13350.00 NPR
```


# API Used

https://api.exchangerate-api.com


# Project Structure

```text
forex-exchange-api/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```


# Future Improvements

- Add GUI interface
- Build web version using Flask
- Add historical exchange rates
- Add graphical currency charts
- Add support for multiple conversions


# Author

Karan Bhatt
