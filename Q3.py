year=int(input("請輸入西元年: "))
an={4:"rat",5:"ox",6:"tiger",7:"rabbit",8:"dragon",9:"snake",10:"horse",11:"sheep",12:"monkey",1:"rooster",2:"dog",3:"pig"}
ans=year%12
print(an[ans])