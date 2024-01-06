import fitz  # PyMuPDF


def add_image_below_text(pdf_path, target_text, image_path, output_path):
    doc = fitz.open(pdf_path)

    for page_num in range(doc.page_count):
        page = doc[page_num]
        text_instances = page.search_for(target_text)

        for text_rect in text_instances:
            image_rect = fitz.Rect(
                text_rect.x0, text_rect.y1, text_rect.x1 + 20, text_rect.y1 + 80
            )  # Adjust the size of the image_rect as needed
            image = page.insert_image(image_rect, filename=image_path)

    doc.save(output_path)
    doc.close()


# Example usage
pdf_path = "format.pdf"
target_text = "Bendahara"
image_path = "TT NANDAR.png"
output_path = "output2.pdf"

add_image_below_text(pdf_path, target_text, image_path, output_path)
