from flask import Flask, request, render_template, session, redirect
import pickle
import pandas as pd
import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
#print(X)
#print(len(result))
app = Flask(__name__)
def download_csv():
    connect_str = 'DefaultEndpointsProtocol=https;AccountName=manojdatascience;AccountKey=OPfP0NjfGs/D8aPJyFr2tMxczOMMbZCbBFchYTcKu3/JkrhnPruHbfA15rRFH+wSMlq5JugjTWpv+AStwDSVqw==;EndpointSuffix=core.windows.net'
    blob_name = os.getenv('blob_name')
    print("blob Name: " + blob_name)
    
    #connect to container
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)


    #to fetch container 
    container_client = blob_service_client.get_container_client('practice')
    with open("input_download.csv", "wb") as my_blob:
        download_stream = container_client.download_blob(blob_name)
        my_blob.write(download_stream.readall())
        #print(my_blob)
    

@app.route('/run', methods=["POST", "GET"])
def churn():
    download_csv()
    model =  pickle.load(open('Churnfinalized_model(2).sav', 'rb'))
    X = pd.read_csv('input_download.csv').iloc[:, 1:]
    result = model.predict(X)
    X['Churn'] = result
    return  X.to_html(header="true", table_id="table")

@app.route('/', methods=["GET"])
def default():
    return  "working"

if (__name__ == '__main__'):
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)