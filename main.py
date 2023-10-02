nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
ciudad = input('¿Cuál es tu ciudad? ')
profesion = input('¿Cuál es tu profesion? ')
persona = {'nombre': nombre, 'edad': edad, 'ciudad': ciudad, 'profesion': profesion}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['ciudad'], 'y su profesion es', persona['profesion'])