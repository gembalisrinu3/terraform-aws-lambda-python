module "lambda_python" {
  source            = "../../"

  #aws_profile       = "default"
  aws_region        = "us-west-2"

  pip_path          = "usr/bin/pip"

  lambda_name       = "lambda_example"
  #lambda_api_name   = "lambda_example_api"
  lambda_iam_name   = "lambda_example_iam"

  #api_stage_name    = "dev"
  #api_resource_path = "example"
  #api_http_method   = "POST"
}
