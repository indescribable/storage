# -*- coding: utf-8 -*-

from chatterbot import ChatBot

bot = ChatBot(
    "Math & Time Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter"
    ],
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter",
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer')


#bot.train("chatterbot.corpus.chinese")


# 回答和时间相关的问题

question = "你是谁？"

print(question)

response = bot.get_response(question)

print(response)

# 进行数学计算

question = "What is 4 + 9?"

print(question)
response = bot.get_response(question)

print(response)

print("\n")

# 回答和时间相关的问题

question = "What time is it?"

print(question)

response = bot.get_response(question)

print(response)
