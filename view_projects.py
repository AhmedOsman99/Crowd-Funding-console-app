import json
from create import validate_date


# open the JSON file and load the data into a dictionary

# function to search projects by date
def search_projects_by_date():
    with open('projects.json', 'r') as file:
        data = json.load(file)
    print("Search by date")
    print(2*"=====================")

    search_date = input("Enter date you want to search by: ")
    print(2*"=====================")
    validate_date(search_date, status="start")

    # create a list of all start dates from the data
    all_startdates = [project["startdate"]
                      for email_data in data.values() for project in email_data]

    # check if the search date is in the list of start dates
    if search_date in all_startdates:
        # loop through the data and print any projects with a start date matching the search date
        for ema_data in data.values():
            for each_project in ema_data:
                if each_project["startdate"] == search_date:
                    print(each_project)
                    print(2*"=====================")
        file.close()

    else:
        print("There is no projects starts on this date")
        print(2*"=====================")
        file.close()


def view_all_projects(email):
    with open('projects.json', 'r') as file:
        data = json.load(file)
    # function to view all projects for a specific email

    def view_user_data(email):
        projects = data[email]
        print(projects)

    # function to view all projects for all emails

    def view_all_data(email):
        all_projects = [email_data for email_data in data.values()]
        print(all_projects)

    # check if the email exists in the data
    if email not in data:
        print("This user does not have any projects to view")
        print(2*"=====================")
        return

    while True:
        print(2*"=====================")
        print("1. View your projects\n2. View all projects\n3. Search by date\n4. Exit")
        print(2*"=====================")

        command = input("Enter a command number: ")
        print(2*"=====================")
        if command == "1":
            view_user_data(email)
            break
        elif command == "2":
            view_all_data(email)
            break
        elif command == "3":
            search_projects_by_date()
            break
        elif command == "4":
            return
        else:
            print("Invalid command")
            print(2*"=====================")

        file.close()
