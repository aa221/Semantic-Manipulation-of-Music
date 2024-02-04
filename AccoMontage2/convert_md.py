
import os
import json 
# Takes in the file path  then converts it to our dictionary
## If the process suceeds we delete the md file from the file path 


def process_md(file_path):
    
    try: 
        with open(file_path, 'r') as file:
            lst = []
            mood_dict = {'mood': {}}

            for line in file:
                if 'genre_tzanetakis' in line:
                    line = line.replace('**','').replace('\n','')
                    parts = line.split('|')
                    genres = parts[1].split('<br>')
                    scores = parts[2].split('<br>')
                    # Create the dictionary
                    genre_dict = {"genre": {genres[i]: scores[i] for i in range(len(genres))}}

                    # Print the dictionary
                    print(genre_dict)

                if 'mood' in line:
                    print("cock")
                    parts = line.split('|')
                    moods = parts[1].split('<br>')
                    scores = parts[2].split('<br>')
                    scores = [score.strip('*') for score in scores]
                    for mood, score in zip(moods, scores):
                        mood_dict['mood'][mood.strip()] = score.strip()

            # delete the file path if our process works. 
            if os.path.exists(file_path):
                # Delete the file
                os.remove(file_path)
                print(f"File '{file_path}' has been deleted.")
            else:
                print(f"The file '{file_path}' does not exist.")


            lst.append(mood_dict)
            lst.append(genre_dict)
            json_data = json.dumps(lst, indent=4)

            json_path = file_path.replace('.md','.json').replace('.wav','')

            # Write to file
            with open(json_path, 'w') as file:
                file.write(json_data)


        return json_data

            
            
    except Exception as e:
        return e 
    


