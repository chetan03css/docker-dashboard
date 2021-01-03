from django.shortcuts import render
import re,os

# Create your views here.
def homepage(request):
    return render(request,'dockerdashboard.html')

def dockerdashboard(request):
    base_directory =os.path.dirname(os.path.abspath(__file__))

    imfile = os.path.join(base_directory,"files/dockerimages.txt")
    acfile = os.path.join(base_directory,"files/dockerallcontainers.txt")
    rcfile = os.path.join(base_directory,"files/dockerrunningcontainers.txt")

    filesList = [imfile, acfile, rcfile]

    data = {}

    for fname in filesList:

        fp = open(fname, "r")
        opList = []
        for line in fp.readlines():
            # remove more tha 2 whitespaces
            line = re.sub('  +', ':', line)
            # remove any newline char
            line = re.sub('\n', '', line)
            # split all the fields and store in list
            infoList = line.split(":")
            # to avoid any empty lis

            if len(infoList)==6:
                infoList.insert(5,"NO PORT MAPPED")

            if len(infoList) > 1:
                opList.append(infoList)

        # copy the list of list into dictionary
        if fname==imfile:
            data["images"] = opList
        elif fname==acfile:
            data["allcontainers"] = opList

        elif fname==rcfile:
            data["runningcontainers"] = opList

    for doc, val in data.items():
        print(doc, val)
    # data = {"name":"chetan"}

    return render(request,'dockerdashboard.html',context=data)

#
# request=" "
# dockerdashboard(request)
