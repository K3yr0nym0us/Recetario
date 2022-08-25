#vamos a programar un programa que lea recetas desde diferentes directorios

#1 saludo de bienvenida
#2 las recetas estan en:
#3 cuantas recetas hay
#4 escoje una opcion:
#
#[1] leer receta
    #elegir categoria
    #mostrar recetas
    #elegir receta

#[2] crear receta
    #elegir categoria
    #crear nombre
    #crear contenido

#[3] crear categoria
    #nombre categoria
    #carpeta nueva

#[4] eliminar receta
    #elegir categoria
    #mostrar recetas
    #elegir receta
    #eliminar receta

#[5] eliminar categoria
    #elegir categoria
    #eliminar categoria

#[6] finalizar programa
    #cerrar codigo

#'envolver' el codigo en un loop while
#para repetir todo hasta que usuario presione salir (opcion 6)

#usar system('cls') para limpiar pantalla cada vez que el usuario vuelva a la pantalla principal

#buscar mas metodos Path

#usar muchas funciones para hacerlo mas legible y ordenado

import os
from pathlib import Path
from os import system, remove

recetas = Path('Recetas')

def obtener_categorias():
    #funcion que agrega cada palabra a un diccionario y le da el valor + 1 por cada palabra
    ruta = os.listdir(recetas)
    categoria = {}
    numero_categorias = 0
    for palabra in ruta:
        numero_categorias += 1 
        categoria[numero_categorias] = palabra
        print(f'[{numero_categorias}]',categoria[numero_categorias])
    return categoria

def obtener_recetas():

    categoria = obtener_categorias()

    #esta funcion extrae la respuesta del usuario y la convierte en una ruta path
    usuario = int(input('\n'))
    consulta = categoria[usuario]
    print(consulta)
    ruta_variable = recetas.joinpath(consulta)
    system('cls')
    print(f"Las recetas disponibles en '{ruta_variable.stem}' son:\n")
    
    #funcion que imprime la/las receta que se encuentren en el directorio ingresado por el ususario
    lista_recetas_disponibles = {}
    numero_recetas = 0
    for txt in Path(ruta_variable).glob('**/*.txt'):
        recetas_disponibles = os.path.basename(txt)
        numero_recetas += 1
        lista_recetas_disponibles[numero_recetas] = recetas_disponibles
        print(f'[{numero_recetas}]',lista_recetas_disponibles[numero_recetas])
    
    return lista_recetas_disponibles,ruta_variable

def saludo():
    numero = 0
    cantidad_recetas = Path(recetas)
    for txt in Path(cantidad_recetas).glob('**/*.txt'): 
        numero += 1
    print(f"Bienvenido a su recetario!\n\nSus recetas estan en el directorio: '{recetas}'\nY existe un total de {numero} recetas.")
    opciones()

def opciones():
    opcion = int(input('Escoja una opcion:\n\n[1] Leer receta\n[2] Crear receta\n[3] Crear categoria\n[4] Eliminar receta\n[5] Eliminar categoria\n[6] Finalizar programa\n'))
    system('cls')
    if opcion == 1:
        system('cls')
        opcion_1()
    elif opcion == 2:
        system('cls')
        opcion_2()
    elif opcion == 3:
        system('cls')
        opcion_3()
    elif opcion == 4:
        system('cls')
        opcion_4()
    elif opcion == 5:
        system('cls')
        opcion_5()
    elif opcion == 6:
        system('cls')
        opcion_6()
    else:
        system('cls')
        print("Ingrese una opcion valida!")
        opciones()

def opcion_1():
    print('Escoje el numero de una categoria:\n')
    lista_recetas_disponibles,ruta_variable = obtener_recetas()

    #funcion que selecciona una receta para luego mostrarla en pantalla
    ingreso_N_receta = int(input("Selecciona el numero de tu receta: "))
    system('cls')
    receta = lista_recetas_disponibles[ingreso_N_receta]
    receta = Path(ruta_variable,receta)
    print(receta.read_text(),'\n')
    
def opcion_2():
    print('Escoje el numero de una categoria:\n')
    categoria = obtener_categorias()

    #esta funcion extrae la respuesta del usuario y la convierte en una ruta path
    usuario = int(input())
    consulta = categoria[usuario]
    print(consulta)
    ruta_variable = recetas.joinpath(consulta)
    system('cls')
    print(f"Te encuentras en la categoria: '{ruta_variable.stem}'\n") 

    #aca se creara la receta nueva con un nombre ingresado por el usuario
    nombre_receta_nueva = input('Ingresa el nombre de la receta que quieres crear:\n\n')
    archivo_nuevo = open(f'{ruta_variable / nombre_receta_nueva}.txt','a')
    system('cls')
    archivo_nuevo.close()
    
    #respuesta de exito al crear la receta
    receta_nueva = Path(ruta_variable,nombre_receta_nueva)
    print(f"Receta: '{receta_nueva.name}' creada exitosamente!\n")

    #ahora aniadimos el contenido a la receta
    edit_receta_nueva = open(f'{receta_nueva}.txt','a')
    edit_receta_nueva.write('Ingredientes:\n\n')
    edit_receta_nueva.close()
    edit_receta_nueva = open(f'{receta_nueva}.txt','a')
    edit_receta_nueva.write(input("Ingresa los ingredientes y luego pulsa Enter: \n"))
    edit_receta_nueva.close()
    system('cls')
    edit_receta_nueva = open(f'{receta_nueva}.txt','a')
    edit_receta_nueva.write('\n\n')
    edit_receta_nueva.close()
    edit_receta_nueva = open(f'{receta_nueva}.txt','a')
    edit_receta_nueva.write('Preparacion:\n\n')
    edit_receta_nueva.close()
    print('Ingredientes ingresados correctamente!\n')
    edit_receta_nueva = open(f'{receta_nueva}.txt','a')
    edit_receta_nueva.write(input("Ingresa los pasos de la preparacion y luego pulsa Enter: \n"))
    system('cls')
    print('Listo! receta guardada correctamente!\n')

def opcion_3():
    #esta funcion crea una categoria/directorio dentro de la ruta "recetas"
    categoria_nueva = input('Ingresa el nombre de la categoria a crear:\n')
    os.mkdir(recetas / categoria_nueva)
    system('cls')
    print(f"Categoria '{categoria_nueva}' creada exitosamente!\n")

def opcion_4():
    print('Escoje el numero de una categoria:\n')
    lista_recetas_disponibles,ruta_variable = obtener_recetas()

    archivo_a_borrar = int(input('Ingrese el numero de la receta que desea eliminar: '))
    system('cls')
    receta = lista_recetas_disponibles[archivo_a_borrar]
    receta = Path(ruta_variable,receta)
    remove(receta)
    print(f"Receta '{receta.stem}' eliminada correctamente!\n")
    
def opcion_5():
    print('Escoje el numero de la categoria que deseas eliminar:\n')
    categoria = obtener_categorias()

    directorio_borrar = int(input())
    consulta = categoria[directorio_borrar]
    ruta_variable = recetas.joinpath(consulta)
    os.rmdir(ruta_variable)
    system('cls')
    print(f"La categoria '{ruta_variable.stem}' fue eliminada exitosamente!\n")

def opcion_6():
    respuesta = input("Desea cerrar el programa?\n(s=Si/n=No)\n")
    if respuesta == 's':
        system('cls')
        print("Hasta la proxima!")
        quit()
    elif respuesta == 'n':
        system('cls')
        opciones()
    else:
        system('cls')
        print("Ingresa una opcion correcta!\n")
        opcion_6()

saludo()
while opcion_6() != 's':
    opciones()