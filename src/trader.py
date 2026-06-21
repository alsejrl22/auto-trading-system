DRY_RUN = True


def buy_stock(stock_code, quantity, price):
    """
    매수 주문 함수

    현재는 안전을 위해 실제 주문을 넣지 않고,
    매수 신호만 출력한다.
    """

    if DRY_RUN:
        print(f"[DRY RUN] 매수 신호 발생: 종목={stock_code}, 수량={quantity}, 가격={price}")
        return

    print("실제 매수 주문 기능은 안전을 위해 비활성화되어 있습니다.")


def sell_stock(stock_code, quantity, price):
    """
    매도 주문 함수

    현재는 안전을 위해 실제 주문을 넣지 않고,
    매도 신호만 출력한다.
    """

    if DRY_RUN:
        print(f"[DRY RUN] 매도 신호 발생: 종목={stock_code}, 수량={quantity}, 가격={price}")
        return

    print("실제 매도 주문 기능은 안전을 위해 비활성화되어 있습니다.")