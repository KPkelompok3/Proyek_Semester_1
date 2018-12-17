import library.tes as lib

print("Program Inventory")

while True:
	run = lib.Menu()
	if run == '1':
		lib.coba():
			lib.Barang_Baru()
		lib.error()

	elif run =='2':
		lib.coba():
			lib.Tambah_Stock()
		lib.error()
			
	elif run == '3':
		lib.coba():
			lib.Check_Stock()
		lib.error()

	elif run == '4':
		lib.coba():
			lib.Terjual()
		lib.error()
			
	elif run == 'q':
		break

	else:
		print("Masukan Pilihan yang tepat!")

print("Terima Kasih")