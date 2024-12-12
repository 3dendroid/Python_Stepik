first, second, third = input (), input (), input ()

min = min (first, second, third)
max = max (first, second, third)
middle = first + second + third
middle = middle.replace (min, "").replace (max, "")

print (min, middle, max)
