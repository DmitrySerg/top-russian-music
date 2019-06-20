
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
from ast import literal_eval


print("Reading data")

data = pd.read_csv("/Users/dmitrys/Yandex.Disk.localized/top_russian_music/comments/union_superreduced_comments.csv")
print(data.shape)


data = data[~data.text_bow.isnull()]

print("Cleaning data")
data = data[data['comment_len']>40]
texts = data.text_bow.apply(literal_eval)
print(data.shape)
print("Bigrams")
# Build the bigram  models
bigram = models.Phrases(texts, min_count=3, threshold=5) # higher threshold fewer phrases.

# Faster way to get a sentence clubbed as a bigram
bigram_mod = models.phrases.Phraser(bigram)

def make_bigrams(texts):
    return [bigram_mod[doc] for doc in texts]

texts = make_bigrams(texts)

print("Corpora")
dictionary = corpora.Dictionary(texts)                 # составляем словарь из терминов
print('Размер словаря до фильтрации: {}'.format(len(dictionary)))

dictionary.filter_extremes(no_below=3, no_above=0.4, keep_n=3*10**6)
print('Размер словаря после фильтрации: {}'.format(len(dictionary)))

corpus = [dictionary.doc2bow(text) for text in texts]  # составляем корпус документов

with open('lda_models/corpus', 'wb') as f:
    pickle.dump(corpus, f)

print("Fitting model")
np.random.seed(42)
ldamodel_30 = models.ldamodel.LdaModel(
    corpus, 
    id2word=dictionary, 
    eval_every=20, 
    num_topics=30, 
    passes=5
    )

print("Saving model")
ldamodel_30.save("lda_models/ldamodel_30_bigrams_long_comments")

topics = ldamodel_30.show_topics(num_topics=30, num_words=100,formatted=False)
print("Saving topics")
# Сохраняем словарик с id пользователей
with open('lda_models/lda_30_topics_bigrams_long_comments', 'wb') as f:
    pickle.dump(topics, f)