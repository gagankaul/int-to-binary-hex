

print("Welcome to the Binary/Hexadecimal Converter App\n")

num = int(input("Compute binary and hexadecimal values up to the following decimal number: "))
print("Generating lists .... complete!\n")

print("Using slices, we will now show a portion of each list.")
start_num = int(input("What decimal number would you like to start at: "))
end_num = int(input("What decimal number would you like to stop at: "))

dec_list = []
bin_list = []
hex_list = []

for i in range(1,num+1):
    dec_list.append(i)
    bin_list.append(bin(i))

    # bin_num = "{0.b}".format(i)
    # bin_list.append(bin_num)

    hex_list.append(hex(i))

print("\nDecimal Values from " + str(start_num) + " to " + str(end_num))
for i in range(start_num-1, end_num):
    print(dec_list[i])

print("\nBinary Values from " + str(start_num) + " to " + str(end_num))
for i in range(start_num-1, end_num):
    print(bin_list[i])

print("\nHexadecimal Values from " + str(start_num) + " to " + str(end_num))
for i in range(start_num-1, end_num):
    print(hex_list[i])

input("Press Enter to see all values from 1 to 40.")
print("Decimal----Binary----Hexadecimal")
print("----------------------------------------------------")

for dec_num, bin_num, hex_num in zip(dec_list, bin_list, hex_list):
    print(str(dec_num) + "----" + str(bin_num) + "----" + str(hex_num))