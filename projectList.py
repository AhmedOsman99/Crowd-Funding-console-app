from create import create
from edit import edit_project
from delete import delete_project
from view_projects import view_all_projects, search_projects_by_date


def projectList(email):
    while True:
        print(2*"=====================")
        print("1. Create project")
        print("2. View all projects")
        print("3. Edit project")
        print("4. Delete project")
        print("5. Search project by date (bonus)")
        print("6. Exit")
        print(2*"=====================")

        choice = input("Enter your choice: ")
        if choice == "1":
            create(email)

        elif choice == "2":
            view_all_projects(email)
        elif choice == "3":
            edit_project(email)
        elif choice == "4":
            delete_project(email)
        elif choice == "5":
            search_projects_by_date()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
            print(2*"=====================")
