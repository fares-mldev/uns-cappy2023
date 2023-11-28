# Dados dos sets con nombres de estudiantes, uno con los
# anotados para rendir el siguiente examen y el otro con
# los inscriptos para rendir el proyecto final, implemente
# funciones para responder las siguientes consultas:
#
# a) ¿Cuáles son los estudiantes anotados en el examen y en el proyecto final?
# b) ¿Cuáles son los estudiantes que solo se presentan a una de las instancias de evaluación?
# c) ¿Cuántos son los estudiantes anotados en total?
# d) ¿Cuáles son los estudiantes que solo presentan el proyecto final?

set_examen = { 'E1', 'E2', 'E3' }
set_proyecto = { 'E1', 'E3', 'E4' }

# a) ¿Cuáles son los estudiantes anotados en el examen y en el proyecto final?

set_a = set_examen.intersection(set_proyecto)
print(f'a) Los estudiantes anotados en el examen y en el proyecto final: {set_a}')

# b) ¿Cuáles son los estudiantes que solo se presentan a una de las instancias de evaluación?

set_b = set_examen.difference(set_proyecto).union(set_proyecto.difference(set_examen))
print(f'b) Los estudiantes que solo se presentan a una de las instancias de evaluación: {set_b}')

# c) ¿Cuántos son los estudiantes anotados en total?

set_c = set_examen.union(set_proyecto)
print(f'c) Los estudiantes anotados en total: {set_c}')

# d) ¿Cuáles son los estudiantes que solo presentan el proyecto final?

set_d = set_proyecto.difference(set_examen)
print(f'b) Los estudiantes que solo presentan el proyecto final?: {set_d}')
