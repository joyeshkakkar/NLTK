# Porter Stemmer
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print stemmer.stem('cooking')
print stemmer.stem('cookery')

# LancasterStemmer
from nltk.stem import LancasterStemmer
stemmer = LancasterStemmer()
print stemmer.stem('cooking')
print stemmer.stem('cookery')

# RegexpStemmer
from nltk.stem import RegexpStemmer
stemmer = RegexpStemmer('ing')
print stemmer.stem('cooking')
print stemmer.stem('cookery')
print stemmer.stem('ingleside')

# SnowballStemmer
from nltk.stem import SnowballStemmer
print SnowballStemmer.languages
spanish_stemmer = SnowballStemmer('spanish')
print spanish_stemmer.stem('hola')