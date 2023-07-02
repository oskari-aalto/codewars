MORSE_CODE =  {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
               '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
               '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
               '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
               '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
               '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
               '...--': '3', '....-': '4', '.....': '5', '-....': '6',
               '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.',
               '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
               '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
               '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+',
               '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$',
               '.--.-.': '@', '...---...': 'SOS'}


def decode_morse(morse_code: str):
    cipher = ''
    characters = morse_code.strip().split(' ')

    for c in characters:
        if c in MORSE_CODE:
            cipher += MORSE_CODE[c]
        elif c == '' and cipher[-1] != ' ':
            cipher += ' '

if __name__ == "__main__":
    #("Should obtain correct decoding of Morse code for basic examples")
    # decode_morse('.-') #  'A'
    # decode_morse('--...') #  '7'
    # decode_morse('...-..-') #  '$'
    # decode_morse('.') #  'E'
    # decode_morse('..') #  'I'
    # decode_morse('. .') #  'EE'
    # decode_morse('.   .') #  'E E'
    # decode_morse('...-..- ...-..- ...-..-'), '$$$'
    # decode_morse('----- .---- ..--- ---.. ----.'), '01289'
    # decode_morse('.-... ---...   -..-. --...'), '&: /7'
    # decode_morse('...---...'), 'SOS'
    # decode_morse('... --- ...'), 'SOS'
    # decode_morse('...   ---   ...'), 'S O S'
        
    #("Should obtain correct decoding of Morse code for examples with extra spaces")
    # decode_morse(' . '), 'E'
    # decode_morse('   .   . '), 'E E'

    #("Should obtain correct decoding of Morse code for a complex example, and should ignore leading and trailing whitespace")
    decode_morse(f'      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-\
                    -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...\
                    --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  ')
                #  'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'


