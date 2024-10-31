def ngrams(text, n):
    words = text.split()
    out = []
    for i in range(len(words) - n + 1):
        out.append(words[i:i+n])
    return out
text = "I am a cat and I like to sleep all day"
n=3
x=ngrams(text,n)
print(x)