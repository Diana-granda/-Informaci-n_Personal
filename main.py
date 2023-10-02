informacion_personal = {
    "Nombre": "Diana Granda",
    "Edad": 25,
    "Ciudad": "Lago Agrio",
    "Profesion":""
}

informacion_personal["Ciudad"] = "Lago agrio"
informacion_personal["Profesion"] = "Sistemas informaticos"

# Verificar si "telefono" no está presente y luego agregarlo
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "0968227024"

# Verificar si "edad" está presente y luego eliminarlo
if "Edad" in informacion_personal:
    del informacion_personal["Edad"]

print(informacion_personal)

