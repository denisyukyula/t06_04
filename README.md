def init():
    """ Викликається 1 раз на початку виконання програми. """
    pass

def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    pass

def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та 
             False у іншому разі. """
    return False

def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    pass

def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, 
    то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку."""
    return []
