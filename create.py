import json
import datetime

# Load the existing data from the JSON file
with open("projects.json", "r") as file:
    data = json.load(file)


def validate_project_title(project_title):
    while True:
        # Get a list of all project titles in the data
        all_titles = [project["title"]
                      for email_data in data.values() for project in email_data]

        # Check if there is already a project with the same title
        if project_title in all_titles:
            print(2*"=====================")
            print(
                "A project with the same title already exists.\nPlease enter a unique title.")
            print(2*"=====================")
            project_title = input("Enter project title: ")

        else:
            break
    return project_title

# Define a function to validate the project target


def validate_project_target(project_target):
    while True:
        try:
            if project_target.isdigit():
                project_target = int(project_target)
                break
            else:
                raise ValueError
        except ValueError:
            print(2*"=====================")
            print("Invalid input. Please enter an integer value.")
            print(2*"=====================")
            project_target = input(
                "Enter project target (must be an integer):")
    return project_target

# Define a function to validate a given date in the format 'YYYY-MM-DD'


def validate_date(newDate, status):
    while True:
        try:
            datetime.datetime.strptime(newDate, '%Y-%m-%d')
            break
        except ValueError:
            print(2*"=====================")
            print("Invalid input ..")
            print(2*"=====================")

            # Prompt the user to enter a valid date in the correct format
            newDate = input(f"Please enter a valid date({status}) 2022-7-25: ")
    return newDate


# Define the main function that creates a new project for a given user
def create(email):
    print(2*"=====================")
    # Prompt the user to enter details for the new project
    project_title = input("Enter project title: ")
    project_title = validate_project_title(project_title)

    project_details = input("Enter project details: ")

    project_target = input("Enter project target (must be an integer): ")
    project_target = validate_project_target(project_target)

    # Validate the project start date using the validate_date function
    project_startdate = input("Enter project start date: ")
    project_startdate = validate_date(project_startdate, status="start")

    # Validate the project end time using the validate_date function
    project_enddate = input("Enter project end date: ")
    project_enddate = validate_date(project_enddate, status="end")
    print(2*"=====================")
    print("Your project has been created successfully")

    # Add the new data to the existing data
    if email not in data:
        data[email] = []
    data[email].append({
        "title": project_title,
        "details": project_details,
        "target": project_target,
        "startdate": project_startdate,
        "enddate": project_enddate
    })

    # Write the updated data back to the JSON file
    with open("projects.json", "w") as file:
        json.dump(data, file)
    file.close()


file.close()
