import nltk
from nltk import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt_tab')
nltk.download('stopwords')
text = "I am a student of MCA"
print("sentence tokenization:")
print(sent_tokenize(text))
print("word tokenization:")
print(word_tokenize(text))
text1 = word_tokenize(text)
text2 = [i for i in text1 if i not in stopwords.words('english')]
print("")
print("After removing stopwords:")
print(text2)
print("")
print("ngrams:")
unigrams = ngrams(text2,3)
for grams in unigrams:
    print(grams)