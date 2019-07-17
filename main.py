import pyperclip
import json
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch



with open("privateData.json", "r") as rf:
    data = json.load(rf)

skills = data['skills']
name = data['name']
phone = data['phone']
email = data['email']

# ask about cover letter info
company = input("Company name? ") # first ask for the company name
jobsite = input("What site did you find this job? ")
jobname = input("What is the job name? ")
skill_1 = int(input("What block is skill 1 in? "))
skill_2 = int(input("What block is skill 2 in? "))
skill_3 = int(input("What block is skill 3 in? "))

#after all seletions are made generate text and then print
h1 = ("Dear " + str(company) + " Human Resources:\n")
p0 = ("Your job opportunity on " + str(jobsite) + " for a " + str(jobname)
    + " interests me. With my experience in " + str(skills[skill_1]['name']) + ", "
    + str(skills[skill_2]['name']) + " and " + str(skills[skill_3]['name'])
    + ", I can serve " + str(company) + " well.\n")
p1 = (skills[skill_1]['block'] + "\n")
p2 = (skills[skill_2]['block'] + "\n")
p3 = (skills[skill_3]['block'] + "\n")
p4 = ("After you have read my resume for the details of my qualifications,"
    + " I will be happy to answer any questions. Please contact me at "
    + str(email) + ", so we can discuss how my experience in "
    + str(skills[skill_1]['name']) + ", " + str(skills[skill_2]['name']) + " and "
    + str(skills[skill_3]['name']) + " will benefit you at " + str(company) +
    ". I look forward to hearing from you.\n\n")
e1 = ("Sincerely,\n")
e2 = (str(name))
m = (h1 + p0 + p1 + p2 + p3 + p4 + e1 + e2) # now you can copy

print(m)
pyperclip.copy(m)
print("\ncopied to clipboard")

ml = [h1, p0, p1, p2, p3, p4 , e1, e2]
# now we make pdf >:3
pdfname = "Cover Letter - " + str(company) + " " + str(jobname) + ".pdf"
doc = SimpleDocTemplate(pdfname, pagesize=letter,
rightMargin=72, leftMargin=72,
topMargin=72, bottomMargin=18)

Story=[]
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))


myStyle = ParagraphStyle(
   'myStyle',
    parent=styles['Normal'],
    fontSize=11,
    leading=16,
    fontName="Helvetica",
)

for i in range(len(ml)):
    if not i == 0:
        Story.append(Spacer(1,12))
    if i == 6:
        Story.append(Spacer(1,12))
    text = '<font size=11>%s</font>' % ml[i]
    Story.append(Paragraph(text, myStyle))
    
doc.build(Story)