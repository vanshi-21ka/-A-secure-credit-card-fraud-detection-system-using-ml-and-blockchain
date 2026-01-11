import hashlib
import datetime

def generate_hash(transaction_id, prediction):
    timestamp = datetime.datetime.utcnow().isoformat()
    raw_data = f"{transaction_id}|{prediction}|{timestamp}"
    hash_value = hashlib.sha512(raw_data.encode()).hexdigest()
    return timestamp, hash_value
