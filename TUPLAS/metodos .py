# Lista de nombres y edades de personas
personas = [("Ana", 25), ("Juan", 30), ("María", 22), ("Pedro", 35), ("Luisa", 22)]

# Convertir la lista en una tupla
tupla_personas = tuple(personas)

# Encontrar la persona más joven y la persona más vieja
xd = sorted(tupla_personas, key=lambda x: x[1])
persona_mas_joven = xd[0]
persona_mas_vieja = xd[-1]

print("La persona más joven es:", persona_mas_joven)
print("La persona más vieja es:", persona_mas_vieja)

# Contar cuántas personas tienen una edad específica
edad_especifica = 22
cantidad_personas_con_edad_especifica = tupla_personas.count((None, edad_especifica))
print(f"Hay {cantidad_personas_con_edad_especifica} personas con {edad_especifica} años.")
