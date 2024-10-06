# Morse Code Dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

inverse_morse_code_dict = {value: key for key, value in morse_code_dict.items()}

def text_to_morse(text):
    text = text.upper()
    morse_code = []

    for char in text:
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append('')

    return ' '.join(morse_code)

def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = []

    for code in morse_code:
        if code in inverse_morse_code_dict:
            text.append(inverse_morse_code_dict[code])
        else:
            text.append('')

    return ''.join(text).replace('/', ' ')

text = input("Enter text: ")
morse_code = text_to_morse(text)
print(f"Text to Morse code: {morse_code}")

morse_code_input = input("Enter youre morse code: ")
text_output = morse_to_text(morse_code_input)
print(f"Morse code to text: {text_output}")


