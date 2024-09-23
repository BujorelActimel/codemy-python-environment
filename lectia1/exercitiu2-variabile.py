# Stefan - abc5, 8, abcabcabc9
# Aron   - 
# Ioan   - abca, 8, abc5abc5abc5...9
# Bujor  - "abca", 8, "abcabcabc9"

x = "abc"
y = 3
z = x * y + "9"  #"abc" * 3 + "9" = "abcabcabc" + "9" = "abcabcabc9"
a = "5"
x = x + "a"      # x = "abc" + "a" = "abca"
y = y + int(a)   # y = 3 + 5 = 8

print(x, y, z)