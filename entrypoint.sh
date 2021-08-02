#!/bin/sh

sleep 1s

# create SNS topic
aws --endpoint-url=http://localhost:4566 sns create-topic --name pismo

# create SQS queue
aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name pismo-queue

# subscribe SQS queue in SNS topic
aws --endpoint-url=http://localhost:4566 sns subscribe --topic-arn "arn:aws:sns:us-east-1:000000000000:pismo" --protocol sqs --notification-endpoint "arn:aws:sqs:us-east-1:000000000000:pismo-queue"