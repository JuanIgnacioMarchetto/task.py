from datetime import datetime
from colorama import init, Fore, Back, Style

# Inicialización de Colorama para colores en consola
init(autoreset=True)

# Lista de tareas inicial
listaDeTareas = [
    {"nombre_tarea": "Comprar leche",
        "descrip": "Ir al supermercado y comprar leche",
        "fecha_vencimiento": "20/06/2024",
        "completada": False},
    {"nombre_tarea": "Hacer ejercicio",
        "descrip": "Hacer una rutina de ejercicios de 30 minutos",
        "fecha_vencimiento": "21/06/2024",
        "completada": False},
    {"nombre_tarea": "Estudiar Python",
        "descrip": "Completar el capítulo 3 del libro de Python",
        "fecha_vencimiento": "22/06/2024",
        "completada": False}
]

# Función para agregar una tarea
def agregar_tarea(nombre, descripcion, fecha_vencimiento):
    # Implementación de la función agregar_tarea
    pass

# Función para ver el listado de tareas
def ver_listado():
    # Implementación de la función ver_listado
    pass

# Función para borrar una tarea
def borrar_tarea(nombre):
    # Implementación de la función borrar_tarea
    pass

# Función para editar una tarea
def editar_tarea(nombre):
    # Implementación de la función editar_tarea
    pass

# Función para buscar una tarea por descripción
def buscar_tarea(descripcion):
    # Implementación de la función buscar_tarea
    pass

# Función para marcar una tarea como completada
def marcar_completada(nombre):
    # Implementación de la función marcar_completada
    pass

# Función para mostrar las opciones del menú
def ver_opciones_menu():
    print(Back.CYAN + "------ PROGRAMA DE TAREAS ---------")
    print("1) Ver listado de tareas")
    print("2) Agregar una tarea nueva")
    print("3) Editar una tarea existente")
    print("4) Eliminar una tarea de la lista")
    print("5) Buscar una tarea por descripción")
    print("6) Marcar tarea como completada")
    print("7) Salir del programa" + Style.RESET_ALL)

# Función para el inicio de sesión
def login():
    usuario_correcto = "Marcos"
    contrasena_correcta = "1234"
    intentos = 3
    
    while intentos > 0:
        usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")
        
        if usuario == usuario_correcto and contrasena == contrasena_correcta:
            print(Fore.GREEN + "Inicio de sesión exitoso")
            return True
        else:
            intentos -= 1
            print(Fore.RED + f"Nombre de usuario o contraseña incorrectos. Intentos restantes: {intentos}")
    
    print(Fore.RED + "Se han agotado los intentos. Acceso denegado.")
    return False

# Función principal del programa
def main():
    if not login():
        return
    
    ejecutarPrograma = True

    while ejecutarPrograma:
        ver_opciones_menu()
        opcion = input("Elige una opción: ")

        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 1:
                ver_listado()
            elif opcion == 2:
                tareaNueva_nombre = input("Ingrese el nombre de la nueva tarea: ")
                tareaNueva_descripcion = input("Ingresa la descripción de la nueva tarea: ")
                tareaNueva_fecha = input("Ingresa la fecha de vencimiento (DD/MM/YYYY): ")
                agregar_tarea(tareaNueva_nombre, tareaNueva_descripcion, tareaNueva_fecha)
            elif opcion == 3:
                tarea_a_editar = input("Ingrese el nombre de la tarea a EDITAR: ")
                editar_tarea(tarea_a_editar)
            elif opcion == 4:
                tarea_a_borrar = input("Ingrese el nombre de la tarea que quieras borrar: ")
                borrar_tarea(tarea_a_borrar)
            elif opcion == 5:
                tarea_a_buscar = input("Ingrese la descripción de la tarea a buscar: ")
                buscar_tarea(tarea_a_buscar)
            elif opcion == 6:
                tarea_a_completar = input("Ingrese el nombre de la tarea a marcar como completada: ")
                marcar_completada(tarea_a_completar)
            elif opcion == 7:
                print(Fore.YELLOW + "Saliendo del programa")
                ejecutarPrograma = False
            else:
                print(Fore.RED + "Selecciona una opción válida")
        else:
            print(Fore.RED + "Selecciona una opción válida")

if __name__ == "__main__":
    main()
