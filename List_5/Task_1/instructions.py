import expressions
import abc
import copy


class Instruction(abc.ABC):
    @abc.abstractmethod
    def __init__(): ...

    @abc.abstractmethod
    def wykonaj(self, zmienne) -> dict[str, int]:
        '''Evaluate the instruction'''
        ...

    @abc.abstractmethod
    def __str__(self): ...


class If(Instruction):
    def __init__(self, cond: expressions.Wyrazenie, branch_true: Instruction, branch_false: Instruction):
        self._cond = cond
        self._branch_true = branch_true
        self._branch_false = branch_false

    def wykonaj(self, zmienne):
        if self._cond.oblicz(zmienne) == 0:
            lokalne_zmienne = self._branch_true.wykonaj(copy.copy(zmienne))
        else:
            lokalne_zmienne = self._branch_false.wykonaj(copy.copy(zmienne))

        for key in lokalne_zmienne:
            if key in zmienne:
                zmienne[key] = lokalne_zmienne[key]

        return zmienne

    def __str__(self):
        tab, nl = '\n\t\t', '\n'
        return f'if {str(self._cond)}\n\n\tthen\t{tab.join(str(self._branch_true).split(nl))}\n\n\telse\t{tab.join(str(self._branch_false).split(nl))}\n'


class While(Instruction):
    def __init__(self, cond: expressions.Wyrazenie, branch: Instruction):
        self._cond = cond
        self._branch = branch

    def wykonaj(self, zmienne):
        while self._cond.oblicz(zmienne):
            lokalne_zmienne = self._branch.wykonaj(copy.copy(zmienne))
            for key in lokalne_zmienne:
                if key in zmienne:
                    zmienne[key] = lokalne_zmienne[key]
        return zmienne

    def __str__(self):
        tab, nl = '\n\t\t', '\n'
        return f'while {str(self._cond)}\n\n\tdo\t{tab.join(str(self._branch).split(nl))}\n'


class Chain(Instruction):
    def __init__(self, instructions: list[Instruction]):
        self._chain = instructions

    def wykonaj(self, zmienne):
        for inst in self._chain:
            zmienne = inst.wykonaj(zmienne)
        return zmienne

    def __str__(self):
        return '\n'.join([str(inst) for inst in self._chain])


class Assign(Instruction):
    def __init__(self, var: expressions.Zmienna, val: expressions.Wyrazenie):
        self._var = var
        self._val = val

    def wykonaj(self, zmienne):
        zmienne[str(self._var)] = self._val.oblicz(zmienne)
        return zmienne

    def __str__(self):
        return f'{self._var} = {self._val}'
