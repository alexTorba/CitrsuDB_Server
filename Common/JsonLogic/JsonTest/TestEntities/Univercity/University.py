from Common.Entity.BaseEntity import BaseEntity
from Common.JsonLogic.JsonTest.TestEntities.Univercity.UniversityData import UniversityData
from Entities.EntityType import EntityType


class University(BaseEntity[UniversityData]):

    @property
    def entity_type(self):
        return EntityType.university

    @staticmethod
    def get_test_university():
        university: University = University()
        u_data = UniversityData()
        u_data.name = "ХНУРЭ"
        u_data.some_list = [1, 2, 3, 4, 5]
        university.data = u_data
        return university
