import random, time

results = []
dice = 0
sides = 0
class app():

    def __init__(self):
        super().__init__()
    
    def init(self, dice, sides, results):
        print("RNG // SimpleSenpai")
        print()
        dice = int(input("How many dice do you want to roll? "))
        print()
        sides = int(input("How many sides do you want your dice to have? "))
        print()
        print("Rolling...")
        x = 0
        y = 0
        
        while x != dice:
            y = random.randint(1, sides)
            results.append(y)
            x = x + 1
        time.sleep(0.5)
        print("Your dice roll results are as follows:")
        for z in results:
            print(z)

app().init(dice, sides, results)