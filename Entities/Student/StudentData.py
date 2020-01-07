from Common.JsonLogic.JsonContract import JsonContract


class StudentData(JsonContract):
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

    @property
    def _json_fields(self) -> dict:
        return {
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
    def get_test_student_data() -> "StudentData":
        student_data = StudentData()
        student_data.Id = 1
        student_data.FirstName = "Alex"
        student_data.LastName = "Torba"
        student_data.MiddleName = "Olegovich"
        student_data.DateOfBirth = "29.04.1998"
        student_data.Height = 180
        student_data.Weight = 68
        student_data.Citizenship = "Ukraine"
        student_data.KnowledgeOfLanguage = "Russian, Ukraine, English"
        student_data.GroupId = 1

        return student_data
