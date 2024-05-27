import os
import warnings
#import re
#import string
#import json

import boto3
#import pinecone
#import nltk
#from nltk.corpus import stopwords
#from nltk.stem import WordNetLemmatizer
#from sentence_transformers import SentenceTransformer

#Handle warnings
warnings.filterwarnings('ignore', category = UserWarning)
warnings.filterwarnings('always', category=DeprecationWarning)

#Initialize AWS credentials
os.environ['AWS_ACCESS_KEY_ID'] =''
os.environ['AWS_SECRET_ACCESS_KEY'] =''
os.environ['AWS_DEFAULT_REGION'] = ''

#step 1: Locate PDFs
def find_pdfs(directory):
    pdf_files = []
    for root, dirs, files in os.walk(directory):
       
     for file in files:
        if file.lower().endswith('.pdf'):
        
         pdf_files.append(os.path.join(root, file))
    return pdf_files

#Define directory
directory_path = '/home/space/CropAfia/CropAfia/coffee'
pdf_files = find_pdfs(directory_path)
print(f"Found PDF files : {pdf_files}")

#step 2: Upload PDF docs to S3 storage
#def upload_pdfs_to_s3(pdf_files, bucket_name):
  #s3_client = boto3.client('s3')
  #for pdf in pdf_files:
   # try:
      #file_name = os.path.basename(pdf)
     # s3_client.upload_file(pdf, bucket_name, file_name)
      #print(f"Uploaded {pdf} to {bucket_name}/{file_name}")
    #except Exception as e:
      #print(f"Error uploading {pdf}:{e}")

#define the s3 bucket name
#bucket_name = ''
#upload the PDF docs to amazon s3
#upload_pdfs_to_s3(pdf_files, bucket_name)

#print("Upload Completed Succesfully.")
