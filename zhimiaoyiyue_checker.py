import json

import requests
import schedule
import time

from settings import REFERER, USER_AGENT


def make_request(url, user_agent: str = USER_AGENT, referer: str = REFERER):
    #  url = 'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=GetCat2&id=1'
    response = requests.get(url=url, headers={"User-Agent": user_agent, 'referer': referer})
    if response.status_code != 200:
        print()
    return response.text


url_dongguan = 'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerList&city=%5B%22%E5%B9%BF%E4%B8%9C%E7%9C%81%22%2C%22%E4%B8%9C%E8%8E%9E%E5%B8%82%22%2C%22%22%5D&lat=22.57022476196289&lng=113.95006561279297&id=0&cityCode=441900&product=1'


# 格式化成2016-03-20 11:45:39形式
def check_dongguandalingshan():
    url_detail = "https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=4219&lat=22.570261001586914&lng=113.9500732421875"
    response_text = make_request(url_detail)
    now_date = time.strftime("%m-%d", time.localtime())  # todo判断出还没开始的，
    print(f"now is {now_date}")
    json_response = json.loads(response_text)
    for i in json_response["list"]:
        if i['text'].find("九价") != -1 and i['BtnLable'] != "立即预约":
            print(i['date'].split(" ")[0])


schedule.every().day.at("00:00").do(check_dongguandalingshan, url_dongguan)
while True:
    schedule.run_pending()
    time.sleep(10)  # TODO add email and settings the remote environment
