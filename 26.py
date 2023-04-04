hoten=input('Ho ten: ')
ngaycong=int(input('So ngay cong: '))
DonGia=int(input('Don gia ngay cong: '))
HeSo=float(input('He so phu cap: '))
TamUng=int(input('Tam ung: '))
luong=ngaycong*DonGia*HeSo
thuclinh=luong-TamUng
print('Nhan vien ',hoten,',',sep='',end='')
print(' Co tien Luong=',luong,sep='',end='')
print(',',sep='',end='')
print(' Tam ung=',round(TamUng,1),sep='',end='')
print(' va Thuc linh=',round(thuclinh,1),sep='')