import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image


def add_images_to_pdf(pdf_path, output_path, text1, img1_path, text2, img2_path):
    # Open the existing PDF file
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        # Create a new PDF file for output
        with open(output_path, "wb") as output_pdf:
            pdf_writer = PyPDF2.PdfFileWriter()

            # Iterate through each page in the original PDF
            for page_num in range(pdf_reader.numPages):
                # Get the page
                page = pdf_reader.getPage(page_num)

                # Check if text1 is present on the page
                if text1 in page.extractText():
                    # Add image1 below text1
                    image1 = Image.open(img1_path)
                    width, height = letter
                    pdf_writer.addPage(page)
                    pdf_writer.addBlankPage(width, height)
                    pdf_writer.getPage(page_num + 1).mergeTranslatedPage(
                        page, 0, -image1.height
                    )

                # Check if text2 is present on the page
                if text2 in page.extractText():
                    # Add image2 below text2
                    image2 = Image.open(img2_path)
                    width, height = letter
                    pdf_writer.addPage(page)
                    pdf_writer.addBlankPage(width, height)
                    pdf_writer.getPage(page_num + 1).mergeTranslatedPage(
                        page, 0, -image2.height
                    )

                else:
                    pdf_writer.addPage(page)

            # Save the modified PDF to the output file
            pdf_writer.write(output_pdf)


# Example usage:
add_images_to_pdf(
    "format.pdf",
    "output.pdf",
    "Bendahara",
    "TT NANDAR.png",
    "Kepala Sekolah",
    "TT KEPSEK.png",
)
