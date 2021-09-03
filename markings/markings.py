'''
'''
from typing import Union, Callable, Any
import inspect
from dataclasses import dataclass


@dataclass
class Mark:
    filename: str
    funcname: str
    lineno: int
    message: str

    def __str__(self) -> str:
        return f'{self.filename}:{self.funcname}:{self.lineno}: {self.message}'


class _Marker:
    def __init__(self, name):
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
        def decorator(function):
            self.marks.append(Mark(funcname=function.__name__, filename=caller_frame.filename, lineno=caller_frame.lineno, message=message))
            return function

        return decorator(func) if func else decorator

    def clear_all(self):
        self.marks.clear()


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

    def __iter__(self):
        return iter(self.markers_dict.items())


marker = Marker()
todo = marker.todo
known_issue = marker.known_issue
