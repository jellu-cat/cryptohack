from binascii import unhexlify

"""
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf 
"""

def xor_keys(x, y):
    """Returns the xor of two hexadecimal strings."""
    # Since xor (^) works with numbers, first i need to
    # turn the string in hex numbers
    # The output of xor is a number in decimal form, so i need
    # to format it
    return format(int(x, 16) ^ int(y, 16), 'x')
    

# k_1
KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
# print("key1", "=", key1)

# k_2 ^ k_3
KEY2_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
# print("key23", "=", key23)

# f ^ a ^ b
X = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# ## ---------

# # since (f ^ key1 ^ key2_3) = (f ^ a)
# # and (f ^ a = x) ==> (f = x ^ a)

a = xor_keys(KEY1, KEY2_3)
print(f"[-] K1 ^ K2 ^ K3 = {a}")

flag = xor_keys(a, X)
print(f"[-] FLAG = {flag}")

# unhexlify() in this case returns the binary representation (ascii) of each hex digit in the number
print(f"[*] FLAG = {unhexlify(flag)}")

