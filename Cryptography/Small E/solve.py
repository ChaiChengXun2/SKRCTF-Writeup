import gmpy2

n=91401655596661773066154930780102428385236855004133210729170159798059723053894336867560347131631952332857718383766118221054743660000104054380881409954672459759905364040450222929481206116665010512840607309735484651457322640684656804214747214675891230694109905235328054635184004465834580499758589565987517821531
e=3
c=4821735227044737729172894050832578813733965898452420107360773622174975905446542522417312328623823461

for t in range(10):
	m, is_true_root = gmpy2.iroot(t * n + c, e)
	if is_true_root:
		print(bytearray.fromhex(format(m, "x")).decode())