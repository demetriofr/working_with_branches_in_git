def upper_str(value: str):
    """Функция, которая принимает на вход строку, возвращает ее со всеми заглавными буквами"""
    if len(value) > 0:
        return value.upper()


def title_str(value: str):
    """Функция, которая делает заглавными первые буквы каждого слова в строке"""
    if len(value) > 0:
        return value.title()
