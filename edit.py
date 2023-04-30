import json
from create import validate_date, validate_project_target, validate_project_title


def edit_project(email):
    # Load the existing data from the JSON file
    with open("projects.json", "r") as projectsFile:
        data = json.load(projectsFile)

    # Check if the email exists in the data
    if email not in data:
        print(2*"=====================")
        print("Email does not have any ptojects to edit yet")
        print(2*"=====================")
        return

    # Get the list of projects for the email
    print(f"projects list for the email {email}")

    projects = data[email]
    # Display a list of projects to the user to select which project to edit
    print("Select project to edit")
    print(2*"=====================")
    for i in range(len(projects)):
        print(str(i+1) + ". " + projects[i]["title"])
    print(2*"=====================")

    try:
        selectedProject = input("Enter project number: ")
        selectedProject = int(selectedProject)
        if selectedProject < 1 or selectedProject > len(projects):
            raise ValueError
    except ValueError:
        print(2*"=====================")
        print("Invalid project number")
        print(2*"=====================")
        return

    # Get the project to edit
    project = projects[selectedProject-1]

    while True:
        print(2*"=====================")
        print(f"Editing project {project['title']}")
        print("Choose the field you want to edit")
        print("1. Title")
        print("2. Details")
        print("3. Target")
        print("4. Start Date")
        print("5. End Date")
        print("6. Exit")
        print(2*"=====================")

        selectedField = input("Enter field number: ")
        print(2*"=====================")
        if selectedField == "1":
            newTitle = input("Enter new title: ")
            newTitle = validate_project_title(newTitle)
            project["title"] = newTitle

        elif selectedField == "2":
            newDetails = input("Enter new details: ")
            project["details"] = newDetails

        elif selectedField == "3":
            newTarget = input("Enter new target: ")
            newTarget = validate_project_target(newTarget)

            project["target"] = newTarget

        elif selectedField == "4":
            newStartDate = input("Enter new start date: ")
            newStartDate = validate_date(newStartDate, status="start")
            project["startdate"] = newStartDate

        elif selectedField == "5":
            newEndDate = input("Enter new end date: ")
            newEndDate = validate_date(newEndDate, status="End")
            project["enddate"] = newEndDate

        elif selectedField == "6":
            break

        else:
            print("Invalid choice. Please try again.")
            print(2*"=====================")

        # Write the updated data back to the JSON file
        with open("projects.json", "w") as projectsFile:
            json.dump(data, projectsFile)

        projectsFile.close()
