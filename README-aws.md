AWS
---

## S3 Related

### 


* Bucket Policy - Allow full access
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowListBucket",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::235471311047:user/aws_dev"
            },
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::ymoon-au-dbt-fx-raw"
        },
        {
            "Sid": "AllowGetObject",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::235471311047:user/aws_dev"
            },
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::ymoon-au-dbt-fx-raw/*"
        }
    ]
}
```
