import urllib.request, urllib.parse, urllib.error
import requests
import re
import json

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
        self.reg  = re.compile(',{1,}')

    def translate(self, data, lang1, lang2): 
        data = urllib.parse.urlencode({"q":data})
        url  = self.addr % (lang1, lang2, data)
        req  = requests.get(url)
        data = re.sub(self.reg, ',', req.text)
        data = json.loads(data)
        data = ' '.join([ind[0] for ind in data[0]])
        return data







