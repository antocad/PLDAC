from ParserArticle import ParserArticle

corpus = ParserArticle.parse("../corpus_short.fr")
for doc in corpus :
    print(doc.getId(),doc.getTitle())
