import os
from google.cloud import storage

# path to GCP credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\User\Desktop\GCP\ppnj-463412-13c39ea0960c.json"

# function to upload files to GCS
def upload_to_gcs(bucket_name, source_file, destination_blob):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob)
    
    blob.upload_from_filename(source_file)
    print(f"Uploaded {source_file} to gs://{bucket_name}/{destination_blob}")
    

# Files to upload
files_to_upload = [
    {
        "source_file": r"C:\Users\User\Desktop\Data Analyst\End To End Project\PPNJ\customer.csv",
        "destination_blob": "files/customer.csv"
    },
    {
        "source_file": r"C:\Users\User\Desktop\Data Analyst\End To End Project\PPNJ\feedback.csv",
        "destination_blob": "files/feedback.csv"
    },
    {
        "source_file": r"C:\Users\User\Desktop\Data Analyst\End To End Project\PPNJ\refund.csv",
        "destination_blob": "files/refund.csv"
    },
    {
        "source_file": r"C:\Users\User\Desktop\Data Analyst\End To End Project\PPNJ\sales.csv",
        "destination_blob": "files/sales.csv"
    },
    {
        "source_file": r"C:\Users\User\Desktop\Data Analyst\End To End Project\PPNJ\travel_guide.csv",
        "destination_blob": "files/travel_guide.csv"
    },
    {
        "source_file": r"C:\Users\User\Desktop\Data Analyst\End To End Project\PPNJ\travel_package.csv",
        "destination_blob": "files/travel_package.csv"
    }
]

# Upload all files to GCS
for file in files_to_upload:
    upload_to_gcs("ppnj_data", file['source_file'], file['destination_blob'])

