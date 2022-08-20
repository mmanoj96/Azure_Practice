import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Quick start code goes here

except Exception as ex:
    print('Exception:')
    print(ex)

connect_str = 'DefaultEndpointsProtocol=https;AccountName=manojdatascience;AccountKey=OPfP0NjfGs/D8aPJyFr2tMxczOMMbZCbBFchYTcKu3/JkrhnPruHbfA15rRFH+wSMlq5JugjTWpv+AStwDSVqw==;EndpointSuffix=core.windows.net'
print("\nListing blobs...")
#connect to container
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

#to fetch container 
container_client = blob_service_client.get_container_client('practice')

print("\nListing blobs...")

# List the blobs in the container
blob_list = container_client.list_blobs()
for blob in blob_list:
    print("\t" + blob.name)
    #blob_client = container_client.get_blob_client(blob.name) 
    #print(blob_client)
    #print("\nDownloading blob to \n\t" + download_file_path)

    with open("input_download.csv", "wb") as my_blob:
        download_stream = container_client.download_blob('dataset/intput.csv')
        my_blob.write(download_stream.readall())
        print(my_blob)

import pickle
import pandas as pd
model =  pickle.load(open('Churnfinalized_model(2).sav', 'rb'))

X = pd.read_csv('input_download.csv').iloc[:, 1:]

result = model.predict(X)
X['Churn'] = result

print(result)