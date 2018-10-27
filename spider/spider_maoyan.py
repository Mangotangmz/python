import requests
import re


# http://p0.meituan.net/movie/283292171619cdfd5b240c8fd093f1eb255670.jpg@160w_220h_1e_1c



def get_one_page(offset):
	url = "http://maoyan.com/board/4?offset=%d" % offset
	headers =  {
		"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)" 
	}
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		# print(response.text)
		return response.text
	return None


def parse_one_page(html):
	# 排名信息 
	# pattern = re.compile("<dd>.*?board-index.*?>(.*?)</i>", re.S)
	# 加 图片链接
	# pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?<img.*?<img.*?src="(.*?)"', re.S)
	# 加 主演 上映时间
	# pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?<img.*?<img.*?src="(.*?)".*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>', re.S)

	# pattern = re.compile("movieId.*?>(.*?)</a>", re.S)

	# pattern = re.compile('<p class="star">(.*?)</p>', re.S)
	pattern = re.compile('movieId.*?>.*?<img.*?<img.*?alt="(.*?)" class.*?', re.S)

	# pattern = re.compile('movieId.*?>.*?<img.*?<img.*?src="(.*?)"', re.S)

	items = re.findall(pattern, html)
	
	return items		

def get_all_page():
	for i in range(1):
		offset = i * 0
		html = get_one_page(offset)
		items = parse_one_page(html)
		print(items)
		# for item in items:
		# 	# print(item)
		# 	write_img(item)

def write_img(url):
	url_parts = url.split("@")
	url_result = url_parts[0]
	filename = "./images/%s" % url_result.split("/")[-1]
	print(filename)

	r = requests.get(url)
	with open(filename, "wb") as f:
		f.write(r.content) 

def main():
	get_all_page()

if __name__ == "__main__":
	main()
