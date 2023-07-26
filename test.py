from jinja2 import Environment, FileSystemLoader

# Define the variables
name = "John Doe"
email = "johndoe@example.com"
phone = "555-1234"
education = {
    "degree": "Bachelor of Science in Computer Science",
    "university": "University of Example",
    "date": "May 2020"
}
experience = [
    {
        "position": "Software Engineer",
        "company": "Example Inc.",
        "date": "May 2020 - Present",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed suscipit metus sed ligula tincidunt, eu blandit turpis faucibus. Praesent in sagittis metus. Aliquam erat volutpat."
    },
    {
        "position": "Intern",
        "company": "ABC Corp.",
        "date": "May 2019 - August 2019",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed suscipit metus sed ligula tincidunt, eu blandit turpis faucibus. Praesent in sagittis metus. Aliquam erat volutpat."
    }
]
skills = ["Python", "JavaScript", "HTML/CSS", "SQL"]

# Load the Jinja template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('cv_template2.html')

# Render the template with the variables
output = template.render(name=name, email=email, phone=phone, education=education, experience=experience, skills=skills)

# Print the output
print(output)
