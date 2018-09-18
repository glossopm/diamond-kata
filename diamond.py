from printer import Printer
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

class Diamond:
    def __init__(self,letter):
        self.letter = letter

    def generate_string(self, outside_space, inside_space, string, i):
        string += outside_space*" "+alphabet[i]+inside_space*" "+alphabet[i]+"\n"
        return string

    def validate_input(self):
        return self.letter.isalpha() and len(self.letter) == 1

    def draw(self):
        if not self.validate_input():
            return "Enter a valid letter in the Alphabet, looking at you Ben."
            
        letter_index = alphabet.index(self.letter)
        string = ""
        if self.letter == 'A':
            return 'A'
        string =letter_index*" "+'A\n'
        inside_space = 0


        for i in range(1, letter_index+1):
            outside_space = letter_index - i
            if i==1:
                inside_space = 1
            elif i>1:
                inside_space += 2
            string = self.generate_string(outside_space, inside_space, string, i)
        outside_space = 0


        for i in range(letter_index-1,0,-1):
            if i==1:
                inside_space = 1
            elif i>1:
                inside_space += -2
            outside_space += 1
            string = self.generate_string(outside_space, inside_space, string, i)
        string +=letter_index*" "+'A'
        return string