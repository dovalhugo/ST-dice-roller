import config
import random
import re
import logging
import Commands as cmds
from telegram.ext import Updater
from telegram.ext import CommandHandler

# Method for rolling dices as per Storytelling (CofD 2e) system,
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
    wrong_arg = False

    if m:
        dice_pool = int(m.group(1))
        if m.group(2) == 'r':
            isRote = True
        else: 
            isRote = False
            wrong_arg = True        
    else:
        dice_pool = int(dice_arguments)    
        isRote = False

    return dice_pool, isRote, wrong_arg

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a Chronicles of Darkness dice simple roller. Type /help for instructions")

#Main function which mainly contain necessary handlers and dispatchers from Telegram API
def main():
    #Import telegram api token key
    token_id = config.telegram_token

    #Defining commands handlers variables
    sr, sr8, sr9, src, drink = cmds.sr, cmds.sr8, cmds.sr9, cmds.src, cmds.drink

    # Telegram must have basics and Logging
    updater = Updater(token=token_id, use_context=True) #Remember to copy TOKEN from telegram's botFather
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    #Command Handlers
    start_handler = CommandHandler('start', start)
    sr_handler = CommandHandler('sr',sr)
    sr8_handler = CommandHandler('sr8',sr8)
    sr9_handler = CommandHandler('sr9',sr9)
    src_handler = CommandHandler('src',src)
    drink_handler = CommandHandler('drink',drink)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(sr_handler)
    dispatcher.add_handler(sr8_handler)
    dispatcher.add_handler(sr9_handler)
    dispatcher.add_handler(src_handler)
    dispatcher.add_handler(drink_handler)

    #Bot initialization
    updater.start_polling()

if __name__ == '__main__':
    main()

