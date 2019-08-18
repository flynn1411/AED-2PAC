#-*-coding:utf-8-*-
from Translator import*

csv = Translator("csv")
tsv = Translator("tsv")

print (csv.translate("archivo.csv"))

print (tsv.translate("archivo.tsv"))