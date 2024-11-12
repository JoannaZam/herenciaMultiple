class Departamento:
    def __init__(self):
        self.nombre = ""
        self.ID = ""
        self.areas = ""

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_ID(self):
        return self.ID

    def set_ID(self, ID):
        self.ID = ID

    def get_areas(self):
        return self.areas

    def set_areas(self, areas):
        self.areas = areas

    def mostrarinformacionDepartamento(self):
        return f"nombre: {self.nombre}, ID: {self.ID}, areas: {self.areas}"
