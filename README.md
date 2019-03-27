# aws-serverless-website
Code for my serverless website facilitated by Amazon Web Services.

# Cloud Services Used
* <strong>AWS S3</strong>: AWS Simple Storage Service is used to store and host the website files.
* <strong>AWS RDS</strong>: A MySQL database is used to store information about currently hosted repositories in my Github account. 
           This is to avoid making request to the Github API everytime a user visits the website.
* <strong>AWS Lambda</strong>: Two Lambda functions are used. The first function uses Github API to update the repositories in the database. 
           The second function acts as a rest API, it serves JSON content containing details of my github repositories currently stored in the database.
 * <strong>AWS ApiGateway</strong>: AWS API Gateway is used as a trigger for the lambda function that serves as the rest API.
 * <strong>AWS CloudWatch</strong>: A Cloudwatch rule is used as a trigger for the lambda function that updates the database. A cron expression was used to schedule updating the database.
