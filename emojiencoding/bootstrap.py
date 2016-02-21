from . import emoji

import sys, codecs
if sys.stdout.encoding != 'emoji':
    sys.stdout = codecs.getwriter('emoji')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding != 'emoji':
    sys.stderr = codecs.getwriter('emoji')(sys.stderr.buffer, 'strict')
