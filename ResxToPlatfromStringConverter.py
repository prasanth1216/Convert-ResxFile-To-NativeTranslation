#!/usr/bin/python
import os
import xml.etree.ElementTree as ET
import argparse

defaultOutputDir = "."
parser = argparse.ArgumentParser()

parser.add_argument('-idir', type=str, default=".", required=True, help="path to source directory")
parser.add_argument('-iextension', type=str, default=".resx", required=False, help="input file extension")
parser.add_argument('-odir', type=str, default=defaultOutputDir, required=False, help="path to output directory")
parser.add_argument('-platform', type=str, default="ios", required=False, help="platform ios or android")
parser.add_argument('-log', type=bool, default=False, required=False, help="verbose log")

args = parser.parse_args()

inputDirectory = args.idir
inputFileExtension = args.iextension
outputDirectory = args.odir
isAndroid = (args.platform == "android")
outputName = "Localizable"
outputExtension = ".strings"
if isAndroid == True:
    outputExtension = ".xml"
    outputName = "strings"

translationLanguageSep = "."

if args.log == True:
    print("Input Dir:" + inputDirectory)
    print("Input file extension:" + inputFileExtension)
    print("Output Dir:" + outputDirectory)
    print("Output filename:" + outputName)
    print("Output extension:" + outputExtension)

dir_list = os.listdir(inputDirectory)
inputfile_list = []

print("Execution begins..")

if not outputDirectory == defaultOutputDir:
    # Check whether the output path exists or not
    isExist = os.path.exists(outputDirectory)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(outputDirectory)
        print("The output directory is created.")

if args.log == True:
    print("Input files:")

for file in dir_list:
    if file.endswith(inputFileExtension):
        completefile_path = os.path.join(inputDirectory, file)
        inputfile_list.append(completefile_path)
        
        if args.log == True:
            print(completefile_path)

for inputfile in inputfile_list:

    head, tail = os.path.split(inputfile)

    # Finding language code
    lang_code = tail[tail.find(translationLanguageSep)+1 : tail.find(inputFileExtension)]

    if not len(lang_code) == 0:
        outputfile_path = os.path.join(outputDirectory, outputName + translationLanguageSep + lang_code + outputExtension)
    else:
        outputfile_path = os.path.join(outputDirectory, outputName + outputExtension)

    if args.log == True:
        print("Language Code: " + lang_code)
        print("Output file: " + outputfile_path)
    
    # Parsing code
    fileTree = ET.parse(inputfile)
    rootElement = fileTree.getroot()

    if isAndroid == True:
        outputRootElement = ET.Element('resources')
        outputRootElement.tail = "\n"  
        for element in rootElement.findall('data'):
            stringElement = ET.SubElement(outputRootElement, 'string')
            stringElement.attrib['name'] = element.attrib['name']
            stringElement.text = element.find('value').text
            stringElement.tail = "\n"   
        outputTree = ET.ElementTree(outputRootElement)
        outputTree.write(outputfile_path)
    else:
        outputfile = open(outputfile_path, 'w')

        # Processing code
        print("Processing the file: " + inputfile)
    
        for element in rootElement.findall('data'):
            text = "\"" + element.attrib['name'] + "\" = \"" + element.find('value').text + "\""
            outputfile.write(text)
            outputfile.write('\n')
            if args.log == True:
                print(text)
        
        outputfile.close()
print("Execution finished!")