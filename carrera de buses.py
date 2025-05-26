import random
import time

class Bus:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def move(self):
        event = random.randint(1, 30)  # Aumenté el rango para más variedad de eventos

        if event == 1:
            print(f"⚠️ {self.name} se le ponchó una llanta y se retrasa! ⚠️")
            self.distance -= 5
        elif event == 2:
            print(f"🔥 {self.name} acelera como loco! 🔥")
            self.distance += 10
        elif event == 3:
            print(f"🛑 {self.name} quedó atrapado en el tráfico! 🛑")
            self.distance -= 3
        elif event == 4:
            print(f"🎒 Un pasajero de última hora sube a {self.name}, pierde tiempo. 🎒")
            self.distance -= 2
        elif event == 5:
            print(f"🚀 {self.name} encuentra un turbo sorpresa y acelera brutalmente! 🚀")
            self.distance += 15
        elif event == 6:
            print(f"🚔 {self.name} ve una patrulla y debe frenar. 🚔")
            self.distance -= 7
        elif event == 7:
            print(f"💥 {self.name} sufre una llanta explotada y pierde bastante tiempo! 💥")
            self.distance -= 10
        elif event == 8:
            print(f"🌬️ {self.name} recibe un viento a favor y gana velocidad. 🌬️")
            self.distance += 8
        else:
            self.distance += random.randint(1, 10) * random.choice([1, 1, 2, 2, 3, 0, -1])
        
        if self.distance < 0:
            self.distance = 0

    def __str__(self):
        return f"{self.name}: [{' ' * (self.distance // 2)}🚌]"

class Race:
    def __init__(self, buses, laps=1):
        self.buses = [Bus(name) for name in buses]
        self.laps = laps
        self.bets = {}
        self.players = {}
        self.finish_line = 100 * laps

    def place_bets(self):
        num_players = int(input("¿Cuántos jugadores apuestan? "))
        for i in range(1, num_players + 1):
            print("Opciones de autobuses:")
            for idx, bus in enumerate(self.buses):
                print(f"{idx + 1}. {bus.name}")
            bet = int(input(f"Jugador {i}, ¿a qué autobús apuestas? (1-{len(self.buses)}): ")) - 1
            self.bets[i] = bet
            self.players[i] = 0
        print("Apuestas realizadas:")
        for player, bet in self.bets.items():
            print(f"Jugador {player} apostó por {self.buses[bet].name}")

    def start(self):
        self.place_bets()
        print("¡Comienza la carrera de autobuses!")
        while True:
            time.sleep(0.5)
            for bus in self.buses:
                bus.move()
                print(bus)
                
                if bus.distance >= self.finish_line:
                    print("🏁" * 20)
                    print(f"🏆 ¡¡¡{bus.name} ha ganado la carrera!!! 🏆")
                    print("🚌" * 10)
                    print(" " * 10 + "🚌 GANADOR 🚌")
                    print("🚌" * 10)
                    self.check_bets(bus.name)
                    input("\nPresiona Enter para salir...")
                    return
            print("-" * 50)

    def check_bets(self, winner_name):
        for player, bet in self.bets.items():
            if self.buses[bet].name == winner_name:
                print(f"🎉 Jugador {player} ha ganado su apuesta! 🎉")
                self.players[player] += 1
            else:
                print(f"Jugador {player} ha perdido su apuesta.")
        print("\nPuntajes actuales:")
        for player, score in self.players.items():
            print(f"Jugador {player}: {score} puntos")

if __name__ == "__main__":
    buses = ["El Rápido de Tepito", "La Bestia del Norte", "El Tamalero Veloz", "La Bala de Iztapalapa", "El Metrobus Asesino"]
    vueltas = int(input("¿Cuántas vueltas dará la carrera? "))
    carrera = Race(buses, laps=vueltas)
    carrera.start()
