name1 = str(input('Introduce el primer nuemro : '))
name2 = str(input('Introduce el segundo nombre : '))

def mixChars (name1, name2):
    #                               0 a 2                   3 al final
    name_mix = name2[:3] + name1[3:]
    name_mix2 = name1[:3] + name2[3:]
    salida_name = ('Salida del nombre revuelto1 \"{}\"  || nombre revuelto2 \"{}\"enla '. format(name_mix,name_mix2))
    return salida_name

print(mixChars(name1,name2))
