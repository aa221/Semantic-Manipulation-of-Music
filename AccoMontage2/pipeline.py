## This is where the pipeline of the whole thing lives. 
## We take in the midi, upload it to the api, get an md file then convert it into a json 
from classifier import *
from convert_md import *


def upload_pipeline(midi_filepath):
    credential_setup()
    uri,file_path = file_to_data_uri(midi_filepath)
    output = run_classifier(uri)
    output_file_path = download_md_file(output,file_path)
    return process_md(output_file_path)
    


upload_pipeline('276e5c05-3a0c-4d9f-aed4-a125ab308a6f__output.wav')