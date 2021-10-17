from collections import deque

"""
First, you will be given a sequence of integers representing firework effects. Afterwards you will be given another sequence of integers representing explosive power.
You need to start from the first firework effect and try to mix it with the last explosive power. If the sum of their values is:
    • divisible by 3, but it is not divisible by 5 – create Palm firework and remove both materials
    • divisible by 5, but it is not divisible by 3 – create Willow firework and remove both materials
    • divisible by both 3 and 5 – create Crossette firework and remove both materials
Otherwise, decrease the value of the firework effect by 1 and move it at the end of the sequence. Then, try to mix the same explosive power with the next firework effect. 
If any value is equal to or below 0, you should remove it from the sequence before trying to mix it with the other. 
When you have successfully prepared enough fireworks for the show or you have no more firework punches or explosive power, you need to stop mixing. 
To make the perfect firework show, Maria needs 3 of each of the firework types.
"""

effects = deque([int(x) for x in input().split(", ")])
power = [int(x) for x in input().split(", ")]
crossette, palm, willow, = 0, 0, 0
perfect_show = False
while True:
    if crossette >= 3 and palm >= 3 and willow >= 3:
        perfect_show = True
        break
    if len(effects) == 0 or len(power) == 0:
        break
    while True:
        if crossette >= 3 and palm >= 3 and willow >= 3:
            break

        for i in range(len(power)):
            if power[-1] > 0:
                break
            else:
                power.pop()
                continue
        for j in range(len(effects)):
            if effects[0] > 0:
                break
            else:
                effects.popleft()
                continue
        if len(effects) == 0 or len(power) == 0:
            break
        if power[-1] > 0 and effects[0] > 0:
            mix = power[-1] + effects[0]
            if mix % 3 == 0 and mix % 5 == 0:
                crossette += 1
                power.pop()
                effects.popleft()
                break
            elif mix % 3 == 0:
                palm += 1
                power.pop()
                effects.popleft()
                break
            if mix % 5 == 0:
                willow += 1
                power.pop()
                effects.popleft()
                break
            else:
                effects.append(effects.popleft() - 1)
                continue
        else:
            if power[-1] <= 0:
                power.pop()
            elif effects[0] <= 0:
                effects.popleft()
            break

if perfect_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f'Firework Effects left: {", ".join(str(x) for x in effects)}')
if power:
    print(f'Explosive Power left: {", ".join(str(x) for x in power)}')

print(f'Palm Fireworks: {palm}\nWillow Fireworks: {willow}\n'
      f'Crossette Fireworks: {crossette}')