import json


def donate_to_project(email):
    # Load the existing data from the JSON file
    with open("projects.json", "r") as projectsFile:
        data = json.load(projectsFile)

    # Display a list of all projects in the JSON file
    allProjects = []
    for userEmail in data:
        allProjects.extend(data[userEmail])

    print("Select project to donate to")
    print(2*"=====================")
    for i in range(len(allProjects)):
        print(str(i+1) + ". " + allProjects[i]["title"])
    print(2*"=====================")

    try:
        selectedProject = input("Enter project number: ")
        selectedProject = int(selectedProject)
        if selectedProject < 1 or selectedProject > len(allProjects):
            raise ValueError
    except ValueError:
        print(2*"=====================")
        print("Invalid project number")
        print(2*"=====================")
        return

    # Get the selected project
    project = allProjects[selectedProject-1]

    amount = input("Enter donation amount: ")
    try:
        amount = float(amount)
    except ValueError:
        print(2*"=====================")
        print("Invalid donation amount")
        print(2*"=====================")
        return

    # Add the donation to the project's donations list
    if "donations" not in project:
        project["donations"] = []
    project["donations"].append({
        "email": email,
        "amount": amount
    })

    # Write the updated data back to the JSON file
    with open("projects.json", "w") as projectsFile:
        json.dump(data, projectsFile)
