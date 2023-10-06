def base(x):
    def interior(y):
        return x+y
    return interior


def base(x):
    def suma(y):
        return x+y
    def resta(y):
        return x-y
    return[suma,resta]


usoFuncion=base(10)
print(usoFuncion[0](20))
