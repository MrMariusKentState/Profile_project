#1. Basic

for x in range(0, 151):
    print(x)


#2. Multiples of Five

for x in range(5,1001,5):
    print(x)

#3. Counting, the Dojo Way

for x in range(1,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")

#4. Whoa. That sucker's huge

sum = 0;
i = 1;

while i < 500000:
    sum = sum + i
    i = i + 2

print(sum)


#5. Countdown by fours:

i = 2018;

while i > 0:
    print(i)
    i = i - 4

#6. Flexible counter:

lownum = 1;
highnum = 11;
mult = 4;

for x in range(lownum, highnum + 1):
    if x % mult == 0:
        print(x)