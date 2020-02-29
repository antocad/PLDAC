# -*- coding: utf-8 -*-
from TraitementNGrams import TraitementNGrams
from collections import Counter

trait = TraitementNGrams(2,'French')
words = trait.preprocessing('Je fais une Phrase pour tester le prétraitement pour tester .')
print(Counter(words))
