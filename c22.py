niemyet=int(input('Nhap Gia niem yet: '))
chietkhau=int(input('Nhap Chiet khau: '))
vat=(niemyet - chietkhau)*0.01
giaban= niemyet - chietkhau + vat
print('Gia ban: ',giaban)