import random

# to operate manual file handling 
print("Hello, welcome to the file handling system")

while True:
    user_activity = int(input("""What operation do you want to perform?\
                                1. Create a file
                                2. Read a file
                                3. Write to a file
                                4. Append to a file
                                5. Changing a Word
                                6. Quit \n >>> """))    


    if user_activity == 1:
        # To create a file
        file_name = str(input("What is the name of the file you want to create: \n"))
        file = open(f"{file_name}", "a")
        print("File created successfully")
        file.close()
    elif user_activity == 2:
        # To read the file 
        file_name = str(input("What is the name of the file you want to open? \n"))
        file = None
        try:
            file = open(f"{file_name}", "r")
            print(f'Your file says >>> "{file.read()}"')
        except FileNotFoundError:
            print("The file you want to read doesn't exist! ")
        finally:
            if file is not None:
                file.close()
    elif user_activity == 3:
        # To write to the file
        file_name = str(input("What is the name of the file you want to write to? \n"))
        file = None
        try:
            file = open(f"{file_name}", "w")
            user_input = input("Enter text to write to the file: ")
            file.write(user_input)
            print("Operation complete! ")
            file.close()
        except FileNotFoundError:
            print("The file you want to write to doesn't exist! ")
        finally:
            if file is not None:
                file.close()
    elif user_activity == 4:
        # To open and append to the file
        file_name = str(input("What is the name of the file you want to append to? \n"))
        file = None
        try:
            file = open(f"{file_name}", "a")
            user_input = input("Enter text to append to the file: ")
            file.write(user_input)
            print("Operation complete")
            file.close()
        except FileNotFoundError:
            print("The file you want to append doesn't exist! ")
        finally:
            if file is not None:
                file.close()
    elif user_activity == 5:
        # to change words in the file 
        file_name = str(input("What is the name of the file you want to modify? \n"))
        file = None
        try:
            with open(f"{file_name}", "a"):
                content = file.read()
                word_to_be_replaced = input("Enter the word that you want to replace: ")
                replacement_word = input("Enter the replacement word: ")
                new_content = content.replace(word_to_be_replaced, replacement_word)
                with open(f"{file_name}", "w") as file:
                    file.write(new_content)
                print("Word replacement complete")
        except FileNotFoundError:
            print("The file you want to modify doesn't exist! ")
    elif user_activity == 6:
        break
    else:
        print("Invalid input! Please choose a valid operation")




