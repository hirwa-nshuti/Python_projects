import argparse
from dictionary import LoadData
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='DictionaryAPP',
                                     usage='%(prog)s [options] : word',
                                     description="Definition of different words",
                                     epilog='Thanks for using our dictionary')

    # Arguments
    parser.add_argument("word",
                        metavar="word",
                        type=str,
                        help="Word to search in Dictionary")
    args = parser.parse_known_args()
    try:
        word_to_search = sys.argv[1]
        file_name = "dictionary.json"
        dict_data = LoadData(file_name)
        print(dict_data.translate(word_to_search))
    except UserWarning:
        print("Enter the valid arguments")
        sys.exit()
