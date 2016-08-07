#!/usr/bin/env python
import unittest
from xml.dom.minidom import parseString

SAMPLE_WIKI = 'h4. Confluence Markup\n\n* A\n* B\n'
SAMPLE_XML = """<h4>Confluence Markup</h4>

<ul>
    <li>A</li>
    <li>B</li>
</ul>
"""


class ConfluenceTests(unittest.TestCase):
    # _multiprocess_can_split_ = True

    def setUp(self):
        from confluence import Confluence
        self.conf = Confluence(profile="confluence")

    # def test_getPage(self):
    #    page = self.conf.getPage(page='test',space='ds')
    #    print page

    def test_renderContent(self):
        result = self.conf.renderContent(page='Welcome to Confluence', space='ds')
        # tree = ElementTree.fromstring(result)
        # html = lxml.html.fromstring(result)

        x = parseString(result)
        e = x.getElementById('Content')
        self.assertFalse(e is None, "Unable to find element with id=Content in: '%s'" % result)
        e.toxml()

        # result = html.get_element_by_id("Content").__str__()

        self.assertEqual(result, SAMPLE_XML, "Got '%s' while expecting '%s'." % (result, SAMPLE_XML))

    def test_storePageContent(self):
        self.conf.storePageContent(page='test', space='ds', content=SAMPLE_WIKI)
        result = self.conf.getPage(page='test', space='ds')['content']
        print(":".join("{0:x}".format(ord(c)) for c in result))
        print(":".join("{0:x}".format(ord(c)) for c in SAMPLE_XML))
        self.assertEqual(result, SAMPLE_WIKI, "Got '%s' while expecting '%s'." % (result, SAMPLE_XML))


class Confluence5Tests(ConfluenceTests):

    def setUp(self):
        from confluence import Confluence
        self.conf = Confluence(profile="confluence-test")


if __name__ == "__main__":
    unittest.main()
