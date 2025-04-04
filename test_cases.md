# Test Cases (Ejemplos con jugadores de Fúrbol)

## Stack (Cambios en el partido)
- Agregar cambios en el orden que ocurren.
- Verificar que `peek()` devuelva el último cambio.
- Usar `pop()` para revertir el último cambio.
- Verificar que `is_empty()` detecte correctamente si no hay más cambios por hacer.

## Queue (Fila para autógrafos)
- Agregar jugadores en el orden que llegan.
- Verificar que el primero en entrar sea el primero en salir (`dequeue`).
- Usar `front()` para ver quién sigue sin quitarlo de la fila.
- Verificar `is_empty()` en la fila vacía.

## Table (Estadísticas de jugador)
- Insertar datos como nombre, goles, asistencias.
- Acceder a estadísticas específicas con `get()`.
- Eliminar un atributo y verificar que ya no existe.
- Mostrar todos los atributos actuales con `keys()` o `items()`.
