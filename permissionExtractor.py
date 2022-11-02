from xml.dom import minidom
import shutil
import os

dir = input("APKs directory: ")

for file in os.listdir(dir):
    try:
        if file.endswith(".apk"):

            os.system("apktool d %s" %(file))
            maniDir = os.path.splitext(file)[0]
            try:
                xmldoc = minidom.parse('%s/AndroidManifest.xml' %(maniDir))
                itemlist = xmldoc.getElementsByTagName('uses-permission')

                f = open("%s.txt" %(maniDir), "a")
                for s in itemlist:
                    f.write(s.attributes['android:name'].value)
                    f.write("\n")

            except:
                shutil.rmtree(maniDir)
                print("failed for file, moving to next")

            shutil.rmtree(maniDir)

    except:
        print("failed for file %s" %(file))
