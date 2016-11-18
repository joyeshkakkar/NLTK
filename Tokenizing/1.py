# Tokenizing
from nltk.tokenize import sent_tokenize
para = "Hello World. It's good to see you. Thanks for using nltk!"
print sent_tokenize(para)


# Tokenizing after loading tokenizer
import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
para = "Hello World. It's good to see you. Thanks for using nltk!"
print tokenizer.tokenize(para)


# Word Tokenize
from nltk.tokenize import word_tokenize
print word_tokenize('Hello World.') ## Wrapper method


# Underlying tokenizer code
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
print tokenizer.tokenize('Hello World.')


# Tokenizing contractions
print word_tokenize("can't is a contraction")

from nltk.tokenize import WordPunctTokenizer
tokenizer = WordPunctTokenizer()
print tokenizer.tokenize("Can't is a contraction.")

## Regexp tokenizer
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[\w']+")
print tokenizer.tokenize("Can't is a contraction. So, is don't.")


from nltk.tokenize import regexp_tokenize
print regexp_tokenize("Can't is a contraction. So, is don't.", "[\w']+")


tokenizer = RegexpTokenizer('\s+', gaps=True)
print tokenizer.tokenize("Can't is a contraction. So, is don't.")


# Stopwords
from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
words = word_tokenize('All he needs to do is what he presumably does best: build something.')
print [word for word in words if word not in english_stops]
print [fileid.encode('ascii') for fileid in stopwords.fileids()]


# Wordnet
from nltk.corpus import wordnet
syn = wordnet.synsets('cookbook')[0]
print syn.name()
print syn.definition()
print syn.examples()
print syn.hypernyms()
print syn.hypernyms()[0].hyponyms()
print syn.root_hypernyms()
print syn.hypernym_paths()
print syn.pos()
print len(wordnet.synsets('great'))
print len(wordnet.synsets('great', pos='n'))
print len(wordnet.synsets('great', pos='a'))

## Lemmas
lemmas = syn.lemmas()
print len(lemmas)
print lemmas[0].name()
print lemmas[1].name()
print lemmas[0].synset == lemmas[1].synset
print [lemma.name().encode('ascii') for lemma in syn.lemmas()]
synonyms = []
for syn in wordnet.synsets('book'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print len(synonyms)
print len(set(synonyms))


## Antonyms
gn2 = wordnet.synset('good.n.02')
print gn2.definition()
evil = gn2.lemmas()[0].antonyms()[0]
print evil.name()
ga1 = wordnet.synset('good.a.01')
print ga1.definition()
bad = ga1.lemmas()[0].antonyms()[0]
print bad.name()

# word similarity
cb = wordnet.synset('cookbook.n.01')
ib = wordnet.synset('instruction_book.n.01')
print cb.wup_similarity(ib)

dog = wordnet.synset('dog.n.01') # wordnet.synsets('dog')[0]
# dog = wordnet.synsets('dog')[0]
print dog.wup_similarity(cb)

## shortest path distance
ref = cb.hypernyms()[0]
print cb.shortest_path_distance(ref)
print ib.shortest_path_distance(ref)
print cb.shortest_path_distance(ib)

print dog.common_hypernyms(cb)

## verb similarity
cook = wordnet.synset('cook.v.01')
bake = wordnet.synset('bake.v.02')
print cook.wup_similarity(bake)

# Word collocations
from nltk.corpus import webtext
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
words = [w.lower() for w in webtext.words('pirates.txt')]
bcf = BigramCollocationFinder.from_words(words)
result = bcf.nbest(BigramAssocMeasures.likelihood_ratio, 4)
print [[i.encode('utf8') for i in t] for t in result]

from nltk.corpus import stopwords
stopset = set(stopwords.words('english'))
filter_stops = lambda w: len(w) < 3 or w in stopset
bcf.apply_word_filter(filter_stops)
result = bcf.nbest(BigramAssocMeasures.likelihood_ratio, 4)
print [[i.encode('utf8') for i in t] for t in result]


from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures
words = [w.lower() for w in webtext.words('overheard.txt')]
tcf = TrigramCollocationFinder.from_words(words)
tcf.apply_word_filter(filter_stops)
tcf.apply_freq_filter(3)
result = tcf.nbest(TrigramAssocMeasures.likelihood_ratio, 4)
print [[i.encode('utf8') for i in t] for t in result]