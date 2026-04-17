import re
import regular_expressions
htmlElemPattern:re.Pattern = re.compile(regular_expressions.htmlElementRegex())
def extractHtmlContent(htmlText:str, tag:str = None)->list[str]:
    '''
    returns list of HTML elemet contents inside element according to  a given tag
    if tag isn't defined HTML element contents from all elements should be returned
    example: html = <p>hhhh</p> <span>ssss</span> <span>any text</span>
    extractHtmlContent(html, "span") -> ['ssss', 'any text']
     extractHtmlContent(html) -> ['hhhh','ssss', 'any text']
    '''
    htmlContents = [mo.group(2) for mo in htmlElemPattern.finditer(htmlText) if not tag or tag in mo.group(1) ]
    
    return htmlContents
if __name__ == "__main__":
        
   extractHtmlContent("<p>hhhh</p> <span>ssss</span> <span>any text</span>") 