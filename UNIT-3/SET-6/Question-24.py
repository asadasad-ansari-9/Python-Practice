# Organise a program using functions to:
# Accept student name and marks
# Calculate total
# Calculate average
# Determine grade
# Display result

# Condition: main() should control the complete program, while each individual task
# should be performed by a separate function.

def get_marks():
    list = []
    for i in range(1,6):
        list.append(int(input(f"Enter {i} Subject marks :")))
    return list

def count_total(marks):
    return sum(marks)

def Grade(num):
    if num<=100 and num>=90:
        return "A+"
    elif num<90 and num>=80:
        return "A"
    elif num<80 and num>=70:
        return "B+"
    elif num<70 and num>=60:
        return "B"
    elif num<60 and num>=50:
        return "C+"
    elif num<50 and num>=40:
        return "C"
    else:
        return "Fail"
def main():
    name = input("Enter your name: ")
    print("Enter your five subject marks.")
    marks = get_marks()
    print(f"Hello {name}!")
    print(f"You got {count_total(marks)}/500 marks.")
    print(f"Your average is {count_total(marks)/5}")
    print(f"Your grade :{Grade(count_total(marks)/5)}")
main()