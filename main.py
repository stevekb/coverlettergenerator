import pyperclip
import json

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
h1 = "Dear " + str(company) + " Human Resources:\n"
p0 = ("Your job opportunity on " + str(jobsite) + " for a " + str(jobname)
    + " interests me. With my experience in " + str(skills[skill_1]['name']) + ", "
    + str(skills[skill_2]['name']) + " and " + str(skills[skill_3]['name'])
    + ", I can serve " + str(company) + " well.\n")
p1 = skills[skill_1]['block'] + "\n"
p2 = skills[skill_2]['block'] + "\n"
p3 = skills[skill_3]['block'] + "\n"
p4 = ("After you have read my resume for the details of my qualifications,"
    + " I will be happy to answer any questions. Please contact me at "
    + str(email) + ", so we can discuss how my experience in "
    + str(skills[skill_1]['name']) + ", " + str(skills[skill_2]['name']) + " and "
    + str(skills[skill_3]['name']) + " will benefit you at " + str(company) +
    ". I look forward to hearing from you.\n\n")
e1 = "Sincerely,\n" + str(name)

m = (h1 + p0 + p1 + p2 + p3 + p4 + e1) # now you can copy
print(m)
pyperclip.copy(m)
print("\ncopied to clipboard")