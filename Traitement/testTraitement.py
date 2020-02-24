# -*- coding: utf-8 -*-
from TraitementSimple import TraitementSimple

trait = TraitementSimple('French')
words = trait.preprocessing('Je fais une Phrase pour tester le prétraitement. == .')
print(words)
