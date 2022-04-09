# 讀取資料的留言檔的長度
# 測試印出data清單
# 只印出第0筆看看

#data = []
#with open('reviews.txt', 'r') as f:
	#for line in f:
		#data.append(line)
#print(len(data)) #這是讀取總留言筆數

#print(data) 這是讀取全部的留言

#print(data[0]) #這是讀取第一筆留言
#print('--------------------------') #這是印出分隔符號
#print(data[1]) #然後再印出第二筆留言

# 延伸功能: 在讀取檔案過程中, 印出len(data), 才知道讀取進度
# 方法: 加入變數count, 讓檔案美讀取一則留言count就加1, 
# 方始: 當count的數字除以10000的餘數是0, 也就是讀到100000的倍數時, 印出來

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))

print('檔案讀取完了, 總共有', len(data), '筆資料')

# 進階挑戰:算出每筆留言的平均長度
# 解決方法:把字串d當成清單,用len()去抓出每一筆留言的長度
# 解決方法:用for loop的功能, 將data清單中的每筆留言(d)都抓出來, 並將每筆留言的字母數長度加總
# 解決方法:最後再將加總結果(總字母數),除以總筆數

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data))

# 加入篩選的概念
# 挑戰: 篩選出留言字母數小於100的筆數
# 重點: 先寫一個for loop, 就是一筆一筆把清單裡的資訊抓出來
# 重點: 如果字母樹長度小於100, 就把它裝進new清單中

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有',len(new),'筆留言的字母數低於100個字')

print(new[100])
print(new[101])

