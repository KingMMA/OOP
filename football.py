# Кравченко Богдан
# 28.10.2023
# Клас "футболіст"


class FootballPlayer:
    
    def __init__(self, name: str, position: str) -> None:
        self.name = name
        self.position = position
        
    def __str__(self) -> str:
        return (
            f"Name: {self.name}\n"
            f"Position: {self.position}\n"
        )

players = {
    "Сергій Шумілов": "Воротар",
    "Віталій Федоров": "Захисник",
    "Андрій Бусько": "Захисник",
    "Кирило Влага": "Захисник",
    "Олександр Авраменко": "Захисник",
    "Віктор Віктор Ян": "Півзахисник",
    "Генадій Синчук": "Півзахисник",
    "Роман Горенко": "Півзахисник",
    "Єгор Абрамов": "Півзахисник",
    "Євген Ісаєнко": "Нападник",
    "Петро Луців": "Нападник"
}

team = []

for player in players.items():
    pl = FootballPlayer(*player)
    team.append(pl)
    print(pl)