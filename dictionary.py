def main():
    #create a dictionary with student IDs as
    #the keys and student names as the values.

    student_dict = {
        "42-039-436": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis"
    }

    #adding an itme to the dictionary.
    student_dict["81-298-9238"] = "Sama Patel"

    #REMOVING an item from the dictionary
    student_dict.pop("61-315-0160")

    #get the number of items in the dictionary.
    length = len(student_dict)
    print(f"length: {length}")

    #print entire dictionary
    print(student_dict)
    print()

    id = input("Enter a student ID:")

    if id in student_dict:
        name = student_dict[id]

        print(name)

    else:
        print("No such student")


if __name__ == "__main__":
    main()