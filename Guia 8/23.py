grupoA = {
    12: 'Juan',
    20: 'Rosa',
    35: 'Pedro',
    42: 'Roberto',
    50: 'Ana'
}

grupoB = {
    10: 'Luis',
    25: 'Carmen',
    31: 'Berta',
    45: 'Pablo',
    55: 'Dolores'
}

estudiantes = {**grupoA, **grupoB}

for clave in sorted(estudiantes):
    print(clave, '--›', estudiantes[clave])
