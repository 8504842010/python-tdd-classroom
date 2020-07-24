class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        str1=input_str[::-1]
        return str1

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        if character=="A" or character=="I" or character=="O" or character=="E" or character=="U":
            return True
        elif character=="a" or character=="i" or character=="o" or character=="e" or character=="u":
            return True
        else:
            return False


    def find_longest_word(self, sentence):

        current_max = 0
        for v in sentence.split():
            le = len(v)
            if le > current_max:
                current_max = le
                word = v
        return word

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        list1=[]
        for v in text.split():
            list1.append(len(v))

        return list1
