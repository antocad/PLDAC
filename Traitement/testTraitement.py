# -*- coding: utf-8 -*-
from TraitementNGrams import TraitementNGrams
from collections import Counter

trait = TraitementNGrams(1,3,'French')
words = trait.preprocessing("l’insuffisance rénale.")
print(words)
