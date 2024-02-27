from safetensors.torch import save_file

from safetensors import safe_open
import sys,os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))) #TODO:tidy this up

from transformers import AutoConfig
from safetensors import safe_open
from  sentiment_classifier.classifier_model import Wav2Vec2ForSpeechClassification


tensors = {}
with safe_open("model_final.safetensors", framework="pt", device='cpu') as f:
    for k in f.keys():
        tensors[k] = f.get_tensor(k).to('cpu') # loads the full tensor given a key


model_name_or_path = "lighteternal/wav2vec2-large-xlsr-53-greek"
pooling_mode = "mean"
label_list = ['Q1', 'Q2', 'Q3', 'Q4']
config = AutoConfig.from_pretrained(
    model_name_or_path,
    num_labels=4,
    label2id={label: i for i, label in enumerate(label_list)},
    id2label={i: label for i, label in enumerate(label_list)},
    finetuning_task="wav2vec2_clf",
    hidden_layer = 650
)
setattr(config, 'pooling_mode', pooling_mode)

# Initialize the model
model = Wav2Vec2ForSpeechClassification(config)

# Load the tensors
with safe_open("model_final.safetensors", framework="pt", device="cpu") as f:
    tensors = {k: f.get_tensor(k) for k in f.keys()}

# Use the loaded tensors to update the model's state dictionary
final_model = model.load_state_dict(tensors)

# Set the model to evaluation mode if you're doing inference
final_model = model.eval()

