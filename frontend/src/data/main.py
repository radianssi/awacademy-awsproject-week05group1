from functions import insert_data, push_data_to_database

def main():
    print("Welcome to Time Managament Tool!")
    print("This tool allows you to insert data into the Time Managament database.")

    while True:
        run_functions = input("Do you wanto to add worked hours?(Y/N): ")
        if run_functions.lower() == "y":
            data = insert_data()    
            push_data_to_database(data[0], data[1], data[2], data[3])
        elif run_functions.lower() == "n":
            print("Thank you for using Time Managament app!")
            break
        else:
            print("Please select correct option")

if __name__ == "__main__":
    main()