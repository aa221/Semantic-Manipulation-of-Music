## This is where the pipeline of the whole thing lives. 
## We take in the midi, upload it to the api, get an md file then convert it into a json 
from get_instrumentation import * 
from MIDI_to_WAV import * 
from emotion_change import * 
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))) #TODO:tidy this up
from helper_functions import write_to_txt
from helper_functions import get_circle_path
from sentiment_classifier.predictions import get_probabilities
from circle_plot import plot_weighted_point_in_circle


"""
There are three folders that save outputs 

"""



def upload_pipeline(midi_filepath_input,semitones=15): # the input here is the single stem midi , ## semitone value is a hyper-parameter for whether you want happy or sad.
    ## higher value for semitones mean we are making the song happier, 
    ## negative values mean we are making the song sadder. 
    ## select style (soundfont)
    ## TODO: create logic so that certain genres correlate to certain sounds. 

    ## first step is to  convert this into wav format:

    try:
        wav_before_change = midi_to_wav(midi_filepath_input,'soundfonts/Mario_World_HDv1.1.sf2')
        print(wav_before_change)
        
         
     
        new_midi = transpose(midi_filepath_input,semitones)
        generated_path = create_instrumentation(new_midi)
        wav_path = midi_to_wav(generated_path,'soundfonts/Mario_World_HDv1.1.sf2')
        
        
        
        probabilities_before_change = get_probabilities(wav_before_change) ## probabilities after changing emotion.
        print(probabilities_before_change)
        write_to_txt(wav_before_change,probabilities_before_change,output=False)
        

        probabilities = get_probabilities(wav_path) ## probabilities after changing emotion. 
        # Open the specified text file for writing, this will create the file if it doesn't exist
        write_to_txt(wav_path,probabilities)
        plot_weighted_point_in_circle(probabilities_before_change[0],probabilities_before_change[1],probabilities_before_change[2],probabilities_before_change[3],get_circle_path(wav_before_change))
        plot_weighted_point_in_circle(probabilities[0],probabilities[1],probabilities[2],probabilities[3],get_circle_path(wav_path))
        

    except Exception as e:
        print('An error occured')
        print(e)
        return (e) 
        

    return probabilities
    
## example usage: 

#upload_pipeline('AccoMontage2/MIDI demos/inputs/076/melody.mid')

