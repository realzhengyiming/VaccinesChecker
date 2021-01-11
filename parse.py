import urllib.parse


def url_decode(url: str) -> str:
    return urllib.parse.quote(url, safe='/', encoding=None, errors=None)


def url_encode(url: str) -> str:
    return urllib.parse.unquote(url)


url_daling = 'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=4219&lat=22.570261001586914&lng=113.9500732421875'
url_detail = "https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=4219&lat=22.570261001586914&lng=113.9500732421875"

print(url_encode(url_daling))
print(url_decode(url_daling))

print(url_encode(url_detail))
print(url_decode(url_detail))

base_url = 'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?'

parament = 'act=CustomerList&city=%5B%22%E5%B9%BF%E4%B8%9C%E7%9C%81%22%2C%22%E4%B8%9C%E8%8E%9E%E5%B8%82%22%2C%22%22%5D&lat=22.57022476196289&lng=113.95006561279297&id=0&cityCode=441900&product=1'

print(url_decode(parament))
print(url_encode(parament))


def split_parments(strings: str):
    for parments in strings.split("&"):
        key, value = parments.split("=")
        print(f"key:{key}, value:{value}")


split_parments(url_encode(parament))
