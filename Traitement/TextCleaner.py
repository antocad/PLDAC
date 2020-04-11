# -*- coding: utf-8 -*-
import re
import sys

class TextCleaner():
    """nettoie un text en retirant des caractéres étranges par exemple"""
    @staticmethod
    def clean(txt):
        res = txt.replace("\xa0", " ").replace("\u2009", " ").replace("\u202f", " ")#les espaces
        res = res.replace("\xad", "-").replace("−","-").replace("–","-")#les tirets 
        res = res.replace("’","'")#apostrophe
        res = res.replace('\x0c','').replace('■','')
        res = res.replace(' -- ',' ')
        res = re.sub('^ ?-{1,2} ?','',res,flags=re.MULTILINE)
        res = re.sub(r" +"," ",res)
        return res
        
if __name__=="__main__":
    txtpath = sys.argv[1]
    destpath = sys.argv[2]
    with open(txtpath,'r',encoding='utf_8') as f:
        txt = f.read()
    txtclean = TextCleaner.clean(txt)
    with open(destpath,'w',encoding="utf-8") as f:
        f.write(txtclean)
        