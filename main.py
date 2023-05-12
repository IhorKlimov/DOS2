import random

def calculate_damage(lowest, highest, critical_chance, critical_multiplier):
    avg = (lowest + highest) / 2
    num_of_loops = 100000
    sum = 0
    for i in range(num_of_loops):
        r = random.random()
        if r <= critical_chance:
            damage = avg * critical_multiplier
        else:
            damage = avg

        sum = sum + damage
    total_avg = sum / num_of_loops
    print(total_avg)
    return total_avg


def onslaught(lowest, highest, critical_chance, critical_multiplier):
    two_attacks = calculate_damage() + calculate_damage()
    print("Two attacks: " + str(two_attacks))

    avg = (lowest * 0.6 + highest * 0.6) / 2

    num_of_loops = 100000
    onslaught_damage = 0

    for n in range(5):
        sum = 0

        for i in range(num_of_loops):
            r = random.random()
            if r <= critical_chance:
                damage = avg * critical_multiplier
            else:
                damage = avg

            sum = sum + damage

        total_avg = sum / num_of_loops
        print(total_avg)
        onslaught_damage += total_avg

    print("Onslaught damage = " + str(onslaught_damage))
    print(onslaught_damage / two_attacks)


if __name__ == '__main__':
    # Lohse
    # calculate_damage(419, 519, 0.6, 1.65) # -> 651
    # calculate_damage(396, 489, 0.51, 1.65) # -> 588

    # Ifan
    # calculate_damage(746, 868, 0.44, 2.25) # -> 1253
    # calculate_damage(907, 1048, 0.39, 2.25) # -> 1451
    # calculate_damage(885, 1024, 0.34, 2.25) # -> 1358
    # calculate_damage(918, 1062, 0.38, 2.25) # -> 1461
    # calculate_damage(885, 1024, 0.44, 2.25) # -> Thrasher 1479
    # calculate_damage(954, 1059, 0.58, 2.30) # -> Stormbringer 1766
    calculate_damage(996, 1040, 0.69, 2.25) # -> Voor 1894


