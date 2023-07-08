from spellchecker import SpellChecker

spell = SpellChecker()

input_text = "I wnt too tha store to by som fruts and vgitables."

words = input_text.split()
corrected_words = []
for word in words:
    corrected_word = spell.correction(word)
    if corrected_word is not None:
        corrected_words.append(corrected_word)
    else:
        corrected_words.append(word)

corrected_text = ' '.join(corrected_words)

print(corrected_text)
