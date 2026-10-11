import  random


# ==================== ВОЛНА 1 ====================
def wave_1():
    """Волна 1: Обычный зомби"""
    print("\n=== ВОЛНА 1 ===")
    print("Вы встречаете зомби! Ваши действия")

    hp = 100
    money = 100
    hp_zombi = 100
    damage_zombi = 20

    while hp_zombi > 0 and hp > 0:
        print(f"\nВаше здоровье: {hp} | Здоровье зомби: {hp_zombi} | Монеты: {money}")
        print("1. Атаковать горохострелом (урон: 50, стоимость: 100 монет)")
        print("2. Поставить орех (стоимость: 50 монет, защита: 100% на один ход)")
        print("3. Атаковать грибом (урон: 64, стоимость: 20 монет)")

        try:
            action = int(input("Выберите действие (1-3): "))
        except ValueError:
            print("Пожалуйста, введите число от 1 до 3.")
            continue

        if action == 1:
            if money >= 100:
                hp_zombi -= 50
                money -= 100
                print("Горохострел выстрелил! Зомби получил 50 урона.")
            else:
                print("Недостаточно монет для горохострела!")
                continue
        elif action == 2:
            if money >= 50:
                money -= 50
                print("Вы поставили орех. Зомби не смог вас атаковать!")
                continue
            else:
                print("Недостаточно монет для ореха!")
                continue
        elif action == 3:
            if money >= 20:
                hp_zombi -= 64
                money -= 20
                print("Гриб атаковал! Зомби получил 64 урона.")
            else:
                print("Недостаточно монет для гриба!")
                continue
        else:
            print("Неверный выбор, попробуйте снова.")
            continue

        if hp_zombi > 0:
            hp -= damage_zombi
            print(f"Зомби вас атаковал на {damage_zombi} HP!")

    if hp <= 0:
        print("\nВы погибли в первой волне! Игра окончена.")
        return False
    else:
        print("\nЗомби повержен! Вы переходите к следующей волне.")
        return True


# ==================== ВОЛНА 2 ====================
def wave_2():
    """Волна 2: Зомби-гипноденс"""
    print("\n=== ВОЛНА 2 ===")
    print("Вы встречаете Зомби-гипноденс! Ваши действия")

    hp = 100
    money = 100
    hp_zombi = 67
    damage_zombi = 60

    while hp_zombi > 0 and hp > 0:
        print(f"\nВаше здоровье: {hp} | Здоровье гипноденса: {hp_zombi} | Монеты: {money}")
        print("1. Скрестить горохострел и гриб судьбы (урон: смертельный, стоимость: 100 монет)")
        print("2. Сказать 'бурмалда3' (стоимость: 0 монет, снижает урон зомби на 50% в этом ходу)")
        print("3. Атаковать дробовиком (урон: 99, стоимость: 20 монет)")
        print("4. Бросить гранату (урон: 40 всем, включая вас: -20 HP, стоимость: 30 монет)")
        print("5. Сбежать и собрать ресурсы (пропуск хода, +20 монет, гипноденс атакует)")

        try:
            action = int(input("Выберите действие (1-5): "))
        except ValueError:
            print("Пожалуйста, введите число от 1 до 5.")
            continue

        zombie_attack = True
        reduced_damage = int(damage_zombi * 0.5)

        if action == 1:
            if money >= 100:
                hp_zombi = 0
                money -= 100
                print("Вы скрестили растения! Гипноденс уничтожен!")
                zombie_attack = False
            else:
                print("Недостаточно монет!")
                continue
        elif action == 2:
            print(f"Вы сказали 'бурмалда3'. Защита активирована! Урон гипноденса снижен до {reduced_damage}.")
        elif action == 3:
            if money >= 20:
                hp_zombi -= 99
                money -= 20
                print("Дробовик выстрелил! Гипноденс получил 99 урона.")
            else:
                print("Недостаточно монет!")
                continue
        elif action == 4:
            if money >= 30:
                money -= 30
                hp_zombi -= 40
                hp -= 20
                print(f"Граната взорвалась! Гипноденс потерял 40 HP, вы потеряли 20 HP.")
                if hp <= 0:
                    break
            else:
                print("Недостаточно монет для гранаты!")
                continue
        elif action == 5:
            money += 20
            print("Вы собрали ресурсы и получили 20 монет. Но гипноденс воспользовался моментом!")
        else:
            print("Неверный выбор, попробуйте снова.")
            continue

        if hp_zombi > 0 and zombie_attack:
            if action == 2:
                hp -= reduced_damage
                print(f"Гипноденс вас атаковал, но защита сработала! Вы потеряли {reduced_damage} HP.")
            else:
                hp -= damage_zombi
                print(f"Гипноденс вас атаковал на {damage_zombi} HP!")

    if hp <= 0:
        print("\nВы погибли во второй волне! Игра окончена.")
        return False
    else:
        print("\nГипноденс повержен! Победа!")
        return True


# ==================== ВОЛНА 3 ====================
def wave_3():
    """Волна 3: Босс-робот, на которого ДЕЙСТВУЮТ комплимент и секретная атака 'Гипер Смерть'"""
    hp = 1000
    money = 4989
    hp_zombi = 9999
    base_damage_zombi = 80

    special_plant_ready = False
    sunflowers_planted = 0
    max_sunflowers = 4
    poison_stack = 0
    shield_active = False
    stun_turns = 0
    overheat_cooldown = 0
    player_stunned = False
    water_cooldown = 0

    secret_used = False

    print("\n=== ВОЛНА 3: БОСС РОБОТ АКТИВИРОВАН ===")
    print("Босс изучает ваши действия. Будьте осторожны, он адаптируется!")
    print("СОВЕТ: Робот боится ВОДЫ! Используй её, чтобы наносить огромный урон.")

    while hp_zombi > 0 and hp > 0:
        if player_stunned and stun_turns > 0:
            print("\n--- ВАШ ХОД (ОГЛУШЕН) ---")
            print(f"Здоровье: {hp} | Здоровье Босса: {hp_zombi} | Монеты: {money}")
            print("Вы оглушены электромагнитным импульсом! Вы не можете действовать.")
            stun_turns -= 1
            if stun_turns == 0:
                player_stunned = False
                print("Оглушение прошло. Вы снова можете сражаться!")
            else:
                print(f"Оглушение продлится еще {stun_turns} ход(а).")

            if hp_zombi > 0:
                boss_action = random.randint(1, 10)
                dmg = base_damage_zombi
                if boss_action <= 6:
                    if boss_action <= 3:
                        if shield_active:
                            dmg = int(dmg * 0.5)
                            print(f"Босс атакует, но щит поглощает часть урона! Получено {dmg} HP.")
                        else:
                            print(f"Босс робот вас атаковал на {dmg} HP!")
                    else:
                        dmg = int(base_damage_zombi * 1.5)
                        print(f"БОСС ИСПОЛЬЗУЕТ СПЕЦИАЛЬНУЮ АТАКУ! Вы получили {dmg} HP урона (щит не помог).")
                hp -= dmg
                shield_active = False

                if poison_stack > 0:
                    poison_damage = poison_stack * 10
                    hp_zombi -= poison_damage
                    print(f"Босс страдает от яда! Получено {poison_damage} урона.")
                    poison_stack -= 1

            if water_cooldown > 0:
                water_cooldown -= 1
            if overheat_cooldown > 0:
                overheat_cooldown -= 1

            if hp <= 0:
                break
            continue

        print(f"\n--- ВАШ ХОД ---")
        print(f"Здоровье: {hp} | Здоровье Босса: {hp_zombi} | Монеты: {money}")
        print(f"Подсолнухов: {sunflowers_planted}/{max_sunflowers} | Яд на боссе: {poison_stack} | Щит: {shield_active}")

        print("1. Скрестить Ледо гриб и Гриб судьбы (100 монет) - Создает особое растение.")
        print("2. Сказать комплимент (Бесплатно) - Дает щит на 1 ход, снижает урон босса на 50%.")
        print("3. Атаковать дробовиком (99 урона, 20 монет).")

        if special_plant_ready:
            print("4. Использовать особое растение (350 урона, 150 монет).")
        elif sunflowers_planted < max_sunflowers:
            print("4. Посадить подсолнух (+150 монет).")
        else:
            print("4. (Лимит подсолнухов достигнут).")

        if money >= 300 and max_sunflowers < 5:
            print("5. Купить ХЛЕБ (300 монет) - Даёт +1 слот для подсолнуха!")

        print("6. Огненный шар (150 урона, 50 монет) - Шанс поджечь босса.")
        print("7. Ядовитый дротик (80 урона + яд, 30 монет).")
        print("8. Электро-разряд (200 урона, 80 монет) - Игнорирует защиту, требует перезарядки.")
        print("9. Удар щитом (Блок урона + контратака) - Бесплатно.")
        print("10. Перезарядка (Бесплатно) - Сброс кулдаунов, +50 HP.")
        print("11. Поиск аптечки (Бесплатно) - Шанс найти лут.")
        if water_cooldown > 0:
            print(f"12. ВОДА (перезарядка: {water_cooldown} ход.)")
        else:
            print("12. ВОДА (300 урона, 40 монет) - Робот боится воды! Короткое замыкание.")

        try:
            action = int(input("Выберите действие: "))
        except ValueError:
            print("Введите число!")
            continue

        if action == 111:
            if not secret_used:
                print("\n" + "=" * 50)
                print("⚡⚡⚡ СЕКРЕТНАЯ АТАКА: ГИПЕР СМЕРТЬ! ⚡⚡⚡")
                print("=" * 50)
                print("Вы активировали запретную технику!")
                print("Всё пространство вокруг наполняется энергией...")
                print("БОСС ПОЛУЧАЕТ 9998 УРОНА!")
                hp_zombi -= 9998
                secret_used = True
                print(f"Здоровье Босса после атаки: {hp_zombi}")
                print("=" * 50)
                if hp_zombi <= 0:
                    break
                continue
            else:
                print("\nСекретная атака уже была использована! Больше она недоступна.")
                continue

        player_attacked = True
        skip_boss_turn = False

        if action == 1:
            if money >= 100:
                money -= 100
                special_plant_ready = True
                print("Генетическая модификация успешна! Особое растение готово.")
            else:
                print("Недостаточно монет!")
                continue

        elif action == 2:
            shield_active = True
            print("Искренний комплимент! Щит активирован (снижение урона 50%).")
            player_attacked = False

        elif action == 3:
            if money >= 20:
                hp_zombi -= 99
                money -= 20
                print("Дробовик выстрелил! Босс получил 99 урона.")
            else:
                print("Не хватает монет!")
                continue

        elif action == 4:
            if special_plant_ready:
                if money >= 150:
                    money -= 150
                    hp_zombi -= 350
                    special_plant_ready = False
                    print("Особое растение взорвалось! Босс получил 350 урона!")
                else:
                    print("Недостаточно монет!")
                    continue
            elif sunflowers_planted < max_sunflowers:
                sunflowers_planted += 1
                money += 150
                print(f"Посажен подсолнух! Получено 150 монет. Всего: {sunflowers_planted}/{max_sunflowers}")
                player_attacked = False
                skip_boss_turn = True
            else:
                print("Лимит подсолнухов достигнут!")
                continue

        elif action == 5:
            if money >= 300 and max_sunflowers < 5:
                money -= 300
                max_sunflowers += 1
                print(f"Вы съели ХЛЕБ! Теперь лимит подсолнухов увеличен до {max_sunflowers}.")
                player_attacked = False
            else:
                print("Нельзя купить хлеб.")
                continue

        elif action == 6:
            if money >= 50:
                money -= 50
                hp_zombi -= 150
                if random.random() > 0.5:
                    poison_stack += 1
                    print("Огненный шар нанес 150 урона! Босс загорелся (+10 урона/ход).")
                else:
                    print("Огненный шар нанес 150 урона.")
            else:
                print("Недостаточно монет!")
                continue

        elif action == 7:
            if money >= 30:
                money -= 30
                hp_zombi -= 80
                poison_stack += 2
                print(f"Ядовитый дротик вонзился! 80 урона сразу и {poison_stack * 10} урона в будущем.")
            else:
                print("Недостаточно монет!")
                continue

        elif action == 8:
            if overheat_cooldown > 0:
                print(f"Перегрев! Осталось ходов: {overheat_cooldown}")
                continue
            if money >= 80:
                money -= 80
                hp_zombi -= 200
                overheat_cooldown = 2
                print("Мощный разряд пробил броню! 200 чистого урона.")
            else:
                print("Недостаточно монет!")
                continue

        elif action == 9:
            if random.randint(1, 10) > 3:
                print("Успешный блок и контратака!")
                hp_zombi -= 50
                shield_active = True
                skip_boss_turn = True
            else:
                print("Удар щитом прошел мимо!")
                player_attacked = False

        elif action == 10:
            overheat_cooldown = 0
            hp += 50
            if hp > 1000:
                hp = 1000
            print("Перезарядка завершена. +50 HP, кулдауны сброшены.")
            player_attacked = False

        elif action == 11:
            loot_chance = random.randint(1, 10)
            if loot_chance > 6:
                money += 100
                print("Вы нашли аптечку! +100 монет.")
            else:
                print("Поиск не увенчался успехом. Вы ничего не нашли.")
            player_attacked = False

        elif action == 12:
            if water_cooldown > 0:
                print(f"Вода ещё не готова! Осталось ходов: {water_cooldown}")
                continue
            if money >= 40:
                money -= 40
                hp_zombi -= 300
                water_cooldown = 2
                print("Вы облили робота водой! Короткое замыкание! 300 урона!")
                if random.random() > 0.6:
                    print("⚡ Босс заискрился и пропускает следующий ход!")
                    skip_boss_turn = True
            else:
                print("Недостаточно монет для воды!")
                continue

        else:
            print("Неверный выбор, попробуйте снова.")
            continue

        if overheat_cooldown > 0:
            overheat_cooldown -= 1
        if water_cooldown > 0 and action != 12:
            water_cooldown -= 1

        if hp_zombi > 0 and player_attacked and not skip_boss_turn:
            boss_action = random.randint(1, 10)
            dmg = base_damage_zombi

            if boss_action <= 6:
                if boss_action <= 3:
                    if shield_active:
                        dmg = int(dmg * 0.5)
                        print(f"Босс атакует, но щит поглощает часть урона! Получено {dmg} HP.")
                    else:
                        print(f"Босс робот вас атаковал на {dmg} HP!")
                else:
                    dmg = int(base_damage_zombi * 1.5)
                    print(f"БОСС ИСПОЛЬЗУЕТ СПЕЦИАЛЬНУЮ АТАКУ! Вы получили {dmg} HP урона.")
            elif boss_action <= 8:
                print("Босс перезаряжается, пропуская атаку.")
                dmg = 0
            else:
                print("Босс оглушает вас электромагнитным импульсом!")
                player_stunned = True
                stun_turns = 1
                dmg = 0

            hp -= dmg
            shield_active = False

        if poison_stack > 0 and hp_zombi > 0:
            poison_damage = poison_stack * 10
            hp_zombi -= poison_damage
            print(f"Босс страдает от яда! Получено {poison_damage} урона.")
            poison_stack -= 1

    if hp <= 0:
        print("\nВы погибли в битве с боссом! Игра окончена.")
        return False
    else:
        print("\nБосс повержен! Вы настоящий герой!")
        return True


# ==================== ВОЛНА 4 ====================
def wave_4():
    """Волна 4: Зомби в броне из пластика"""
    print("\n=== ВОЛНА 4 ===")
    print("Вы встречаете зомби в броне из пластика! Ваши действия")

    hp = 300
    money = 400
    hp_zombi = 200
    base_damage_zombi = 19
    damage_multiplier = 1.0
    has_armor_effect = False

    while hp_zombi > 0 and hp > 0:
        print(f"\nВаше здоровье: {hp} | Здоровье зомби: {hp_zombi} | Монеты: {money}")
        print("1. Атаковать мангострелом (урон: 60, стоимость: 100 монет)")
        print("2. Поставить бронеорех (стоимость: 50 монет, защита: снижает урон зомби на 9% на следующий ход)")
        print("3. Атаковать грибом (урон: 64, стоимость: 20 монет)")

        try:
            action = int(input("Выберите действие (1-3): "))
        except ValueError:
            print("Пожалуйста, введите число от 1 до 3.")
            continue

        if action == 1:
            if money >= 100:
                hp_zombi -= 60
                money -= 100
                print("Мангострел выстрелил! Зомби получил 60 урона.")
            else:
                print("Недостаточно монет для мангострела!")
                continue
        elif action == 2:
            if money >= 50:
                money -= 50
                has_armor_effect = True
                damage_multiplier = 0.91
                print("Вы поставили бронеорех! Урон зомби будет снижен на 9% в его следующий ход.")
            else:
                print("Недостаточно монет для ореха!")
                continue
        elif action == 3:
            if money >= 20:
                hp_zombi -= 64
                money -= 20
                print("Гриб атаковал! Зомби получил 64 урона.")
            else:
                print("Недостаточно монет для гриба!")
                continue
        else:
            print("Неверный выбор, попробуйте снова.")
            continue

        if hp_zombi > 0:
            actual_damage = int(base_damage_zombi * damage_multiplier)
            hp -= actual_damage

            if has_armor_effect:
                print(f"Зомби вас атаковал, но бронеорех сработал! Вы получили уменьшенный урон: {actual_damage} HP!")
                has_armor_effect = False
                damage_multiplier = 1.0
            else:
                print(f"Зомби вас атаковал на {actual_damage} HP!")

    if hp <= 0:
        print("\nВы погибли в четвёртой волне! Игра окончена.")
        return False
    else:
        print("\nЗомби повержен! Вы переходите к следующей волне.")
        return True


# ==================== ВОЛНА 5 ====================
def wave_5():
    """Волна 5: Мини-босс"""
    print("\n=== ВОЛНА 5: МИНИ-БОСС ===")
    print("Вы встречаете мини босса футболиста! Ваши действия")

    hp =300
    money = 667
    hp_zombi = 899
    base_damage_zombi = 19
    damage_multiplier = 1.0
    has_armor_effect = False

    while hp_zombi > 0 and hp > 0:
        print(f"\nВаше здоровье: {hp} | Здоровье зомби: {hp_zombi} | Монеты: {money}")
        print("1. Атаковать мангострелом (урон: 60, стоимость: 100 монет)")
        print("2. Поставить бронеорех (стоимость: 50 монет, защита: снижает урон зомби на 9% на следующий ход)")
        print("3. Атаковать грибом (урон: 64, стоимость: 20 монет)")

        try:
            action = int(input("Выберите действие (1-3): "))
        except ValueError:
            print("Пожалуйста, введите число от 1 до 3.")
            continue

        if action == 1:
            if money >= 100:
                hp_zombi -= 60
                money -= 100
                print("Мангострел выстрелил! Зомби получил 60 урона.")
            else:
                print("Недостаточно монет для мангострела!")
                continue
        elif action == 2:
            if money >= 50:
                money -= 50
                has_armor_effect = True
                damage_multiplier = 0.91
                print("Вы поставили бронеорех! Урон зомби будет снижен на 9% в его следующий ход.")
            else:
                print("Недостаточно монет для ореха!")
                continue
        elif action == 3:
            if money >= 20:
                hp_zombi -= 64
                money -= 20
                print("Гриб атаковал! Зомби получил 64 урона.")
            else:
                print("Недостаточно монет для гриба!")
                continue
        else:
            print("Неверный выбор, попробуйте снова.")
            continue

        if hp_zombi > 0:
            actual_damage = int(base_damage_zombi * damage_multiplier)
            hp -= actual_damage

            if has_armor_effect:
                print(f"Зомби вас атаковал, но бронеорех сработал! Вы получили уменьшенный урон: {actual_damage} HP!")
                has_armor_effect = False
                damage_multiplier = 1.0
            else:
                print(f"Зомби вас атаковал на {actual_damage} HP!")

    if hp <= 0:
        print("\nВы погибли в пятой волне! Игра окончена.")
        return False
    else:
        print("\nМини-босс повержен! Вы переходите к следующей волне.")
        return True


# ==================== ВОЛНА 6 ====================

def wave_6():
    """Волна 6:  Босс-робот, на которого НЕ действуют комплимент и секретная атака 'Гипер Смерть'"""
    hp = 1000
    money = 4989
    hp_zombi = 8057
    base_damage_zombi = 1

    special_plant_ready = False
    sunflowers_planted = 0
    max_sunflowers = 4
    poison_stack = 0
    shield_active = False
    stun_turns = 0
    overheat_cooldown = 0
    player_stunned = False
    water_cooldown = 0

    secret_attempts = 0

    print("\n=== ВОЛНА 6: ВИДИМО ЭТОТ МЕТАЛАЛОМ С СОЗНАНИЕМ РЕШИЛ БОРОТЬСЯ ДО КОНЦА! ===")
    print("поломаный Босс неизучает ваши действия ведь он знает что млжет умереть. Будьте осторожны,он решил что то неладное!")
    print("СОВЕТ: Робот боится ВОДЫ! Используй её, чтобы наносить огромный урон.")

    while hp_zombi > 0 and hp > 0:
        # ---------- ХОД ИГРОКА В ОГЛУШЕНИИ ----------
        if player_stunned and stun_turns > 0:
            print("\n--- ВАШ ХОД (ОГЛУШЕН) ---")
            print(f"Здоровье: {hp} | Здоровье Босса: {hp_zombi} | Монеты: {money}")
            print("Вы оглушены электромагнитным импульсом! Вы не можете действовать.")
            stun_turns -= 1
            if stun_turns == 0:
                player_stunned = False
                print("Оглушение прошло. Вы снова можете сражаться!")
            else:
                print(f"Оглушение продлится еще {stun_turns} ход(а).")

            if hp_zombi > 0:
                boss_action = random.randint(1, 10)
                dmg = base_damage_zombi
                if boss_action <= 6:
                    if boss_action <= 3:
                        if shield_active:
                            dmg = int(dmg * 0.5)
                            print(f"Босс атакует, но щит поглощает часть урона! Получено {dmg} HP.")
                        else:
                            print(f"Босс робот вас атаковал на {dmg} HP!")
                    else:
                        dmg = int(base_damage_zombi * 1.5)
                        print(f"БОСС ИСПОЛЬЗУЕТ СПЕЦИАЛЬНУЮ АТАКУ! Вы получили {dmg} HP урона (щит не помог).")
                hp -= dmg
                shield_active = False

                if poison_stack > 0:
                    poison_damage = poison_stack * 10
                    hp_zombi -= poison_damage
                    print(f"Босс страдает от яда! Получено {poison_damage} урона.")
                    poison_stack -= 1

            if water_cooldown > 0:
                water_cooldown -= 1
            if overheat_cooldown > 0:
                overheat_cooldown -= 1

            if hp <= 0:
                break
            continue

        # ---------- ОБЫЧНЫЙ ХОД ИГРОКА ----------
        print(f"\n--- ВАШ ХОД ---")
        print(f"Здоровье: {hp} | Здоровье Босса: {hp_zombi} | Монеты: {money}")
        print(f"Подсолнухов: {sunflowers_planted}/{max_sunflowers} | Яд на боссе: {poison_stack} | Щит: {shield_active}")

        print("1. Скрестить Ледо гриб и Гриб судьбы (100 монет) - Создает особое растение.")
        print("2. Сказать комплимент (Бесплатно) - Босс знает, что вы хотите его убить! Щит НЕ даст.")
        print("3. Атаковать дробовиком (99 урона, 20 монет).")

        if special_plant_ready:
            print("4. Использовать особое растение (350 урона, 150 монет).")
        elif sunflowers_planted < max_sunflowers:
            print("4. Посадить подсолнух (+150 монет).")
        else:
            print("4. (Лимит подсолнухов достигнут).")

        if money >= 300 and max_sunflowers < 5:
            print("5. Купить ХЛЕБ (300 монет) - Даёт +1 слот для подсолнуха!")

        print("6. Огненный шар (150 урона, 50 монет) - Шанс поджечь босса.")
        print("7. Ядовитый дротик (80 урона + яд, 30 монет).")
        print("8. Электро-разряд (200 урона, 80 монет) - Игнорирует защиту, требует перезарядки.")
        print("9. Удар щитом (Блок урона + контратака) - Бесплатно.")
        print("10. Перезарядка (Бесплатно) - Сброс кулдаунов, +50 HP.")
        print("11. Поиск аптечки (Бесплатно) - Шанс найти лут.")
        if water_cooldown > 0:
            print(f"12. ВОДА (перезарядка: {water_cooldown} ход.)")
        else:
            print("12. ВОДА (300 урона, 40 монет) - Робот боится воды! Короткое замыкание.")

        try:
            action = int(input("Выберите действие: "))
        except ValueError:
            print("Введите число!")
            continue

        # ---------- СЕКРЕТНАЯ АТАКА (НЕ РАБОТАЕТ) ----------
        if action == 111:
            secret_attempts += 1

            print("\n" + "=" * 50)
            print("⚡⚡⚡ СЕКРЕТНАЯ АТАКА: ГИПЕР СМЕРТЬ! ⚡⚡⚡")
            print("=" * 50)
            print("Вы активировали запретную технику!")
            print("Всё пространство вокруг наполняется энергией...")
            print("...")

            if secret_attempts == 1:
                print("Но босс лишь усмехается.")
                print("Босс: «Неа.»")
                print("Босс: «НЕТ! не получится.»")
            elif secret_attempts == 2:
                print("Босс даже не поворачивается.")
                print("Босс: «Я же сказал — нет.»")
            elif secret_attempts == 3:
                print("Босс раздражённо вздыхает.")
                print("Босс: «Ты глухой? Я. Сказал. НЕТ.»")
            else:
                print("Босс молча смотрит на вас.")
                print("Босс: «...»")
                print("(Босс потерял к вам всякий интерес.)")

            print("=" * 50)
            print("Секретная атака не сработала! Босс её заблокировал.")
            print("=" * 50)
            player_attacked = False
            continue

        # ---------- ОСНОВНЫЕ ДЕЙСТВИЯ ----------
        player_attacked = True
        skip_boss_turn = False

        if action == 1:
            if money >= 100:
                money -= 100
                special_plant_ready = True
                print("Генетическая модификация успешна! Особое растение готово.")
            else:
                print("Недостаточно монет!")
                continue

        elif action == 2:
            print("Босс: «Комплименты? Серьёзно?» Щит не активирован.")
            player_attacked = False

        elif action == 3:
            if money >= 20:
                hp_zombi -= 99
                money -= 20
                print("Дробовик выстрелил! Босс получил 99 урона.")
            else:
                print("Не хватает монет!")
                continue

        elif action == 4:
            if special_plant_ready:
                if money >= 150:
                    money -= 150
                    hp_zombi -= 350
                    special_plant_ready = False
                    print("Особое растение взорвалось! Босс получил 350 урона!")
                else:
                    print("Недостаточно монет!")
                    continue
            elif sunflowers_planted < max_sunflowers:
                sunflowers_planted += 1
                money += 150
                print(f"Посажен подсолнух! Получено 150 монет. Всего: {sunflowers_planted}/{max_sunflowers}")
                player_attacked = False
                skip_boss_turn = True
            else:
                print("Лимит подсолнухов достигнут!")
                continue

        elif action == 5:
            if money >= 300 and max_sunflowers < 5:
                money -= 300
                max_sunflowers += 1
                print(f"Вы съели ХЛЕБ! Теперь лимит подсолнухов увеличен до {max_sunflowers}.")
                player_attacked = False
            else:
                print("Нельзя купить хлеб.")
                continue

        elif action == 6:
            if money >= 50:
                money -= 50
                hp_zombi -= 150
                if random.random() > 0.5:
                    poison_stack += 1
                    print("Огненный шар нанес 150 урона! Босс загорелся (+10 урона/ход).")
                else:
                    print("Огненный шар нанес 150 урона.")
            else:
                print("Недостаточно монет!")
                continue

        elif action == 7:
            if money >= 30:
                money -= 30
                hp_zombi -= 80
                poison_stack += 2
                print(f"Ядовитый дротик вонзился! 80 урона сразу и {poison_stack * 10} урона в будущем.")
            else:
                print("Недостаточно монет!")
                continue

        elif action == 8:
            if overheat_cooldown > 0:
                print(f"Перегрев! Осталось ходов: {overheat_cooldown}")
                continue
            if money >= 80:
                money -= 80
                hp_zombi -= 200
                overheat_cooldown = 2
                print("Мощный разряд пробил броню! 200 чистого урона.")
            else:
                print("Недостаточно монет!")
                continue

        elif action == 9:
            if random.randint(1, 10) > 3:
                print("Успешный блок и контратака!")
                hp_zombi -= 50
                shield_active = True
                skip_boss_turn = True
            else:
                print("Удар щитом прошел мимо!")
                player_attacked = False

        elif action == 10:
            overheat_cooldown = 0
            water_cooldown = 0
            hp += 50
            if hp > 1000:
                hp = 1000
            print("Перезарядка завершена. +50 HP, кулдауны сброшены.")
            player_attacked = False

        elif action == 11:
            loot_chance = random.randint(1, 10)
            if loot_chance > 6:
                money += 100
                print("Вы нашли аптечку! +100 монет.")
            else:
                print("Поиск не увенчался успехом. Вы ничего не нашли.")
            player_attacked = False

        elif action == 12:
            if water_cooldown > 0:
                print(f"Вода ещё не готова! Осталось ходов: {water_cooldown}")
                continue
            if money >= 40:
                money -= 40
                hp_zombi -= 300
                water_cooldown = 2
                print("Вы облили робота водой! Короткое замыкание! 300 урона!")
                if random.random() > 0.6:
                    print("⚡ Босс заискрился и пропускает следующий ход!")
                    skip_boss_turn = True
            else:
                print("Недостаточно монет для воды!")
                continue

        else:
            print("Неверный выбор, попробуйте снова.")
            continue

        # ---------- КУЛДАУНЫ ----------
        if overheat_cooldown > 0:
            overheat_cooldown -= 1
        if water_cooldown > 0 and action != 12:
            water_cooldown -= 1

        # ---------- ХОД БОССА ----------
        if hp_zombi > 0 and player_attacked and not skip_boss_turn:
            boss_action = random.randint(1, 10)
            dmg = base_damage_zombi

            if boss_action <= 6:
                if boss_action <= 3:
                    if shield_active:
                        dmg = int(dmg * 0.5)
                        print(f"Босс атакует, но щит поглощает часть урона! Получено {dmg} HP.")
                    else:
                        print(f"Босс робот вас атаковал на {dmg} HP!")
                else:
                    dmg = int(base_damage_zombi * 1.5)
                    print(f"БОСС ИСПОЛЬЗУЕТ СПЕЦИАЛЬНУЮ АТАКУ! Вы получили {dmg} HP урона.")
            elif boss_action <= 8:
                print("Босс перезаряжается, пропуская атаку.")
                dmg = 0
            else:
                print("Босс оглушает вас электромагнитным импульсом!")
                player_stunned = True
                stun_turns = 1
                dmg = 0

            hp -= dmg
            shield_active = False

        # ---------- ЯД НА БОССЕ ----------
        if poison_stack > 0 and hp_zombi > 0:
            poison_damage = poison_stack * 10
            hp_zombi -= poison_damage
            print(f"Босс страдает от яда! Получено {poison_damage} урона.")
            poison_stack -= 1

    # ---------- ИТОГ ВОЛНЫ ----------
    if hp <= 0:
        print("\nВы погибли в битве с боссом! Игра окончена.")
        return False
    else:
        print("\nБосс повержен! Вы настоящий герой!")
        return True














# ==================== ЗАПУСК ИГРЫ ====================
def main():
    print("=" * 50)
    print("     В̲̤̤̻͔͊ͩ̆͛̄ Э̭̑Т̵̷͉̟͈͎̰͇ͪͬӦ̺͈̜͖̞̒ͦ͋Й̩̤̖̼̬̉ͅ И̴̰̟̜̞͔͊͊ͩͬ͋Г̪͖̯ͦ̓ͩ̊Р̴͕̜̼͈͑̂̋̄̊̒Е̶́̿ М̟͍͉̽И̶̱͓̰̖͚̍͌̑̈ͩ̍Р̷̦̘͙̝ͦ̿͑͊ Г̹̏͂ͪͦ͊̇Н̩̲͈И̶̖̪Ё̷̰͚͊ͩТ̵ͮ̽͐̌")
    print("=" * 50)

    waves = [wave_1, wave_2, wave_3, wave_4, wave_5, wave_6]

    for i, wave in enumerate(waves, start=1):
        if not wave():
            print(f"\n💀 Игра окончена на волне {i}.")
            print("Спасибо за игру!")
            return

    print("\n" + "=" * 50)
    print("🎉 ПОБЕДА! Вы прошли начало приключения!")
    print("=" * 50)




if __name__ == "__main__":
    main() 
    
import time

print("Начало")
time.sleep(2)
print("Прошло 2 секунды")
time.sleep(1)
print("Прошла ещё 1 секунда")
print("Конец")
