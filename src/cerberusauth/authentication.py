"""
Authentication module for CerberusAuth.
"""

import xkcdpass.xkcd_password as xp

wordfile = xp.locate_wordfile()
words = xp.generate_wordlist(wordfile=wordfile, min_length=5, max_length=8)


def get_password():
    """Return password based on @wordlist."""
    return xp.generate_xkcdpassword(words, numwords=5)
