# Lemmatizing
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print lemmatizer.lemmatize('cooking')
print lemmatizer.lemmatize('cooking', pos='v')
print lemmatizer.lemmatize('cookbooks')

# Difference with stemming
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print stemmer.stem('believes')
print lemmatizer.lemmatize('believes')
