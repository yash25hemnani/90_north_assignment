# AWS Lambda: Add Two Numbers

This project contains an AWS Lambda function written in Python to add two numbers. The function accepts input via a JSON payload, processes the addition, and returns the result in a JSON response.

---

## Features
- Accepts two numbers via a JSON payload.
- Validates the inputs.
- Performs addition on the input numbers.
- Returns the result in a structured JSON format.

---

## Example Payload

### Input
The Lambda function expects a payload in the following format:
```json
{
    "number1": 10,
    "number2": 20
}
```

### Output
The function returns the sum of the two numbers:
```json
{
    "message": "Addition successful",
    "result": 30
}
```
