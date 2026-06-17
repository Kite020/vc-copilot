from pdf2image import convert_from_path


def convert_pdf_to_images(pdf_path):

    pages = convert_from_path(pdf_path)

    image_paths = []

    for i, page in enumerate(pages):

        image_path = f"slide_{i + 1}.png"

        page.save(
            image_path,
            "PNG"
        )

        image_paths.append(
            image_path
        )

    return image_paths