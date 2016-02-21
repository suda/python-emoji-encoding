# Emoji encoding for 🐍

This module provides a custom source code encoding allowing usage of Emoji's for things like variable names or function names.

## Usage

Install the package with pip:
```
pip install emoji-encoding
```
**It's recommended to install it in [a virtualenv](https://virtualenv.readthedocs.org/en/latest/)**

After installation you can specify the encoding in the beginning of a Python file:

```python
# -*- coding: emoji -*-
def 📢(✉️):
    print(✉️)

📢("✋ 🌏")
```

## Uninstalling

This package will create `emoji.pth` file in your `site-packages` directory to autoload the codec. After removing the module you need to remove this file manually.

## Known issues

Currently the encoding is only available in imported modules so trying to run Emoji encoded file directly will fail:

```
$ python emoji.py
  File "emoji.py", line 1
SyntaxError: encoding problem: emoji
```

Easy workaround is to have an another file that imports the Emoji encoded file:

```shell
$ cat bootstrap.py
import emoji
$ python bootstrap.py
✋ 🌏
```

## History

It all started with Ola Sendecka's talk about [Emoji Driven Development](https://speakerdeck.com/jezdezcon/ola-sendecka-emoji-driven-development) which made me wonder: "why *can't* we use Emoji's in Python?". After a bit of hacking I was able to use them [with a patched cpython](https://twitter.com/suda/status/614814994367168512). This wasn't a perfect solution so playing with this idea I ended up with custom [codec](https://docs.python.org/3/library/codecs.html) that translates Emoji's to their ASCII representations and adds prefix/suffix to decode such unique string back to Unicode.
