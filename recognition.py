import spacy
import numpy as np
import networkx as nx  
import matplotlib.pyplot as plt  

nlp = spacy.load("en_core_web_sm")

f = open("turnip.txt", "r")
for x in f:
  sentences = x
  
doc = nlp(sentences)

nouns = [token.text.lower() for token in doc if token.dep_ == 'nsubj']
actions = [token.head.text for token in doc if token.dep_ == 'nsubj']

for i in range(len(nouns)):
    print(str(nouns[i])+ ' ' + str(actions[i]))
    
dict_actors = {}

for i in range(len(nouns)):
    if nouns[i] in dict_actors.keys():
        dict_actors[nouns[i]].append(actions[i])
    else:
        dict_actors[nouns[i]] = [actions[i]]   

for actor in dict_actors.keys():
    plt.figure()
    G = nx.MultiDiGraph()
    actions_actor = dict_actors[actor]
    for i in range(len(actions_actor)-1):
        G.add_edge(actions_actor[i], actions_actor[i+1])
    pos = nx.spring_layout(G) 
    nx.draw_networkx(G, pos, arrows=True)  
    plt.title(actor)
    plt.show()


