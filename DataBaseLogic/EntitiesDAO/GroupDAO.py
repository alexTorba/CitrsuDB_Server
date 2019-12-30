
from DataBaseLogic.EntitiesDAO.EntityDAO import EntityDAO
from Entities.EntityType import EntityType


class GroupDAO(EntityDAO):

    @property
    def entity_type(self) -> EntityType:
        return EntityType.group

    def __init__(self, cursor):
        super().__init__(cursor)
