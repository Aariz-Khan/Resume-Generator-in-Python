# import required libraries
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader

# define function to get user input
def get_user_input():
    name = input("What's your name? ")
    email = input("What's your email address? ")
    phone = input("What's your phone number? ")
    opteducation = input("What's your educational background?\n1. High School\n2. Bachelor's Degree\n3. Master's Degree\n4. Doctoral Degree\n5. Other\n")
    experience = input("What's your work experience? ")
    skills = input("What are your skills? ")
    if opteducation == '1':
        education = 'High School'
    elif opteducation == '2':
        education = "Bachelor's Degree"
    elif opteducation == '3':
        education = "Master's Degree"
    elif opteducation == '4':
        education = "Doctoral Degree"
    elif opteducation == '5':
        education = input("What's your educational background? ")
    return {
        'name': name,
        'email': email,
        'phone': phone,
        'education': education,
        'experience': experience,
        'skills': skills
    }

# define function to create the CV HTML template
def create_cv_html_template(user_input):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('cv_template.html')
    return template.render(user=user_input)

# define function to export the CV HTML to PDF
def export_cv_pdf(cv_html, output_path):
    HTML(string=cv_html).write_pdf(output_path)

# get user input and create the CV HTML template
user_input = get_user_input()
cv_html = create_cv_html_template(user_input)

# export the CV HTML to PDF
export_cv_pdf(cv_html, 'cv.pdf')
