'''
prueba clase Persona_parametrizada
Fecha: 05/09/2024
'''
# del arcivo clases.py importar solo Persona_parametrizada
from clases import Persona_parametrizada as pp
per1 = pp()
per2 = pp('Juan')
per3 = pp('Maria', 50)
print(per1)
print(per2)
print(per3)
per3.caminar(16,'campo')
print(per3)