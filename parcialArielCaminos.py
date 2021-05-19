usuario = input('ingrese el usuario:\t')
password = input('Ingrese la contrasena:\t')

minuscula = 0
mayuscula = 0
numero = 0

if (len(password) >= 6 and len(password) <= 12):
    
    for i in password:
        if int(ord(i)) >= int(ord('a')) and ord(i) <= int(ord('z')):
            minuscula += 1
    
    for i in password:
         if int(ord(i)) >= int(ord('A')) and int(ord(i)) <= int(ord('Z')):
            mayuscula += 1
        
    for i in password:
        if ord(i) >= ord('0') and ord(i) <= ord('9'):
            numero += 1
    if minuscula > 0 and mayuscula > 0 and numero > 0:
        print('Hola ', usuario,' el registro de la clave fue exitosa')

    elif minuscula > 0 and mayuscula > 0 and numero == 0:
        print(usuario,': No se registra numero en su clave')

    elif minuscula == 0 and mayuscula > 0 and numero > 0:
        print(usuario,': No se registra minusculas')

    elif minuscula > 0 and mayuscula == 0 and numero > 0:
        print(usuario, ': No se registran mayusculas')

    elif minuscula > 0 and mayuscula == 0 and numero == 0:
        print(usuario,': No se registra numero ni mayusculas en su clave')

    elif minuscula == 0 and mayuscula == 0 and numero == 0:
        print(usuario, ': No se registra ni mayuscula, ni minuscula, ni numeros')

    else:
        print('error')
    

else:
    print(usuario,': la clave ingresada no esta dentro del rango establecido')