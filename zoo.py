# Кравченко Богдан
# 28.10.2023
# Зооферма

import random

fib = lambda x: 1 if x in (1,2) else (0 if not x else fib(x-1) + fib(x-2))

class Pet:
    """Віртуальний вихованець"""
    total = 0

    @staticmethod   
    def status():
        print("Загальна кількість звірят", Pet.total)

    def __init__(self, name, age = 1):
        Pet.total += 1
        self.__name = name
        self.hunger = random.randint(0, 5)
        self.boredom = random.randint(0, 5)
        self.age = age
        self.fib_state = 1

    def pass_time(self):
        if self.hunger >= 10 or self.age >= 20:
            print(f"Спи звірятко, спи ...\nІм'я: {self.name}")
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
        self.pass_time()
    
    def eat(self, food: int):
        print("Мррр...  Дякую!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.pass_time()

    def play(self, fun: int):
        print("Уііі!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.pass_time()
        
    def __str__(self) -> str:
        return (
            f"name: {self.name}\n"
            f"hunger: {self.hunger}\n"
            f"boredom: {self.boredom}\n"
            f"age: {self.age}\n"
            f"fib_state: {self.fib_state}\n"
        )
        
        
        
class Zoo:
    def __init__(self, pets: list) -> None:
        self.pets: list[Pet] = pets
        
    def __check_pets(self):
        if not bool(self.pets):
            raise Exception
        
    def talk(self):
        for pet in self.pets:
            try:
                pet.talk()
            except Exception:
                self.pets.remove(pet)
        self.__check_pets()
    
    def eat(self, food: int):
        for pet in self.pets:
            try:
                pet.eat(food)
            except Exception:
                self.pets.remove(pet)
        self.__check_pets()
    
    def play(self, time: int):
        for pet in self.pets:
            try:
                pet.play(time)
            except Exception:
                self.pets.remove(pet)
        self.__check_pets()
                
    def __str__(self) -> str:
        for pet in self.pets:
            print(pet)



def main():
    zoo = Zoo([Pet(i) for i in(input("Введіть назву звіряток через кому: ")).split(sep=",")])
     
    try:
        while True:
            print (
                f"Моя зооферма\n"
                f"0 - Вийти\n"
                f"1 - Дізнатися про самопочуття звіряток\n"
                f"2 - Годувати звіряток\n"
                f"3 - Пограти зі звірятками\n"
            )

            # вихід
            if (choice := input("Ваш вибір: ")) == "0":
                print("До побачення.")
                break

            # бесіда зі звірятком
            elif choice == "1":
                zoo.talk()
                
            # годування звірятка
            elif choice == "2":
                zoo.eat(int(input("Скільки їжі дати звіряткам? ")))
         
            # гра зі звірятком
            elif choice == "3":
                zoo.play(int(input("Скільки часу витратити на гру? ")))
          
            elif choice == "4":
                print(zoo)
        
            # незрозуміле введення користувача
            else:
                print(f"Вибачте, у меню немає пункту {choice}")
    
    except Exception:
        print("Game Over")

main()