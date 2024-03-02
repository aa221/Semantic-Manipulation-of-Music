import mido
import os
from music21 import converter, interval, pitch, key

# def transpose(file_path, semitones):
#     try:
#         midi_file = mido.MidiFile(file_path)
#         if len(midi_file.tracks) == 0:
#             raise ValueError("MIDI file has no tracks.")

#         for track in midi_file.tracks:
#             for msg in track:
#                 if msg.type == 'note_on' or msg.type == 'note_off':
#                     # Ensure the note is within the 0-127 MIDI range after transposition
#                     msg.note = max(0, min(127, msg.note + semitones))

#         output_dir = 'changed_midis'
#         if not os.path.exists(output_dir):
#             os.makedirs(output_dir)

#         # Extracting the directory number to create the output file name
#         dir_number = file_path.split('/')[-2]  # Assumes the file_path format as given
#         output_file_name = f"{dir_number}_melody.mid"
#         new_file_path = os.path.join(output_dir, output_file_name)
#         midi_file.save(new_file_path)
#         print("Transposed MIDI saved at:", new_file_path)
#         return new_file_path

#     except Exception as e:
#         print("Error while transposing MIDI:", e)
#         return None
    


def transpose(file_path, target_key_name, output_dir='changed_midis'):
    try:
        # Load the MIDI file
        score = converter.parse(file_path)
        
        # Analyze the key of the original score
        original_key = score.analyze('key')
        print("Original key:", original_key.name)
        
        # Determine the interval needed to transpose the score to the target key
        transposition_interval = interval.Interval(original_key.tonic, pitch.Pitch(target_key_name))
        
        # Transpose the score
        transposed_score = score.transpose(transposition_interval)
        
        # Prepare the output directory
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # Create the output file name based on the input file path
        dir_number = file_path.split('/')[-2]
        output_file_name = f"{dir_number}_transposed.mid"
        new_file_path = os.path.join(output_dir, output_file_name)
        
        # Save the transposed score as a MIDI file
        transposed_score.write('midi', fp=new_file_path)
        print("Transposed MIDI saved at:", new_file_path)
        
        # Optionally, analyze the key of the transposed score and print it (can be removed if not needed)
        transposed_score = converter.parse(new_file_path)
        transposed_key = transposed_score.analyze('key')
        print("Transposed key:", transposed_key.name)
        
        return new_file_path

    except Exception as e:
        print("Error while transposing MIDI:", e)
        return None


# Example usage with transposition of 2 semitones up
#transpose('AccoMontage2/MIDI demos/inputs/076/melody.mid', 6)
