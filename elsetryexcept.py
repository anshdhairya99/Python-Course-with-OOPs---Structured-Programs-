# Else & Finally In Try Except:-----------

f1 = open("HRX.txt")

try:
    f = open("does.txt")

except Exception as e:
    print(e)
else:
    print("This will run only if except is not running")
finally:
    print("Run this anyway>>>>")
    f.close()
    f1.close()

    print("Important stuff")
