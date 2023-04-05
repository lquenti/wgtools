import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

init_message_id = None

EINKAUFSLISTE_HEADER = "Einkaufsliste:"

EINKAUFS_LISTE = []

EINKAUFSLISTE_FOOTER = "Nutze /add um einen Eintrag hinzuzufügen.\nNutze /delete n um den n-ten Eintrag zu löschen."

def build_einkaufsliste():
    if len(EINKAUFS_LISTE) == 0:
        elements =  "Die Liste ist leer\n"
    else:
        elements = ""
        for i, element in enumerate(EINKAUFS_LISTE):
            elements += f"{i + 1}) {element}\n"
    
    return EINKAUFSLISTE_HEADER + "\n\n" + elements + "\n" + EINKAUFSLISTE_FOOTER

async def new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global init_message_id
    msg = await context.bot.send_message(chat_id=update.effective_chat.id, text=build_einkaufsliste())
    init_message_id = msg.message_id
    print(init_message_id)

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if init_message_id is None:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please use /new first")
        return
    element = update.message.text.split(' ', 1)[1]
    EINKAUFS_LISTE.append(element)
    await context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=init_message_id, text=build_einkaufsliste())


async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if init_message_id is None:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please use /new first")
        return
    msg = update.message.text.split(" ")[1:]

    if len(EINKAUFS_LISTE) == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Die Liste ist leer")
        return

    print(msg[0].lower().strip())

    if msg[0].lower().strip() == "all":
        while len(EINKAUFS_LISTE) != 0:
            elem = EINKAUFSLISTE.pop(0)
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"{elem} wurde gekauft")
    else:
        index = int(update.message.text.split(' ', 1)[1])
        if index > len(EINKAUFS_LISTE):
            context.bot.send_message(chat_id=update.effective_chat.id, text="Die Zahl ist zu groß")
            return
        elem = EINKAUFS_LISTE.pop(index - 1)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"{elem} wurde gekauft")
    await context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=init_message_id, text=build_einkaufsliste())

if __name__ == '__main__':
    application = ApplicationBuilder().token('').build()

    new_handler = CommandHandler('new', new)
    add_handler = CommandHandler('add', add)
    delete_handler = CommandHandler('delete', delete)

    application.add_handler(new_handler)
    application.add_handler(add_handler)
    application.add_handler(delete_handler)

    application.run_polling()
