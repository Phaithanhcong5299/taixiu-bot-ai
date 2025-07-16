from sheets_helper import *
from lstm_model import predict_with_lstm, update_lstm_model
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

USERNAME = "cauhuy5299"
PASSWORD = "Cauhuy521999!"
MAX_HISTORY = 100

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get("https://web.sun.win")
time.sleep(5)

print("Đang kết nối...")

last_game_id = get_last_game_id()
history = get_recent_results()

while True:
    try:
        game_id, dice, total, result = get_current_game(driver)
        if game_id is None or game_id == last_game_id:
            time.sleep(3)
            continue

        lost = "✅" if game_id - last_game_id > 1 else "—"
        prediction_voting = pattern_vote(history)
        prediction_lstm = predict_with_lstm(history)
        final = prediction_lstm if prediction_lstm == prediction_voting else prediction_voting
        correct = "✅" if final == result else "❌"

        history.append(result)
        if len(history) > MAX_HISTORY:
            history.pop(0)

        acc = calc_accuracy()
        row = [game_id, "-".join(map(str, dice)), total, result,
               prediction_voting, prediction_lstm,
               "✅" if prediction_voting == prediction_lstm else "❌",
               final, correct, f"{acc:.1f}%", lost, timestamp()]
        append_row(row)
        update_latest_100()
        last_game_id = game_id

        if len(history) > 50 and game_id % 50 == 0:
            update_lstm_model(history)

        print(f"[{game_id}] {result} | Dự đoán: {final} ({correct})")
        time.sleep(3)
    except Exception as e:
        print("Lỗi:", e)
        time.sleep(5)
