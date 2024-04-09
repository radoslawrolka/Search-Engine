import os
import re
from nltk.corpus import stopwords
from nltk.stem import porter


def text_preprocessing():
    counter = 0
    all_file_dict = {}
    word_in_diff_file = {}
    stemmer = porter.PorterStemmer()
    for file in os.listdir('./wiki'):
        local_dict = {}
        with open(f'./wiki/{file}', 'r') as f:
            text = f.read()
            text = text.lower()
            text = re.sub(r'[^a-z]', ' ', text)
            text = re.sub(r'\s+', ' ', text)
            text = text.strip()
            words = text.split(' ')
            words = [word for word in words if word not in stopwords.words('english')]
            words = [stemmer.stem(word) for word in words]
            words = [word for word in words if len(word) >= 3]
            for word in words:
                if word not in word_in_diff_file:
                    word_in_diff_file[word] = 1
                    all_file_dict[word] = 1
                else:
                    word_in_diff_file[word] += 1
                    all_file_dict[word] += 1
                if word not in local_dict:
                    local_dict[word] = 1
                else:
                    local_dict[word] += 1

        with open(f'./dicts/{file}', 'w') as f:
            f.write(f'{len(words)}\n')
            for key, value in local_dict.items():
                f.write(f'{key} {value}\n')

        counter += 1
        print(f'Processed {counter}')

    with open('./main_dict.txt', 'w') as f:
        for key, value in all_file_dict.items():
            f.write(f'{key} {value}\n')
    
    with open('./word_in_diff_file.txt', 'w') as f:
        for key, value in word_in_diff_file.items():
            f.write(f'{key} {value}\n')

