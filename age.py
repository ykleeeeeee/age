#流程: 1.建立專案 2.寫有的部分 3.寫沒有的部分 4.寫其他部分 5.上傳

driving = input('請問你有開過車嗎?')
if driving != '有' and driving != '沒有':
    print('只能輸入  有/沒有')
    raise SystemExit

age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你聰過測驗了')
	else:
		print('奇怪  你怎麼會有開過車?')
elif driving == '沒有':
    if age >= 18:
    	print('你可以考駕照了啊, 怎麼還不去考?')
    else:
    	print('很好,  再過幾年就可以考駕照了')
