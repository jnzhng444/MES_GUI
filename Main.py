from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt

#Iniciar applicacion
app = QtWidgets.QApplication([])

#Cargas archivos .ui
loginSup= uic.loadUi("Login supervisora.ui")
loginOp= uic.loadUi("Login operario.ui")
menuSup=uic.loadUi("Menu supervisora.ui")

# Ocultar la barra de título
loginSup.setWindowFlags(Qt.WindowType.FramelessWindowHint)
loginOp.setWindowFlags(Qt.WindowType.FramelessWindowHint)
menuSup.setWindowFlags(Qt.WindowType.FramelessWindowHint)


# Hacer el fondo transparente
loginSup.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
loginOp.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
menuSup.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

#Variables
failed_Login = 0


#Login de supervisor/a
def sup_Login():
    global failed_Login
    user = loginSup.lineEdit.text()
    password = loginSup.lineEdit_2.text()
    loginSup.lineEdit.clear()
    loginSup.lineEdit_2.clear()
    if len(user) == 0 or len(password) == 0:
        loginSup.label_3.setText("Estimado/a usuario, porfavor ingrese todos los datos.")
    elif user == "jian" and password == "1234":
        menu_Sup()
    else:
        failed_Login += 1
        if failed_Login==3:
            loginSup.lineEdit.setDisabled(True)
            loginSup.lineEdit_2.setDisabled(True)
            loginSup.pushButton_3.setDisabled(True)
            loginSup.label_3.setText("Has alcanzado el máximo de intentos fallidos.")
        else:
            loginSup.label_3.setText("Estimado/a usuario, los datos ingresados son incorrectos.")

#Cambiar de pestanas
def menu_Sup():
    loginSup.hide()
    menuSup.show()

def switch_Sup_Op():
    loginSup.hide()
    loginOp.show()

def switch_Op_Sup():
    loginOp.hide()
    loginSup.show()


def exit():
    app.exit()

#Se conectan los botones con funciones
loginSup.pushButton_2.clicked.connect(exit)
loginOp.pushButton_2.clicked.connect(exit)
menuSup.pushButton.clicked.connect(exit)
loginSup.pushButton.clicked.connect(switch_Sup_Op)
loginOp.pushButton.clicked.connect(switch_Op_Sup)
loginSup.pushButton_3.clicked.connect(sup_Login)



#Ejecutable
loginSup.show()
app.exec()