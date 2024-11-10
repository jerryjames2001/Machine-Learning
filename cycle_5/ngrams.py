print("Jerry James \n23MCA036")

def gen_ngrams(text, words_combine):
    words = text.split()
    output = []
    for i in range(len(words) - words_combine + 1):
        output.append(words[i:i+words_combine])
    return output

x = gen_ngrams("I am a student of MCA", 3)
print(x)