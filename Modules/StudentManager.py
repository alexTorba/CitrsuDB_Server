from Common.JsonLogic.JsonFormatter import JsonFormatter
from Common.NetworkLogic.Request.RequestDto import RequestDto
from Common.NetworkLogic.Responce.BaseResponceDto import BaseResponceDto
from Entities.EntityType import EntityType
from Entities.Student.Student import Student
from Modules.CacheItemManager import CacheItemManager


class StudentManager:
    class StudentDto(RequestDto[Student]):
        pass

    @staticmethod
    def create_student(dto: StudentDto) -> BaseResponceDto:
        student = dto.data
        # todo: validate student
        s_json = JsonFormatter.serialize(student)
        CacheItemManager.add(EntityType.student, s_json)
        return BaseResponceDto(200)

    @staticmethod
    def delete_student(dto: StudentDto):
        student = dto.data
        CacheItemManager.remove(EntityType.student, student.id)

    @staticmethod
    def update_student(dto: StudentDto):
        # cx = CacheItemManager.get(EntityType.student, dto.student.id)
        # cx.edit().data = dto.student.data
        # cx.save()
        pass

    @staticmethod
    def init(handlers: dict):
        handlers["CreateStudent"] = (StudentManager.StudentDto, StudentManager.create_student)
