from spellchecker import SpellChecker

def grammar_check(text):
    spell = SpellChecker()
    words = text.split()
    corrected_words = []
    for word in words:
        corrected_word = spell.correction(word)
        if corrected_word is not None:
            corrected_words.append(corrected_word)
        else:
            corrected_words.append(word)  # Use the original word if no correction found

    corrected_text = ' '.join(corrected_words)

    return corrected_text

def simplify_grammar(text):
    corrected_text = grammar_check(text)
    return corrected_text

input_text = input("Enter a sentence: ")

corrected_text = simplify_grammar(input_text)
print("Corrected sentence:")
print(corrected_text)
