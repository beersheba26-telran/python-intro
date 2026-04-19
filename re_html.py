
def openHtmlTag():
    """Returns regexp for open HTML tag.
       open HTML tag must be in the form: <tagname>
       where tagname is a valid HTML tag name (consists of letters, digits and hyphens, and starts with a letter)
    """
    # return r'<[a-zA-Z][a-zA-Z0-9-]*>'
    # return r'<[^<>]+>'
    return r'<([a-zA-Z][a-zA-Z0-9-]*)(\s+[^<>]*)?>'

def closeHtmlTag():
    """Returns regexp for close HTML tag.
       close HTML tag must be in the form: </tagname>
       where tagname is a valid HTML tag name (consists of letters, digits and hyphens, and starts with a letter)
    """
    # return r'</[a-zA-Z][a-zA-Z0-9-]*>'
    return r'</\1>'

def contentHtmlRegex():
    """Returns regexp for content of HTML tag.
       content of HTML tag can be any string that does not contain the closing tag
    """
    return r'[^<>]+'

def htmlElementRegex():
    """Returns regexp for HTML element.
       HTML element must be in the form: <tagname>content</tagname>
       where tagname is a valid HTML tag name (consists of letters, digits and hyphens, and starts with a letter)
       and content can be any string that does not contain the closing tag
    """
    # return rf'{openHtmlTag()}({contentHtmlRegex()}){closeHtmlTag()}'
    return r'<([a-zA-Z][a-zA-Z0-9-]*)(\s+[^<>]*)?>([^<>]+)</\1>'  # with attrinutes in open tag
