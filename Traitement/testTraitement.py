# -*- coding: utf-8 -*-
from TraitementNGrams import TraitementNGrams

trait = TraitementNGrams(3,'French')
words = trait.preprocessing('Je fais une Phrase pour tester le prétraitement. == .')
print(words)
