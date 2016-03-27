def welcome(name):
    """
    be nice and greet somebody
    name: name of the person

    >>> welcome()
    'Hello!'

    >>> welcome(lang='de')
    'Hallo!'

    >>> welcome('Guido')
    'Hello Guido!'

    """
    return 'Hallo {}!'.format(name)
