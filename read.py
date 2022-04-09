# 讀取資料的留言檔的長度
# 測試印出data清單
# 只印出第0筆看看

#data = []
#with open('reviews.txt', 'r') as f:
	#for line in f:
		#data.append(line)
#print(len(data)) #這是讀取總留言筆數

# print(data) 這是讀取全部的留言

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

print(data[100]) 
print('--------------------------') 
print(data[101]) 
