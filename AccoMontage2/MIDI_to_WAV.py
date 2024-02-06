import subprocess
import os 

def midi_to_wav(midi_file, sound_font):
    """
    Converts a MIDI file to WAV using FluidSynth.

    Parameters:
    - midi_file: Path to the MIDI file.
    - sound_font: Path to the SoundFont file (.sf2).
    - wav_file: Path to the output WAV file.
    """
    base_name = os.path.basename(midi_file)
    name_without_extension = os.path.splitext(base_name)[0]
    wav_file = 'output_wavs'+'/'+name_without_extension+'.wav'
    print(wav_file)
    try:
        # Construct the FluidSynth command
        command = [
            'fluidsynth',
            '-ni', sound_font, midi_file,
            '-F', wav_file, '-r', '44100'
        ]
        
        # Execute the command
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        
        # Check for errors
        if result.returncode == 0:
            print("Conversion successful.")
            return wav_file
        else:
            print(f"Error during conversion: {result.stderr.decode('utf-8')}")
    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.stderr.decode('utf-8')}")

print(midi_to_wav("AccoMontage2/076_melody.mid_output_results/chord_gen.mid", "soundfonts/Mario_World_HDv1.1.sf2"))