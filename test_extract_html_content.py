from unittest import TestCase

from extract_content import extractHtmlContent


class TestExtractHtmlContent(TestCase):
    def test_tag_provided(self):
        html = "<p>hhhh</p> <span>ssss</span> <span>any text</span>"
        self.assertEqual(extractHtmlContent(
            html, "span"), ["ssss", "any text"])

    def test_tag_not_provided(self):
        html = "<p>hhhh</p> <span>ssss</span> <span>any text</span>"
        self.assertEqual(extractHtmlContent(html), [
                         "hhhh", "ssss", "any text"])

    def test_no_matching_tag(self):
        html = "<p>hhhh</p> <span>ssss</span>"
        self.assertEqual(extractHtmlContent(html, "div"), [])
    
    def test_nested_elements(self):
        html = "<p><p><span>xxxx</span></p></p>"  
        self.assertEqual(extractHtmlContent(html), ['xxxx'])  
