import os
import glob
from xml.etree import ElementTree as ET


def convert_xml_to_txt(xml_content):
    namespace = {'ns': 'http://openlyrics.info/namespace/2009/song'}
    root = ET.fromstring(xml_content)
    lyrics = root.find('ns:lyrics', namespace)

    verses = []
    for verse in lyrics.findall('ns:verse', namespace):
        verse_name = verse.get('name')
        lines = verse.find('ns:lines', namespace)
        if lines is not None:
            lines_text = '\n'.join(line for line in lines.itertext())
            verses.append((verse_name, lines_text))

    text = ''
    for i, (verse_name, lines) in enumerate(verses):
        text += lines
        if i < len(verses) - 1:
            text += '\n'
    return text


input_folder = '/Users/alfie/Downloads/ProPresenter/OpenLP backups/Songs'
output_folder = '/Users/alfie/Downloads/ProPresenter/OpenLP backups/songs_txt'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

xml_files = glob.glob(os.path.join(input_folder, '*.xml'))
total_files = len(xml_files)
errored_files = []

for index, xml_file in enumerate(xml_files):
    try:
        with open(xml_file, 'r', encoding='utf-8') as file:
            xml_content = file.read()

        txt_content = convert_xml_to_txt(xml_content)
        output_filename = os.path.splitext(os.path.basename(xml_file))[0] + '.txt'

        with open(os.path.join(output_folder, output_filename), 'w', encoding='utf-8') as file:
            file.write(txt_content)
        print(f"{index + 1}/{total_files} done")
    except Exception as e:
        print(f"Error processing file '{xml_file}': {e}")
        errored_files.append(xml_file)

if errored_files:
    print("\nFiles that had errors during processing:")
    for file in errored_files:
        print(file)
