"""Defining methods that can be used to read and process
data from the file
"""
from operator import itemgetter

LOADED_DATA = []


class LoadData:
    """Loading the text file to work on with"""

    def __init__(self, file_name):
        self.file_name = file_name

    def load_items_data(self):

        """Loading the data file amd extracting the data structure
        to use I chose to use a 2D array(Matrix)
        """
        try:
            with open(self.file_name, 'r') as file:
                for item in file.readlines():
                    LOADED_DATA.append(item.split())
            return LOADED_DATA
        except FileNotFoundError:
            pass

    def convert_to_number_columns(self, data):
        """As the loaded file is in string mode and we have some
        numerical values I chose to change them from string to numbers
        """

        for element in data:
            for index, val in enumerate(element):
                if val.isnumeric():
                    element[index] = int(val)

        return data

    def encode_data(self, data: list):
        """Encoding the string values we have on priority column for
        Easy sorting"""
        for num in data:
            for index, val in enumerate(num):
                num[len(num)-1] = num[len(num)-1].upper()
                if val == "LOW":
                    num[index] = 1
                elif val == "MEDIUM":
                    num[index] = 2
                elif val == "HIGH":
                    num[index] = 3
        return data

    def decode_data(self, data):
        """Decoding the encoded values to get our data originality"""
        for num in data:
            for index, val in enumerate(num):
                if index == 2:
                    if val == 1:
                        num[index] = "LOW"
                    if val == 2:
                        num[index] = "MEDIUM"
                    if val == 3:
                        num[index] = "HIGH"
        return data

    def ascending_sorting(self, data_to_sort, col_name: str, sort_type: str):
        """
        Getting user request and sort the data to be written to the file
        in ascending and descending order
        """
        err_message = "Sorry Unknown inputs try to restart the system"
        try:
            if sort_type == "ascending":

                if col_name == "sequence":
                    user_data = sorted(data_to_sort, key=itemgetter(0))
                elif col_name == "size":
                    user_data = sorted(data_to_sort, key=itemgetter(1))
                elif col_name == "priority":
                    user_data = sorted(data_to_sort, key=itemgetter(2))
                else:
                    return "Choice not available try to restart the system"
                return user_data
            elif sort_type == "descending":
                if col_name == "sequence":
                    user_data = sorted(data_to_sort, key=itemgetter(0))[::-1]
                elif col_name == "size":
                    user_data = sorted(data_to_sort, key=itemgetter(1))[::-1]
                elif col_name == "priority":
                    user_data = sorted(data_to_sort, key=itemgetter(2))[::-1]
                else:
                    return err_message
                return user_data
        except UserWarning:
            pass

    def write_text_file(self, out_file_name, user_data):
        """Method to write text file containing the sorted Items data"""
        with open(out_file_name, "w") as out_f:
            for element in user_data:
                element = str(element).replace("[",
                                               "").replace("]", "").replace(",",
                                                                            "").replace("'", "")
                out_f.write(element + "\n")
