import random
import re
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler

# Method for rolling dies as per Storytelling (CofD 2e) system,
# Rolls are stored for exhibition purposes only
def st_roller(dice_pool, mode):
    successes = 0
    rolls = []
    again, rote, chance = mode['again'], mode['isRote'], mode['isChance']
    succ_range = 10 if chance else 8   
    if dice_pool > 0:    
        for i in range(dice_pool):
            roll = random.randint(1,10)
            if rote and roll <succ_range:            
                roll = random.randint(1,10)            
            rolls.append(roll)
            while(roll >= again):
                successes +=1
                roll = random.randint(1,10)
                rolls.append(roll)
            if roll >= succ_range:
                successes +=1
    else:
        roll = random.randint(1,10)
        if rote and roll <succ_range and roll !=1:            
                roll = random.randint(1,10)
        if roll == 10:
                successes +=1
        rolls.append(roll)
    return successes,rolls

#Argument reader for dices. Made so the roller can detect the "r" flag, whic means its a Rote action.
def dice_arg_reader(dice_arguments):
    r = re.compile("([0-9]+)([a-zA-Z]+)")
    m = r.match(dice_arguments)
    if m:
        dice_pool = int(m.group(1))
        isRote = True if m.group(2) == 'r' else False
    else:
        dice_pool = int(dice_arguments)    
        isRote = False

    return dice_pool, isRote

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a Chronicles of Darkness dice simple roller. Type /help for instructions")

#Roll dice_pool with 10-again normally
def sr(update, context):
    try:
        dice_arguments = str(context.args[0])        
        dice_pool, isRote = dice_arg_reader(dice_arguments)            

        mode = {
        'again':10,
        'isRote':isRote,
        'isChance':False,   
        }
        successes, rolls = st_roller(dice_pool, mode)
        update.message.reply_text("Sucesses: "+str(successes)+" || Dados: "+str(rolls))
        #context.bot.send_message(chat_id=update.effective_chat.id, text="Sucesses: "+str(successes)+" || Dados: "+str(rolls))
    except (IndexError, ValueError):
        update.message.reply_text('Not enough dies!')

def sr8(update, context):
    try:
        dice_arguments = str(context.args[0])        
        dice_pool, isRote = dice_arg_reader(dice_arguments)            

        mode = {
        'again':8,
        'isRote':isRote,
        'isChance':False,   
        }
        successes, rolls = st_roller(dice_pool, mode)
        update.message.reply_text("Sucesses: "+str(successes)+" || Dados: "+str(rolls))
        #context.bot.send_message(chat_id=update.effective_chat.id, text="Sucesses: "+str(successes)+" || Dados: "+str(rolls))
    except (IndexError, ValueError):
        update.message.reply_text('Not enough dies!')

def sr9(update, context):
    try:
        dice_arguments = str(context.args[0])        
        dice_pool, isRote = dice_arg_reader(dice_arguments)            

        mode = {
        'again':9,
        'isRote':isRote,
        'isChance':False,   
        }
        successes, rolls = st_roller(dice_pool, mode)
        update.message.reply_text("Sucesses: "+str(successes)+" || Dados: "+str(rolls))
        #context.bot.send_message(chat_id=update.effective_chat.id, text="Sucesses: "+str(successes)+" || Dados: "+str(rolls))
    except (IndexError, ValueError):
        update.message.reply_text('Not enough dies!')

def src(update, context):    
    try:
        dice_pool = 1 
        dice_arguments = str(context.args[0]) if context.args else "no"      
        isRote = True if dice_arguments == 'r' else False
        isChance = True        

        mode = {
        'again':11,
        'isRote':isRote,
        'isChance':isChance,   
        }
        successes, rolls = st_roller(dice_pool, mode)
        update.message.reply_text("Sucesses: "+str(successes)+" || Dados: "+str(rolls))
        #context.bot.send_message(chat_id=update.effective_chat.id, text="Sucesses: "+str(successes)+" || Dados: "+str(rolls))
    except (ValueError):
        update.message.reply_text('Something went wrong, perhaps too many arguments!')


# Telegram must have basics and Logging
updater = Updater(token='1775606717:AAF65GiWEgQP1ThrmUZfs2dU6d3pnXi8Buc', use_context=True) #Remember to copy TOKEN from telegram's botFather
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#CommandHandler
start_handler = CommandHandler('start', start)
sr_handler = CommandHandler('sr',sr)
sr8_handler = CommandHandler('sr8',sr8)
sr9_handler = CommandHandler('sr9',sr9)
src_handler = CommandHandler('src',src)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(sr_handler)
dispatcher.add_handler(sr8_handler)
dispatcher.add_handler(sr9_handler)
dispatcher.add_handler(src_handler)

#Bot initiation
updater.start_polling()

#Mode is user input. Can be 8,9 or 10-again, also a chance die or no-again. Finally it should input if Rote or not


