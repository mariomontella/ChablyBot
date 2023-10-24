from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_first_response
from chatterbot.comparisons import levenshtein_distance

import logging

logging.basicConfig(level=logging.CRITICAL)

#utilizzo della classe "chatbot" per istanziare il bot

bot = ChatBot(
    "Chably", #nome che assegniamo al bot
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="./db.sqlite3",
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparison.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"

        }
    ]
)

with open("C:/Users/Mario/Desktop/chably_bot/conversazione.txt") as f:
    conversation = f.readlines()
    trainer = ListTrainer(bot)
    trainer.train(conversation)


#utilizzo del ciclo while per rendere la chat continua...
    while True:
        try:
            user_input = input("Tu: ")
            response =bot.get_response(user_input)
            print("Chably:", response)
        except(KeyboardInterrupt, SystemExit):
            print("ciao ciao!")
            break    
