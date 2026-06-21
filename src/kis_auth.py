import requests
from config import BASE_URL, APP_KEY, APP_SECRET, check_config


def get_access_token():
    check_config()

    url = f"{BASE_URL}/oauth2/tokenP"

    headers = {
        "content-type": "application/json"
    }

    body = {
        "grant_type": "client_credentials",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET
    }

    response = requests.post(url, headers=headers, json=body)
    data = response.json()

    if "access_token" not in data:
        print("토큰 발급 실패")
        print(data)
        raise RuntimeError("access_token을 받지 못했습니다.")

    return data["access_token"]


if __name__ == "__main__":
    token = get_access_token()
    print("access token 발급 성공")
    print(token[:20] + "...")