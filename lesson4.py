from random import randint, choice


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.name} health: {self.health} damage: {self.damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if isinstance(hero, Berserk) and self.defence != hero.ability:
                    blocked = choice([5, 10])
                    hero.blocked_damage = blocked
                    hero.health -= (self.damage - blocked)
                else:
                    hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def apply_super_power(self, boss, heroes):
        pass

    def attack(self, boss):
        boss.health -= self.damage


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_power(self, boss, heroes):
        coefficient = randint(2, 5)
        boss.health -= self.damage * coefficient
        print(f'Warrior {self.name} hit critically {self.damage * coefficient}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BOOST')

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                extra_damage = 5
                hero.damage += extra_damage
                print(f'Magic {self.name} boosted {hero.name}\'s damage by {extra_damage}.')


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_AND_REVERT')
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage} damage.')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points
                print(f'Medic {self.name} healed {hero.name} for {self.__heal_points} points.')


        if self.health > 0:
            damage_taken = randint(5, 15)
            self.health -= damage_taken
            print(f'Witcher {self.name} received {damage_taken} damage from the boss.')

            dead_heroes = [hero for hero in heroes if hero.health <= 0]
            if dead_heroes and randint(1, 100) <= 20:  # 20% chance to revive a dead hero
                revived_hero = dead_heroes[0]
                revived_hero.health = 50  # Устанавливаем здоровье в какое-то значение
                print(f'Witcher {self.name} revived {revived_hero.name}!')
                self.health = 0  # Witcher dies


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'STEAL_HEALTH')
        self.stolen_health = 0

    def apply_super_power(self, boss, heroes):
        if boss.health > 0:
            self.stolen_health = randint(10, 20)
            boss.health -= self.stolen_health
            target_hero = choice(heroes)
            if target_hero.health > 0:
                target_hero.health += self.stolen_health
                print(f'Hacker {self.name} stole {self.stolen_health} health from the boss and gave it to {target_hero.name}.')


round_number = 0


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = all(hero.health <= 0 for hero in heroes)
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def play_round(boss, heroes):
    global round_number
    round_number += 1
    print(f'\n--- Round {round_number} ---')
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and hero.ability != boss.defence:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def show_statistics(boss, heroes):
    print(boss)
    for hero in heroes:
        print(hero)


# Пример использования:

# Создание персонажей
boss = Boss("Dark Lord", 100, 15)
warrior = Warrior("Thor", 80, 10)
magic = Magic("Gandalf", 60, 8)
berserk = Berserk("Hulk", 100, 12)
medic = Medic("Florence", 70, 5, 20)
witcher = Witcher("Geralt", 70, 12)
hacker = Hacker("Neo", 60, 7)

heroes = [warrior, magic, berserk, medic, witcher, hacker]

# Игровой цикл
while not is_game_over(boss, heroes):
    play_round(boss, heroes)


round_number = 0


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

