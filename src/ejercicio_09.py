# Eres ayudante en una cátedra que recibió registros de alumnos desde
# múltiples fuentes. Los datos llegaron con errores: nombres con formatos
# inconsistentes, notas faltantes, registros nulos y alumnos duplicados con distintas notas.
# Tu tarea es limpiar los datos y generar un listado final.

# Debe realizar las siguientes operaciones:
# Eliminar registros con nombre nulo, vacío o solo espacios.
# Eliminar registros con nota nula, vacía o no numérica (como "absent").
# Normalizar nombres a formato título y estados a formato título.
# Eliminar duplicados por nombre, quedándose con la nota más alta de cada alumno.
# Ordenar alfabéticamente por nombre.

students = [
{"name": " Ana García ", "grade": "8", "status":
"aprobado"},
{"name": "pedro lópez", "grade": "4", "status":
"DESAPROBADO"},
{"name": "MARÍA FERNÁNDEZ", "grade": "10", "status":
"Aprobado"},
{"name": "ana garcía", "grade": "9", "status":
"aprobado"},
{"name": None, "grade": "7", "status": "aprobado"},
{"name": "Luis Martínez ", "grade": None, "status":
"aprobado"},
{"name": " carlos RUIZ", "grade": "6", "status":
"aprobado"},
{"name": "PEDRO LÓPEZ ", "grade": "3", "status":
"desaprobado"},
{"name": " ", "grade": "5", "status": "aprobado"},
{"name": "María Fernández", "grade": "7", "status":
"APROBADO"},
{"name": "Sofía Torres", "grade": "9", "status":
"Aprobado"},
{"name": " sofía torres ", "grade": "8", "status":
"aprobado"},
{"name": "Carlos Ruiz", "grade": "6", "status":
"APROBADO"},
{"name": "Roberto Díaz", "grade": "absent", "status":
"ausente"},
{"name": "roberto díaz", "grade": "", "status":
"Ausente"},
{"name": None, "grade": None, "status": None},
{"name": "Laura Méndez", "grade": "7", "status":
"aprobado"},
{"name": " laura méndez", "grade": "8", "status":
"Aprobado"},
{"name": "GABRIELA RÍOS", "grade": "5", "status":
"aprobado"},
{"name": "gabriela ríos ", "grade": "4", "status":
"Desaprobado"},
]


def limpieza_nombres_nulos(students) -> list:
    students_new = []
    for student in students:
        name = student["name"]
        if name is None or name.strip() == "":
            continue
        else:
            student_copy = student.copy()
            student_copy["name"] = name.strip().title()
            students_new.append(student_copy)
    return students_new

def limpieza_notas_nulas(students) -> list:
    students_new = []
    for student in students:
        grade = student["grade"]
        if grade is None or grade.strip() == "" or not grade.isdigit():
            continue
        else:
            student_copy = student.copy()
            student_copy["grade"] = int(grade)
            students_new.append(student_copy)
    return students_new

def limpieza_estados_nulos(students) -> list:
    students_new = []
    for student in students:
        status = student["status"]
        if status is None or status.strip() == "":
            continue
        else:
            student_copy = student.copy()
            student_copy["status"] = status.strip().title()
            students_new.append(student_copy)
    return students_new


def eliminacion_duplicados(students) -> list:
    students_order = sorted(students, key=lambda stu: stu["grade"], reverse=True)
    names = set()
    result = []
    for student in students_order:
        if student["name"] not in names:
            result.append(student)
            names.add(student["name"])
    return result

def orden_alfabetico(students) -> list:
    students_new = sorted(students, key=lambda stu: stu ["name"].lower())
    return students_new

students_name = limpieza_nombres_nulos(students)
students_grade = limpieza_notas_nulas(students_name)
students_status = limpieza_nombres_nulos(students_grade)
students_ok = eliminacion_duplicados(students_status)
students_final = orden_alfabetico(students_ok)
print("Registros limpios de alumnos:")
print(f"{'Nombre':<20} {'Nota':<6} {'Estado':<10}")
print("--------------------------------------------------")
for student in students_final:
    print(f"{student["name"]:<20} {student["grade"]:<6} {student["status"]:<10}")
print()
print(f"Total de alumnos válidos: {len(students_final)}")
