def crc(data, generator):
    code = data
    while len(code) < len(data) + len(generator) - 1:
        code += "0"
    remainder = div(code, generator)
    return data + remainder

def div(num1, num2):
    pointer = len(num2)
    result = num1[0:pointer]
    remainder = ""
    for i in range(len(num2)):
        if result[i] == num2[i]:
            remainder += "0"
        else:
            remainder += "1"
    while pointer < len(num1):
        if remainder[0] == '0':
            remainder = remainder[1:]
            remainder += num1[pointer]
            pointer += 1
        result = remainder
        remainder = ""
        for i in range(len(num2)):
            if result[i] == num2[i]:
                remainder += "0"
            else:
                remainder += "1"
    return remainder[1:]

data = input("Data: ")
generator = input("Generator: ")
code = crc(data, generator)
print("Transmitted code word:", code)

received = input("Received: ")
remainder = div(received, generator)
if int(remainder) == 0: print("Received code word has no errors.")
else: print("Received code word has errors.")
