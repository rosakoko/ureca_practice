import nltk
from nltk.parse.stanford import StanfordParser
from nltk.parse.stanford import StanfordDependencyParser
import string
import networkx as nx
from nltk.stem.wordnet import WordNetLemmatizer
import matplotlib.pyplot as plt
# from nltk.stem.snowball import SnowballStemmer

path_to_jar = 'C:\Users\t_quacd\AppData\Local\stanford-parser-full-2015-12-09/stanford-parser.jar'
path_to_models_jar = 'C:\Users\t_quacd\AppData\Local\stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models.jar'
parser = StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
dep_parser = StanfordDependencyParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
sentence = "The decor is vibrant and eye-pleasing with several semi-private boths on the right side of the dining hall, which are great for a date"
result = dep_parser.raw_parse(sentence)
dep = result.next()
DG = nx.DiGraph()
# a = list(dep.triples())
# for triple in dep.triples():
#     print triple[1],"(",triple[0][0],", ",triple[2][0],")"
for each in dep.to_dot().split("\n")[4:-1]:
    each = str(each)
    each = each.translate(string.maketrans("", ""), string.punctuation.replace(">", "").replace("=", ""))
    if ">" in each:
        relationship = each.split("=")[-1]
        each = each.split()
        DG.add_edge(each[0], each[2], label = relationship)
    else:
        each = each.split()
        DG.add_node(each[0], label=each[-1])
edge_labels = dict([((u, v,), d['label']) for u, v, d in DG.edges(data=True)])
node_labels = dict([(node, d['label']) for node, d in DG.nodes(data=True)])
pos=nx.spring_layout(DG)
nx.draw_networkx_edge_labels(DG,pos,edge_labels=edge_labels)
nx.draw_networkx(DG, pos, labels=node_labels)
plt.show()
# aspect_Term = "dining hall"
# test = test.split()
# position = 0
# from_index =0
# to_index = 0
# to_char = 106
# from_char = 95
# for each in test:
#     print each, len(each)
#     if position + len(each) + 1 <= from_char:
#         position += len(each) + 1
#     else:
#         from_index = test.index(each)
#         break
# position = 0
# if len(aspect_Term.split()) == 1:
#     to_index = from_index
# else:
#     for each in test:
#         if position + len(each) + 1 < to_char:
#             position += len(each) + 1
#         else:
#             to_index =test.index(each)
#             break
# print from_index, to_index

# parsed_Sentence = parser.raw_parse(sentence)
# for line in parsed_Sentence:
#        print line
#        line.draw()
#
# parsed_Sentence = [parse.tree() for parse in dep_parser.raw_parse(sentence)]
# print parsed_Sentence
#
# # GUI
# for line in parsed_Sentence:
#         print line
#         line.draw()
# list_word = nltk.word_tokenize(sentence)
# postagger = nltk.pos_tag(list_word)
# grammar = r"""
#         NP:     {<PDT>?<DT|IN|WDT|WP\$|PRP\$>?<CD|JJ.*>*<PRP|WP|NN.*>+}
#         PP:     {<IN|TO|RP><NP>}
#         VP:     {<RB.?>*<MD>*<TO>*<VB.?>+<RB.*|WRB>*<RP>*<NP|PP|JJ*>*}
#         CL:     {<NP><VP>}
#          """
# grammar = r"""
#     NP:
#         {<NN><NN><NN>}
#         {<NNP><NNP><NNP>}
#         {<NNP><NNP><NN>}
#         {<NNS><NN><NN>}
#         {<FW><NN><NN>}
#         {<NN><NN>}
#         {<NNP><NNP>}
#         {<NNP><NN>}
#         {<FW><NN>}
#         {<NNS><NNS>}
#         {<NN><NNS>}
#         {<DT><JJ><NNS>}
#         {<IN><JJ><NNS>}
#         {<NN>}
#         {<NNP>}
#         {<NNS>}
#         {<DT>?<JJ>*<NN>}
#      """
# print postagger
# parser = nltk.RegexpParser(grammar)
# result = parser.parse(postagger)
# print result
# result.draw()
