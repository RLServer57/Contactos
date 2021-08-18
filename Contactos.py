import os, sys

CARPETA = 'contactos/'
EXTENSION = '.txt'

def clear():
    ptf = os.name
    if ptf == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    crear_directorio()
    mostrar_menu()

    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: ')

        if opcion.isnumeric():
            if int(opcion) == 1:
                clear()
                agregar_contacto()
                preguntar = False
            elif int(opcion) == 2:
                clear()
                editar_contacto()
                preguntar = False
            elif int(opcion) == 3:
                clear()
                mostrar_contactos()
                preguntar = False
            elif int(opcion) == 4:
                clear()
                buscar_contacto()
                preguntar = False
            elif int(opcion) == 5:
                clear()
                eliminar_contacto()
                preguntar = False
            else:
                print('Opción no válida!!!')
        elif opcion != "":
            print('Opción no válida')
        else:
            break

def eliminar_contacto():
    print('Eliminar un contacto ❌')
    nombre = input('Ingrese el nombre del contacto: ')
    try:
        clear()
        os.remove(CARPETA+nombre+EXTENSION)
        print('❗❗❗Contacto eliminado❗❗❗')
        print('------------------------------')
    except:
        clear()
        print('❕❕❕El contacto no existe❕❕❕')
        print('---------------------------------')
    app()

def buscar_contacto():
    print('Búsqueda de contacto 🔍')
    nombre = input('Ingrese el nombre del contacto: ')

    try:
        clear()
        print('Información del contacto:')
        with open(CARPETA+nombre+EXTENSION) as contacto:
            for linea in contacto:
                print(linea.rstrip())
        print('-------------------------')
        input('\nPulse ENTER para continuar al menú')
        clear()
    except IOError:
        clear()
        print('❕❕❕El archivo no existe❕❕❕')
        print(IOError)
        print('-------------------------')
    app()

def mostrar_contactos():
    print('Contactos almacenados')
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                sys.stdout.write(linea)
            print("\n------------------------------------")
    input('\nPulse ENTER para continuar al menú')
    clear()
    app()

def editar_contacto():
    print('Escribe nombre de Contacto')
    nombre_anterior = input('Nombre de Contacto: ')

    existe = existe_contacto(nombre_anterior)

    if existe:
        print('Proceda a editar 📝')
        with open(CARPETA+nombre_anterior+EXTENSION, 'w') as archivo:
            nombre_contacto = input('Ingrese el nuevo nombre: ')
            telefono_contacto = input('Ingrese el nuevo número: ')
            categoria_contacto = input('Categoría: ')

            contacto = Contacto(
                nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write(contacto.nombre+'\n')
            archivo.write(contacto.telefono+'\n')
            archivo.write(contacto.categoria)

            os.rename(CARPETA+nombre_anterior+EXTENSION,
                      CARPETA+nombre_contacto+EXTENSION)

            clear()
            print('Contacto editado correctamente ✅')
            print('---------------------------------')
    else:
        clear()
        print('❕❕❕Ese contacto no existe❕❕❕')
        print('----------------------------------')
    app()

def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)

def mostrar_menu():
    print('Menú de opciones de Contactos')
    print('1) Agregar Contacto 👤')
    print('2) Editar Contacto 📝')
    print('3) Ver Contactos 📖')
    print('4) Buscar Contacto 🔍')
    print('5) Eliminar Contacto ❌')
    print('ENTER) para salir')

def agregar_contacto():
    print('Nuevo contacto 👤')
    nombre_contacto = input('Nombre del contacto: ')

    existe = existe_contacto(nombre_contacto)

    if not existe:
        with open(CARPETA+nombre_contacto+EXTENSION, 'w') as archivo:

            telefono_contacto = input('Ingrese el numero: ')
            categoria_contacto = input('Categoría: ')

            contacto = Contacto(
                nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write(contacto.nombre+'\n')
            archivo.write(contacto.telefono+'\n')
            archivo.write(contacto.categoria)

            clear()
            print('Contacto creado correctamente ✅')
            print('--------------------------------')
    else:
        clear()
        print('❕❕❕ Ese contacto ya existe ❕❕❕')
        print('------------------------------------')
    app()

def existe_contacto(nombre):
    return os.path.isfile(CARPETA+nombre+EXTENSION)

clear()
app()