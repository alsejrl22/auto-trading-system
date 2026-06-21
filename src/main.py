import time
import csv
from datetime import datetime
from pathlib import Path

from kis_auth import get_access_token
from kis_rest import get_current_price
from strategy import simple_strategy
from trader import buy_stock, sell_stock


def save_log(stock_name, stock_code, price, signal):
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    file_path = data_dir / "trading_log.csv"
    file_exists = file_path.exists()

    with open(file_path, "a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["time", "stock_name", "stock_code", "price", "signal"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            stock_name,
            stock_code,
            price,
            signal
        ])


def main():
    stock_name = "태성"
    stock_code = "323280"

    prices = []

    print("====================================")
    print("한투 API 자동매매시스템 시작")
    print("현재 모드: DRY_RUN")
    print("실제 주문은 실행되지 않습니다.")
    print(f"대상 종목: {stock_name}({stock_code})")
    print("====================================")

    access_token = get_access_token()
    print("access token 발급 완료")

    try:
        while True:
            price = get_current_price(access_token, stock_code)
            prices.append(price)

            signal = simple_strategy(prices)
            save_log(stock_name, stock_code, price, signal)

            print("------------------------------------")
            print(f"종목명: {stock_name}")
            print(f"종목코드: {stock_code}")
            print(f"현재가: {price}원")
            print(f"저장된 가격 개수: {len(prices)}개")
            print(f"매매 신호: {signal}")

            if signal == "BUY":
                buy_stock(stock_code, quantity=1, price=price)

            elif signal == "SELL":
                sell_stock(stock_code, quantity=1, price=price)

            else:
                print("대기합니다.")

            time.sleep(10)

    except KeyboardInterrupt:
        print("\n자동매매시스템을 종료합니다.")


if __name__ == "__main__":
    main()