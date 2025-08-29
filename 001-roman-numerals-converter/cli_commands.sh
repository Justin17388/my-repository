#!/bin/bash

aws ec2 create-security-group --group-name RomanNumSecurityGroup --description "Open HTTP, open port 80, open 8080, open SSH"

aws ec2 authorize-security-group-ingress \
    --group-id RomanNumSecurityGroup \
    --protocol tcp \
    --port 22 \
    --cidr 0.0.0.0/0

aws ec2 authorize-security-group-ingress \
    --group-id RomanNumSecurityGroup \
    --protocol tcp \
    --port 80\
    --cidr 0.0.0.0/0

aws ec2 authorize-security-group-ingress \
    --group-id RomanNumSecurityGroup \
    --protocol tcp \
    --port 8080 \
    --cidr 0.0.0.0/0

Latest_AMI=$(aws ssm get-parameter \
    --name "/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64" \
    --query 'Parameter.Value' \
    --output text)

aws ec2 run-instance \
    --image-id: $Latest_AMI \
    --instance-type t2.micro \
    --key-name justin-clarusway-keypair \
    --security-groups RomanNumSecurityGroup \
    --user-data file://home/ec2-user/user_data.sh

