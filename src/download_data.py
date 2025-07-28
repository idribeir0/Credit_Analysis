import zipfile
import os

zip_path = 'default-of-credit-card-clients-dataset.zip'
extract_to = 'data/'

os.makedirs(extract_to, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

os.remove(zip_path)

print('✅ file in data/')