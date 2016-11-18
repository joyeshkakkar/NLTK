# Regex Replacer
from replacers import RegexpReplacer
replacer = RegexpReplacer()
print replacer.replace("can't is a contraction")
print replacer.replace("I should've done that thing I didn't do")


# Before Tokenizing
from nltk.tokenize import word_tokenize
replacer = RegexpReplacer()
print word_tokenize("can't is a contraction")
print word_tokenize(replacer.replace("can't is a contraction"))


# Replace repeating characters
from replacers import RepeatReplacer
replacer = RepeatReplacer()
print replacer.replace('looooove')
print replacer.replace('oooooh')
print replacer.replace('goose')


# Replacing snonnyms from a word map
from replacers import WordReplacer
replacer = WordReplacer({'bday': 'birthday'})
print replacer.replace('bday')
print replacer.replace('happy')


# Word replacing using synonym file
from replacers import CsvWordReplacer
replacer = CsvWordReplacer('synonyms.csv')
print replacer.replace('bday')
print replacer.replace('happy')
print replacer.replace('hbd')
print replacer.replace('ttyl')


# Word replacing using synonym yaml file
from replacers import YamlWordReplacer
replacer = YamlWordReplacer('synonyms.yaml')
print replacer.replace('bday')
print replacer.replace('happy')
print replacer.replace('hbd')
print replacer.replace('ttyl')


# Replacing antonyms
from replacers import AntonymReplacer
replacer = AntonymReplacer()
print replacer.replace('good')
print replacer.replace('uglify')
sent = "let's not uglify our code"
print " ".join(replacer.replace_negations(sent.split()))


# Replacing antonyms using word map
from replacers import AntonymWordReplacer
replacer = AntonymWordReplacer({'evil': 'good'})
sent = 'good is not evil'
print " ".join(replacer.replace_negations(sent.split()))





