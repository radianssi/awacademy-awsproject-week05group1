from functions import insert_data, push_data_to_database

def main():
    print("Welcome to Time Managament Tool!")
    print("This tool allows you to insert data into the Time Managament database.")

    while True:
        run_functions = input("Do you wanto to add worked hours?(Y/N): ")
        if run_functions == "y" or "Y":
            data = insert_data()    
            push_data_to_database(data[0], data[1])
        elif run_functions == "n" or "N":
            print("Thank you for using Time Managament app!")
            break
        else:
            run_functions = input("Please select correct option: ")

if __name__ == "__main__":
    main()