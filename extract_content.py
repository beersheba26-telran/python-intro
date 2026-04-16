def extractHtmlContent(htmlText:str, tag:str = None)->list[str]:
    '''
    returns list of HTML elemet contents inside element according to  a given tag
    if tag isn't defined HTML element contents from all elements should be returned
    example: html = <p>hhhh</p> <span>ssss</span> <span>any text</span>
    extractHtmlContent(html, "span") -> ['ssss', 'any text']
     extractHtmlContent(html) -> ['hhhh','ssss', 'any text']
    
    '''
    