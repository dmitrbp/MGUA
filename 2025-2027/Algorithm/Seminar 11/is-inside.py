x1 = float(input('enter x1:'))
y1 = float(input('enter y1:'))
x2 = float(input('enter x2:'))
y2 = float(input('enter y2:'))

left = min(x1, x2)
right = max(x1, x2)
top = min(y1, y2)
bottom = max(y1, y2)

x = float(input('enter x:'))
y = float(input('enter y:'))

inside = (x >= left and x <= right and y >= top and y <= bottom)
print(inside)