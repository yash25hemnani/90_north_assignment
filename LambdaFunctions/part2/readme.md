# AWS Lambda: Store Document in S3

This project contains an AWS Lambda function that uploads a document (e.g., PDF file) to an S3 bucket. The file is provided as a Base64-encoded string in the input payload and is stored securely in the specified S3 bucket.

---

## Features
- Accepts a document or PDF as a Base64-encoded string in the payload.
- Decodes the Base64 string and uploads the file to an S3 bucket.
- Generates a unique file name if not provided.
- Returns the public URL of the uploaded file.

---

## Example Payload

### Input
The Lambda function expects a payload in the following format:
```json
{
    "file_content": "BASE64_ENCODED_STRING_HERE",
    "file_name": "example-document.pdf"
}
```
## Example Output

### Output
On successful execution, the function returns:
```json
{
    "message": "File uploaded successfully",
    "file_url": "https://<bucket-name>.s3.amazonaws.com/example-document.pdf"
}
```

## Add Environment Variables
The Lambda function requires an environment variable to specify the S3 bucket where files will be stored.

- Navigate to the Configuration tab in your Lambda function.
- Click Environment variables → Edit → Add environment variable:
- Key: S3_BUCKET_NAME
- Value: Your bucket name (e.g., my-upload-bucket).
