from web3 import Web3
import json
import sys
import os
import warnings

warnings.filterwarnings(
    "ignore",
    message="X does not have valid feature names"
)

# Allow imports from parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ml.predict import predict_transaction
from ml.hash_utils import generate_hash

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
assert w3.is_connected(), "Ganache not running!"

# Load ABI
ABI_PATH = os.path.join(os.path.dirname(__file__), "fraud_logger_abi.json")
with open(ABI_PATH) as f:
    abi = json.load(f)

raw_address = "0x4CB7bCD1412e40ac83a7a31dD220Ed9f85D44571"
contract_address = Web3.to_checksum_address(raw_address)

contract = w3.eth.contract(
    address=contract_address,
    abi=abi
)


account = w3.eth.accounts[0]

transaction_id = "TXN_982341"
features = features = [
    0.1, -1.2, 0.3, 0.4, 0.5,
    -0.6, 0.7, 0.8, -0.9, 1.0,
    0.11, -0.12, 0.13, 0.14, -0.15,
    0.16, 0.17, -0.18, 0.19, 0.20,
    -0.21, 0.22, 0.23, -0.24, 0.25,
    0.26, -0.27, 0.28, 120.4, 98234
]

expected_label = 1

# --- ML Prediction ---
prediction = predict_transaction(features)

# --- Validation ---
is_correct = None
if expected_label is not None:
    is_correct = prediction == expected_label

# --- Hash Generation ---
timestamp, hash_value = generate_hash(transaction_id, prediction)

# --- Output ---
label_map = {0: "LEGIT", 1: "FRAUD"}

print("\n ML PREDICTION RESULT")
print("-" * 40)
print(f"Transaction ID : {transaction_id}")
print(f"Features       : {features}")
print(f"Prediction     : {label_map[prediction]} ({prediction})")

if expected_label is not None:
    print(f"Expected Label : {label_map[expected_label]} ({expected_label})")
    print(f"Correct        : {'YES' if is_correct else 'NO'}")

print(f"Timestamp      : {timestamp}")
print(f"Hash (SHA-512) : {hash_value}")
prediction = predict_transaction(features)
timestamp, hash_value = generate_hash(transaction_id, prediction)

tx_hash = contract.functions.storeRecord(
    transaction_id,
    prediction,
    timestamp,
    hash_value
).transact({"from": account})

receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print("Transaction hash:", receipt["transactionHash"].hex())
print("Connected:", w3.is_connected())
print("Using account:", account)
print("Contract address:", contract.address)

