from sys import path
import os

path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "packages",
            "extrapack.zip"
        )
    )
)

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import FunI
from extra.good.beta import FunB

print(sig.FunS())
print(alp.FunA())
print(FunI())
print(FunB())
