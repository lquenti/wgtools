import json
import os

from datetime import datetime, date, timedelta

BASE_PATH: str = os.path.dirname(os.path.realpath(__file__))
WG_FILENAME: str = "wg.json"
WG_FILEPATH: str = os.path.join(BASE_PATH, WG_FILENAME)

suffix = """has cleaning duty this week
This includes the following:
- Take out the trash (2 bins outside, 2 in the kitchen)
- Take out the glass under the sink
- Wash the common utilities, i.e. all kitchen towels, both bath mats, and both bath hand towels. The dirty towels can be found next to the wooden bank in the living room, the clean ones can be found in shelf 11b."""

def generate_message(who):
    return f"{who} {suffix}"

def read_cfg():
    with open(WG_FILEPATH) as fp:
        d = json.load(fp)
        return d['flatmates'], datetime.fromisoformat(d['starting_date']).date()

def calculate_current_flatmate(flatmates, starting_date):
    today = date.today()
    last_monday = today - timedelta(days=today.weekday())
    current_flatmate = 0
    while starting_date < last_monday:
        current_flatmate = (current_flatmate + 1) % len(flatmates)
        starting_date += timedelta(days=7)
    return flatmates[current_flatmate]


def main():
    flatmates, starting_date = read_cfg()
    current_flatmate = calculate_current_flatmate(flatmates, starting_date)
    print(generate_message(current_flatmate))


if __name__ == "__main__":
    main()
