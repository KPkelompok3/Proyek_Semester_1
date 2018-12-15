print("Program Inventory")

def menu():
	print("""
		   Harjuna 	  Kacamata
		============Menu=============
		Tekan 1 : Masukan Barang Baru
		Tekan 2 : Tambah Stock Barang
		Tekan 3 : Check Stock Barang
		Tekan 4 : Barang Terjual
		Tekan q : Keluar
		=============================
		""")
	return str(input("Masukan pilihan anda: "))



stock ={'LS 155':0,'CB 434':0,'CB 449':0,'CB 494':0,'NS 150':0}


while True:
	run = menu()
	if run == '1':
		
		file = open("Database.txt","a")
		
		addStock = input("Masukan Barang baru: ")
		jumlah = int(input("Jumlah barang masuk: "))
		stock[addStock] = jumlah

		file.write("{}".format(addStock) + ": {}\n".format(jumlah))
		file.close()

	elif run =='2':
		print("Stock yang akan ditambah?")
		for key in stock.items():
			print("{}".format(key))
		item = input("Masukan Barang yang akan ditambah:")
		stock[item] += int(input("Masukan  Jumlah barang: "))	

	elif run == '3':
		for key, value in stock.items():
			print("{} tersisa {}".format(key, value)) 

	elif run == '4':
		item = input("Barang yang terjual: ")
		if stock[item] > 0:
			stock[item] -= int(input("Terjual: "))
			print("{} tersisa {}".format(item, stock[item]))
		else:
			print("stock barang {} habis".format(item))
	
	elif run == 'q':
		break

	else:
		print("Masukan Pilihan yang tepat!")

print("Terima Kasih")
