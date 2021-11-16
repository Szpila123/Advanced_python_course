import abc
import enum
import operator
import collections


class Priority(enum.Enum):
    BASE = enum.auto()
    SUM = enum.auto()
    DIV = enum.auto()
    MUL = enum.auto()
    POW = enum.auto()
    VAR = enum.auto()

    def __lt__(self, arg):
        return self.value < arg.value


class Wyrazenie(abc.ABC):
    _priority: Priority

    @abc.abstractmethod
    def __init__(): ...

    def __add__(self, arg):
        return Suma(self, arg)

    def __sub__(self, arg):
        return Roznica(self, arg)

    def __mul__(self, arg):
        return Iloczyn(self, arg)

    def __div__(self, arg):
        return Iloraz(self, arg)

    @abc.abstractmethod
    def __str__(self): ...

    @abc.abstractmethod
    def oblicz(self, zmienne: dict[str, int]):
        """Evaluate the expression"""
        ...

    @property
    def priority(self):
        """Get priority of this operand"""
        return self._priority


class Operacja(Wyrazenie):
    _arg1: Wyrazenie
    _arg2: Wyrazenie
    _oper: collections.Callable[[int, int], int]
    _oper_str: str

    def __str__(self):
        string = ''
        if self._arg1.priority < self.priority:
            string += f'({str(self._arg1)})'
        else:
            string += str(self._arg1)

        string += f' {self._oper_str} '

        if self._arg2.priority < self.priority:
            string += f'({str(self._arg2)})'
        else:
            string += str(self._arg2)

        return string

    def oblicz(self, zmienne):
        try:
            return self._oper(self._arg1.oblicz(zmienne), self._arg2.oblicz(zmienne))
        except ArithmeticError as error:
            raise ExpressionArithmeticError from error


class Suma(Operacja):
    def __init__(self, arg1: Wyrazenie, arg2: Wyrazenie):
        self._arg1, self._arg2 = arg1, arg2
        self._oper = operator.add
        self._oper_str = '+'
        self._priority = Priority.SUM


class Roznica(Operacja):
    def __init__(self, arg1: Wyrazenie, arg2: Wyrazenie):
        self._arg1, self._arg2 = arg1, arg2
        self._oper = operator.sub
        self._oper_str = '-'
        self._priority = Priority.SUM


class Iloczyn(Operacja):
    def __init__(self, arg1: Wyrazenie, arg2: Wyrazenie):
        self._arg1, self._arg2 = arg1, arg2
        self._oper_str = '*'
        self._oper = operator.mul
        self._priority = Priority.MUL


class Iloraz(Operacja):
    __priority_ = 2

    def __init__(self, arg1: Wyrazenie, arg2: Wyrazenie):
        self._arg1, self._arg2 = arg1, arg2
        self._oper = operator.truediv
        self._oper_str = '/'
        self._priority = Priority.DIV


class Zmienna(Wyrazenie):
    def __init__(self, repr: str):
        if (repr == ''):
            raise EmptyVarName

        self._repr = repr
        self._priority = Priority.VAR

    def __str__(self):
        return self._repr

    def oblicz(self, zmienne):
        try:
            return zmienne[self._repr]
        except LookupError as error:
            raise VariableNotDefined from error


class Stala(Wyrazenie):
    def __init__(self, value: int):
        self._value = value
        self._priority = Priority.VAR

    def __str__(self):
        return str(self._value)

    def oblicz(self, zmienne):
        return self._value


class ExpressionException(Exception):
    pass


class ExpressionArithmeticError(ExpressionException):
    pass


class VariableNotDefined(ExpressionException):
    pass


class EmptyVarName(ExpressionException):
    pass
