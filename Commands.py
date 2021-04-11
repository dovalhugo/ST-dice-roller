import main
import random as rnd

#Roll dice_pool with 10-again normally or as Rote action
def sr(update, context):
    try:
        dice_arguments = str(context.args[0])        
        dice_pool, isRote, wrong_arg = main.dice_arg_reader(dice_arguments)

        if wrong_arg:
            raise Exception(update.message.reply_text('Invalid argument. Use "r" if you want to roll a Rote Action'))

        mode = {
        'again':10,
        'isRote':isRote,
        'isChance':False,   
        }

        if dice_pool >150:
            raise Exception(update.message.reply_text('Too many dices! Take it easy, no one has a dice pool THIS big!'))        

        successes, rolls = main.st_roller(dice_pool, mode)
        update.message.reply_text("Sucesses: "+str(successes)+" || Dices: "+str(rolls))

    except (IndexError, ValueError):
        update.message.reply_text('Not enough dices!')        

#Roll dice_pool with 8-again normally or as Rote action
def sr8(update, context):
    try:
        dice_arguments = str(context.args[0])        
        dice_pool, isRote, wrong_arg = main.dice_arg_reader(dice_arguments)
        if wrong_arg:
            raise Exception(update.message.reply_text('Invalid argument. Use "r" if you want to roll a Rote Action'))         

        mode = {
        'again':8,
        'isRote':isRote,
        'isChance':False,   
        }

        if dice_pool >150:
            raise Exception(update.message.reply_text('Too many dices! Take it easy, no one has a dice pool THIS big!'))

        successes, rolls = main.st_roller(dice_pool, mode)
        update.message.reply_text("Sucesses: "+str(successes)+" || Dices: "+str(rolls))

    except (IndexError, ValueError):
        update.message.reply_text('Not enough dices!')

#Roll dice_pool with 9-again normally or as Rote action
def sr9(update, context):
    try:
        dice_arguments = str(context.args[0])        
        dice_pool, isRote, wrong_arg = main.dice_arg_reader(dice_arguments)            
        if wrong_arg:
            raise Exception(update.message.reply_text('Invalid argument. Use "r" if you want to roll a Rote Action'))

        mode = {
        'again':9,
        'isRote':isRote,
        'isChance':False,   
        }
        if dice_pool >150:
            raise Exception(update.message.reply_text('Too many dices! Take it easy, no one has a dice pool THIS big!'))

        successes, rolls = main.st_roller(dice_pool, mode)
        update.message.reply_text("Sucesses: "+str(successes)+" || Dices: "+str(rolls))

    except (IndexError, ValueError):
        update.message.reply_text('Not enough dices!')

#Roll dice_pool of 1 as a chance die, setting up isChance flag to True
def src(update, context):    
    try:
        dice_pool = 1 
        if context.args:
            dice_arguments = str(context.args[0])
            if dice_arguments != 'r':
                raise Exception(update.message.reply_text('Invalid argument. Use "r" if you want to roll a Rote Action'))
            else:
                isRote = True       
        
        isChance, isRote = True, False     
        mode = {
        'again':11,
        'isRote':isRote,
        'isChance':isChance,   
        }

        successes, rolls = main.st_roller(dice_pool, mode)
        update.message.reply_text("Sucesses: "+str(successes)+" || Dices: "+str(rolls))

    except (IndexError, ValueError):
        update.message.reply_text('Something went wrong, perhaps too many arguments!')


def victim_calculator(prob_mod):  
  prob_ranges = [[0.20,0.5,0.275,0.02,0.005],[0.1,0.50,0.35,0.040,0.01],[0.05,0.40,0.43,0.1,0.020],[0.01,0.24,0.50,0.2,0.05]
           ,[0.01,0.15,0.44,0.3,0.10],[0.0,0.05,0.4,0.4,0.15]]
  victim = rnd.random()
  current_prob = prob_ranges[prob_mod]   

  for i in range(len(current_prob)):
    victim -= current_prob[i]
    if victim <=0:      
      vic = i
      break

  return vic

#Generate the text for the response accordingly
def victim_text_generator(stamina):
    #Simple ajustment to make more obvious sense with the Storytelling system dots that range from 1 to 5.
    stamina +=1
    health_class ={
        1:"Not your luck day, such a weak person. 1 dot of stamina only.",
        2:"Nothing out of ordinary here. It is a common person with 2 dots of stamina.",
        3:"Noice! A Healthy snack... I mean, a healthy person with 3 dots of stamina.",
        4:'Woah! That one must be an athlete or something. 4 dots of stamina!',
        5:"What the actual fuck? Is that a person? Well, it looks like a gallon of blood anyway. 5 fucking dots of Stamina.",
    }
    return health_class[stamina]


def drink(update, context):
    try:
        prob_mod = int(context.args[0])
        stamina = victim_calculator(prob_mod)
        result_text = victim_text_generator(stamina)
        update.message.reply_text(result_text)

    except ValueError:
        update.message.reply_text('Please type numbers only!')    
    except IndexError:
        if len(context.args) <= 0:
            stamina = victim_calculator(0)
            result_text = victim_text_generator(stamina)
            update.message.reply_text(result_text)
        else:
            update.message.reply_text('Not a valid number, my kindred.')