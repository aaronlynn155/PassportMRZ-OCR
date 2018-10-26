import argparse
import io

from google.cloud import vision

# Needs GOOGLE_APPLICATION_CREDENTIALS to be set to the API key file before running

def detect_document(filein):
    """Detects document features in an image."""
    client = vision.ImageAnnotatorClient()

    with io.open(filein, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    parse_string = ''
    parsed_text = []

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            # print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                # print('Paragraph confidence: {}'.format(paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(word_text, word.confidence))

                    for symbol in word.symbols:
                        # print('\tSymbol: {} (confidence: {})'.format(symbol.text, symbol.confidence))
                        parse_string += symbol.text
                    if '<' not in parse_string and '\u00AB' not in parse_string:
                        parsed_text.append(parse_string)
                    parse_string = ''

    print(parsed_text)
    return parsed_text


def to_file(text_array, fileout):
    """Outputs an array of strings to a file"""
    if fileout == 0:
        filename = 'result.txt'
    else:
        filename = fileout

    file = open(filename, 'w+')

    for word in text_array:
        file.write(word + '\n')

    print('Wrote results to \"' + filename + '\"')
    file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('detect_file', help='The image for text detection.')
    parser.add_argument('-out_file', help='Optional output file', default=0)
    args = parser.parse_args()

    parser = argparse.ArgumentParser()
    text = detect_document(args.detect_file)
    to_file(text, args.out_file)
