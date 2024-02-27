import torch
import sys,os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))) #TODO:tidy this up

import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from sentiment_classifier.model_loader import model
import pandas as pd
from sentiment_classifier.preprocess import preprocess_function

class AudioDataset(Dataset):
    def __init__(self, input_values, labels=None):
        self.input_values = input_values
        self.labels = labels

    def __len__(self):
        return len(self.input_values)

    def __getitem__(self, idx):
        item = {
            "input_values": torch.tensor(self.input_values[idx], dtype=torch.float) 
                          }
        if self.labels is not None:
            item["labels"] = self.labels[idx]
        return item


# Assuming 'data_dict' contains your data
    
def get_probabilities(input_wav): ## takes in a wav and returns array that represent the probabilites for each quadrant.
    the_input = pd.DataFrame()
    the_input['path'] = [input_wav]
    the_input = preprocess_function(the_input)


    dataset = AudioDataset(the_input['input_values'])
    data_loader = DataLoader(dataset, batch_size=1, shuffle=True)  # Adjust batch_size as needed

    # Assuming 'model' is your loaded and configured model
    model.eval()  # Set the model to evaluation mode
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    probs = []

    with torch.no_grad():  # Disable gradient computation for inference
        for batch in data_loader:
            input_values = batch["input_values"].to(device)
            print(input_values[0].shape)
            # If your model uses attention masks, include them in the model call
            # attention_mask = batch["attention_mask"].to(device)
            output = model(input_values[0])  # Add attention_mask=attention_mask as argument if needed
            # Convert logits to probabilities
            probabilities = F.softmax(output.logits, dim=-1)

            # Move probabilities to CPU for further processing if needed
            probabilities_cpu = probabilities.cpu().numpy()

            # Process your probabilities here (e.g., print, analyze, etc.)
            probs.append(probabilities_cpu)
    return probabilities_cpu[0]

# Note: This example directly passes 'input_values' assuming the model expects them in the correct format.
# If your model expects differently formatted inputs, adjust the data preparation accordingly.

#print(get_probabilities('276e5c05-3a0c-4d9f-aed4-a125ab308a6f__output.wav'))