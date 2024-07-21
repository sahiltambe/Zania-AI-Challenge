import PyPDF2

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file.

    Args:
        pdf_file (str): Path to the PDF file.

    Returns:
        str: Text extracted from the PDF.
    """
    # Create a PDF file reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Initialize an empty string to store the extracted text
    text = ""

    # Iterate over each page in the PDF file
    for page_num in range(len(pdf_reader.pages)):
        # Get the page object
        page = pdf_reader.pages[page_num]

        # Extract the text from the page and append it to the text variable
        text += page.extract_text()

    # Return the extracted text
    return text

# Extract text from a PDF file
# :param pdf_file: Path to the PDF file.
# :return: Text extracted from the PDF.



# import PyPDF2

# def extract_text_from_pdf(pdf_file):
#     with open(pdf_file, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         text = ''
#         for page in reader.pages:
#             text += page.extract_text()
#     return text