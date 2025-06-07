from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.input_amount = QtWidgets.QLineEdit(Form)
        self.input_amount.setPlaceholderText("თანხა")
        self.verticalLayout.addWidget(self.input_amount)

        self.comboBox_from = QtWidgets.QComboBox(Form)
        self.verticalLayout.addWidget(self.comboBox_from)

        self.comboBox_to = QtWidgets.QComboBox(Form)
        self.verticalLayout.addWidget(self.comboBox_to)

        self.convert_button = QtWidgets.QPushButton(Form)
        self.convert_button.setText("კონვერტაცია")
        self.verticalLayout.addWidget(self.convert_button)

        self.result_label = QtWidgets.QLabel(Form)
        self.result_label.setText("შედეგი გამოჩნდება აქ")
        self.verticalLayout.addWidget(self.result_label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Currency Converter"))
