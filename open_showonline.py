from selenium import webdriver
import time

def main():
  bs = webdriver.Chrome()
  bs.get('https://www.showonline.com.cn/')
  time.sleep(3)
  bs.add_cookie({'name': 'user', 'value': '%7B%22isImport%22%3A0%2C%22password%22%3A%22hidden%22%2C%22wechatOpenid%22%3A%22hidden%22%2C%22createTime%22%3A1517813782000%2C%22name%22%3A%22Q%22%2C%22mobile%22%3A%2213588303924%22%2C%22wechatUnionid%22%3A%22hidden%22%2C%22id%22%3A%222c91faca6141995a016164c058b60a25%22%2C%22userType%22%3A3%2C%22dp%22%3A%22https%3A%2F%2Fwww.showonline.com.cn%2Fimage%2F2c91faca5fbdd6dc016164c09b9e1f0d%40thumb.JPG%22%2C%22status%22%3A2%7D', 'domain': '.showonline.com.cn'})
  bs.add_cookie({'name':'accessToken', 'value': '864183e3-1477-48af-8313-45138e8fddc0', 'domain': '.showonline.com.cn'})
  bs.add_cookie({'name':'Hm_lvt_7212311011e441f5bd2fafeff0e4c8f8', 'value': '1539451928', 'domain': '.showonline.com.cn'})
  bs.add_cookie({'name':'Hm_lpvt_7212311011e441f5bd2fafeff0e4c8f8', 'value': '1539454018', 'domain': '.showonline.com.cn'})
  bs.get('https://www.showonline.com.cn/')

  time.sleep(1000000)

if __name__ == '__main__':
  main()