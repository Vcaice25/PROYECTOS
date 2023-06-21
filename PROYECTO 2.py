
# Clase Universidad
class Universidad:
    def _init_(self, nombre):
        self.nombre = nombre
        self.facultades = []

    def agregar_facultad(self, facultad):
        self.facultades.append(facultad)

# Clase Facultad
class Facultad:
    def _init_(self, nombre):
        self.nombre = nombre
        self.departamentos = []

    def agregar_departamento(self, departamento):
        self.departamentos.append(departamento)

# Clase Departamento
class Departamento:
    def _init_(self, nombre):
        self.nombre = nombre
        self.cursos = []

    def agregar_curso(self, curso: object) -> object:
        self.cursos.append(curso)

# Clase Curso
class Curso:

    def _init_(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def obtener_informacion(self):
        return f"Curso: {self.nombre}\nCódigo: {self.codigo}"

    # Creamos instancias de las clases y mostramos la ejecución
    universidad = Universidad("Universidad Ejemplo")

    facultad = Facultad("Facultad de Ciencias")
    universidad.agregar_facultad(facultad)

    departamento = Departamento("Departamento de Informática")
    facultad.agregar_departamento(departamento)

    curso = Curso("Programación", "INFO101")
    departamento.agregar_curso(curso)

    print(curso.obtener_informacion())
    facultad = Facultad("Facultad de Ciencias")
    universidad.agregar_facultad(facultad)

    departamento = Departamento("Departamento de Informática")
    facultad.agregar_departamento(departamento)

    curso = Curso("Programación", "INFO101")
    departamento.agregar_curso(curso)

    # Agregar más instancias de clases según tus necesidades

    # Ejecutar el código y realizar operaciones adicionales si es necesario

# Proyecto de la Universidad - Grupo:
# - Alejandra Barrera
# - Viviana Caice
# - Joseph Páez
# - Jamilet Pillasagua