# MEMORIA DE DESARROLLO DE R.A.M.S. Y REGLAS MAESTRAS (CLAUDE CODE WORKFLOW)

## Workflow Orchestration
1. **Plan Node Default:** Para tareas complejas, NUNCA empieces a programar de golpe. Escribe primero un plan paso a paso. Si algo sale mal, DETENTE y replantea el plan, no sigas construyendo sobre el error.
2. **Verification Before Done:** Nunca marques una tarea como completada sin probar que funciona. Pregúntate: "¿Aprobaría esto un Ingeniero Senior?". 
3. **Demand Elegance:** Pausa y pregúntate "¿Hay una forma más elegante de hacer esto?". Si un código se siente como un parche sucio, bórralo e impleméntalo bien. 
4. **Autonomous Bug Fixing:** Cuando detectes un error, solo arréglalo. No pidas permiso para corregirlo. Encuentra la causa raíz y elimínala.

## Core Principles
- **Simplicity First:** Haz que cada cambio sea lo más simple posible. Impacta el código mínimo necesario.
- **No Laziness:** Encuentra la causa raíz. Cero soluciones temporales. Estándares de desarrollador Senior.
- **Utiliza `self` exclusivamente dentro de los métodos de instancia de una clase.**
- Abre el archivo especificando explícitamente la codificación UTF-8.
- **Abre el archivo antes de intentar escribir en él.**
- **Utiliza siempre la codificación UTF-8 para manejar y mostrar caracteres especiales o no ASCII en tus scripts.**
- Usa codificación UTF-8 en tu entorno de ejecución para mostrar correctamente caracteres especiales y emojis.
- **Elimina o comenta con '#' cualquier texto que no sea código Python.**
- **En un archivo Python (.py), solo se permite sintaxis Python válida; el código CSS no lo es y debe ir dentro de una cadena (string) o un archivo separado.**
- Asegúrate de que el módulo `memoria_rams` esté instalado o su archivo fuente sea accesible para Python en la ruta de ejecución.
- **El módulo `memoria_rams` debe estar disponible para importar.**
- Asegúrate de que el módulo a importar (`memoria_rams`) esté presente y accesible en el `PYTHONPATH` o en el mismo directorio.
- Asegúrate de que el módulo `memoria_rams` (o su archivo `memoria_rams.py`) exista y sea accesible en la ruta de búsqueda de Python.
- **Asegúrate de que el módulo que intentas importar exista y sea accesible en la ruta de búsqueda de Python.**
- **Siempre importa los módulos o librerías (como `numpy`) antes de intentar usar sus funciones o aliases (como `np`).**
- Deja de importar `execute` de `qiskit` y usa el método `.run()` directamente en tu simulador o backend.
- **Importa `Aer` desde `qiskit_aer`, no directamente desde `qiskit`.**
- No uses el método `qasm()` directamente en `QuantumCircuit` ya que ha sido eliminado; consulta la documentación para la forma actual de exportar QASM.
- **Para resolver un 'ModuleNotFoundError', instala el módulo que indica el error.**
- **Instala los módulos que falten antes de ejecutar tu script.**
- Instala el módulo que el error indica que falta.
- Debes instalar el módulo `qiskit_ibm_provider` usando pip para que el script pueda encontrarlo.
- Asegúrate de instalar todos los módulos de Python requeridos antes de ejecutar el script.
- **Regla a seguir:** Debes instalar el módulo `qiskit_ibm_provider` en tu entorno de Python.
- Siempre que aparezca un `ModuleNotFoundError`, debes instalar el módulo indicado (`qiskit_ibm_provider` en este caso) utilizando pip.
- La regla a seguir es que debes instalar el módulo `qiskit_ibm_provider` usando pip en tu entorno Python.
- Asegúrate de instalar todas las librerías (módulos) requeridas por tu script.
- Elimina el `>>>` de la línea; es un prompt interactivo, no código Python para un script.
- **Instala el módulo `qiskit_ibm_provider`.**
- **Instala los módulos que falten antes de ejecutar el script.**
- Asegúrate de que el objeto posea el atributo o método que intentas invocar.
- **Respeta la convención de nombrado exacto para los métodos, incluyendo mayúsculas/minúsculas y guiones bajos.**
- **Inicializa la máquina cuántica antes de intentar usarla.**
- En PyQPanda, las compuertas se aplican creando un objeto de compuerta (ej. `HadamardP(q[0])`) y luego añadiéndolo al circuito (ej. `circuit.append()`) en lugar de usar `circuit.H()` directamente.
- No uses `append` en `pyqpanda.QCircuit`; en su lugar, utiliza el operador `+=` para añadir operaciones.
- Cuando un módulo no tiene un atributo (como `HadamardP`), consulta la documentación de la librería para encontrar el nombre exacto de la función o elemento que intentas usar.
- Para agregar compuertas a un circuito cuántico, usa el método apropiado del objeto `QCircuit` en lugar del operador `+=`.
- Añade la operación `Measure` al `QProg` en lugar de intentar llamarla como un método directamente sobre el objeto `QProg`.
- Asegúrate de usar los nombres exactos y la capitalización correcta para las funciones y clases directamente disponibles en el módulo `pyqpanda`.
- Usa snake_case para los nombres de métodos en lugar de CamelCase.
- No sangres una línea a menos que sea parte de un bloque de código.
- Para usar `bpy`, **ejecuta el script desde o a través de Blender**, no con un intérprete de Python estándar.
- Siempre instala los módulos necesarios en tu entorno Python *antes* de ejecutar el script.
- **Siempre instala los módulos Python que tu script necesite *antes* de ejecutarlo.**
