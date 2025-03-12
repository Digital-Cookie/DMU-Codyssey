try:
	with open("Mars_Base_Inventory_List.csv", "r") as read:
		file = read.readlines()
except:
    print('Error in reading file.')
else:
	for i in file:
		print(i.strip())

	data = [i.strip().split(",") for i in file[1:]]

	data.sort(key = lambda k: float(k[4]), reverse = True)

	with open("Mars_Base_Inventory_List.bin", "wb") as write_binary:
		write_binary.write(file[0].encode())
		for i in data:
			i = ','.join(i) + '\n'
			write_binary.write(i.encode())

	with open("Mars_Base_Inventory_List.bin", "rb") as read_binary:
		data_binary = read_binary.read().decode()
	
	print(data_binary)

	#이진 파일은 0과 1로 저장된다
	#텍스트 파일도 이진파일인데, ASCII 같은 인코딩으로 사람이 읽을 수 있는 문자로 저장된다
	#장단점: 텍스트 파일은 다른 시스템에 쉽게 전송할 수 있지만 이진 파일은 안된다
	#장단점: 이진 파일은 프로그램에서 처리하는 데 걸리는 시간이 텍스트 파일 보다 적다

	new_data = [file[0].strip().split(",")] + [i for i in data if float(i[4]) >= 0.7]

	with open("Mars_Base_Inventory_danger.csv", "w") as write:
		for i in new_data:
			print(i)
			write.write(','.join(i) + '\n')
