
def main():
    real_points_sum = 0
    all_grades = []
    while True:
        student_input = input("Exam points and exercises completed: ")
        
        if student_input == "":
            break
        
        try:
            first_grade, second_grade = map(int, student_input.split())
        except ValueError:
            print("Input must be in the format '12 34'. Try again.")
            continue
        
        real_points_sum += first_grade + convert_exercise_to_points(second_grade)  
        final_grade = calculate_final_grade(first_grade, second_grade)
        all_grades.append(final_grade)

    average_points_to_print = real_points_sum / len(all_grades)

    passed_grades_list = [grade for grade in all_grades if grade >= 1]
    pass_percentage = (len(passed_grades_list) / len(all_grades)) * 100
    print("Statistics:")
    print(f"Points average: {average_points_to_print:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    
    grade_distribution(all_grades)
    
    

def grade_distribution(all_grades_list: list):

    five_counter = 0
    four_counter = 0
    three_counter = 0
    two_counter = 0
    one_counter = 0
    zero_counter = 0
    for grade in all_grades_list:
        if grade == 5:
            five_counter += 1
        elif grade == 4:
            four_counter += 1
        elif grade == 3:
            three_counter += 1
        elif grade == 2:
            two_counter += 1
        elif grade == 1:
            one_counter += 1
        else:
            zero_counter += 1

    print("Grade distribution: ")
    print(f"5: {'*' * five_counter}")
    print(f"4: {'*' * four_counter}")
    print(f"3: {'*' * three_counter}")
    print(f"2: {'*' * two_counter}")
    print(f"1: {'*' * one_counter}")
    print(f"0: {'*' * zero_counter}")
    


def calculate_final_grade(first_number: int, second_number: int) -> int:
    grade = first_number + convert_exercise_to_points(second_number)
    
    if first_number < 10:
        final_grade = 0        
    elif grade >= 0 and grade < 15:
        final_grade = 0
    elif grade >= 15 and grade < 18:
        final_grade = 1
    elif grade >= 18 and grade < 21:
        final_grade = 2
    elif grade >= 21 and grade < 24:
        final_grade = 3
    elif grade >= 24 and grade < 28:
        final_grade = 4
    else:
        final_grade = 5

    return final_grade



def convert_exercise_to_points(second_number: int) -> int:
    return second_number // 10
    
    
    

main()