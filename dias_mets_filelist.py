## This generates a an output list file in CSV with two columns - the dias-mets.xml path and the file checksum
## The list can be generated from one or more dias-mets.xml files
## The output list file consists of one line for each file entry of the archive in a dias-mest.xml file

import xml.etree.ElementTree as ET
import pathlib

import uuid

import sys

dias_path = "."

list_output_folder = pathlib.Path("./list_output")

dias_files = [path for path in sys.argv[1:]]

if len(dias_files)<2:
    dias_files = pathlib.Path(dias_path).rglob('dias-mets.xml')

short_uuid = str(uuid.uuid4())[:7]
print(short_uuid)
file_name = "checksum_list_" + short_uuid + ".csv"
file_name = list_output_folder / file_name

textfile = open(file_name, "w")
print("oppretter liste: " + str(file_name))

checksum_list = []

for dias_file in dias_files:
    print("leser inn: " + str(dias_file))
    root = ET.parse(dias_file).getroot()

    counter = 0
    for fileSec in root:
        for fileGrp in fileSec:
                for file in fileGrp:
                    if file.tag == '{http://www.loc.gov/METS/}file':
                        counter += 1
                        element = [(str(dias_file), file.attrib["CHECKSUM"])]
                        checksum_list += element
                        textfile.write(str(element[0][0])+ ";" + str(element[0][1]) + '\n')
textfile.close()
print("Listen ble opprettet: " + str(file_name))
