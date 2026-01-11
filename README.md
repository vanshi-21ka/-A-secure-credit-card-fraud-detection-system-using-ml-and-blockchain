# Fraud Detection Project

This project is a simple demo that combines **Machine Learning** and **Blockchain**.

The goal is to show how a transaction can be:

- predicted using an ML model
- secured using a hash
- stored safely on a blockchain

---

## How It Works

1. Transaction data is given to the ML model
2. The model predicts if it is fraud or not
3. A hash is created from the result
4. The data is saved on the blockchain

---

## Setup

1. Create and activate a virtual environment:

- python -m venv venv

- venv\Scripts\activate # Windows

# or

- source venv/bin/activate # macOS/Linux

2. Install required packages:

- pip install -r requirements.txt

---

## Blockchain

- Run Ganache
- Deploy the smart contract using Remix
- Copy the contract address into `store_to_blockchain.py`

---

## Run

From the project root:

python blockchain/store_to_blockchain.py

---

## Output

The program prints:

- the model prediction
- the generated hash
- the blockchain transaction hash

---

This project shows a basic flow from **ML → Hash → Blockchain**.
