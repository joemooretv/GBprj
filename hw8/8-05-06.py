"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП. """


class EquipmentStore:
    size_cube_m: float
    _items_list: list

    def __init__(self, size_cube_m: float):
        self._items_list = []
        self.size_cube_m = size_cube_m

    def receive_in_store(self, equipment: object):
        if not isinstance(equipment, OfficeEquipment):
            raise TypeError('Object must be \'OfficeEquipment\' class element')
        volume = self.size_cube_m - equipment.dimensions_cube_m
        if volume <= 0:
            raise NotEnoughStorage(equipment.name)
        equipment.current_store = self.__hash__()
        self._items_list.append(equipment)
        self.size_cube_m = volume

    def relocate(self, equipment: object, store: object):
        if not isinstance(store, EquipmentStore):
            raise TypeError('Object must be \'EquipmentStore\' class element')
        elif not isinstance(equipment, OfficeEquipment):
            raise TypeError('Object must be \'OfficeEquipment\' class element')
        elif self.__hash__() == store.__hash__():
            raise TypeError('Can\'t relocate equipment inside one store')
        elif equipment not in self._items_list:
            raise TypeError(f'There\'s no {equipment.name} in this store')
        else:
            self._items_list.remove(equipment)
            self.size_cube_m = self.size_cube_m + equipment.dimensions_cube_m
            store.receive_in_store(equipment)

    def show_equipment(self):
        res = ''
        for eq in self._items_list:
            res = res + f'{self._items_list.index(eq) + 1}. {eq.name} ({eq.__class__.__name__})\n'
        return res

    def show_quantity(self):
        return len(self._items_list)


class OfficeEquipment:
    name: str
    dimensions_cube_m: float
    current_store: int

    def __init__(self, name: str, dimensions_cube_m: float):
        self.name = name
        self.dimensions_cube_m = dimensions_cube_m


class Printer(OfficeEquipment):
    is_xerox: float
    is_scanner: float
    ink_on_pages_rate: int

    def __init__(self, name: str, dimensions_cube_m: float, ink_on_pages_rate: int,
                 is_xerox: float = False, is_scanner: float = False):
        super().__init__(name, dimensions_cube_m)
        self.is_xerox = is_xerox
        self.is_scanner = is_scanner
        self.ink_on_pages_rate = ink_on_pages_rate


class Shredder(OfficeEquipment):
    speed_pages_per_min: float
    container_size_liters: float

    def __init__(self, name: str, dimensions_cube_m: float, speed_pages_per_min: float,
                 container_size_liters: float):
        super().__init__(name, dimensions_cube_m)
        self.speed_pages_per_min = speed_pages_per_min
        self.container_size_liters = container_size_liters


class DocumentBox(OfficeEquipment):
    pass


class NotEnoughStorage(Exception):

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'Not enough storage for {self.name}'


item1 = Printer('Sony', 06.68, 5768)
item2 = Shredder('Konix', 04.75, 245, 4.1)
item3 = DocumentBox('Noname', 16.68)

store1 = EquipmentStore(29.64)
store2 = EquipmentStore(18.7)

store1.receive_in_store(item1)
store1.receive_in_store(item2)
store1.receive_in_store(item3)
store1.relocate(item3, store2)

print(f'Store1 contains {store1.show_quantity()} items:\n{store1.show_equipment()}')
print(f'Store2 contains {store2.show_quantity()} items:\n{store2.show_equipment()}\n')
