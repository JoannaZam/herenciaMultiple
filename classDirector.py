from classEmpleado import Empleado


class Director(Empleado):
    def __init__(self):
        super().__init__()
        self._nombre = ""
        self._apellido = ""
        self._edad = 0
        self._region = ""
        self._sueldo = ""
        self._departamento_asigado= ""
        self._tiempo_de_experiencia = ""
        self._historico_logros = ""

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

    def get_region(self):
        return self._region

    def set_region(self, region):
        self._region = region

    def get_sueldo(self):
        return self._sueldo

    def set_sueldo(self, sueldo):
        self._sueldo = sueldo

    def get_departamento_asigado(self):
        return self._departamento_asigado

    def set_departamento_asigado(self, departamento_asigado):
        self._departamento_asigado = departamento_asigado

    def get_tiempo_de_experiencia(self):
        return self._tiempo_de_experiencia

    def set_tiempo_de_experiencia(self, tiempo_de_experiencia):
        self._tiempo_de_experiencia = tiempo_de_experiencia

    def get_historico_logros(self):
        return self._historico_logros

    def set_historico_logros(self, historico_logros):
        self._historico_logros = historico_logros

    def mostrarNombre(self):
        return f"Nombre: {self._nombre}"

    def mostrarApellido(self):
        return f"Apellido: {self._apellido}"

    def mostrarEdad(self):
        return f"Edad: {self._edad}"

    def mostrarinformacionRegion(self):
        return f"La Región del Director es {self._region}"

    def mostrarSueldoDirector(self):
        return f"El sueldo del Director es {self._sueldo}"

    def mostrarDepartamentoAsignado(self):
        return f"El departamento del Director es {self._region}"

    def mostrarTiempoDeExperiencia(self):
        return f"El tiempo de experiencia del Director es {self._tiempo_de_experiencia}"

    def mostrarHistoricoLogros(self):
        return f"Su historico de logros es {self._historico_logros}"
