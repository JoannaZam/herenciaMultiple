from classPersona import Persona

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self._nombre = ""
        self._apellido = ""
        self._edad = 0
        self._cargo = ""
        self._sueldo = ""
        self._nomina = ""

    # Getter y Setter

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_apellido(self):
        return self._apellido

    def set_apellido(self, apellido):
        self._apellido = apellido

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    def get_cargo(self):
        return self._cargo

    def set_cargo(self, cargo):
        self._cargo = cargo

    def get_sueldo(self):
        return self._sueldo

    def set_sueldo(self, sueldo):
        self._sueldo = sueldo

    def get_nomina(self):
        return self._nomina

    def set_nomina(self, nomina):
        self._nomina = nomina

    def mostrarinformacionEmpleado(self):
        parentinfo = super().mostrarInformacionPersona()
        return f"{parentinfo}, nombre: {self._nombre}, apellido: {self._apellido}, edad: {self._edad}, cargo: {self._cargo}, sueldo: {self._sueldo}, nomina: {self._nomina}"
