import json
import random
import tensorflow as tf

import constants

class DatasetSelection():
    def __init__(self):
        self.datasets:list[Dataset] = []

    def split(self, index:int, ratio:float):
        d1, d2 = self.datasets[index].split(ratio)
        self.datasets[index] = d1

        self.datasets.append(None)
        for i in reversed(range(index+1, len(self.datasets)-1)):
            self.datasets[i+1] = self.datasets[i]
        
        self.datasets[index+1] = d2

class Dataset:
    def __init__(self, data:list, shuffle=True, name:str=""):
        self.name = name
        if shuffle:
            random.shuffle(data)
        self.data = data

    @classmethod
    def from_json(cls, path:str, balancing=True, name:str=""):
        data = []
        with open(path, mode='r', encoding='utf8') as json_file:
            for line in json_file:
                item = json.loads(line)
                if balancing:
                    n_sample = min(len(item['human_answers']), len(item['chatgpt_answers']))
                    human_answers = random.sample(item['human_answers'], n_sample)
                    chatgpt_answers = random.sample(item['chatgpt_answers'], n_sample)
                else:
                    human_answers = item['human_answers']
                    chatgpt_answers = item['chatgpt_answers']
                    
                for answer in human_answers:
                    data.append({
                        'text': answer,
                        'label': constants.CLASS_HUMAN
                        })
                for answer in chatgpt_answers:
                    data.append({
                        'text': answer,
                        'label': constants.CLASS_CHATGPT
                        })
        
        if not name:
            name = path.split('/')[-1]

        return cls(data, name=name)
    
    def sample_index(self, n):
        return random.sample(range(len(self.data)), n)
    
    def get_from_indexes(self, indexes):
        return [ self.data[i] for i in indexes ]

    def apply(self, func):
        for i in range(len(self.data)):
            self.data[i]['text'] = func(self.data[i]['text'])

    def filter(self, func):
        pass

    def split(self, ratio, shuffle=True):
        data = self.data
        
        if shuffle:
            random.shuffle(data)

        n_data1 = int(ratio * len(data))
        data1 = data[-n_data1:]
        data2 = data[:-n_data1]

        return (Dataset(data1, name=self.name+" (1)"), Dataset(data2, name=self.name+" (2)"))

    def get_texts(self, label=None):
        if label is None:
            return  [x['text'] for x in self.data]
        
        return [x['text'] for x in self.data if x['label'] == label]
    
    def get_labels(self):
        return  [x['label'] for x in self.data]
    
    def make_xy(self, batch_size:int=32) -> tf.data.Dataset:
        x = self.get_texts()
        x = [[s] for s in x]
        y = self.get_labels()

        return tf.data.Dataset.from_tensor_slices((x, y)).batch(batch_size)
    
    def kfold(self, n:int):
        data_size = self.total()
        k, m = divmod(data_size, n)
        for i in range(n):
            k_start = i*k+min(i, m)
            k_end = (i+1)*k+min(i+1, m)
            k_data = self.data[k_start:k_end]
            k_rest = self.data[0:k_start] + self.data[k_end:data_size]
            yield Dataset(k_data), Dataset(k_rest)
    
    def total(self):
        return len(self.data)

    def save(self, path):
        json_object = {
            'human_answers': self.get_texts(constants.CLASS_HUMAN),
            'chatgpt_answers': self.get_texts(constants.CLASS_CHATGPT)
        }
        json_data = json.dumps(json_object)
        with open(path, mode='w', encoding='utf8') as json_file:
            json_file.write(json_data)