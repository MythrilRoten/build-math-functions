from dataclasses import dataclass
import os
from typing import TypeVar, Union
import string
from pathlib import Path

import sys
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QFile
from PySide6 import QtCore
from ui_mainwindow import Ui_MainWindow

from sympy import Symbol, preview, simplify, evalf
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
import numpy as np
import pyqtgraph as pg
from math import log, pi, e, sqrt


NUMBERS = string.digits
BASE_DIR = Path(__file__).parent


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
            x = -1
            eval(function)
            negative_value = True
        except:
            negative_value = False
        try:
            x = 1
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
    expr = ["a*x+a", "x+a", "a*x", "a*x-a", "x-a", "x"]

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
        # self.ui.line_function.setMaxLength(20)

        self.ui.line_intervalA.setPlaceholderText("Интервал А")
        self.ui.line_intervalA.setMaxLength(4)

        self.ui.line_intervalB.setPlaceholderText("Интервал В")
        self.ui.line_intervalB.setMaxLength(4)

        self.ui.line_step.setPlaceholderText("Шаг")
        self.ui.line_step.setMaxLength(4)

        self.ui.action_Authors.triggered.connect(
            lambda: QMessageBox.information(self, "Авторы", "Разработана и подготовлена в рамках курсовой работы\n\
курсантом 331 группы ТАТК ГА\nНедоспасовым Егором"))
        self.ui.action_Instructions.triggered.connect(
            lambda: QMessageBox.information(self, "Инструкция", "Для правильной работы программы необходимо следовать след. инструкциям:\n\
    1. Ввести математическую функцию в поле 'Функция' вида y = expression или expression и согласно синтаксису написания мат. выражений в Python.\n\
    2. Заполнить поля условий постройки функции, а именно 'Интервал А', 'Интервал Б', 'Шаг'.\n\
    3. Нажать на кнопку  'Построить' дли отображения графика в виджете графиков."))

        self.ui.line_function.editingFinished.connect(self.editLine_Function)
        self.ui.but_Graph.clicked.connect(self.prepareMakingGraph)

    # Триггер изменения окна
    def resizeEvent(self, event: PySide6.QtCore.QEvent) -> None:
        return self.ui.mainLayout.parent().setGeometry(10, 10, self.geometry().getRect()[2] - 20,
                                                       self.geometry().getRect()[3] - 55)

    # Обозначение типа функции
    def knowFunctionType(self, function: str) -> TypeFunction | QMessageBox:
        # Упрощение формулы
        formula = function.replace('y', '').replace(
            '=', '').replace(' ', '').replace('^', '**')
        try:
            expr = parse_expr(formula, transformations=transformations)
        except:
            QMessageBox.critical(self, "Критическая",
                                 "Проверьте правильность написания формулы.")
        simplified_formula = simplify(expr)
        print(simplified_formula)

        # Проверка на математический тип функции
        if MathFunction.knowY(simplified_formula):
            formula_replaced_symbols = str(
                simplified_formula).replace('**', '^')

            for num in NUMBERS:
                formula_replaced_symbols = formula_replaced_symbols.replace(
                    num, 'a').replace('.', 'a')
            formula_replaced_symbols = ''.join(
                ch for ch, _ in itertools.groupby(formula_replaced_symbols))
            formula_replaced_symbols = formula_replaced_symbols.replace(
                '^', '**')
            print(formula_replaced_symbols)
            for type_math_func in MathFunction.__subclasses__():
                if formula_replaced_symbols.replace(' ', '') in type_math_func.expr:
                    return type_math_func(simplified_formula)
            else:
                return MathFunction(simplified_formula)

        else:
            raise QMessageBox.critical(
                self, "Ошибка", "Эта функция не является математической.")

    # Изменение состояния двух label
    def editLine_Function(self) -> None:
        self.math_object = self.knowFunctionType(
            self.ui.line_function.text() if self.ui.line_function.text() != '' else None)
        self.ui.lab_type_func.setText(
            "Тип функции: {0}".format(self.math_object.name))
        preview(self.math_object.math_function,
                viewer='file', filename='function.png')
        self.ui.function_photo.setPixmap(
            QPixmap(os.path.join(BASE_DIR, 'function.png')))

    # Подготовка к построению графика
    def prepareMakingGraph(self) -> None | QMessageBox:
        global user

        try:
            if self.chechValidality(intervalA=float(self.ui.line_intervalA.text()),
                                    intervalB=float(self.ui.line_intervalB.text()),
                                    step=float(self.ui.line_step.text())):
                raise Exception

            user = UserPreferences(type_function=type(self.math_object),
                                   function=self.math_object.math_function,
                                   intervalA=float(
                                       self.ui.line_intervalA.text()),
                                   intervalB=float(
                                       self.ui.line_intervalB.text()),
                                   step=float(
                                       self.ui.line_step.text()))
        except:
            return QMessageBox.information(self, "Информация", "Входных данных нет или они введены неверно!")

        user.x_array, user.y_array = self.getXY(user.intervalA,
                                                user.step,
                                                user.intervalB,
                                                user.function)
        print(user.x_array, user.y_array)
        print(np.real(user.x_array), np.real(user.y_array))
        self.settingPlot(user.x_array, user.y_array)

    # Проверка на правильность написанных входных данных
    @staticmethod
    def chechValidality(intervalA: float, intervalB: float, step: float) -> bool:
        if intervalB <= intervalA or \
                step > abs(-intervalB + intervalA):
            return True
        else:
            return False

    # Получение пар координат x, y
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
                y = eval(str(function))
                if type(y) == complex:
                    raise Exception
                y_array.append(y)
                x_array.append(x)
            except:
                pass
            x += step
        return x_array, y_array

    # Построение графика
    def settingPlot(self, array_x: list, array_y: list) -> None | QMessageBox:
        self.ui.graphWidget.clear()
        self.ui.graphWidget.showGrid(x=True, y=True)
        self.ui.graphWidget.setLabel('bottom', 'x')
        self.ui.graphWidget.setLabel('left', 'y')
        self.ui.graphWidget.setTitle(f"{self.math_object.name}")
        pen = pg.mkPen(color='red', width=1)
        try:
            self.ui.graphWidget.plot(np.real(array_x), np.real(array_y), pen=pen)
        except:
            return QMessageBox.critical(self, "Ошибка", "Введеная формула слишком сложная для расчета,\n либо использует комплексные числа для построения графика.")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
