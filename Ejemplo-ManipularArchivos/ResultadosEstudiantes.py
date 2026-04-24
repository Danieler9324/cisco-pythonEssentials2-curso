# Pida al usuario el nombre del archivo del profesor Jekyll.
# Lea el contenido del archivo y cuenta la suma de los puntos recibidos por cada estudiante.
# Imprima un informe simple (pero ordenado), como este:
# Output
# Andrew   Cox      1.5
# Anna     Boleyn   15.5
# John     Smith    7.0

class StudentsDataException(Exception):
    def __init__ (self, message = "Error en los datos de los estudiantes"):
        super().__init__(message)

class BadLine(StudentsDataException):
    def __init__(self, line_number, line_content):
        message = f"Linea invalida en la linea: {line_number} : {line_content}" 
        super().__init__(message)
        self.line_number = line_number
        self.line_content = line_content

class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__("El archivo esta vacio")

src = input("Escriba la direccion del archivo:")

try:
    archivo = open(src, "rt")
    lineas = archivo.readlines()
    
    if not lineas:
        raise FileEmpty
    
    alumnos = {}

    for i,linea in enumerate(lineas, start=1):
            partes = linea.strip().split()

            if len(partes) != 3:
                raise BadLine(i, linea)

            nombre, apellido, puntos = partes

            try:
                puntos = float(puntos)
            except:
                raise BadLine(i, linea)
            
            clave = (nombre, apellido)
        
            if clave not in alumnos:
                alumnos[clave] = 0
            
            alumnos[clave] += puntos
    
    for (nombre, apellido) in sorted(alumnos):
         print(f"{nombre:<10} {apellido:<10} {alumnos[(nombre, apellido)]}")

except FileNotFoundError:
     print("El archivo no existe")
except FileEmpty as e:
     print("Error: ", e)
except BadLine as e:
     print("Error: ", e)
except StudentsDataException as e:
     print("Error", e)
