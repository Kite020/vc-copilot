from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_pdf(
    memo_text,
    output_file
):

    doc = SimpleDocTemplate(
        output_file
    )

    styles = getSampleStyleSheet()

    content = []

    for paragraph in memo_text.split("\n\n"):

        content.append(
            Paragraph(
                paragraph,
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(
                1,
                12
            )
        )

    doc.build(content)