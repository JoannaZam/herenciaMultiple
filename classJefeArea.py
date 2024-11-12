from classEmpleado import Empleado
from classEmpleado import Persona

class JefeArea(Empleado):
    def __init__(self):
        super().__init__()
        self._nombre = ""
        self._apellido = ""
        self._edad = 0
        self._turno= ""
        self._proyectos = ""
        self._contacto_emergencia = ""

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

    def get_turno(self):
        return self._turno

    def set_turno(self, turno):
        self._turno = turno

    def get_proyectos(self):
        return self._proyectos

    def set_proyectos(self, proyectos):
        self._proyectos = proyectos

    def get_contacto_emergencia(self):
        return self._contacto_emergencia

    def set_contacto_emergencia(self, contacto_emergencia):
        self._contacto_emergencia = contacto_emergencia

    def mostrarNombre(self):
        return f"Nombre: {self._nombre}"

    def mostrarApellido(self):
        return f"Apellido: {self._apellido}"

    def mostrarEdad(self):
        return f"Edad: {self._edad}"

    def mostrarinformacionTurno(self):
        return f"El turno del Jefe de area es {self._turno}"

    def mostrarinformacionProyectos(self):
        return f"Los proyectos del Jefe son {self._proyectos}"

    def mostrarinformacionContactoEmergencia(self):
        return f"El contacto de emergecia del Jefe es {self._contacto_emergencia}"
