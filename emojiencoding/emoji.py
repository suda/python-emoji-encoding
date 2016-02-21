import codecs
import emote
import re

decoding_prefix = "emoji_start_"
decoding_sufix = "_emoji_end"
# TODO: Make regex non greedy
decoding_pattern = re.compile("%s([\w\-]+)%s" % (decoding_prefix, decoding_sufix))
try:
    # UCS-4
    highpoints = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
except re.error:
    # UCS-2
    highpoints = re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')

class EmojiCodec(codecs.Codec):
    def encode(self, input, errors='strict'):
        emojis = decoding_pattern.finditer(input)
        for emoji in emojis:
            emoji_string = emoji.group(1)
            input = input.replace(emoji.group(0), emote.lookup(emoji_string))
        return (input.encode('utf8'), len(input))

    def decode(self, input, errors='strict'):
        input_string = codecs.decode(input, 'utf8')
        emojis = highpoints.finditer(input_string)

        for emoji in emojis:
            emoji_string = emoji.group(0)
            substitute = "%s%s%s" % (decoding_prefix, emote.decode(emoji_string), decoding_sufix)
            input_string = input_string.replace(emoji_string, substitute)
        return (input_string, len(input))

class EmojiIncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return EmojiCodec().encode(input)

class EmojiIncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return EmojiCodec().decode(input)

class EmojiStreamReader(EmojiCodec, codecs.StreamReader):
    pass

class EmojiStreamWriter(EmojiCodec, codecs.StreamWriter):
    pass

def search(encoding):
    if encoding == "emoji":
        return codecs.CodecInfo(
            name='emoji',
            encode=EmojiCodec().encode,
            decode=EmojiCodec().decode,
            incrementalencoder=EmojiIncrementalEncoder,
            incrementaldecoder=EmojiIncrementalDecoder,
            streamreader=EmojiStreamReader,
            streamwriter=EmojiStreamWriter,
        )
    return None

codecs.register(search)
