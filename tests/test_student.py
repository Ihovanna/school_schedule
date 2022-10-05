from school_schedule.student import Student

def test_new_student():
    # arrange
    name = "Aminah"
    grade = "Freshman"
    classes = ["Chemistry", "Algebra", "Cooking", "Paint", "Poetry"]

    # act
    aminah = Student(name, grade, classes)

    # assert
    assert aminah.name == name
    assert aminah.grade == grade
    assert amina.classes= classes
    assert len(aminah.classes) == 5

    