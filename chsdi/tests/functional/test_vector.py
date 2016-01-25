# -*- coding: utf-8 -*-

import unittest

from chsdi.models.vector import getFallbackLangMatch


class Test_AttributesTranslations(unittest.TestCase):

    def test_no_lang_specific_attribute(self):
        # No match, so no based on lang - return attr
        queryableAttrs = ['toto', 'tutu', 'tata']
        availableLangs = 'de'
        attr = 'toto'
        self.assertEqual('toto', getFallbackLangMatch(queryableAttrs, availableLangs, attr))

    def test_lang_specific_attribute(self):
        queryableAttrs = ['toto', 'toto_de', 'toto_fr']
        availableLangs = 'fr'
        attr = 'toto_fr'
        self.assertEqual('toto_fr', getFallbackLangMatch(queryableAttrs, availableLangs, attr))

    def test_attribute_fallback_en_to_de(self):
        queryableAttrs = ['toto', 'toto_de', 'toto_fr']
        availableLangs = 'en'
        attr = 'toto_de'
        self.assertEqual('toto_de', getFallbackLangMatch(queryableAttrs, availableLangs, attr))

    def test_attribute_fallback_rm_to_de(self):
        queryableAttrs = ['toto', 'toto_de', 'toto_fr']
        availableLangs = 'rm'
        attr = 'toto_de'
        self.assertEqual('toto_de', getFallbackLangMatch(queryableAttrs, availableLangs, attr))

    def test_attribute_fallback_it_to_fr(self):
        queryableAttrs = ['toto', 'toto_de', 'toto_fr']
        availableLangs = 'it'
        attr = 'toto_fr'
        self.assertEqual('toto_fr', getFallbackLangMatch(queryableAttrs, availableLangs, attr))
