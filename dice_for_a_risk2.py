import random
attack_list = []
defend_list = []

for i in range(3):
    attack = random.randint(1, 6)
    attack_list.append(attack)
print("Attacker: {}".format(attack_list))

for j in range(2):
    defend = random.randint(1, 6)
    defend_list.append(defend)
print("Defender: {}".format(defend_list))

defend_list = sorted(defend_list, reverse = True)
print(defend_list)
attack_list = sorted(attack_list, reverse = True)
print(attack_list)

sign = 0

for index in range(2):
    if defend_list[sign] >= attack_list[sign]:
        print("Attacker lost a unit.")
    elif defend_list[sign] < attack_list[sign]:
        print("Defender lost a unit.")

    sign += 1
