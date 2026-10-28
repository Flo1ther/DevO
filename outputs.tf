
output "api_url" {
  description = "Public GET endpoint"
  value = "${aws_apigatewayv2_api.api.api_endpoint}/files"
}

output "s3_bucket_name" {
  description = "Created S3 bucket"
  value       = aws_s3_bucket.storage.bucket
}

output "lambda_function_name" {
  value = aws_lambda_function.api.function_name
}
