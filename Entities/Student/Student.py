from Common.IJsonFormatable import IJsonFormatable


class Student(IJsonFormatable):
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

    def to_json(self) -> dict:
        dict_view = {"i": self.Id,
                     "f": self.FirstName,
                     "l": self.LastName,
                     "m": self.MiddleName,
                     "d": self.DateOfBirth,
                     "h": self.Height,
                     "w": self.Weight,
                     "c": self.Citizenship,
                     "k": self.KnowledgeOfLanguage,
                     }

        if hasattr(self, "FirstPhoto"):
            dict_view["fp"] = self.FirstPhoto
        if hasattr(self, "SecondPhoto"):
            dict_view["sp"] = self.SecondPhoto
        if hasattr(self, "GroupId"):
            dict_view["gi"] = self.GroupId

        return dict_view

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
