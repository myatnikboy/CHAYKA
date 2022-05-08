#start: export FLASK_APP=main.py && python3 -m flask run --host=0.0.0.0 --cert=adhoc

from flask import Flask, request
import logging
import json
import random

app = Flask(__name__)

name1 = ["пива", "садоводства", "почтения памяти", "праздника", "малосольных огурчиков",
        "шампанского", "водки", "куклы Барби", "истории", "математики", "трамвая", "похмелья",
        "статуи", "северного оленя", "борща", "белочки", "варенья", "оладушек", "дня", "тортика",
        "капусты", "туалета", "электронной почты", "рождения Винни-Пуха", "яблока", "комиксов",
        "туалетной бумаги", "года", "вареника", "пельмений", "гомункола", "русско-китайского словаря",
        "словаря", "таблеток", "кактуса", "огурца", "слоновой кости", "помидоров", "тунца", "сварщика"]

logging.basicConfig(level=logging.DEBUG)

@app.route("/", methods=["POST"])
def main():
    logging.info(request.json)

    response = {
        "version": request.json["version"],
        "session": request.json["session"],
        "response": {
            "end_session": False
        }
    }

    req = request.json
    if req["session"]["new"]:
        response["response"]["text"] = "Привет! Знаешь какой сегодня праздник? Или ты хочешь узнать?"
    else:
        if req["request"]["original_utterance"].lower() in ["хочу", "давай", "да", "почему бы и нет"]:
            random.shuffle(name1)
            response["response"]["text"] = "Смотри, а ты знал, что сегодня классный праздник!\nСегодня праздник: День %"%name1
        elif req["request"]["original_utterance"].lower() in ["нет", "не знаю"]:
            response["response"]["text"] = "Это печально... Давай я тебе щас скажу, а ты запомнишь, хорошо?\nСегодня праздник: День %"%name1

    return json.dumps(response)