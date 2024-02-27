import torchaudio
from transformers import Wav2Vec2Processor



processor = Wav2Vec2Processor.from_pretrained("lighteternal/wav2vec2-large-xlsr-53-greek")

input_column = "path"

def speech_file_to_array_fn(path):
    speech_array, sampling_rate = torchaudio.load(path)
    resampler = torchaudio.transforms.Resample(sampling_rate, 16000)
    speech = resampler(speech_array).squeeze().numpy()
    return speech

def label_to_id(label, label_list):

    if len(label_list) > 0:
        return label_list.index(label) if label in label_list else -1

    return label

def preprocess_function(examples):
    speech_list = [speech_file_to_array_fn(path) for path in examples[input_column]]
    result = processor(speech_list, sampling_rate=16000)

    return result