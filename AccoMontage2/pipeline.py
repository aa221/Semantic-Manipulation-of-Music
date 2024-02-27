## This is where the pipeline of the whole thing lives. 
## We take in the midi, upload it to the api, get an md file then convert it into a json 
from get_instrumentation import * 
from classifier import *
from convert_md import *
from MIDI_to_WAV import * 
from emotion_change import * 


"""
There are three folders that save outputs 

"""

def upload_pipeline(midi_filepath_input,semitones=30): # the input here is the single stem midi , ## semitone value is a hyper-parameter for whether you want happy or sad.
    ## higher value for semitones mean we are making the song happier, 
    ## negative values mean we are making the song sadder. 
    ## select style (soundfont)
    ## TODO: create logic so that certain genres correlate to certain sounds. 

    ## first step is to  convert this into wav format:

    try:    
        new_midi = transpose(midi_filepath_input,semitones)
        print(new_midi)
        generated_path = create_instrumentation(new_midi)
        wav_path = midi_to_wav(generated_path,'soundfonts/Mario_World_HDv1.1.sf2')
        uri,file_path = file_to_data_uri(wav_path)
        print(file_path) 
        print('drake')
        print('uri')
        output = run_classifier(uri)
        output_file_path = download_md_file(output,file_path, path_name=wav_path, folder_path='mood_attributes')
        

    except Exception as e:
        print('An error occured')
        print(e)
        return (e) 
        

    return process_md(output_file_path)
    
upload_pipeline('AccoMontage2/MIDI demos/inputs/114/melody.mid')
    