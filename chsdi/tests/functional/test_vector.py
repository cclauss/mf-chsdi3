# -*- coding: utf-8 -*-

import unittest

from chsdi.models.vector import getFallbackLangMatch


class Test_AttributesTranslations(unittest.TestCase):

    def test_lang_specific_attribute(self):
        queryableAttrs = ['toto', 'tutu', 'tata']
        lang = 'de'
        availableLangs = 'de'
        attr = 'toto'

        self.assertEqual('toto', getFallbackLangMatch(queryableAttrs, lang, availableLangs, attr))

    def test_no_lang_specific_attribute(self):
        queryableAttrs = ['toto', 'toto_de', 'toto_fr']
        lang = 'fr'
        availableLangs = 'fr'
        attr = 'toto_fr'

        self.assertEqual(None, getFallbackLangMatch(queryableAttrs, lang, availableLangs, attr))

    def test_attribute_fallback_to_de(self):
        queryableAttrs = ['toto', 'toto_de', 'toto_fr']
        lang = 'en'
        availableLangs = 'de'
        attr = 'toto_de'

        self.assertEqual('toto_de', getFallbackLangMatch(queryableAttrs, lang, availableLangs, attr))
