def welcome(name='', lang='en'):
    """
    be nice and greet somebody
    name: name of the person, may be empty
    lang: two character language code

    >>> welcome()
    'Hello!'

    >>> welcome(lang='de')
    'Hallo!'

    >>> welcome('Guido')
    'Hello Guido!'

    >>> welcome('Guido', 'nl')  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ValueError: ...

    >>> welcome('Guido', 'nl')  # doctest: +SKIP
    'Goedendag Guido!'

    """
    greetings = {'de': 'Hallo',
                 'en': 'Hello',
                 'fr': 'Bonjour'}
    try:
        greeting = greetings[lang]
    except KeyError:
        errmsg = 'unknown language: {}'.format(lang)
        raise ValueError(errmsg)
    if name:
        greeting = ' '.join([greeting, name])
    return greeting+'!'
