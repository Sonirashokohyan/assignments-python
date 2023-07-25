class1 = {"sepehr", "shaida", "yusof", "bozorg", 'me'}
class2 = {"sepehr", "shaida"}
x = class1.issuperset(class2)
print(x)


myRoom = {"bed", "fan", "desk", "clock", "tv", "chair"}
bozorgRoom = {"bed", "clock", "tv", "chair"}
x = myRoom.issuperset(bozorgRoom)
print(x)