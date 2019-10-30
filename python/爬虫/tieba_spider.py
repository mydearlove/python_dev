# author wangzhaoyang
import requests


class TiebaSpider(object):
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "http://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

    def get_url_list(self):  # g构造url列表
        return [self.url_temp.format(i * 50) for i in range(10)]

    def parse_url(self, url):  # 发送请求，获取响应
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()  # 不管是什么编码格式，都转换成Unicode

    def save_html(self, html_str, page_num):
        file_path = "{}-第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(html_str)

    def run(self):  # 实现最要逻辑
        # 1构造url列表
        url_list = self.get_url_list()
        # 遍历，发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 保存
            page_num = url_list.index(url) + 1  # 页码数
            self.save_html(html_str, page_num)


if __name__ == '__main__':
    tieba_spider = TiebaSpider('李毅')
    tieba_spider.run()
