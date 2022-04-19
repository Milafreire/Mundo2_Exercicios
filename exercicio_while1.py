from numpy import kaiser


sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo  = str(input('Dados inválidos. Por favor, informe o seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')