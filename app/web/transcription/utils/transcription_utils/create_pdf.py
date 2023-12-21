from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(transcripts):

    now = datetime.now()
    date_time_str = now.strftime("%Y%m%d_%H%M%S")
    pdf_filename = f"output_transcript_{date_time_str}.pdf"

    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    styles = getSampleStyleSheet()

    story = []

    for i, transcript in enumerate(transcripts, start=1):
        text = f"Segment {i}: {transcript}\n\n"
        p = Paragraph(text, styles['Normal'])
        story.append(p)
        story.append(Spacer(1, 12))  # Add some space between segments

    doc.build(story)

    return pdf_filename
