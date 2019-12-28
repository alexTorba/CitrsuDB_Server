from Common.JsonContract import JsonContract


class Student(JsonContract):
    Id: int
    FirstName: str
    LastName: str
    MiddleName: str
    DateOfBirth: str
    Height: float
    Weight: float
    Citizenship: str
    KnowledgeOfLanguage: str
    FirstPhoto: bytearray
    SecondPhoto: bytearray
    GroupId: int

    _json_field = {
        "i": "Id",
        "f": "FirstName",
        "l": "LastName",
        "m": "MiddleName",
        "d": "DateOfBirth",
        "h": "Height",
        "w": "Weight",
        "c": "Citizenship",
        "k": "KnowledgeOfLanguage",
        "fp": "FirstPhoto",
        "sp": "SecondPhoto",
        "gi": "GroupId"
    }

    @staticmethod
    def get_test_student():
        student = Student()
        student.Id = 1
        student.FirstName = "Alex"
        student.LastName = "Torba"
        student.MiddleName = "Olegovich"
        student.DateOfBirth = "29.04.1998"
        student.Height = 180
        student.Weight = 68
        student.Citizenship = "Ukraine"
        student.KnowledgeOfLanguage = "Russian, Ukraine, English"
        student.GroupId = 1

        return student
