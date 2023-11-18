import math
print("degree\tsin(x)\tcos(x)\ttan(x)\t")
print("#" * 40)
degrees = [0,15,30,45,60,90,18]
for degree in degrees:
    sin = math.sin(math.pi * (degree/180))
    cos = math.cos(math.pi * (degree/180))
    tan = math.tan(math.pi * (degree/180))
    print(f"{degree:2d}\t\t{sin:.4f}\t{cos:.4f}\t{tan:.4f}\t")
