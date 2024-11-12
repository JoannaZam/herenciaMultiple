from classPersona import Persona
from classEmpleado import Empleado
from classDepartamento import Departamento
from classArea import Area
from classDirector import Director
from classGerente import Gerente
from classJefeArea import JefeArea

def main():
    # Crear instancia de Persona
    print("Persona:")
    persona = Persona()
    persona.set_nombre("Juan")
    persona.set_apellido("Pérez")
    persona.set_edad(30)
    print(persona.mostrarInformacionPersona())

    # Crear instancia de Empleado
    print("\nEmpleado:")
    empleado = Empleado()
    empleado.set_nombre("Ana")
    empleado.set_apellido("López")
    empleado.set_edad(28)
    empleado.set_cargo("Desarrolladora")
    empleado.set_sueldo(2500)
    empleado.set_nomina("A1234")
    print(empleado.mostrarinformacionEmpleado())


    # Crear instancia de Departamento
    print("\nDepartamento:")
    departamento = Departamento()
    departamento.set_nombre("TI")
    departamento.set_ID("D001")
    departamento.set_areas("Desarrollo, Soporte")
    print(departamento.mostrarinformacionDepartamento())

    # Crear instancia de Area
    print("\nArea:")
    area = Area()
    area.set_nombre("Desarrollo Web")
    area.set_tipo("Tecnológico")
    area.set_numero_de_empleados(10)
    print(area.mostrarinformacionArea())

    # Crear instancia de Director
    print("\nDirector:")
    director = Director()
    director.set_nombre("Octavio")
    director.set_apellido("Reyes")
    director.set_edad(19)
    director.set_region("Tecnologia")
    director.set_sueldo(8000)
    director.set_departamento_asigado("Departamento de TI")
    director.set_tiempo_de_experiencia(20)
    director.set_historico_logros("Implementación de proyectos exitosos")
    print(director.mostrarinformacionEmpleado())
    print(director.mostrarNombre())
    print(director.mostrarApellido())
    print(director.mostrarEdad())
    print(director.mostrarinformacionRegion())
    print(director.mostrarSueldoDirector())
    print(director.mostrarDepartamentoAsignado())
    print(director.mostrarTiempoDeExperiencia())
    print(director.mostrarHistoricoLogros())

    # Crear instancia de Gerente
    print("\nGerente:")
    gerente = Gerente()
    gerente.set_nombre("Alejandro")
    gerente.set_apellido("Gómez")
    gerente.set_edad(38)
    gerente.set_especializacion("Seguridad Informática")
    gerente.set_equipo_a_cargo("Equipo de Seguridad")
    gerente.set_habilidades_liderazgo("Comunicación, toma de decisiones")
    print(gerente.mostrarinformacionEmpleado())
    print(gerente.mostrarNombre())
    print(gerente.mostrarApellido())
    print(gerente.mostrarEdad())
    print(gerente.mostrarinformacionEspecializacion())
    print(gerente.mostrarEquipoACargo("Equipo A"))
    print(gerente.mostrarInformacionHabilidadesLiderazgo())

    # Crear instancia de JefeArea
    print("\nJefe Area:")
    jefe_area = JefeArea()
    jefe_area.set_nombre("Miguel")
    jefe_area.set_apellido("Sánchez")
    jefe_area.set_edad(40)
    jefe_area.set_turno("Matutino")
    jefe_area.set_proyectos("Desarrollo de plataforma web")
    jefe_area.set_contacto_emergencia("987654321")
    print(jefe_area.mostrarNombre())
    print(jefe_area.mostrarApellido())
    print(jefe_area.mostrarEdad())
    print(jefe_area.mostrarinformacionTurno())
    print(jefe_area.mostrarinformacionProyectos())
    print(jefe_area.mostrarinformacionContactoEmergencia())

if __name__ == "__main__":
    main()
