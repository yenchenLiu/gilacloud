import os
import heapq

urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]

file_count = {}
for url in urls:
    file_name = os.path.split(url)[1]
    if file_name not in file_count:
        file_count[file_name] = 0
    file_count[file_name] += 1

heap = [(value, key) for key,value in file_count.items()]
largest = heapq.nlargest(3, heap)
for value, key in largest:
    print(key, value)
