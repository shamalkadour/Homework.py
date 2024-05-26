# Question1
# A
L1 = ["HTTP", "HTTPS", "FTP", "DNS"]
L2 = [80, 443, 21, 53]
x_dict = {}
for i in range(len(L1)):
    x_dict[L1[i]] = L2[i]

print(x_dict)
