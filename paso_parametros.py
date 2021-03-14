def parametros_args(*args):
    return (args)
    
def parametros_kwargs(**kwargs):
    return (kwargs)
    
print(parametros_args(1,2,"hola")) #tupla

aux = parametros_kwargs(a = 1, b = 2, c = "hola") #diccionario

print(tuple(aux.values()))

