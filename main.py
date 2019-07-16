skills = [
    ("awesomeness","I learned how to be awesome while growing up."),
    ("superness", "I'm super just like super man."),
    ("communication", "I can speak English.")
]

# contact me if you are offering a software dev/engineering job.
name = "Stephen Kelly-Bazan"
phone = "678-654-8038"
email = "stephenkb44@gmail.com"
company = input("Company name?") # first ask for the company name
jobsite = input("What site did you find this job?")
jobname = input("What is the job name")
skill_1 = input("What block is skill 1 in?")
skill_2 = input("What block is skill 2 in?")
skill_3 = input("What block is skill 3 in?")

#after all seletions are made generate text and then print
h1 = "Dear " + str(company) + " Human Resources:\n"
p0 = "Your job opportunity on " + str(jobsite) + " for a "
+ str(jobname) + " interests me. With my experience in "
+ str(skills[skill_1][0]) + ", " + str(skills[skill_2][0])
+ " and " + str(skills[skill_3][0]) + ", I can serve "
+ str(company) + " well.\n"
p1 = skills[skill_1][1] + "\n"
p2 = skills[skill_2][1] + "\n"
p3 = skills[skill_3][1] + "\n"
p4 = "After you have read my resume for the details of my qualifications,"
+ " I will be happy to answer any questions. Please contact me at "
+ str(email) + ", so we can discuss how my experience in "
+ str(skills[skill_1][0]) + ", " + str(skills[skill_2][0])
+ " and " + str(skills[skill_3][0]) + " will benefit you at "
+ str(company) + ". I look forward to hearing from you.\n\n"
e1 = "Sincerely,\n"
+ str(name)