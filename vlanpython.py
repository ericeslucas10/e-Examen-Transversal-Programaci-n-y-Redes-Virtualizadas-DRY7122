vlan = int(input("ingresar la vlan: "))

if 1 <= vlan <= 1005:
    print("La VLAN es normal (1-1005)")
elif 1006 <= vlan <= 4094:
    print("La VLAN es EXTENDIDO (1006-4094)")
