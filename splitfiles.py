import os
from random import shuffle
from math import floor

def get_file_list_from_dir(datadir):
    all_files = os.listdir(os.path.abspath(datadir))
    return all_files

def randomize_files(file_list):
    shuffle(file_list)

def get_training_and_testing_sets(file_list):
    split = 0.9
    split_index = floor(len(file_list) * split)
    training = file_list[:split_index]
    testing = file_list[split_index:]
    return training, testing

def write_to_txt_file(txt_filename, file_list):
    txt_file = open(txt_filename, "w")

    # For keeping track of "\n" addition
    length = len(file_list)
    count = 0
    for image_file in file_list:
        # Check if there is only one file in the list or the count is the end
        if (count == 0 and length == 1) or (count == length - 1):
            txt_file.write("%s" % image_file)
        else:
            txt_file.write("%s\n" % image_file)

        # Increment the count
        count += 1

def compose_tr_val_tst_txt_files(training, validation, testing):
    # Write the training files
    write_to_txt_file(os.getcwd() + "/Names/train.txt", training)
    # Write the validation files
    write_to_txt_file(os.getcwd() + "/Names/valid.txt", validation)
    # Write the testing files
    write_to_txt_file(os.getcwd() + "/Names/test.txt", testing)

if __name__ == "__main__":
    # Path to the images folder
    data_dir = os.getcwd() + "/Images"

    # Get a list of all the image files
    data_files = get_file_list_from_dir(data_dir)

    # Split into training and test
    training, testing = get_training_and_testing_sets(data_files)

    # Split training into training and validation
    training, validation = get_training_and_testing_sets(training)

    # Write the file names for training, validation and testing into respective files
    compose_tr_val_tst_txt_files(training, validation, testing)
