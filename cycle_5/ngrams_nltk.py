print("Jerry James \n 23MCA036")
from nltk import ngrams
text = "I am a student of MCA"
n=3

out=ngrams(text.split(),n)
for i in out:
    print(i)
