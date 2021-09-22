# First solution
def spin_words(sentence):
    spin_sentence = []
    words = sentence.split(" ")
    for word in words:
        if len(word) >= 5:
            spin_sentence.append(word[::-1])
        else:
            spin_sentence.append(word)
    return " ".join(spin_sentence)

# Clear solution


def spin_words(sentence):
    spin_sentence = [
        word[::-1] if len(word) >= 5 else word for word in sentence.split(" ")]
    return " ".join(spin_sentence)


print(spin_words("Hey fellow warriors"))
print(spin_words("Welcome"))
print(spin_words("This is a test"))
print(spin_words("This is another test"))
