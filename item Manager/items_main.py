"""
The main file to communicate with user on what he really wants
"""
import items_manager as im

ITEMS_FILE = "items.txt"
OUT_FILE_SEQUENCE = "order_by_sequence.txt"
OUT_FILE_SIZE = "order_by_size.txt"
OUT_FILE_PRIORITY = "order_by_priority.txt"

if __name__ == "__main__":
    """Loading the text file with Items data and returning a usable data structure 
    and instantiating the object"""
    loaded_data = im.LoadData(ITEMS_FILE)

    # getting the data structure to use

    items_data = loaded_data.load_items_data()

    # converting string numerical values to integers

    main_data = loaded_data.convert_to_number_columns(items_data)
    encoded_data = loaded_data.encode_data(main_data)
    # getting inputs from user about Sorting method and sorting choice

    column_name = input("Enter one of either Size, Sequence or priority as sorting media: \n")
    column_name = column_name.lower()

    sort_type = input("What is your favorite between Ascending and descending ordered data: \n")
    sort_type = sort_type.lower()

    # sorting data

    sorted_data = loaded_data.ascending_sorting(main_data, column_name, sort_type)
    sorted_data = loaded_data.decode_data(sorted_data)
    # writing text file
    if column_name == "sequence":
        loaded_data.write_text_file(OUT_FILE_SEQUENCE, sorted_data)
    elif column_name == "size":
        loaded_data.write_text_file(OUT_FILE_SIZE, sorted_data)
    elif column_name == "priority":
        loaded_data.write_text_file(OUT_FILE_PRIORITY, sorted_data)
    else:
        print("Unknown input please restart the system")
