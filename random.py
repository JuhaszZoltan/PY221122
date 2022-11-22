import random as r

# ZÁRT - ZÁRT intervallumon belül, a két szám közül választ egyet véletlenszerűen (int)
veletlen_szam_1:int = r.randint(10, 100)
print(veletlen_szam_1)

# ZÁRT - NYÍLT [0;1) intervallumon belül előállít egy lebegőpontos számot (float)
veletlen_szam_2:int = r.random()
print(veletlen_szam_2)

# [start; stop) 'step' esével vett számintervallumon belülről választ egyet véletlenszerűen (int)
veletlen_szam_3:int = r.randrange(11, 100, 2)
print(veletlen_szam_3)