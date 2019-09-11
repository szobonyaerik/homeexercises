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
