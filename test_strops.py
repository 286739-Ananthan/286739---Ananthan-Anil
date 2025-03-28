# ***************************************************************************************************************************************************
#  *Author           : Ananthan.A - 286739
#  *File             : setup.py
#  *Title            : Python String Operations Module Development
#  *Description      : Interactive test file
#  ****************************************************************************************************************************************************

import strops

# Function to print a header
def print_header():
    print("-" * 100)
    print("Welcome to the Interactive String Operations Test!")
    print("-" * 100)

# Function to print a footer
def print_footer():
    print("-" * 100)

def interactive_test():
    print_header()

    print("You can test the following functions:")
    print("1. getspan(s, ss) – Returns the start and end index of substring ss in string s.")
    print("2. reverseWords(s) – Reverses the order of words in s.")
    print("3. removePunctuation(s) – Removes all punctuation from s.")
    print("4. countWords(s) – Counts the number of words in s.")
    print("5. characterMap(s) – Returns a dictionary with characters and their frequencies.")
    print("6. makeTitle(s) – Converts s to title case.")
    print("7. normalizeSpaces(s) – Removes extra spaces, leaving only single spaces between words.")
    print("8. transform(s) – Reverses the string and swaps case.")
    print("9. getPermutations(s) – Returns all permutations of the string s.")
    print("To exit, type 'exit' at any prompt.")
    print("-" * 100)

    while True:
        print("\nEnter a string to work with, or type 'exit' to quit:")
        s = input("> ")

        if s.lower() == 'exit':
            print("Goodbye!")
            break

        print("\nSelect a function to test:")
        print("1. getspan(s, ss)")
        print("2. reverseWords(s)")
        print("3. removePunctuation(s)")
        print("4. countWords(s)")
        print("5. characterMap(s)")
        print("6. makeTitle(s)")
        print("7. normalizeSpaces(s)")
        print("8. transform(s)")
        print("9. getPermutations(s)")
        print("-" * 100)

        choice = input("> ")
        print("-" * 100)

        if choice == "1":
            print("Enter the substring to find:")
            ss = input("> ")
            print(f"Span of '{ss}' in '{s}':", strops.getspan(s, ss))
        
        elif choice == "2":
            print("Reversed words in string:", strops.reverseWords(s))
        
        elif choice == "3":
            print("String without punctuation:", strops.removePunctuation(s))
        
        elif choice == "4":
            print("Word count:", strops.countWords(s))
        
        elif choice == "5":
            print("Character map:", strops.characterMap(s))
        
        elif choice == "6":
            print("Title case string:", strops.makeTitle(s))
        
        elif choice == "7":
            print("Normalized spaces string:", strops.normalizeSpaces(s))
        
        elif choice == "8":
            print("Transformed string:", strops.transform(s))
        
        elif choice == "9":
            print("Permutations of the string:", strops.getPermutations(s))
        
        else:
            print("Invalid choice. Please select a valid option.")
        print("-" * 100)

    print_footer()

# Run the interactive test if the script is executed directly
if __name__ == "__main__":
    interactive_test()
