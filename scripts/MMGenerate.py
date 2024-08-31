from Main import main as APmain
from BaseClasses import get_seed
from typing import Optional


def generate(seed: Optional[int] = None, callback=APmain):
    seed = get_seed(seed)
    return callback(erargs, seed)
