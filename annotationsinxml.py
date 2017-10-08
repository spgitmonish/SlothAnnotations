import os
import json
import shutil
import numpy as np

from pprint import pprint
from PIL import Image
import xml.etree.cElementTree as ET

def CopyAnnotatedImages():
    # Open the JSON file
    annotations_json_file = open('annotations.json')

    # Serialize JSON file into python dictionary
    annotation_data = json.load(annotations_json_file)

    # Current working directory
    for element in annotation_data:
        if element["annotations"]:
            # Copy the file from image_data to annotated_image_data
            filename = os.path.basename(element["filename"])

            # Source location of the file
            src_file = element["filename"]
            dst_file = os.getcwd() + "/Images/" + filename.strip(".png") + ".jpg"

            # Convert the .png image to .jpg and save it the "Images" folder
            jpg_image = Image.open(src_file)
            jpg_image.save(dst_file, "JPEG")

def CreateXMLAnnotationFiles():
    # Open the JSON file
    annotations_json_file = open('annotations.json')

    # Serialize JSON file into python dictionary
    annotation_data = json.load(annotations_json_file)

    # Current working directory
    for element in annotation_data:
        if element["annotations"]:
            # Set the root
            annotation_tag = ET.Element("annotation")

            # Get the folder and the file names
            filepath = element["filename"]
            _, filename = os.path.split(filepath)

            # Create folder and filename tags under <annotation>
            folder_tag = ET.SubElement(annotation_tag, "folder")
            folder_tag.text = "SimTrafficLightData"
            filename_tag = ET.SubElement(annotation_tag, "filename")
            filename_tag.text = filename.strip(".png") + ".jpg"

            # Source tag and it's associated children under annotation_tag
            source_tag = ET.SubElement(annotation_tag, "source")
            ET.SubElement(source_tag, "database").text = "Udacity Simulator"

            # Size tag under annotation_tag
            size_tag = ET.SubElement(annotation_tag, "size")
            image = Image.open(filepath)
            (width, height) = image.size
            _,_,depth = np.asarray(image).shape

            ET.SubElement(size_tag, "width").text = str(width)
            ET.SubElement(size_tag, "height").text = str(height)
            ET.SubElement(size_tag, "depth").text = str(depth)

            # Segmented tag
            segmented_tag = ET.SubElement(annotation_tag, "segmented")
            segmented_tag.text = str(0)

            # Object tags for each of the annotatations
            # NOTE: All the object tags are under the annotation_tag
            for annotation in element["annotations"]:
                object_tag = ET.SubElement(annotation_tag, "object")
                ET.SubElement(object_tag, "name").text = annotation["label"]
                ET.SubElement(object_tag, "pose").text = "Unknown"
                ET.SubElement(object_tag, "truncated").text = "Unknown"
                ET.SubElement(object_tag, "difficult").text = "Unknown"

                # Bounding box tag under object_tag
                bound_box_tag = ET.SubElement(object_tag, "bndbox")
                ET.SubElement(bound_box_tag, "xmin").text = str(int(round(annotation["x"])))
                ET.SubElement(bound_box_tag, "ymin").text = str(int(round(annotation["y"])))
                ET.SubElement(bound_box_tag, "xmax").text = str(int(round(annotation["x"] + annotation["width"])))
                ET.SubElement(bound_box_tag, "ymax").text = str(int(round(annotation["y"] + annotation["height"])))

            # Save the file after getting the tree using the root
            tree = ET.ElementTree(annotation_tag)
            tree.write(os.getcwd() + "/Annotations/" + filename.strip(".png") + ".xml")

if __name__ == '__main__':
    print("Starting the process ...")
    # First copy all the files
    CopyAnnotatedImages()

    # Create the corresponding annotations in .xml format for each of the files
    CreateXMLAnnotationFiles()
    print("Completed!")
