def calcular_promedio_ciudad(temperaturas):
    promedios_ciudades = []

    for ciudad in temperaturas:
        suma_promedio = 0

        for semana in ciudad:
            suma = sum(dia['temp'] for dia in semana)
            promedio_semana = suma / len(semana)
            suma_promedio += promedio_semana

        promedio_ciudad = suma_promedio / len(temperaturas)  # Corregir aquí
        promedios_ciudades.append(promedio_ciudad)

    return promedios_ciudades

# Ejemplo de uso
temperaturas_ejemplo = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 24}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 15}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 31}
        ]
    ],
    [   # Ciudad 2
        # ... datos de temperaturas para la segunda ciudad
    ],
    [   # Ciudad 3
        # ... datos de temperaturas para la tercera ciudad
    ]
]

promedios = calcular_promedio_ciudad(temperaturas_ejemplo)
for i, promedio in enumerate(promedios, 1):
    print(f'El promedio de la ciudad {i} es: {promedio}')