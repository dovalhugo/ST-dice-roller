import random

# Method for rolling dies as per Storytelling (CofD 2e) system,
# Rolls are stored for exhibition purpose
def st_roller(dice_pool, mode):
    successes = 0
    rolls = []
    again, rote = mode['again'], mode['isRote']    
    if dice_pool > 0:    
        for i in range(dice_pool):
            roll = random.randint(1,10)
            if rote and roll <8:            
                roll = random.randint(1,10)            
            rolls.append(roll)
            while(roll >= again):
                successes +=1
                roll = random.randint(1,10)
                rolls.append(roll)
            if roll >= 8:
                successes +=1
    else:
        roll = random.randint(1,10)
        if rote and roll <8 and roll !=1:            
                roll = random.randint(1,10)
        if roll == 10:
                successes +=1
        rolls.append(roll)
    return successes,rolls

#Mode is user input. Can be 8,9 or 10-again, also a chance die or no-again. Finally it should input if Rote or not
again = 10
isRote = False
dice_pool = 5
mode = {
    'again':again,
    'isRote':isRote,   
}
successes, rolls = st_roller(dice_pool, mode)
print ("SUCCESSES: ", successes)
print ("ROLLS: ", rolls)