import binascii
import sys
import os

try:
    import pefile
except ImportError:
    print 'pefile not installed, see http://code.google.com/p/pefile/'
    print 'OR use command line and type "easy_install pefile"'
    sys.exit()

def ValidatePE(arg):
        seccount = len(arg.sections)
        rawdata = arg.sections[seccount-1].SizeOfRawData
        ptrtorawdata = arg.sections[seccount-1].PointerToRawData
        sectionsize = rawdata + ptrtorawdata
        filesizel = os.path.getsize(os.path.join(root,file))
        filesize = str(filesizel)
        if (sectionsize == int(filesize)):
            return "Valid"
        elif (sectionsize > int(filesize)):
            return "Corrupted"
        else:
            return "Overlay"



if ((len(sys.argv)) < 2):
    print "USAGE PEChecker.py <file/folder location>"
elif ((len(sys.argv)) > 2):
      print "USAGE PEChecker.py <file/folder location>"
else:
    if (os.path.isdir(os.path.abspath(sys.argv[1]))):
        for root,dirs,files in os.walk(os.path.abspath(sys.argv[1])):
            for file in files:
                try:
                    pe = pefile.PE(os.path.join(root,file))
                    print os.path.join(root,file) + "," + ValidatePE(pe)

                except:
                    print  os.path.join(root,file) + ",Not a Valid PE File"
    elif(os.path.isfile(sys.argv[1])):
        file = os.path.abspath(sys.argv[1])
        root = os.path.dirname(file)
        try:
            pe = pefile.PE(file)
            print file + "," + ValidatePE(pe)
        except:
            print  file + ",Not a Valid PE File"



