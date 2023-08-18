# 17.08.2023
# PDF script insert JavaScript code into PDF files.

import argparse, ast
import logging
import sys
import os.path
from pypdf import PdfReader, PdfWriter

logging.basicConfig(level=logging.ERROR)
DFileName='TheBattle.pdf'

def ReadPayload(FN): #get payload from file
    try:
        with open(FN,"r") as text:
            res=text.read()
    except:
        logging.error('Error opening file')
    return res

def InjectPayload(FN,PL): # inject payload intoPDF file
    reader = PdfReader(FN)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    # writer.add_js("this.print({bUI:true,bSilent:false,bShrinkToFit:true});") # add payload
    writer.add_js(PL) # add payload
    writer.add_metadata(reader.metadata)
    SaveFNLST=FN.split('.')
    SaveFNLST[1]='PL'
    SaveFN=''.join(SaveFNLST)+'.pdf'
    try:
        with open(SaveFN, "wb") as f: # Save the new PDF to a file
            writer.write(f)
    except:
        print ('Error writing to file')

def SetArgs():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-p", "--payload", help="payload file",required=False,default='payload.js')
    argParser.add_argument("-i", "--input", help="Working file (PDF)",required=False,default=DFileName)
    args = argParser.parse_args()
    return args.payload,args.input

def main():
    UserArgs=SetArgs()
    if os.path.exists(UserArgs[0]) and os.path.exists(UserArgs[1]): # Check if files exist
        payload=ReadPayload(UserArgs[0])
        InjectPayload(UserArgs[1],payload)

    else: #cannot find files
        print('Payload / Working file not exist')
        sys.exit()

if __name__ == '__main__':
    main()