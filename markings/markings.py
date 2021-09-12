'''
'''
from typing import Union, Callable, Any, List, Iterator
import inspect
from dataclasses import dataclass


@dataclass
class Mark:
    filename: str
    funcname: str
    lineno: int
    message: str
    module: str

    def __str__(self) -> str:
        return f'{self.module}:{self.filename}:{self.funcname}:{self.lineno}: {self.message}'


class _Marker:
    name: str
    marks: List[Mark]

    def __init__(self, name: str):
        self.name = name
        self.marks = []

    def __len__(self) -> int:
        return len(self.marks)

    def __bool__(self) -> bool:
        return bool(self.marks)

    def __str__(self) -> str:
        return '\n'.join(map(str, self.marks))

    def __call__(self, func_or_message: Union[Callable, str]) -> Callable:
        if callable(func_or_message):
            message = ''
            func = func_or_message
        else:
            message = func_or_message
            func = None

        caller_frame = inspect.getframeinfo(inspect.currentframe().f_back)
        def decorator(function: Callable):
            module = function.__module__.split(".")[0]
            funcname = function.__name__
            filename = caller_frame.filename
            lineno = caller_frame.lineno

            self.marks.append(Mark(
                module=module,
                funcname=funcname,
                filename=filename,
                lineno=lineno,
                message=message
            ))

            return function

        return decorator(func) if func else decorator

    def clear_all(self):
        self.marks.clear()

    def filter(self, module: str, exact: bool = True) -> Iterator[Mark]:
        if exact:
            match_func = lambda mark: module == mark.module
        else:
            match_func = lambda mark: module in mark.module
        return filter(match_func, self.marks)


class Marker:
    def __init__(self):
        self.markers_dict = {}

    def __getattr__(self, marker_name) -> _Marker:
        return self.markers_dict.setdefault(marker_name, _Marker(marker_name))

    def __str__(self) -> str:
        ret_str = ''
        for name, marker in self.markers_dict.items():
            if not marker:
                continue
            ret_str += f'{name}:\n{str(marker)}\n'
        return ret_str

    def __iter__(self) -> Iterator:
        return iter(self.markers_dict.items())


marker = Marker()
todo = marker.todo
known_issue = marker.known_issue
