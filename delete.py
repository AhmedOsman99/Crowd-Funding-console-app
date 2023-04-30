import json


def delete_project(email):
    # Load the existing data from the JSON file
    with open("projects.json", "r") as projectsFile:
        data = json.load(projectsFile)

    # Check if the email exists in the data
    if email not in data:
        print(2*"=====================")
        print("Email does not have any ptojects to delete yet")
        print(2*"=====================")
        return

    # get list of projects for the email
    print(f"projects list for the email{email}")
    projects = data[email]

    # Display a list of projects to the user to select which project to delete
    print("Select project you want delete :")
    print(2*"=====================")
    for i in range(len(projects)):
        print(str(i+1) + ". " + projects[i]["title"])
    print(2*"=====================")
    while True:
        try:
            selectedProject = input("Enter project number: ")
            selectedProject = int(selectedProject)
            if selectedProject < 1 or selectedProject > len(projects):
                raise ValueError
            break
        except ValueError:
            print(2*"=====================")
            print("Invalid project number")
            print(2*"=====================")

    # delete the project
    del projects[selectedProject-1]
    with open("projects.json", "w") as projectsFile:
        json.dump(data, projectsFile)
        projectsFile.close()
    print("Project deleted.")
