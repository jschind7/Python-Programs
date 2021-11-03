import numpy as np
import pandas as pd
import nltk
import re
import networkx as nx
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity

# Remove stopwords
sw = stopwords.words('english')
def remove_stopwords(sent):
    trim_sent = " ".join([i for i in sent if i not in sw])
    return trim_sent

# Fill word_embeddings dictionary with word as key and coefficients as value
word_embeddings = {}
embeds = open('Glove Embeddings/glove.6B.100d.txt', encoding='utf-8')
for line in embeds:
    values = line.split()
    word = values[0]
    coeffs = np.asarray(values[1:], dtype='float32')
    word_embeddings[word] = coeffs
embeds.close()

# Read in excel sheet with text
df = pd.read_excel('text_to_summarize.xlsx')

for val, comment in enumerate(df["Article Text"]):
    sentences = sent_tokenize(comment)
    # Clean sentences by removing symbols, caps, and stopwords
    clean_sent = pd.Series(sentences).st.replace("[^a-zA-Z]", " ")
    clean_sent = [s.lower() for s in clean_sent]
    clean_sent = [remove_stopwords(r.split()) for r in clean_sent]

    # Create sentence vectors by adding up embeddings for each non-stopword in the sentence
    sentence_vectors = []
    for i in clean_sent:
        if len(i) != 0:
            vec = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()]) / (len(i.split())+0.001)
        else: # only stopwords
            vec = np.zeros((100,))
        sentence_vectors.append(vec)

    # Create similarity matrix by comparing sentence vectors using cosine similarity
    sim_mat = np.zeros([len(sentences), len(sentences)])
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0,0]
    nx_graph = nx.from_numpy_array(sim_mat)
    scores = nx.pagerank(nx_graph)
    # Sort sentences by score
    ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)
    summary_length = min(10,max(3, round(.15*len(ranked_sentences))))
    # Number of sentences returned -> ranked_sentneces[n-1][0]
    nth_sent_score = reanked_sentences[summary_length-1][0]
    # go through sentences in order and display those with n highest scores
    for ind,sent in enumerate(sentences):
        if scores[ind] >= nth_sent_score:
            print(sent)
    
    
