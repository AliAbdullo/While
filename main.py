savol = 'Yoqtirgan kitobingizni yozing '
savol+= F"(Agar 'exit'ni yozsangiz dastur to'xtaydi)"

while True:
  kitob = input(savol)
  if kitob == 'exit':
    break
  else:
    print(kitob)

#chipta narxlari
savol = 'Yoshingizni kiriting '
savol+=f"(Qimatlik qilsa 'Stop' deb yozing va do'stingizdan so'rab turing): "

while True:
  yosh=input(savol)
  if yosh =='stop'or yosh=='exit'or yosh=='quit':
    break
  son = int(yosh)  
  if son <7:
     narx=2000
  elif son<18:
     narx = 3000
  elif son<65:
    narx=10000
  elif son>65:
    narx= 0
  if narx==0:
    print("Sizga chipta bepul")
    
  else:
    print(f'Chipta {narx} so\'m')
  

 
