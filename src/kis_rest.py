import requests

from kis_auth import get_access_token
from config import BASE_URL, APP_KEY, APP_SECRET


def get_current_price(access_token, stock_code):
    """
    한국투자증권 Open API로 국내 주식 현재가를 조회한다.

    stock_code:
    - 태성: 323280
    """

    url = f"{BASE_URL}/uapi/domestic-stock/v1/quotations/inquire-price"

    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {access_token}",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET,
        "tr_id": "FHKST01010100",
    }

    params = {
        "fid_cond_mrkt_div_code": "J",
        "fid_input_iscd": stock_code,
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if "output" not in data:
        print("현재가 조회 실패")
        print(data)
        raise RuntimeError("현재가 데이터를 받지 못했습니다.")

    current_price = data["output"]["stck_prpr"]
    return int(current_price)


if __name__ == "__main__":
    token = get_access_token()

    stock_code = "323280"  # 태성
    price = get_current_price(token, stock_code)

    print(f"종목명: 태성")
    print(f"종목코드: {stock_code}")
    print(f"현재가: {price}원")