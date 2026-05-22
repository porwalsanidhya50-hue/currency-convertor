🌍 Currency Converter
=====================

A simple Python application that converts USD to INR using real-time exchange rates fetched from an API.

---

📋 Table of Contents
--------------------
- Features
- Prerequisites
- Installation
- Usage
- Example
- Project Structure
- Dependencies
- License
- Acknowledgments

---

✨ Features
-----------
- Fetches real-time exchange rates from the ExchangeRate API (https://www.exchangerate-api.com/).
- Converts a user-input amount in USD to INR.
- Handles errors gracefully.

---

⚙️ Prerequisites
-----------------
- Python 3.10 or higher
- pip (Python package manager)

---

🛠️ Installation
----------------
1. Clone the repository:
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate  (On Windows)
   source venv/bin/activate  (On macOS/Linux)

3. Install dependencies:
   pip install -r requirements.txt

4. Set up the `.env` file:
   - The `.env` file is already included in the `.gitignore` for security.
   - Add the following line to your `.env` file:
     API_URL = "https://open.er-api.com/v6/latest/USD"

---

🚀 Usage
--------
1. Run the application:
   python app.py

2. Enter the amount in USD when prompted, and the application will display the equivalent amount in INR.

---

💡 Example
----------
Enter Amount: 100
100$ is equivalent to ₹8300.00

---

📂 Project Structure
--------------------
.
├── app.py             # Main application script
├── .env               # Environment variables (not included in version control)
├── .gitignore         # Git ignore file
├── README.txt         # Project documentation
├── requirements.txt   # Python dependencies
└── venv/              # Virtual environment (ignored in version control)

---

📦 Dependencies
---------------
- requests: For making HTTP requests to the API.
- python-dotenv: For loading environment variables from the `.env` file.

---

📜 License
----------
This project is licensed under the MIT License. See the LICENSE file for details.

---

🙏 Acknowledgments
------------------
- ExchangeRate API ("https://open.er-api.com/v6/latest/USD") for providing the exchange rate data.