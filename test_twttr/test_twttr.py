from twttr import shorten

def test_shorten_lowers():
    assert shorten("twitter") == "twttr"
    assert shorten("analogo") == "nlg"
    assert shorten("cs50") == "cs50"
    assert shorten("murcielago") == "mrclg"
    assert shorten("what's your name?") == "wht's yr nm?"

def test_shorten_uppers():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("ANALOGO") == "NLG"
    assert shorten("CS50") == "CS50"
    assert shorten("MURCIELAGO") == "MRCLG"
    assert shorten("WHAT'S YOUR NAME?") == "WHT'S YR NM?"
