// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FraudLogger {
    struct FraudRecord {
        string transactionId;
        uint8 prediction; 
        string timestamp;
        string hashValue;
    }

    FraudRecord[] public records;

    event FraudStored(
        string transactionId,
        uint8 prediction,
        string timestamp,
        string hashValue
    );

    function storeFraudRecord(
        string memory _transactionId,
        uint8 _prediction,
        string memory _timestamp,
        string memory _hashValue
    ) public {
        records.push(
            FraudRecord(_transactionId, _prediction, _timestamp, _hashValue)
        );

        emit FraudStored(_transactionId, _prediction, _timestamp, _hashValue);
    }
}
