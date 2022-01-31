from google.cloud import storage

storage_client = storage.Client.from_service_account_json(r'C:\Users\avinpandey\Desktop\xyz.json')

bucket = storage_client.get_bucket('sunrise-kfs')
bucket_list = []
for y in bucket.list_blobs(prefix=r'BODS/Configuration'):
    keys = y.name
    if keys.endswith('.txt'):
        bucket_list.append(y)
print(bucket_list)
for x in bucket_list:
    print(x.download_as_string())
    break

