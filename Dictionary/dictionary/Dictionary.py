# Importing the libraries
from difflib import get_close_matches
import json
import sys


class LoadData:
    """
    Loading the json data for processing
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def load_json(self):
        """

        :return: returns loaded file
        """
        try:
            data = json.load(open(self.file_name))
            return data
        except FileNotFoundError:
            sys.exit(1)

    def translate(self, word: str) -> str:
        """
        A function to get user input and return it's definition
        :param word: string containing word to be searched
        :return: string with word definition
        """
        word.lower()
        try:
            data = self.load_json()
            if word in data:
                return data[word]
            elif len(get_close_matches(word, data.keys())) > 0:
                out = get_close_matches(word, data.keys())[0]
                yn = input(f"Enter y for yes or n for no if you are searching for {out} : ")
                yn.lower()
                if yn == "y":
                    return data[out]
                else:
                    return "Word not found"
            else:
                return "Word not found"
        except UserWarning:
            print("You need to specify the word")
            sys.exit(1)
