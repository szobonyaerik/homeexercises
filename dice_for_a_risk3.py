import random

ak = int(input("How many attackers(1,2 or 3): "))
df = int(input("How many defenders(1 or 2): "))
attack_list = []
defend_list = []


while ak > 3 or df > 2:
    ak = int(input("How many attackers(1,2 or 3): "))
    df = int(input("How many defenders(1 or 2): "))



for i in range(ak):
    attack = random.randint(1, 6)
    attack_list.append(attack)
print("Attacker: {}".format(attack_list))

for j in range(df):
    defend = random.randint(1, 6)
    defend_list.append(defend)
print("Defender: {}".format(defend_list))

attack_list = sorted(attack_list, reverse = True)
print(attack_list)
defend_list = sorted(defend_list, reverse = True)
print(defend_list)

sign = 0

if df <= ak:
    for index in range(df):
        if defend_list[sign] >= attack_list[sign]:
            print("Attacker lost a unit.")
        elif defend_list[sign] < attack_list[sign]:
            print("Defender lost a unit.")

        sign += 1
else:
    for pen in range(ak):
        if defend_list[sign] >= attack_list[sign]:
            print("Attacker lost a unit.")
        elif defend_list[sign] < attack_list[sign]:
            print("Defender lost a unit.")
