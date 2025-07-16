import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("1SIS3lmnY74EYhT0n0KEHYmgzJp_0NeipUmHEhWaV5r0").worksheet("Main")
latest_sheet = client.open_by_key("1SIS3lmnY74EYhT0n0KEHYmgzJp_0NeipUmHEhWaV5r0").worksheet("100_van_moi_nhat")

def append_row(data):
    sheet.append_row(data)

def get_last_game_id():
    try:
        rows = sheet.get_all_values()
        for row in reversed(rows):
            if row[0].isdigit():
                return int(row[0])
    except:
        return 0
    return 0

def get_recent_results(n=100):
    try:
        rows = sheet.get_all_values()
        results = [row[3] for row in rows if row[3] in ("Tài", "Xỉu")]
        return results[-n:]
    except:
        return []

def pattern_vote(history):
    if len(history) < 10:
        return "Tài"
    recent = history[-3:]
    patterns = {}
    for i in range(len(history) - 3):
        key = tuple(history[i:i+3])
        next_result = history[i+3]
        if key not in patterns:
            patterns[key] = []
        patterns[key].append(next_result)
    votes = patterns.get(tuple(recent), [])
    if votes.count("Tài") > votes.count("Xỉu"):
        return "Tài"
    return "Xỉu" if votes else "Tài"

def calc_accuracy():
    try:
        rows = sheet.get_all_values()
        correct = sum(1 for row in rows if row[8] == "✅")
        total = sum(1 for row in rows if row[8] in ("✅", "❌"))
        return (correct / total) * 100 if total else 0
    except:
        return 0

def update_latest_100():
    try:
        data = sheet.get_all_values()
        latest = data[-100:] if len(data) >= 100 else data
        latest_sheet.clear()
        latest_sheet.append_rows(latest)
    except:
        pass

def timestamp():
    return datetime.now().strftime("%H:%M:%S")
