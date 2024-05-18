#
# Projekt III - Facebook: Anwendung zur Überprüfung der Betroffenheit einer Datenpanne, Generierung eines Dokuments
#
#

### Füge hier die richtigen Imports ein



### Füge hier dein bot token ein und definiere deinen Bot



### Liste deine States auf mit = range(n)



### Definiere hier deine globalen Variablen



### Definiere hier die Antwortmöglichkeiten für deine ReplyMarkups via Listen



### Schreibe hier die Funktionen für die einzelnen Fragen


def cancel (update, context):
    update.message.reply_text("Der Vorgang wurde abgebrochen.")
    return ConversationHandler.END


### Hier definierst du deinen Conversation Handler

def main():
    updater = Updater(token=bot_api_key, use_context=True)

    dp = updater.dispatcher

    facebook =  ConversationHandler(
         entry_points=[# gib hier deinen Entry Point/ Commands an ],

        states={
            #ordne hier deine states funktionen zu
        },
            
        per_user= True,

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(facebook)
    
    updater.start_polling()

### Diese Funktion brauchst du, damit dein Bot gestartet wird, da wir außerhalb von Jupyter arbeiten

if __name__ == '__main__':
    main()