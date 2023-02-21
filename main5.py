# try:
#     #name = "Serhii"
#     print("Start code")
#     #print(name)
#     print(2 / 0)
#     print('No errors')
# except:
#     print('We have a problem (error).')
#
# print('This code after capsule.')

# try:
#     print('start code')
#     print(name)
#     print(2 / 0)
#     print("no errors.")
# except NameError:
#     print('We have a NameError.')
# except ZeroDivisionError:
#     print('We have a ZeroDivisionError')
#
# print('This code afet capsule')

# try:
#     print('Start code')
#     print(2 / 0)
#     print(name)
#     print('no error')
# except (NameError, ZeroDivisionError):
#     print('We have an Error')
#
# print('code after error')

# try:
#     try:
#         print('start code')
#         print(error)
#         print('no errors')
#     except SyntaxError:
#         print("Wrong Syntax")
# except NameError as error:
#     print(error)


# try:
#     #error = 'q'
#     print('start code')
#     print(error)
#     print('no errors')
# except NameError as error:
#     print(error)
# else:
#     print('I am ELSE')
# finally:
#     print('Finally code')


result = []
def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b



try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
except SyntaxError:
    print('Wrong Syntax')

for key in data:
    res = divider(key, data[kem])
    result.append(res)

print(result)