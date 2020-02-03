from Common.Entity.BaseEntity import BaseEntity
from Entities.EntityType import EntityType
from Entities.Student.StudentData import StudentData


class Student(BaseEntity[StudentData]):
    entity_type: EntityType = EntityType.student

    def __init__(self, entity_id: int = None, data: StudentData = None) -> None:
        super().__init__(entity_id, data)

    @staticmethod
    def get_test_student():
        student_data: StudentData = StudentData.get_test_student_data()
        student = Student(student_data.Id, student_data)
        return student
