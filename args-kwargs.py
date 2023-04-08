
# https://blog.maxkit.com.tw/2018/12/python-args-kwargs.html

def fun(a, *args, **kwargs):
    print("a={}".format(a))
    for arg in args:
        print('Optional argument: {}'.format(arg))

    for k, v in kwargs.items():
        print('Optional kwargs argument key: {} value {}'.format(k, v))


print("")
args = [1, 2, 3, 4]
fun(*args)

print("")
kwargs = {'k1': 10, 'k2': 11}
fun(1, **kwargs)

print("")
fun(1, *args, **kwargs)
