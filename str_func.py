def foo(value: str):
<<<<<<<<< Temporary merge branch 1
    """"возвращает строку в верхнем регистре"""
=========
    """возврат строки в верхнем регистре"""
>>>>>>>>> Temporary merge branch 2
    return value.upper()

def foo2(value: str):
    """делает заглавными первый символ каждого слова в строке"""
    for val in value:
        output = val.title()
        print(output)
