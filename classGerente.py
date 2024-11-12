from classEmpleado import Empleado
from classEmpleado import Persona

class Gerente(Empleado):
    def __init__(self):
        super().__init__()
        self._nombre = ""
        self._apellido = ""
        self._edad = 0
        self._especializacion= ""
        self._equipo_a_cargo = ""
        self._habilidades_liderazgo = ""

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

    def get_especializacion(self):
        return self._especializacion

    def set_especializacion(self, especializacion):
        self._especializacion = especializacion

    def get_equipo_a_cargo(self):
        return self._equipo_a_cargo

    def set_equipo_a_cargo(self, equipo_a_cargo):
        self._equipo_a_cargo = equipo_a_cargo

    def get_habilidades_liderazgo(self):
        return self._habilidades_liderazgo

    def set_habilidades_liderazgo(self, habilidades_liderazgo):
        self._habilidades_liderazgo = habilidades_liderazgo

    def mostrarNombre(self):
        return f"Nombre: {self._nombre}"

    def mostrarApellido(self):
        return f"Apellido: {self._apellido}"

    def mostrarEdad(self):
        return f"Edad: {self._edad}"

    def mostrarinformacionEspecializacion(self):
        return f"La especializacion del Gerente es {self._especializacion}"

    def mostrarEquipoACargo(self, equipo_a_cargo):
        return f"El equipo del Gerente es {self._equipo_a_cargo}"

    def mostrarInformacionHabilidadesLiderazgo(self):
        return f"Las habilidades de liderazgo del Gerente son {self._habilidades_liderazgo}"
