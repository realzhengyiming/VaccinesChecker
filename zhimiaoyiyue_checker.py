import requests

from settings import REFERER, USER_AGENT


def make_request(url, user_agent: str = USER_AGENT, referer: str = REFERER):
    #  url = 'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=GetCat2&id=1'
    response = requests.get(url=url, headers={"User-Agent": user_agent, 'referer': referer})
    if response.status_code!=200:
        print()
    return response.text
