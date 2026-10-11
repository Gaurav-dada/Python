sec=100000

hour=sec//3600
z=sec%3600
x=z%60
minute=z//60

print(f"{hour}hh:{minute}min:{x}sec")
    