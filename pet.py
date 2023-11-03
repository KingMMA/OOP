# Моє звірятко


fib = lambda x: 1 if x in (1,2) else (0 if not x else fib(x-1) + fib(x-2))


class Pet:
    """Віртуальний вихованець"""
    total = 0

    @staticmethod   
    def status():
        print("Загальна кількість звірят", Pet.total)

    def __init__(self, name, hunger = 0, boredom = 0, age = 1):
        Pet.total += 1
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        self.age = age
        self.fib_state = 1

    def __pass_time(self):
        if self.hunger >= 10 or self.age >= 20:
            print("Спи звірятко, спи ...")
            raise Exception
        else:
            self.fib_state += 1
            self.hunger += 1
            self.boredom += 1
            if fib(self.age) <= self.fib_state:
                self.age += 1
                self.fib_state = 1
            
    
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "непогано"
        elif 11 <= unhappiness <= 15:
            m = "не сказати щоб добре"
        else:
            m = "жахливо"
        return m
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Ім'я звірятка не може бути порожнім рядком.")
        else:
            self.__name = new_name
            print("Ім'я успішно змінено.")

    def talk(self):
        print("Мене звати", self.name, ", і зараз я почуваюся", self.mood)
        self.__pass_time()
    
    def eat(self, food: int):
        print("Мррр...  Дякую!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun: int):
        print("Уііі!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
        
    def __str__(self) -> str:
        return (
            f"hunger: {self.hunger}\n"
            f"boredom: {self.boredom}\n"
            f"age: {self.age}\n"
            f"fib_state: {self.fib_state}\n"
        )

def main():
    pet_name = input("Як ви назвете своє звірятко?: ")
    pet = Pet(pet_name)

    choice = None  
    try:
        while True:
            print \
            ("""
            Моє звірятко
    
            0 - Вийти
            1 - Дізнатися про самопочуття звірятка
            2 - Годувати звірятко
            3 - Пограти зі звірятком
            """)
    
            choice = input("Ваш вибір: ")

            # вихід
            if choice == "0":
                print("До побачення.")
                break

            # бесіда зі звірятком
            elif choice == "1":
                pet.talk()
        
            # годування звірятка
            elif choice == "2":
                pet.eat(int(input("Скільки їжі дати звірятку? ")))
         
            # гра зі звірятком
            elif choice == "3":
                pet.play(int(input("Скільки часу витратити на гру? ")))
          
            elif choice == "4":
                print(pet)
        
            # незрозуміле введення користувача
            else:
                print(f"Вибачте, у меню немає пункту {choice}")
    
    except Exception:
        print("Game Over")

main()