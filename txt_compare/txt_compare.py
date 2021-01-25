import docx2txt
def wendangzhuanhua(filename):                                         #将word文档转化为txt文档
	text = docx2txt.process(filename+'.docx')
	with open(filename+'.txt', 'w',encoding='utf-8') as file_object:
		file_object.write(text)

def txt_to_list(file_name):
	with open(file_name,encoding='utf-8') as file_object:
		lines=file_object.readlines()
	mylist1=[]

	for line in lines:
		nline=line.replace('\n','').replace('\r','')      
		mylist1.append(nline)  				#'mylist1‘这个列表存贮的是字符串格式的每一行的内容

		                        
	sumlist=[]
	for elems in mylist1:
		for elem in elems:
			sumlist.append(elem)           #将所有字符以字符串形式单个存进列表
	
	return sumlist

def compare(list1,list2):
	same_words=[]
	for word1 in list1:
		for word2 in list2:
			if word1==word2:
				same_words.append(word1)

	same_words = list(set(same_words))    #为防止有字符多次重复，将列表转化为集合，删去重复元素
	print(f'\n 两个文件中共有{len(same_words)}个字符相同，这些字符分别为🙂:\n\t{same_words}.\
		\n其中，第一个文件中有{len(list1)-len(same_words)}个字符与第二个不同； 第二个文件中有{len(list2)-len(same_words)}个字符与第一个不同。\n')

def statistic1(list3):
	sta_sumlist={}                      #将字符及其重复次数用字典存储
	no_same_list=list(set(list3))
	for word in no_same_list:
		sta_sumlist[word]=0
	for elem3 in list3:
		for elem4 in sta_sumlist.keys():
			if elem3==elem4:
				sta_sumlist[elem4]=sta_sumlist[elem4]+1
	sta_sumlist1=sorted(sta_sumlist.items(), key=lambda item:item[1], reverse=True)
	if len(sta_sumlist1)>=10:
		print('前十名高频字符及其重复频率为🙂：')
		for i in range(0,10):
			print(f'\t({sta_sumlist1[i][0]},{sta_sumlist1[i][1]}) ')
	if len(sta_sumlist1)>0 and len(sta_sumlist1)<10:
		print('由于总字符数小于10，故输出所有字符及其重复频率为🙂：')
		for elem in sta_sumlist1:
			print(f'\t{elem}')	
	print()


name1=input("请输入第一个文件名，不需要加后缀名🙂： ")
name2=input("请输入第二个文件名，不需要加后缀名🙂： ")
wendangzhuanhua(name1)
wendangzhuanhua(name2)
list1=txt_to_list(name1+'.txt')
list2=txt_to_list(name2+'.txt')
print('一. 统计第一个文件高频字符：\n')
statistic1(list1)
print('二. 统计第二个文件高频字符：\n')
statistic1(list2)
print('三. 比较两个文件相似度：\n')
compare(list1,list2)
