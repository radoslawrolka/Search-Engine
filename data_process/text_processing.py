import os
import re
import json
from nltk.corpus import stopwords
from nltk.stem import porter


def text_preprocessing(config):
    counter = 0
    all_file_dict = {}
    word_in_diff_file = {}
    stemmer = porter.PorterStemmer()
    for file in os.listdir('./data/articles'):
        local_dict = {}
        with open(f'./data/articles/{file}', 'r') as f:
            text = f.read()
            text = text.lower()
            text = re.sub(r'[^a-z]', ' ', text)
            text = re.sub(r'\s+', ' ', text)
            text = text.strip()
            words = text.split(' ')
            words = [word for word in words if word not in stopwords.words('english')]
            words = [stemmer.stem(word) for word in words]
            words = [word for word in words if len(word) >= 3]
            
            local_dict = {word: words.count(word) for word in set(words)}
            for word, v in local_dict.items():
                if word not in word_in_diff_file:
                    word_in_diff_file[word] = 1
                    all_file_dict[word] = v
                else:
                    all_file_dict[word] += v
                    word_in_diff_file[word] += 1

        with open(f'./data/dicts/{file}.json', 'w') as f:
            f.write(json.dumps(local_dict))

        counter += 1
        print(f'Processed {counter}')

    sorted_dict = sorted(all_file_dict.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = sorted_dict[:config['BAG_OF_WORDS']]
    sorted_dict = dict(sorted_dict)
    with open('./data/main_dict.json', 'w') as f:
        f.write(json.dumps(sorted_dict))
    
    word_in_diff_file = {k: word_in_diff_file[k] for k in sorted_dict.keys()}
    
    with open('./data/words_in_diff_file.json', 'w') as f:
        f.write(json.dumps(word_in_diff_file))

