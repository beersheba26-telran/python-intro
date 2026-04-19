import unittest
from extract_content import extractHtmlContent

class TestHtmlRegex(unittest.TestCase):
    def test_extract_html_content_no_tag(self):
        self.assertEqual(
            extractHtmlContent("<p>hhhh</p> <span>ssss</span> <span>any text</span>"),
            ["hhhh", "ssss", "any text"]
        )

    def test_extract_html_content_with_tag(self):
        self.assertEqual(
            extractHtmlContent("<p>hhhh</p> <span>ssss</span> <span>any text</span>", "span"),
            ["ssss", "any text"]
        )

    def test_extract_html_content_single_element(self):
        self.assertEqual(
            extractHtmlContent("<div>hello</div>", "div"),
            ["hello"]
        )

    def test_extract_html_content_mixed(self):
        self.assertEqual(
            extractHtmlContent("<p>a</p><p>b</p><span>c</span>", "p"),
            ["a", "b"]
        )

    def test_extract_html_content_no_match(self):
        self.assertEqual(
            extractHtmlContent("<p>test</p>", "span"),
            []
        )

    def test_extract_html_content_spaces(self):
        self.assertEqual(
            extractHtmlContent("<p>  text  </p> <p>ok</p>"),
            ["  text  ", "ok"]
        )
