from string import ascii_lowercase
import inflect

# declare dictionaries
code = {}
numbercode = {}


# assign numberic values to letters
j = 1
for i in ascii_lowercase:
    code[i] = j
    j += 1


# spell numbers between 0 & 99

numbers = []

ones = ["zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"]
tens = ["zero", "teen", "twenty", "thirty", "fourty",
        "fifty", "sixty", "seventy", "eighty", "ninety"]
suffix = ["hundred", "thousand"]

for i in range(0, len(tens)):
    for j in range(0, len(ones)):
        if ones[j] == "zero":
            numbers.append(tens[i])
        elif tens[i] == "zero":
            numbers.append(ones[j])
        elif tens[i] == "teen":
            numbers.append(ones[j] + tens[i])
        else:
            numbers.append(tens[i] + ones[j])

# assign numbers to their spelt version

k = 0
for i in range(0, len(numbers)):
    numbercode[i] = numbers[i]
    k += 1

#Compare number vs spelt length

matches = []
smaller = []
larger = []

for x in numbercode:
    wordsum = 0
    for l in numbercode[x]:
        wordsum = wordsum + code[l]
    print(x, numbercode[x], wordsum)
    if x == wordsum:
        matches.append(x)
    elif x > wordsum:
        larger.append(x)
    else:
        smaller.append(x)

print("Matches: \n", matches)
print("Smaller: \n", smaller)
print("Larger: \n", larger)
