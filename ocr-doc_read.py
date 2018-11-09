import argparse
import io
import os

from google.cloud import vision


def detect_document(filein):
    """
    Detects document features in an image.
    Image file passed in must be a MRZ.
    Returns an array of words containing paired strings/doubles.
    eg. paragraph[word][char position][char, confidence]
    """
    client = vision.ImageAnnotatorClient()

    with io.open(filein, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                parsed_par = []

                for word in paragraph.words:
                    parsed_word = []

                    for symbol in word.symbols:

                        if symbol.text != '<' and symbol.text != '\u00AB' :
                            parsed_word.append([symbol.text, symbol.confidence])

                    if parsed_word:
                        parsed_par.append(parsed_word)

    print(parsed_par)
    return parsed_par


def to_file(text_array, fileout):
    """
    Outputs an array of strings to two files based on content
    filename_text.txt contains text parsed from document, each word on a different line
    filename_confidence.txt contains the confidence for each word, character by character
    """
    if fileout == 0:
        filename_text = 'result_text.txt'
        filename_conf = 'result_confidence.txt'
    else:
        filename_text = fileout + '_text.txt'
        filename_conf = fileout + '_confidence.txt'

    file_text = open(filename_text, 'w+')
    file_conf = open(filename_conf, 'w+')

    for word in text_array:
        for character in word:
            file_text.write(character[0])
            file_conf.write(str(character[1]) + ' ')
        file_text.write('\n')
        file_conf.write('\n')

    print('Wrote results to \"' + filename_text + '\" and \"' + filename_conf + '\"')
    file_text.close()
    file_conf.close()


def set_key(path):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('detect_file', help='The image for text detection.')
    parser.add_argument('-out_file', help='Optional output file', default=0)
    args = parser.parse_args()

    set_key('ocr.json')

    parser = argparse.ArgumentParser()
    text = detect_document(args.detect_file)
    to_file(text, args.out_file)
