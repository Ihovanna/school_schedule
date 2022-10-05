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
    assert aminah.classes == classes
    assert len(aminah.classes) == 5

def test_get_num_classes_adjusts():
        # arrange
    name = "Aminah"
    grade = "Freshman"
    classes = ["Chemistry", "Algebra", "Cooking", "Paint", "Poetry"]

    # act
    aminah = Student(name, grade, classes)
    aminah.add("Gym")

    # assert
    assert aminah.name == name
    assert aminah.grade == grade
    assert aminah.classes == classes
    assert len(aminah.classes) == 6

