def foo(value: str):
    """возврат строки в верхнем регистре"""
    return value.upper()

def foo2(value: str):
    """делает заглавными первый символ каждого слова в строке"""
    for val in value:
        output = val.title()
        print(output)
