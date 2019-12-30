from Entities.GroupData import Group


class GroupContext:
    __group: Group
    __revision: int
    
    @property
    def read(self):
        return self.__group

    def edit(self):
        self.__revision += 1
        return self.__group
      
    def __init__(self, group: Group):
        self.__group = group
    
    def save(self):
      if self.__revision >= 1:
        self.__revision = 0
        # todo: save entity in GroupManager
