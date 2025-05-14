from functools import wraps
from typing import Any


def log(filename: Any = None) -> Any:
    """Декоратор для логирования функций и вывода результатов в консоль или файл и
    принимающий на вход необязательный аргумент filename"""

    def wrapper(func: Any) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as error:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {error}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {error}. Inputs: {args}, {kwargs}")

        return inner

    return wrapper
