from PIL import Image
import math


def combine_slides(
    image_paths,
    output_path="combined_slides.png"
):

    images = [
        Image.open(path)
        for path in image_paths
    ]

    slide_width = max(
        img.width
        for img in images
    )

    slide_height = max(
        img.height
        for img in images
    )

    cols = 2

    rows = math.ceil(
        len(images) / cols
    )

    combined = Image.new(
        "RGB",
        (
            slide_width * cols,
            slide_height * rows
        ),
        "white"
    )

    for idx, img in enumerate(images):

        row = idx // cols
        col = idx % cols

        x = col * slide_width
        y = row * slide_height

        combined.paste(
            img,
            (x, y)
        )

    combined.save(output_path)

    return output_path