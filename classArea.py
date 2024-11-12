from classDepartamento import Departamento

class Area(Departamento):
    def __init__(self):
        super().__init__()
        self._nombre = ""
        self._tipo = ""
        self._numero_de_empleados = ""

    # Getter y Setter
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo

    def get_numero_de_empleados(self):
        return self._numero_de_empleados

    def set_numero_de_empleados(self, numero_de_empleados):
        self._numero_de_empleados = numero_de_empleados

    def mostrarinformacionArea(self):
        return f"nombre {self._nombre}, tipo {self._tipo}, numero de empleados {self._numero_de_empleados}"
