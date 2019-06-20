import pandas as pd              # Пакет для работы с таблицами
import numpy as np               # Пакет для работы с векторами и матрицами

# Из библиотеки для работы с текстами вытащим 
# методы для  предобработки и модели
from gensim import corpora, models
from gensim.models.callbacks import PerplexityMetric

# Пара дополнительных комбинаторных штук для картинок
from collections import defaultdict
import itertools   

# Пакет, чтобы делать глубокие копии
import copy

# Пакет для работы со специфичными для питона данными
import pickle

# Косинусная метрика для рассчёта расстояний 
from scipy.spatial.distance import cosine

import json
import pickle

path = '/Users/dmitrys/Yandex.Disk.localized/top_russian_music/comments/vk/'

print("Reading data")

with open(path + "vk_comments_full_1", 'rb') as f:
    comments = pickle.load(f)
    
with open(path + "vk_comments_full_2", 'rb') as f:
    comments.extend(pickle.load(f))


data = pd.DataFrame(comments)
print("Data shape:",data.shape)

data['text_bow'] = data['text'].str.split()

data['comment_len'] = data['text_bow'].apply(len)

data = data[data['comment_len']>4]
print("Reduced data shape:",data.shape)
data.to_csv("reduced_comments.csv")

