from ParserCorpus import ParserCorpus

corpus = ParserCorpus.parse("../corpus_short.fr")
for doc in corpus :
    print(doc.getId(),doc.getTitle())
