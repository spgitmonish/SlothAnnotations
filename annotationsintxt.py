import os
import json
import shutil
from pprint import pprint

def CopyAnnotatedImages():
    # Open the JSON file
    annotations_json_file = open('annotations.json')

    # Serialize JSON file into python dictionary
    annotation_data = json.load(annotations_json_file)

    # List of valid annotations
    list_of_annotation_data = []

    # Current working directory
    for element in annotation_data:
        if element["annotations"]:
            # Copy the file from image_data to annotated_image_data
            filename = os.path.basename(element["filename"])

            # Source location of the file
            src_file = element["filename"]
            dst_file = os.getcwd() + "/annotated_image_data/" + filename

            # Copy to destination
            shutil.copy(src_file, dst_file)

            # Copy the annotation
            list_of_annotation_data.append(element)

    return list_of_annotation_data

def CreateTxtAnnotationFiles():
    # For the annotations passed in create a text file where each row has:
    # x1 y1 x2 y2 label
    # Open the JSON file
    annotations_json_file = open('annotations.json')

    # Serialize JSON file into python dictionary
    annotation_data = json.load(annotations_json_file)

    # Current working directory
    for data in annotation_data:
        if data["annotations"]:
            # Get the filename of the annotated image
            filename = os.path.basename(data["filename"])

            # Textfile with the annotations for this image
            txt_file = os.getcwd() + "/image_annotations/" + filename.strip(".png") + ".txt"

            # Open the text file
            text_file_to_write = open(txt_file, 'w')

            # Write in a new row with the data described above
            annotations = data["annotations"]
            # Get the length of the annotations
            length = len(annotations)
            # Count of the annotation
            count = 0
            for annotation in annotations:
                # Calculate all the required annotation values
                x1 = annotation["x"]
                y1 = annotation["y"]
                label = annotation["label"]
                x2 = x1 + annotation["width"]
                y2 = y1 + annotation["height"]

                # Round the numeric values to integers
                x1 = int(round(x1))
                y1 = int(round(y1))
                x2 = int(round(x2))
                y2 = int(round(y2))

                # Convert the label into the appropriate number
                # RED = 0, ORANGE = 1, GREEN = 2
                if label == "red_rect":
                    label = 0
                elif label == "orange_rect":
                    label = 1
                elif label == "green_rect":
                    label = 2

                # Check the count and write with the '\n' escape character
                string_to_write = ""
                if (count == 0 and length == 1) or (count == length - 1):
                    string_to_write = str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2) + " " + str(label)
                else:
                    string_to_write = str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2) + " " + str(label) + "\n"
                # Write to the text file
                text_file_to_write.write("%s" % string_to_write)

                # Increment count
                count += 1

            # Close the file
            text_file_to_write.close()
if __name__ == '__main__':
    list_of_annotation_data = CopyAnnotatedImages()
    #pprint(list_of_annotations)
    CreateTxtAnnotationFiles()
