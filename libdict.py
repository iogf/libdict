import urllib
import requests
import re
"""
Lang codes
LANG = ['pt', 'en', 'fr', 'af', 'sq', 'de', 
        'ar', 'hy', 'az', 'eu', 'be', 'bg', 
        'ca', 'zh-CN', 'ko', 'ht', 'hr', 'da',
        'sk', 'sl', 'es', 'et', 'fi', 'gl', 'cy', 
        'ka', 'el', 'lw', 'hi', 'nl', 'hu', 'id', 
        'ga', 'is', 'it', 'ja', 'la', 'lv', 'lt', 
        'mk', 'ms', 'mt', 'no', 'fa', 'pl', 'ro', 
        'ru', 'sr', 'sw', 'sv', 'tl', 'th', 'cs', 
        'tr' ,'uk' ,'ur' ,'vi' ,'yi', 'auto']

This class is used to translate text using google translator.
The auto code is referring to the language detection feature.
"""

class GoogleTranslator(object):
    def __init__(self):
        self.addr = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=%s&tl=%s&dt=t&%s"
        self.reg  = '\[\[\[\"(?P<data>.+?)",'

    def translate(self, data, lang1, lang2): 
        data = urllib.urlencode({"q":data})
        url  = self.addr % (lang1, lang2, data)
        req  = requests.get(url)
        data = self.parse(req.text.encode('utf-8'))
        return data

    def parse(self, data):
        match = re.match(self.reg, data)

        try:
            return match.group('data')
        except AttributeError:
            pass




