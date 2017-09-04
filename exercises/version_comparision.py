ver1 = "9.0.4.1"
ver2 = "8.1.4.5"

num1 = ver1.split(".")
num2 = ver2.split(".")
print num1, num2
while(num1 and num2):
  if(atoi(num1) > atoi(num2)):
    return 1
  if(atoi(num1) < atoi(num2)):
    return -1
  num1 = ver1.split(".")
  num2 = ver2.split(".")

if(num1 == NULL and num2 == NULL):
  return 0
if(num1):
  return 1
if(num2):
  return -1
