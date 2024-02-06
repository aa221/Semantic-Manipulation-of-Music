import os
import json
import replicate
import pathlib
import base64
import requests



auth_file_path = 'AccoMontage2/replicate_credentials.json'
# Read the file and get the token


## set the token as the key to use downstream. 

def credential_setup():
    try:
        with open(auth_file_path, 'r') as file:
            auth_data = json.load(file)
            replicate_api_token = auth_data['REPLICATE_API_TOKEN']

        # Set the environment variable
        if replicate_api_token:
            os.environ['REPLICATE_API_TOKEN'] = replicate_api_token
        else:
            print("REPLICATE_API_TOKEN in auth.json is empty or not set.")
    except FileNotFoundError:
        print(f"File not found: {auth_file_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {auth_file_path}")
    except KeyError:
        print(f"REPLICATE_API_TOKEN key not found in {auth_file_path}")



## takes in a local file path and converts it into a URI to be used by our API
def file_to_data_uri(file_path):
    # Determine the MIME type (example for a PNG image)
    mime_type = 'image/png'

    # Read the file as binary data
    with open(file_path, 'rb') as file:
        binary_data = file.read()

    # Encode the binary data in base64
    base64_encoded_data = base64.b64encode(binary_data)

    # Convert the base64-encoded data to a string
    base64_string = base64_encoded_data.decode('utf-8')

    # Create the data URI
    data_uri = f'data:{mime_type};base64,{base64_string}'
    file_path =  os.path.basename(file_path)
    return [data_uri,file_path]


## this outputs a .md file

def run_classifier(uri):
    output = replicate.run(
        "mtg/music-classifiers:f50a82351535312839a094087ad5f47c947c3afd38b91fb30716ed197933bfb9",
        input={
            "audio":uri
        }
    )
    return output


## downloads the md and put it in the folder
def download_md_file(md_link, file_name, folder_path='mood_attributes'):
    # Send a GET request to the provided Markdown link
    response = requests.get(md_link)

    if response.status_code == 200:
        md_content = response.text

        # Ensure the specified folder exists
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Define the full MD file path
        md_file_path = os.path.join(folder_path, file_name+'.md')

        # Save the MD content to the file
        with open(md_file_path, 'w') as md_file:
            md_file.write(md_content)

        print(f"MD file saved to {md_file_path}")
        return md_file_path
    else:
        print("Failed to download the Markdown file")
        raise Exception("Error fetching the Markdown data")







uri,file_name = file_to_data_uri('276e5c05-3a0c-4d9f-aed4-a125ab308a6f__output.wav')
print(file_name)
# link = run_classifier(uri)
# print(link)
# download_md_file(link,file_name)

