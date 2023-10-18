from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QMessageBox

#Iniciar applicacion
app = QtWidgets.QApplication([])

#Cargas archivos .ui
loginSup= uic.loadUi("Login supervisora.ui")
loginOp= uic.loadUi("Login operario.ui")
menuSup=uic.loadUi("Menu supervisora.ui")
menuOp=uic.loadUi("Menu operario.ui")


# Ocultar la barra de título
loginSup.setWindowFlags(Qt.WindowType.FramelessWindowHint)
loginOp.setWindowFlags(Qt.WindowType.FramelessWindowHint)
menuSup.setWindowFlags(Qt.WindowType.FramelessWindowHint)
menuOp.setWindowFlags(Qt.WindowType.FramelessWindowHint)

# Hacer el fondo transparente
loginSup.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
loginOp.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
menuSup.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
menuOp.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

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


#Login de operario
def op_Login():
    user = loginOp.lineEdit.text()
    loginOp.lineEdit.clear()
    if len(user) == 0:
        loginOp.label_3.setText("Estimado/a usuario, porfavor ingrese todos los datos.")
    elif len(user) > 4:
        loginOp.label_3.setText("Estimado/a usuario, porfavor ingrese tus ultimos 4 digitos del ID")
    elif user.isdigit():
        QMessageBox.information(loginOp, "Éxito", "Ingreso exitoso.")
        menuOp.show()
        loginOp.hide()
    else:
        loginOp.label_3.setText("Por favor, ingrese un número entero válido.")


#Menu operario
def ingreso_Correcto(linea):
    mensaje = f"Has ingresado correctamente a la línea {linea}"
    QMessageBox.information(menuOp, "Estimado/a", mensaje)


#Cambiar de pestanas
def menu_Sup():
    menuSup.show()
    loginSup.hide()


def menu_Op():
    menuOp.show()
    loginOp.hide()


def switch_Sup_Op():
    loginOp.show()
    loginSup.hide()


def switch_Op_Sup():
    loginSup.show()
    loginOp.hide()



def exit():
    app.exit()

#Se conectan los botones con funciones
loginSup.pushButton_2.clicked.connect(exit)
loginOp.pushButton_2.clicked.connect(exit)
menuSup.pushButton.clicked.connect(exit)
menuOp.pushButton.clicked.connect(exit)

loginSup.pushButton.clicked.connect(switch_Sup_Op)
loginOp.pushButton.clicked.connect(switch_Op_Sup)
loginSup.pushButton_3.clicked.connect(sup_Login)
loginOp.pushButton_3.clicked.connect(op_Login)

menuOp.pushButton_2.clicked.connect(lambda: ingreso_Correcto(1))
menuOp.pushButton_3.clicked.connect(lambda: ingreso_Correcto(2))
menuOp.pushButton_4.clicked.connect(lambda: ingreso_Correcto(3))
menuOp.pushButton_5.clicked.connect(lambda: ingreso_Correcto(4))
menuOp.pushButton_6.clicked.connect(lambda: ingreso_Correcto(7))
menuOp.pushButton_7.clicked.connect(lambda: ingreso_Correcto(6))
menuOp.pushButton_8.clicked.connect(lambda: ingreso_Correcto(8))
menuOp.pushButton_9.clicked.connect(lambda: ingreso_Correcto(5))


#Ejecutable
loginOp.show()
app.exec()