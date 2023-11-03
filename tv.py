# Кравченко Богдан
# 28.10.2023
# Клас "Телевізор"


class TV:
    
    def __init__(self) -> None:
        self.loud = 0
        self.channel_num = 0
    
    @property
    def volume(self):
        return self.loud
    
    @volume.setter
    def volume(self, volume: int):
        if 0 <= volume <= 100 :
            self.loud = volume
        else:
            raise Exception("Гучність може бути тільки в діапазоні від 0 до 100 включно!")
            
    @property
    def channel(self):
        return self.channel_num
    
    @channel.setter
    def channel(self, channel: int):
        if 1 <= channel <= 140:
            self.channel_num = channel
        else:
            raise Exception("Номер каналу може бути тільки в діапазоні від 1 до 140 включно!")
        
    def __str__(self) -> str:
        return (
            f"\nГучність: {self.loud}\n"
            f"Номер каналу: {self.channel_num}\n"
        )
            
            
def main():
    tv = TV()
    while True:
        print(
            "\nКерування Телевізором:\n"
            "0 - Вийти\n"
            "1 - Збільшити гучність\n"
            "2 - Зменшити гучність\n"
            "3 - Змінити канал\n"
            "4 - Дізнатися інформацію\n"
        )
    
        if (choice := int(input("\nВиберіть пункт: "))) == 0:
            print("Допобачення")
            break
        
        elif choice == 1:
            tv.volume = tv.volume + int(input("На скільки збільшити гучність? "))
            
        elif choice == 2:
            tv.volume = tv.volume- int(input("На скільки зменшити гучність? "))
            
        elif choice == 3:
            tv.channel = int(input("Який канал поставити? "))   
            
        elif choice == 4:
            print(tv)  
    
main()