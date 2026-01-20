a = input().strip()
print(bytes.fromhex(a).decode('latin1'))

#a=input("16진수를 입력하세요: ").strip()
#dec=""

#if len(a) % 2 == 0:
#    for i in range(0, len(a), 2):
#        chunk = a[i:i+2]
#        num = int(chunk, 16)
#        dec += chr(num)
#    print(dec)
#else:
#    print("16진수가 아닙니다.")


# print(hex(a).decode("utf-8"))

# 2de70ca737c1f4602517c555ddd54165432cf231ffc0e21fb2e23b9dd14e7fb4
