# libdict
The libdict is a python lib to do translations using google translator.

Install
=======

cd /tmp/


Usage
=====

**The python module**

You can use libdict in two ways, one of them is through the python class GoogleTranslator.

~~~python
    from libdict import *
    x = GoogleTranslator()
    print x.translate('word', 'en', 'pt')
    print x.translate('word is cool', 'en', 'pt')
~~~

**Command line**

The other way is through the script gdict.

~~~    
gdict -s en -t pt word is cool
~~~


