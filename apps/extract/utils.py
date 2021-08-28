from pdf2image import convert_from_path
from pytesseract import image_to_string
import re


def convert_pdf_to_img(pdf_file):
    """
    @desc: this function converts a PDF into Image
    
    @params:
        - pdf_file: the file to be converted
    
    @returns:
        - an interable containing image format of all the pages of the PDF
    """
    return convert_from_path(pdf_file)


def convert_image_to_text(file):
    """
    @desc: this function extracts text from image
    
    @params:
        - file: the image file to extract the content
    
    @returns:
        - the textual content of single image
    """
    
    text = image_to_string(file)
    return text


def get_text_from_any_pdf(pdf_file):
    """
    @desc: this function is our final system combining the previous functions
    
    @params:
        - file: the original PDF File
    
    @returns:
        - the textual content of ALL the pages
    """
    images = convert_pdf_to_img(pdf_file)
    final_text = ""
    for pg, img in enumerate(images):
        
        final_text += convert_image_to_text(img)
        #print("Page n°{}".format(pg))
        #print(convert_image_to_text(img))
    
    return final_text


def get_values_from_text(pdf_file):
    """
    @desc: this function is our final system combining the previous functions
    
    @params:
        - file: the original PDF File
    
    @returns:
        - the textual content of ALL the pages
    """

    # capture text from pdf path
    text = get_text_from_any_pdf(pdf_file)

    # dictionary with regural expressions by atribute to search
    regexs = {
        "vendor_name": r'VENDOR NAME:\s?(\w+\s?\.?)+',
        "fiscal_number": r'FISCAL NUMBER:\s?(\w+-?)+',
        "contract": r'CONTRACT\s*#:\s?(\d+)+',
        "start_date": r'START DATE:\s?(\n)*((\d)+/)+(\d){4}',
        "end_date": r'END DATE:\s?(\n)*((\d)+/)+(\d){4}',
        "comments": r'COMMENTS:(\n)*(\w+(\.|,)?\s?)+(\n){1,2}'
    }

    # dictionary to return to creane new extractedData register
    dict_to_return = {"doc_path": pdf_file}

    # populate dictionary by atribute and value found or None otherwise
    for attr, regex in regexs.items():
        match = re.search(regex, text.upper())
        if match:
            value = match.group(0).split(":")[1]
            dict_to_return[attr] = value.strip('\n').lstrip()
        else:
            dict_to_return[attr] = None
    
    return dict_to_return


def handle_uploaded_file(f):
    path = './uploated_files/{}'.format(f.name)
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return path