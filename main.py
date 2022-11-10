from aplicacion.banco.cliente_bancario import ClienteBancario

#--------------------------------------------#
# try: intenta (correr las instrucciones)    #
# except: atrapar el error en una variable e #
# e se puede convertir a String              #
#--------------------------------------------#

try:
    cliente = ClienteBancario("Jaime Andrade", "Hernández Sánchez", 28, 0.0)
    cliente.guardarDinero(300)
    print(cliente)
    cliente.retirarDinero(400)
    print(cliente)
#---------------------------------------------#
# Exception es el objeto más general de error #
#---------------------------------------------#

except Exception as e:
    print("Error "+str(e))

#------------------------------------#
# Error por usar un atributo privado #
#------------------------------------#

try:
    print(cliente.__nombres)
except Exception as e:
    print("Error "+str(e))

#----------------#
# Forma correcta #
#----------------#

print(cliente.nombres)
