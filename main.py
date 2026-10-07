def read_text():
    text = input("Введите текст: ")
    return text.strip()
def tokenize(text):
    text = text.split()
    return text

def build_vocabulary(tokens):
    vocabulary = {}

    for token in tokens:
        if token not in vocabulary:
            vocabulary[token] = len(vocabulary)

    return vocabulary


text = read_text()
text = tokenize(text)
if len(text)  == 0:
    print("Текст не введён")
else:
    print("Исходный текст:", text)
print(build_vocabulary(text))