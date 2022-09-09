import requests
from io import StringIO
import pandas as pd

def die(error_message):
    raise Exception(error_message)

res = requests.get('https://raw.githubusercontent.com/brmson/dataset-sts/master/data/sts/sick2014/SICK_train.txt')
# create dataframe
data = pd.read_csv(StringIO(res.text), sep='\t')
data.head()
# print(data)

# we take all samples from both sentence A and B
sentences = data['sentence_A'].tolist()
sentences[:5]
# print(sentences)

# we take all samples from both sentence A and B
sentences = data['sentence_A'].tolist()
sentence_b = data['sentence_B'].tolist()
sentences.extend(sentence_b)  # merge them
# print(len(set(sentences)))  # together we have ~4.5K unique sentences

#This isn't a particularly large number, so let's pull in a few more similar datasets.0
urls = [
    'https://raw.githubusercontent.com/brmson/dataset-sts/master/data/sts/semeval-sts/2012/MSRpar.train.tsv',
    'https://raw.githubusercontent.com/brmson/dataset-sts/master/data/sts/semeval-sts/2012/MSRpar.test.tsv',
    'https://raw.githubusercontent.com/brmson/dataset-sts/master/data/sts/semeval-sts/2012/OnWN.test.tsv',
    'https://raw.githubusercontent.com/brmson/dataset-sts/master/data/sts/semeval-sts/2013/OnWN.test.tsv',
    'https://raw.githubusercontent.com/brmson/dataset-sts/master/data/sts/semeval-sts/2014/OnWN.test.tsv',
    'https://raw.githubusercontent.com/brmson/dataset-sts/master/data/sts/semeval-sts/2014/images.test.tsv',
    'https://raw.githubusercontent.com/brmson/dataset-sts/master/data/sts/semeval-sts/2015/images.test.tsv'
]

# each of these dataset have the same structure, so we loop through each creating our sentences data
for url in urls:
    res = requests.get(url)
    # extract to dataframe
    data = pd.read_csv(StringIO(res.text), sep='\t', header=None, on_bad_lines='skip')
    # add to columns 1 and 2 to sentences list
    sentences.extend(data[1].tolist())
    sentences.extend(data[2].tolist())

# print(len(set(sentences))) # together we have ~14.5K unique sentences

# remove duplicates and NaN
sentences = [word for word in list(set(sentences)) if type(word) is str]
# print(sentences)

from sentence_transformers import SentenceTransformer
# initialize sentence transformer model
model = SentenceTransformer('bert-base-nli-mean-tokens')
# create sentence embeddings
sentence_embeddings = model.encode(sentences)
print(sentence_embeddings.shape)
# die("")