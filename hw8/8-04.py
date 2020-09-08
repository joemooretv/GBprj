"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники. """


class EquipmentStore:
    size_cube_m: float
    _items_quantity: int
    _items_list: list

    def __init__(self, size_cube_m: float, items_quantity: int = 0, items_list: list = None):
        if items_list is None:
            items_list = []
        self.size_cube_m = size_cube_m
        self._items_quantity = items_quantity
        self._items_list = items_list


class OfficeEquipment:
    name: str
    quantity: int
    dimensions_cube_m: float

    def __init__(self, name: str, dimensions_cube_m: float, quantity: int = 1):
        self.name = name
        self.dimensions_cube_m = dimensions_cube_m
        self.quantity = quantity


class Printer(OfficeEquipment):
    is_xerox: float
    is_scanner: float
    ink_on_pages_rate: int

    def __init__(self, name: str, dimensions_cube_m: float, ink_on_pages_rate: int,
                 is_xerox: float = False, is_scanner: float = False, quantity: int = 1):
        super().__init__(name, dimensions_cube_m, quantity)
        self.is_xerox = is_xerox
        self.is_scanner = is_scanner
        self.ink_on_pages_rate = ink_on_pages_rate


class Shredder(OfficeEquipment):
    speed_pages_per_min: float
    container_size_liters: float

    def __init__(self, name: str, dimensions_cube_m: float, speed_pages_per_min: float,
                 container_size_liters: float, quantity: int = 1):
        super().__init__(name, dimensions_cube_m, quantity)
        self.speed_pages_per_min = speed_pages_per_min
        self.container_size_liters = container_size_liters


class DocumentBox(OfficeEquipment):
    pass


a = Shredder('Sony', 0.68, 245, 4.1)
print(a.quantity)

b = EquipmentStore(25.64)
print(b._items_quantity)
