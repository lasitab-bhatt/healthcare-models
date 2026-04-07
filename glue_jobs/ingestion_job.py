import sys
import requests
import pandas as pd
from datetime import datetime
import boto3
from io import StringIO

# ==============================
# CONFIG
# ==============================
S3_BUCKET = "healthcare-data-lake"
S3_PREFIX = "raw/"
DATA_URL = "https://data.cms.gov/provider-data/hospital-data.csv"

s3_client = boto3.client("s3")


# ==============================
# DOWNLOAD DATA
# ==============================
def fetch_data():
    response = requests.get(DATA_URL)
    response.raise_for_status()
    return response.text


# ==============================
# PROCESS DATA
# ==============================
def process_data(csv_data):
    df = pd.read_csv(StringIO(csv_data))

    # Basic cleaning
    df.dropna(how="all", inplace=True)

    print(f"Rows after cleaning: {len(df)}")

    return df


# ==============================
# GENERATE S3 PATH
# ==============================
def generate_s3_key():
    now = datetime.utcnow()
    return (
        f"{S3_PREFIX}"
        f"year={now.year}/"
        f"month={now.month:02d}/"
        f"day={now.day:02d}/hospital_data.csv"
    )


# ==============================
# UPLOAD TO S3
# ==============================
def upload_to_s3(df):
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    s3_key = generate_s3_key()

    s3_client.put_object(
        Bucket=S3_BUCKET,
        Key=s3_key,
        Body=csv_buffer.getvalue()
    )

    print(f"Uploaded to s3://{S3_BUCKET}/{s3_key}")


# ==============================
# MAIN
# ==============================
def main():
    print("Starting Glue ingestion job...")

    raw_data = fetch_data()
    df = process_data(raw_data)
    upload_to_s3(df)

    print("Ingestion completed successfully.")


if __name__ == "__main__":
    main()
