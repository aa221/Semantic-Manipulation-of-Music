## This is where the pipeline of the whole thing lives. 
## We take in the midi, upload it to the api, get an md file then convert it into a json 
from classifier import *
from convert_md import *
from MIDI_to_WAV import * 


"""
There are three folders that save outputs 

"""


def upload_pipeline(midi_filepath):
    credential_setup()

    ## select style (soundfont)
    ## TODO: create logic so that certain genres correlate to certain sounds. 

    ## first step is to  convert this into wav format:

    try: 
        wav_path = midi_to_wav(midi_filepath,'soundfonts/Mario_World_HDv1.1.sf2')
        uri,file_path = file_to_data_uri(wav_path)
        print(file_path)
        output = run_classifier(uri)
        output_file_path = download_md_file(output,file_path)
        

    except Exception as e:
        print('An error occured')
        return (e) 
        

    return process_md(output_file_path)
    


print(upload_pipeline('AccoMontage2/MIDI demos/inputs/089/chord_gen.mid'))