import datetime as dt
import os

import telegram
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
CURRENT_DATE = dt.datetime.now().date()
HAMOLTON_TOOLS = {
    'Reader Check Plate _1529_\n 28.02.2022': dt.date(2023, 2, 27),
    'Scale WXS _C112364454_\n 01.04.2022': dt.date(2023, 4, 1),
    'Carrier VK _V0106115_\n 18.05.2021': dt.date(2023, 5, 18),
    'Carrier SK _V0105708_\n 10.03.2021': dt.date(2023, 3, 10),
    'IR Sensor _20080026_\n 10.01.2023 (exp)': dt.date(2023, 1, 10),
    'HMD _83208494_\n 16.09.2021': dt.date(2022, 9, 16),
    'Calibration Weight (20 g) _C114466011_\n 15.03.2021': dt.date(2023, 3, 15),
    'WIKA Pressure Sensor _1035_\n 11.01.2022': dt.date(2023, 1, 11),
    'Channel Calibration Tool _3891_\n 13.04.2021': dt.date(2023, 4, 13),
    '384 Adjustment Tool _1296_\n 29.03.2021': dt.date(2023, 3, 29),
    '96 Adjustment Tool _1558_\n 25.11.2020': dt.date(2022, 11, 25),
    'iSWAP\n 19.08.2021': dt.date(2023, 8, 19),
}
bot = telegram.Bot(token=TELEGRAM_TOKEN)


def report_generator(current_date):
    report = []
    for i in HAMOLTON_TOOLS:
        date = (HAMOLTON_TOOLS[i] - current_date).days
        if date <= dt.timedelta(days=90).days:
            date = f'*{date}*'
        report.append("*-* " + f'{i} - {date} days' + "\n")
    return (
        "*Hamilton tools calibration date expiry report:*\n"
        + "\n" + "\n".join(report)
    )


def send_report(report):
    bot.send_message(chat_id=CHAT_ID, text=report, parse_mode='markdown')


def main():
    try:    
        send_report(report_generator(CURRENT_DATE))
    except Exception as e:
        send_report(f'Возникла ошибка - {e}')

main()
