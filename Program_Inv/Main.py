import library.lib as lib

print("Program Inventory")

while True:
	run = lib.Menu()
	if run == '1':
		lib.Barang_Baru()

	elif run =='2':
		lib.Tambah_Stock()
			
	elif run == '3':
		lib.Check_Stock()

	elif run == '4':
		lib.Terjual()

	elif run == 'q':
		break

	else:
		print("Masukan Pilihan yang tepat!")

print("Terima Kasih")