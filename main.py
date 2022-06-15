from dataclasses import dataclass
from typing import TypeVar, Union


import sys
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QFile
from PySide6 import QtCore
from ui_mainwindow import Ui_MainWindow

from sympy import Symbol, preview, simplify
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_application,
    implicit_multiplication,
    implicit_multiplication_application,
    function_exponentiation)
# https://docs.sympy.org/latest/modules/parsing.html

import sympy
import itertools
import pyqtgraph as pg
from math import log, pi


NUMBERS = [i for i in range(0, 10)]

Self = TypeVar('Self')
transformations = (standard_transformations +
                   (implicit_multiplication,
                    implicit_application,
                    function_exponentiation))


class MathFunction:
    """  The main characteristic of mathematical functions  """
    name = "Неопределеная"

    def __init__(self, func) -> None:
        self.math_function = func

    @staticmethod
    def knowY(function: str) -> bool:
        function = str(function)
        try:
            x = -pi/2
            eval(function)
            negative_value = True
        except:
            negative_value = False
        try:
            x = pi/2
            eval(function)
            positive_value = True
        except:
            positive_value = False
        return True if negative_value | positive_value else False


class Line(MathFunction):
    """  
    Linear function\n
    y = kx + b\n
    Ax + Bx + C = 0, where A | B ∈ R but A & B != 0
    """
    name = "Линейная"
    expr = ["a*x+a", "x+a", "a*x", "a*x-a", "x-a"]
    dots = 2

    def __init__(self, func) -> None:
        super().__init__(func)


class Power(MathFunction):
    """  
    Power function\n
    y = 
    """
    name = "Степенная"
    expr = ["a*x**a+a", "x**a+a", "x**a", "a*x**a", "a*x**a-a", "x**a-a"]

    def __init__(self, func) -> None:
        super().__init__(func)


class Logarithm(MathFunction):
    """  Logarithmic function  """
    name = "Логарифмическая"
    expr = ["a*log(x,a)+a", "a*log(x)+a",
            "a*log(x)", "a*log(x, a)", "log(x)",
            "a*log(x,a)-a", "a*log(x)-a",
            "log(x)/log(a)", "a*log(x/a)/log(a)", "a*log(a*x)/log(a)",
            "log(x)**a/log(a)**a"]

    def __init__(self, func) -> None:
        super().__init__(func)


TypeFunction = TypeVar(
    "TypeFunction", *MathFunction.__subclasses__(), MathFunction)


@dataclass
class UserPreferences:
    """  Filled data about construction of a mathematical function  """
    type_function: TypeFunction
    function: str
    intervalA: float | int
    intervalB: float | int
    step: float | int
    x_array: None | list = None
    y_array: None | list = None


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.resize(1140, 640)

        self.ui.line_function.setPlaceholderText("Функция")
        self.ui.line_intervalA.setPlaceholderText("ИнтервалА")
        self.ui.line_intervalB.setPlaceholderText("ИнтервалВ")
        self.ui.line_step.setPlaceholderText("Шаг")

        self.ui.line_function.editingFinished.connect(self.editLine_Function)
        self.ui.but_Graph.clicked.connect(self.prepareMakingGraph)

    def resizeEvent(self, event: PySide6.QtCore.QEvent) -> None:
        return self.ui.mainLayout.parent().setGeometry(10, 10, self.geometry().getRect()[2] - 20,
                                                       self.geometry().getRect()[3] - 55)

    @staticmethod
    def knowFunctionType(function: str) -> TypeFunction | QMessageBox:
        formula = function.replace('y', '').replace(
            '=', '').replace(' ', '').replace('^', '**')
        try:
            expr = parse_expr(formula, transformations=transformations)
        except:
            QMessageBox.critical(window, "Критическая",
                                 "Проверьте правильность написания формулы")
        simplified_formula = simplify(expr)
        print("simplified_formula: ", simplified_formula)

        if MathFunction.knowY(simplified_formula):
            formula_replaced_symbols = str(
                simplified_formula).replace('**', '^')
            for num in NUMBERS:
                formula_replaced_symbols = formula_replaced_symbols.replace(
                    str(num), 'a')
            formula_replaced_symbols = ''.join(
                ch for ch, _ in itertools.groupby(formula_replaced_symbols))
            formula_replaced_symbols = formula_replaced_symbols.replace(
                '^', '**')
            print("general view: ", formula_replaced_symbols)
            for type_math_func in MathFunction.__subclasses__():
                if formula_replaced_symbols.replace(' ', '') in type_math_func.expr:
                    return type_math_func(simplified_formula)
            else:
                return MathFunction(simplified_formula)

        else:
            raise QMessageBox.critical(
                window, "Ошибка", "Эта функция не является математической")

    def editLine_Function(self) -> None:
        self.math_object = self.knowFunctionType(
            self.ui.line_function.text() if self.ui.line_function.text() != '' else None)
        self.ui.lab_type_func.setText(
            "Тип функции: {0}".format(self.math_object.name))
        preview(self.math_object.math_function,
                viewer='file', filename='output.png')
        self.ui.function_photo.setPixmap(
            QPixmap('/home/visor/Projects/kurs/output.png'))

    def prepareMakingGraph(self) -> None:
        global user
        user = UserPreferences(type_function=type(self.math_object),
                               function=self.math_object.math_function,
                               intervalA=float(self.ui.line_intervalA.text()),
                               intervalB=float(self.ui.line_intervalB.text()),
                               step=float(self.ui.line_step.text()))

        user.x_array, user.y_array = self.getXY(
            user.intervalA, user.step, user.intervalB, user.function)
        self.settingPlot(user.x_array, user.y_array)

    @staticmethod
    def getXY(start: float,
              step: float,
              final: float,
              function: sympy.core.add.Add) -> Union[list, list]:

        x_array = []
        y_array = []
        x = start
        while x <= final:
            try:
                y_array.append(eval(str(function)))
                x_array.append(x)
            except:
                pass
            x += step
        return x_array, y_array

    def settingPlot(self, array_x: list, array_y: list) -> None | QMessageBox:
        self.ui.graphWidget.clear()
        self.ui.graphWidget.showGrid(x=True, y=True)
        self.ui.graphWidget.setLabel('bottom', 'x')
        self.ui.graphWidget.setLabel('left', 'y')
        self.ui.graphWidget.setTitle(f"{self.math_object.name}")
        pen = pg.mkPen(color='red', width=1)

        try:
            self.ui.graphWidget.plot(array_x, array_y, pen=pen)
        except:
            return QMessageBox.critical(window, "Ошибка", "Что-то пошло не так")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
