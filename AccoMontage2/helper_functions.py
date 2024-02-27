import os,sys
import re

def write_to_txt(wav_path,probabilities,output=True):
    wav_path=wav_path.split('/')[1].replace('.wav','').strip('_melody').strip('_chord_gen')
    
    folder_name = 'mood_attributes/'+wav_path+'/'+wav_path
    

    print(folder_name)
    if output:
        folder_name= folder_name+'_after_changes'
    
    os.makedirs(os.path.dirname(folder_name), exist_ok=True)
    with open(folder_name, 'w') as file:
            # Write the wav_path to the file
            file.write(f'WAV Path: {wav_path}\n')
            
            # Write the probabilities to the file
            # If probabilities is a list or dict, convert it to a string in a way that makes sense for your application
            probabilities_str = str(probabilities)
            file.write(f'Probabilities: {probabilities_str}\n')

    print({'paths':[folder_name]})
    return 



def get_circle_path(original_path):
    print(original_path)
    # Updated regular expression to match the new file path structure
    match = re.search(r'output_wavs/_([0-9]+)_(.+)\.wav', original_path)
    if match:
        number = match.group(1)
        file_type = match.group(2)  # melody or chord_gen
        # Construct the new path. Assuming you want to keep the filename structure but change the directory
        new_path = f'circle_images/{number}/{number}_{file_type}'
        return new_path
    else:
        return "Invalid path"


print(get_circle_path('output_wavs/_105_melody.wav'))