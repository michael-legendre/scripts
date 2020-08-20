import pandas as pd
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image

student_data = pd.read_csv('report.csv').set_index('stunum')
print(student_data.head())

def create_report(data_row):

    TITLE_MARGIN = 20
    TXT_MARGIN = 150

    filename = f"{data_row.name}.pdf"
    canvas = Canvas(filename)

    #insert logo
    logo = "sullivan-logo-square.jpg"
    canvas.drawImage(logo, 40, 750, width=100, height=92, mask=None)
    # Write student header
    canvas.setFont("Helvetica", 30)
    canvas.drawString(TITLE_MARGIN, 650, f"{data_row['first']} {data_row['last']}")

    # Write report header
    canvas.setFont("Helvetica", 20)
    canvas.drawString(TXT_MARGIN, 600, "Grade Details (through Spring 2020 term)")
    canvas.line(TXT_MARGIN - 50, 580, 500, 580)

    # Write student data
    canvas.drawString(TXT_MARGIN, 550, f"Program: {data_row['pgm_desc']}")
    canvas.drawString(TXT_MARGIN, 500, f"GPA: {data_row['gpa']}")
    canvas.drawString(TXT_MARGIN, 450, f"Class Rank: {data_row['class_rank']}")
    canvas.drawString(TXT_MARGIN, 400, f"Percentile Rank: {data_row['percentile_rank']}")

    canvas.save()

for stunum, data_row in student_data.iterrows():
    create_report(data_row)
