from stack import Stack
from queue import Queue
from table import Table

def demo():
    print("=== Stack Demo (Cambios en el partido) ===")
    cambios = Stack()
    cambios.push("Gignac entra por Ibáñez")
    cambios.push("Córdoba entra por Gorriarán")
    print("Último cambio realizado:", cambios.peek())
    print("Revirtiendo último cambio:", cambios.pop())

    print("\n=== Queue Demo (Fila de jugadores para firmar autógrafos) ===")
    fila = Queue()
    fila.enqueue("Nahuel Guzmán")
    fila.enqueue("Jesús Angulo")
    fila.enqueue("Javier Aquino")
    print("Jugador que sigue:", fila.front())
    print("Jugador atendido:", fila.dequeue())

    print("\n=== Table/Hash Demo (Estadísticas de jugador) ===")
    stats = Table()
    stats.insert("Nombre", "Sebastián Córdova")
    stats.insert("Goles", 7)
    stats.insert("Asistencias", 4)
    print("Jugador:", stats.get("Nombre"))
    print("Goles:", stats.get("Goles"))
    stats.delete("Asistencias")
    print("Atributos disponibles:", stats.keys())

if __name__ == "__main__":
    demo()
