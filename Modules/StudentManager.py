from Common.JsonFormatter.JsonContract import JsonContract
from Common.JsonFormatter.JsonFormatter import JsonFormatter
from Entities.EntityType import EntityType
from Entities.Student.Student import Student
from Modules.CacheItemManager import CacheItemManager


class StudentManager:
    class StudentDto(JsonContract):
        student: Student

        @property
        def _json_fields(self) -> dict:
            return {
                "s": "student"
            }

    @staticmethod
    def create_student(dto: StudentDto):
        student = dto.student
        # todo: validate student
        s_json = JsonFormatter.serialize(student)
        CacheItemManager.add(EntityType.student, s_json)

    @staticmethod
    def delete_student(dto: StudentDto):
        student = dto.student
        CacheItemManager.remove(EntityType.student, student.id)

    @staticmethod
    def update_student(dto: StudentDto):
        cx = CacheItemManager.get(EntityType.student, dto.student.id)
        cx.edit().data = dto.student.data
        cx.save()
