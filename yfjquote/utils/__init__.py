# Copyright (C) 2021 @survivor7777777
# See LICENSE for details.

import random
import re

from . import constant as C
from . import pattern as P

def random_user_agent():
    return random.choice(C.USER_AGENTS)

def remove_commas(text):
    return P.COMMAS.sub('', text)
