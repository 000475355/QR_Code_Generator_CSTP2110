# AWS-Based QR Code Generator

This project implements a serverless QR Code Generator using AWS services.  
Users can input text or a URL and instantly generate a downloadable QR code stored in an S3 bucket.

---

## 🚀 Project Architecture

- **Frontend**: Simple HTML form.
- **API Gateway**: Exposes an HTTPS endpoint to receive user input.
- **AWS Lambda**: Python/Node.js function generates QR code dynamically.
- **AWS S3**: Stores generated QR code images, accessible via public URLs.
- **AWS CloudWatch**: Monitors system health and triggers alarms for any failures.

---

## 🛠️ Setup Instructions

1. **Deploy S3 Bucket**  
   - Enable public read access for generated QR codes (only for the generated files folder).
   - Enable server-side encryption (SSE-S3).

2. **Deploy Lambda Function**  
   - Runtime: Python or Node.js.
   - Role: Limited permissions with access to S3 PutObject.

3. **Create API Gateway Endpoint**  
   - Integration: Lambda Proxy Integration.
   - Method: POST (user sends text or URL).

4. **Connect Frontend to API Gateway**  
   - Update the HTML form to call the API Gateway URL.

5. **Monitoring Setup (CloudWatch)**  
   - Metrics Tracked:
     - Lambda invocation count, duration, errors
     - S3 PUT operations
   - Alarms Created:
     - Lambda errors > 1 in 5 minutes
     - API Gateway 501 errors > 5 per minute

---

## 🔒 Security Setup

- IAM Role for Lambda:
  - Only permission to PutObject in S3.
- S3 Bucket:
  - Public access blocked except for the `/public` folder.
  - Server-side encryption enabled (SSE-S3).
- API Keys:
  - No API keys hardcoded in code.
- AWS Read-Only Reviewer Account:
  - IAM user created with ReadOnlyAccess for project review.
- Private environment variables used inside Lambda.

---

## 📊 Business and System Metrics

- **Business Metric**: Number of QR codes generated (based on Lambda invocations).
- **System Metrics**:
  - `NumberOfMessagesSent` (if using SQS)
  - `NumberOfMessagesReceived`
  - `ApproximateAgeOfOldestMessage`

- **CloudWatch Alarms**:
  - High Lambda Error Rates
  - High API Gateway 5XX Errors



---

## 📎 Notes

- No paid services are activated.
- Project is serverless and fully scalable within the Free Tier.
- All resources are tagged for easy identification.

---

## 📚 References

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [AWS API Gateway Documentation](https://docs.aws.amazon.com/apigateway/)
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)
- [AWS CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/)

---
