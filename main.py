def calculate_average(*grades):
    total_grades = len(grades)
    result = 0
    for grade in grades:
        result += grade
        return result
def calculate_median(*grades):
    grades_list = list(grades)
    grades_list.sort()
    total_grades = len(grades_list)
    if total_grades % 2 != 0:
        first_index_of_middle = (len(grades_list) - 1) / 2
        second_index_of_middle = first_index_of_middle + 1
        first_middle = grades_list[int(first_index_of_middle)]
        second_middle = grades_list[int(second_index_of_middle)]
        return (first_middle + second_middle) // 2


print(calculate_average(85, 90, 78, 92))
print(calculate_average(100, 95))
print(calculate_median(85, 90, 78, 92))