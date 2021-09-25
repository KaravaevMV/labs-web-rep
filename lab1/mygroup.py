group_mates = [
    {
        "first name": "Антон",
        "second name": "Кузнецов",
        "exams": ["Теория графов", "Веб программирование", "Теория чисел"],
        "marks": [5, 5, 5]
    },
    {
        "first name": "Михаил",
        "second name": "Радченко",
        "exams": ["ИВТ", "Матанализ", "Теория графов"],
        "marks": [3, 5, 3]
    },
    {
        "first name": "Григорий",
        "second name": "Герасимчук",
        "exams": ["Статистика", "Метафизика", "Веб програмирование"],
        "marks": [2, 3, 2]
    }
]


def mean(values: list):
    """Функция возвращает среднее арифмитическое списка значений."""
    return sum(values) / len(values)


def mark_filter(students_data: list, filt_avrg_mark):
    """
    Функция для фильтрации студентов по среднему баллу.
    Необходимо ввести средний балл, по которому будет проводиться
    фильтрация.
    """
    filtered_students = []

    for student_data in students_data:
        if mean(student_data["marks"]) > filt_avrg_mark:
            filtered_students.append(student_data["first name"] + " " + student_data["second name"])

    if filtered_students:
        print("Список студентов удовлетворяющих условию:")
        for student in filtered_students:
            print(student)
    else:
        print("Ни один студент не удовлетворяет условиям фильтрации")


if __name__ == "__main__":
    filt_avrg_mark = float(input("Введите средний балл по которому будет проводиться фильтрация: "))
    mark_filter(group_mates, filt_avrg_mark)
