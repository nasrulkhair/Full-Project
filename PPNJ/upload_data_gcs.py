import os
from google_cloud import storage

# function to upload files to GCS

def upload_to_gcs(bucket_name, cource_file, destinantion_blon):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob)
    
    blob.upload_from_filename(source_file)
    print(f"Uploaded {source_file} to gs://{bucket_name}/{destination_blob}")
    

# Files to upload

