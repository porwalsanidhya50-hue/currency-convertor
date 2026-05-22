import requests
from dotenv import load_dotenv
import os

load_dotenv()

try:
    response = requests.get(os.getenv("API_URL"))
    data = response.json()
    inr_rate = data["rates"]["INR"]
    amountInUSD = int(input("Enter Amount: "))
    convertedAmount = amountInUSD * inr_rate
    print(f"{amountInUSD}$ is equivalent to ₹{convertedAmount:.2f}")
except Exception as e:
    print(f"Error: {e}")

    
