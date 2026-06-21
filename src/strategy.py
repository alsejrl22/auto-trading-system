def simple_strategy(prices):
    """
    최근 가격 데이터를 이용해 BUY / SELL / HOLD 신호를 만든다.

    prices 예시:
    [21300, 21400, 21500, 21600, 21700]
    """

    # 가격 데이터가 5개보다 적으면 아직 판단하지 않는다.
    if len(prices) < 5:
        return "HOLD"

    # 최근 5개 가격만 사용한다.
    recent_prices = prices[-5:]

    # 최근 5개 가격의 평균을 계산한다.
    average_price = sum(recent_prices) / len(recent_prices)

    # 가장 최근 가격을 현재 가격으로 사용한다.
    current_price = prices[-1]

    # 현재 가격이 최근 평균보다 0.2% 이상 높으면 매수 신호
    if current_price > average_price * 1.002:
        return "BUY"

    # 현재 가격이 최근 평균보다 0.2% 이상 낮으면 매도 신호
    elif current_price < average_price * 0.998:
        return "SELL"

    # 그 외에는 대기
    else:
        return "HOLD"