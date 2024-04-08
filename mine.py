
class Weapon:
    def attack(self):
        raise NotImplementedError("Метод attack должен быть определен в подклассах.")


class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."


class MagicWand(Weapon):
    def attack(self):
        return "Боец использует магическую силу жезла."


class Fighter:
    def __init__(self, weapon):
        self.weapon = weapon

    def changeWeapon(self, new_weapon):
        self.weapon = new_weapon

    def attack(self):
        print(self.weapon.attack())


class Monster:
    def __init__(self):
        self.health = 100

    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Монстр побежден!")
        else:
            print(f"У монстра осталось {self.health} здоровья.")

def battle(fighter, monster):
    # Предположим, что любая атака наносит фиксированный урон
    monster.takeDamage(50)

if __name__ == "__main__":
    # Создание бойца с мечом
    sword_fighter = Fighter(Sword())
    monster = Monster()
    print("Боец выбирает меч.")
    sword_fighter.attack()
    battle(sword_fighter, monster)

    # Боец меняет оружие на лук
    print("\nБоец выбирает лук.")
    sword_fighter.changeWeapon(Bow())
    sword_fighter.attack()
    battle(sword_fighter, monster)

    # Демонстрация расширяемости, добавляем новый тип оружия - магический жезл
    print("\nБоец выбирает магический жезл.")
    sword_fighter.changeWeapon(MagicWand())
    sword_fighter.attack()
    battle(sword_fighter, monster)