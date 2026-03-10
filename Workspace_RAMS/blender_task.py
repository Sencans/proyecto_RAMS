# SADSAD - Script de Generación de Ciudad Procedural
# R.A.M.S. Central Intelligence

import bpy
import random

# --- CONFIGURACIÓN ---
GRID_SIZE = 10  # Número de edificios por lado (10x10 = 100 edificios)
SPACING = 3.0   # Espacio entre los centros de los edificios
BASE_PLANE_SIZE = GRID_SIZE * SPACING # Tamaño de la base para que encaje la ciudad

# --- LIMPIEZA DE LA ESCENA ---
# Es una buena práctica empezar con un lienzo en blanco.
# Selecciona todos los objetos
if bpy.context.object:
    bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='SELECT')
# Borra los objetos seleccionados
bpy.ops.object.delete()

# --- CREACIÓN DEL MATERIAL ---
# Define el alma de la ciudad: un gris oscuro y uniforme.
mat_edificio = bpy.data.materials.new(name="Material_Gris_Oscuro")
mat_edificio.use_nodes = True
principled_bsdf = mat_edificio.node_tree.nodes.get('Principled BSDF')
if principled_bsdf:
    # Color base (R, G, B, Alpha) - valores bajos para un gris oscuro.
    principled_bsdf.inputs['Base Color'].default_value = (0.05, 0.05, 0.05, 1)
    # Aumentamos un poco la rugosidad para que no parezca plástico.
    principled_bsdf.inputs['Roughness'].default_value = 0.8

# --- CREACIÓN DE LA BASE ---
# El suelo sobre el que se erigirá todo.
bpy.ops.mesh.primitive_plane_add(
    size=BASE_PLANE_SIZE,
    enter_editmode=False,
    align='WORLD',
    location=( (GRID_SIZE-1) * SPACING / 2, (GRID_SIZE-1) * SPACING / 2, 0)
)
base_plane = bpy.context.active_object
base_plane.name = "Base_Ciudad"
# Asignamos el mismo material a la base
base_plane.data.materials.append(mat_edificio)


# --- BUCLE DE GENERACIÓN DE EDIFICIOS ---
# El corazón del proceso. Dos bucles anidados para crear la grilla.
print("Iniciando generación procedural de la ciudad...")

for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        # 1. Determinar una altura aleatoria para cada edificio
        altura_aleatoria = random.uniform(2.0, 15.0)

        # 2. Calcular la posición en la grilla
        pos_x = x * SPACING
        pos_y = y * SPACING
        # El origen de un cubo está en su centro. Para que se asiente sobre
        # el plano (z=0), su centro debe estar en la mitad de su altura.
        pos_z = altura_aleatoria / 2

        # 3. Crear el cubo (edificio)
        bpy.ops.mesh.primitive_cube_add(
            size=2, # Tamaño base de 2x2x2
            enter_editmode=False,
            align='WORLD',
            location=(pos_x, pos_y, pos_z)
        )
        edificio_actual = bpy.context.active_object
        edificio_actual.name = f"Edificio_{x}_{y}"

        # 4. Escalar el cubo para que tenga la altura aleatoria
        # La altura de un cubo de size=2 es 2. Para que tenga 'altura_aleatoria',
        # debemos escalarlo en Z por 'altura_aleatoria / 2'.
        edificio_actual.scale.z = altura_aleatoria / 2

        # 5. Aplicar el material creado
        edificio_actual.data.materials.append(mat_edificio)

print("Generación completada.")