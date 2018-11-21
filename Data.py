print("Selamat Datang")

ans=True

while ans:
	print("""
	1.Masukan jumlah stock barang: 
	2.Masukan jumlah barang terjual: 
	3.Check stock barang
	4.keluar
	""")
	ans = input("Masukan Perintah Anda: ")
	if ans=="1":
		item_1 = int(input("Jumlah stock barang LS 155:	"))
		item_2 = int(input("Jumlah stock barang CB 434:	"))
		item_3 = int(input("Jumlah stock barang CB 449:	"))
		item_4 = int(input("Jumlah stock barang CB 494:	"))
		item_5 = int(input("Jumlah stock barang N5 150:	"))
	elif ans=="2":
		sold_1 = int(input("Jumlah stock barang LS 155:	"))
		sold_2 = int(input("Jumlah stock barang CB 434:	"))
		sold_3 = int(input("Jumlah stock barang CB 449:	"))
		sold_4 = int(input("Jumlah stock barang CB 494:	"))
		sold_5 = int(input("Jumlah stock barang N5 150:	"))
	elif ans=="3":
		rest_1 = (item_1-sold_1)
		rest_2 = (item_2-sold_2)
		rest_3 = (item_3-sold_3)
		rest_4 = (item_4-sold_4)
		rest_5 = (item_5-sold_5)
		print("LS 155: ",rest_1)
		print("CB 434: ",rest_2)
		print("CB 449: ",rest_3)
		print("CB 494: ",rest_4)
		print("N5 150: ",rest_5)
	elif ans=="4":
		print("Alhamdulillah")
		exit()

	else:
		print("Masukan nomor perintah yang sesuai!")