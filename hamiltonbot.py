import datetime as dt
import os

import telegram
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
CURRENT_DATE = dt.datetime.now().date()
HAMOLTON_TOOLS = {
    'Reader Check Plate _1611_\n 08.01.2024': dt.date(2025, 1, 8),
    'Scale WXS _C112364454_\n 19.01.2024': dt.date(2025, 1, 18),
    'Carrier VK _V0106200_\n 25.08.2022': dt.date(2024, 8, 24),
    'IR Sensor _20101162_\n 28.06.2023 (exp)': dt.date(2024, 6, 28),
    'HMD _83321741_\n 16.06.2023': dt.date(2024, 6, 16),
    'Calibration Weight (20 g) _158437_\n 22.02.2023': dt.date(2025, 2, 22),
    'WIKA Pressure Sensor _4776633_\n 09.11.2022': dt.date(2023, 11, 9),
    'Channel Calibration Tool _3891_\n 13.04.2021': dt.date(2023, 4, 13),
    '384 Adjustment Tool _1296_\n 29.03.2021': dt.date(2023, 3, 29),
    '96 Adjustment Tool _2084_\n 19.05.2022': dt.date(2024, 5, 19),
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

if __name__ == "__main__":
    main()
