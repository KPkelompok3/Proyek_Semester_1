stock ={'LS 155':0,'CB 330 barang':0,'CB 449':0,'CB 494':0,'NS 150':0}

def Menu():
	print("""
		   Harjuna 	  Kacamata
		============Menu=============
		Tekan 1 : Masukan Barang Baru
		Tekan 2 : Tambah Stock Barang
		Tekan 3 : Check Stock Barang
		Tekan 4 : Barang Yang Terjual
		Tekan q : Keluar gann
		=============================
		""")
	return str(input("Masukan pilihan anda: "))

def Barang_Baru():
	try:
		global file
		global addStock
		global jumlah
		global stock

		file = open("Database.txt","a")

		addStock = input("Masukan Barang baru: ")
		jumlah = int(input("Jumlah barang masuk: "))
		stock[addStock] = jumlah

		file.write("'{barang}'".format(addStock) + ":{}\n".format(jumlah))
		file.close()

	except ValueError:
		print("Masukan jumlah barang menggunakan bilangan bulat, bukan teks")
	except KeyError:
		print("Barang yang anda masukan tidak terdaftar.")

def Tambah_Stock():
	try:
		global item
		global stock

		print("Stock yang akan di tambah?")
		for key, value in stock.items():
			print("{}:{}, barang".format(key, value))

		item = input("Masukan Barang yang akan ditambah:")
		stock[item] += int(input("Masukan  Jumlah barang: "))
	
	except ValueError:
		print("Masukan jumlah barang menggunakan bilangan bulat, bukan teks")
	except KeyError:
		print("Barang yang anda masukan tidak terdaftar.")

def Check_Stock():
	try:
		global stock
		global key
		global value

		for key, value in stock.items():
			print("{} tersisa {}2".format(key, value))
	
	except ValueError:
		print("Masukan jumlah barang menggunakan angka, bukan teks")
	except KeyError:
		print("Barang yang anda masukan tidak terdaftar.") 

def Terjual():
	try:	
		global item
		global stock

		item = input("Barang yang terjual: ")
	
		if stock[item] > 0:
			stock[item] -= int(input("Terjual: "))
			print("{} tersisa {}".format(item, stock[item]))
		
		else:
			print("stock barang {} habis".format(item))
	
	except ValueError:
		print("Masukan jumlah barang menggunakan bilangan bulat, bukan teks")
	except KeyError:
		print("Barang yang anda masukan tidak terdaftar.")	