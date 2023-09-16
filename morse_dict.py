class Morse():

    def __init__(self, message):
        self.message = message.upper()

    # Get one single morse character, contains morse dictionary
    def get_morse_char(self, character):
        morse = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..--",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            "0": "-----",
            "?": "..--..",
            "!": "-.-.--",
            ".": ".-.-.-",
            ",": "--..--",
            ";": "-.-.-.",
            ":": "---...",
            "+": ".-.-.",
            "-": "-....-",
            "/": "-..-.",
            "=": "-...-",
            " ": "/",
            "\n": ""
        }

        return morse[character]

    # Take the full message and convert to morse
    def to_morse(self):
        morse_message = ''
        for char in self.message:
            morse_message += self.get_morse_char(char)
            morse_message += "   "

        return morse_message

