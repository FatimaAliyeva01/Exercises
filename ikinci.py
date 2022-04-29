# 2) İstifadəçidən aldığı ədədin tək və ya cüt olmasını təyin edən skript

print('Zəhmət olmasa ədəd qeyd edin:')
a = input()

b = []
for i in a:
  if i % 2 != 0:
      b.append(i)
print(b)


