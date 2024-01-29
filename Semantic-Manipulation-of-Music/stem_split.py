

import subprocess

# The way you run demucs is by writing python3 -m demucs "File Name.wav"
# in the terminal.
# This function mimics that action, but runs it as a file. The splitted
# files will be accessible in a folder within the seperated folder by the same name of the filename
# We return the file name, so we can use it later on. 
def run_demucs(filename):
    try:
        # Build the command
        command = ['python3', '-m', 'demucs', filename]

        # Run the command
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Output the result
        print("Output:", result.stdout.decode())
        print("Error (if any):", result.stderr.decode())
    except subprocess.CalledProcessError as e:
        print("Standard Error Output:", e.stderr.decode())
        print("An error occurred while running demucs:", e)
        
    return filename

# Example usage
#run_demucs("music_source_folder/example.mp3")