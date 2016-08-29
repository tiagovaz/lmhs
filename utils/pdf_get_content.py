# -*- coding: utf-8 -*-

import os, sys, django
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

sys.path.append("/var/www/lmhs")
os.environ["DJANGO_SETTINGS_MODULE"] = "lmhs.settings"
django.setup()

from lmhsweb.models import *

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str

objs = Main.objects.all()

pdfs_path = "/var/www/lmhs/lmhsweb/media/"

for o in objs:
    pdf_file = pdfs_path + o.cote_calcul_url + ".pdf"
    if os.path.isfile(pdf_file):
        print o.pk, pdf_file
        text = convert_pdf_to_txt(pdf_file)
        Main.objects.filter(pk=o.pk).update(pdf_text=text)
