from lib2to3.refactor import get_all_fix_names
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from tablib import Dataset

from .models import *

# Create your views here.
def home_view(request):
    return render(request, "home_view.html")

# create another view for the Alphanumeric operations

# now obtain the name parameters or values and pass it on to a variable here. 
# first we need to convert form inputs into a list variable

def results (request):
   return render (request, 'results.html', {'attributes': attributes})

def AlphaResults(request):
    VisitorName = request.GET['name']
    VisitorName = list(VisitorName)
    VisitorAttribute1 = "" # this variable holds the results to be displayed
    i=0
    j=234
    #create a dummy variable that holds all the database entries. 
     # create a dictionary (here we have assigned multiple keys to the same value)
    #pytha_num = {('A', 'S', 'J'):getattr(Alphatables,id=i) , ('B','K','T'):getattr(Alphatables,id=i),
                ###('Z','I','R'):getattr(Alphatables, id=i)}
    # this are the variables that will hold the attributes for each Name letter
    # create another dictionary for the iterations and looping

    pytha_num = {(('A', 'S', 'J'), ('B','K','T'), ('C','L','U'),('D','M','V'),('E','N','W'),
    ('F','O','X'),('G','P','Y'),('H','Q','Z')
    ,('Z','I','R')):getattr(Alphatables, id=i)}

    if (VisitorName[0]=='A' or 'S' or 'J'):
     attributess = getattr(Alphatables, id =244)
     return render (request, 'results.html', {'attributes': attributes})

    if (VisitorName[0]=='B' or 'K' or 'T'):
     attributess = getattr(Alphatables, id =245)

    if (VisitorName[0]=='C' or 'L' or 'U'):
     attributes = getattr(Alphatables, id =246)

    if (VisitorName[0]=='D' or 'M' or 'V'):
     attributes = getattr(AlphaResults, id=247)
    
    if (VisitorName[0]=='E' or 'N' or 'W'):
     attributes = getattr(AlphaResults, id=248)

    if (VisitorName[0]=='F' or 'O' or 'X'):
     attributess = getattr(Alphatables, id =249)

    if (VisitorName[0]=='G' or 'P' or 'Y'):
     attributess = getattr(Alphatables, id =250)

    if (VisitorName[0]=='H' or 'Q' or 'Z'):
        attributes = getattr(Alphatables, id=251)

    if (VisitorName[0]=='I' or 'R'):
     attributes = getattr(AlphaResults, id=252)

#.................................................................................................

    if (VisitorName[1]=='A' or 'S' or 'J'):
     attributess = getattr(Alphatables, id =244)

    if (VisitorName[1]=='B' or 'K' or 'T'):
     attributess = getattr(Alphatables, id =245)

    if (VisitorName[1]=='C' or 'L' or 'U'):
     attributes = getattr(Alphatables, id =246)

    if (VisitorName[1]=='D' or 'M' or 'V'):
     attributes = getattr(AlphaResults, id=247)
    
    if (VisitorName[1]=='E' or 'N' or 'W'):
     attributes = getattr(AlphaResults, id=248)

    if (VisitorName[1]=='F' or 'O' or 'X'):
     attributess = getattr(Alphatables, id =249)

    if (VisitorName[1]=='G' or 'P' or 'Y'):
     attributess = getattr(Alphatables, id =250)

    if (VisitorName[1]=='H' or 'Q' or 'Z'):
        attributes = getattr(Alphatables, id=251)

    if (VisitorName[1]=='I' or 'R'):
     attributes = getattr(AlphaResults, id=252)

#....................................................................................................#


    if (VisitorName[2]=='A' or 'S' or 'J'):
     attributess = getattr(Alphatables, id =244)

    if (VisitorName[2]=='B' or 'K' or 'T'):
     attributess = getattr(Alphatables, id =245)

    if (VisitorName[2]=='C' or 'L' or 'U'):
     attributes = getattr(Alphatables, id =246)

    if (VisitorName[2]=='D' or 'M' or 'V'):
     attributes = getattr(AlphaResults, id=247)
    
    if (VisitorName[2]=='E' or 'N' or 'W'):
     attributes = getattr(AlphaResults, id=248)

    if (VisitorName[2]=='F' or 'O' or 'X'):
     attributess = getattr(Alphatables, id =249)

    if (VisitorName[2]=='G' or 'P' or 'Y'):
     attributess = getattr(Alphatables, id =250)

    if (VisitorName[2]=='H' or 'Q' or 'Z'):
        attributes = getattr(Alphatables, id=251)

    if (VisitorName[2]=='I' or 'R'):
     attributes = getattr(AlphaResults, id=252)
    
#...............................................................................................

    if (VisitorName[3]=='A' or 'S' or 'J'):
     attributess = getattr(Alphatables, id =244)

    if (VisitorName[3]=='B' or 'K' or 'T'):
     attributess = getattr(Alphatables, id =245)

    if (VisitorName[3]=='C' or 'L' or 'U'):
     attributes = getattr(Alphatables, id =246)

    if (VisitorName[3]=='D' or 'M' or 'V'):
     attributes = getattr(AlphaResults, id=247)
    
    if (VisitorName[3]=='E' or 'N' or 'W'):
     attributes = getattr(AlphaResults, id=248)

    if (VisitorName[3]=='F' or 'O' or 'X'):
     attributess = getattr(Alphatables, id =249)

    if (VisitorName[3]=='G' or 'P' or 'Y'):
     attributess = getattr(Alphatables, id =250)

    if (VisitorName[3]=='H' or 'Q' or 'Z'):
        attributes = getattr(Alphatables, id=251)

    if (VisitorName[3]=='I' or 'R'):
     attributes = getattr(AlphaResults, id=252)

#..........................................................................................................

    if (VisitorName[4]=='A' or 'S' or 'J'):
     attributess = getattr(Alphatables, id =244)

    if (VisitorName[4]=='B' or 'K' or 'T'):
     attributess = getattr(Alphatables, id =245)

    if (VisitorName[4]=='C' or 'L' or 'U'):
     attributes = getattr(Alphatables, id =246)

    if (VisitorName[4]=='D' or 'M' or 'V'):
     attributes = getattr(AlphaResults, id=247)
    
    if (VisitorName[4]=='E' or 'N' or 'W'):
     attributes = getattr(AlphaResults, id=248)

    if (VisitorName[4]=='F' or 'O' or 'X'):
     attributess = getattr(Alphatables, id =249)

    if (VisitorName[4]=='G' or 'P' or 'Y'):
     attributess = getattr(Alphatables, id =250)

    if (VisitorName[4]=='H' or 'Q' or 'Z'):
        attributes = getattr(Alphatables, id=251)

    if (VisitorName[4]=='I' or 'R'):
     attributes = getattr(AlphaResults, id=252)
    
#......................................................................................................

    if (VisitorName[5]=='A' or 'S' or 'J'):
     attributess = getattr(Alphatables, id =244)

    if (VisitorName[5]=='B' or 'K' or 'T'):
     attributess = getattr(Alphatables, id =245)

    if (VisitorName[5]=='C' or 'L' or 'U'):
     attributes = getattr(Alphatables, id =246)

    if (VisitorName[5]=='D' or 'M' or 'V'):
     attributes = getattr(AlphaResults, id=247)
    
    if (VisitorName[5]=='E' or 'N' or 'W'):
     attributes = getattr(AlphaResults, id=248)

    if (VisitorName[5]=='F' or 'O' or 'X'):
     attributess = getattr(Alphatables, id =249)

    if (VisitorName[5]=='G' or 'P' or 'Y'):
     attributess = getattr(Alphatables, id =250)

    if (VisitorName[5]=='H' or 'Q' or 'Z'):
        attributes = getattr(Alphatables, id=251)

    if (VisitorName[5]=='I' or 'R'):
     attributes = getattr(AlphaResults, id=252)

#...........................................................................................................
    
    if (VisitorName[6]=='A' or 'S' or 'J'):
     attributess = getattr(Alphatables, id =244)

    if (VisitorName[6]=='B' or 'K' or 'T'):
     attributess = getattr(Alphatables, id =245)

    if (VisitorName[6]=='C' or 'L' or 'U'):
     attributes = getattr(Alphatables, id =246)

    if (VisitorName[6]=='D' or 'M' or 'V'):
     attributes = getattr(AlphaResults, id=247)
    
    if (VisitorName[6]=='E' or 'N' or 'W'):
     attributes = getattr(AlphaResults, id=248)

    if (VisitorName[6]=='F' or 'O' or 'X'):
     attributess = getattr(Alphatables, id =249)

    if (VisitorName[6]=='G' or 'P' or 'Y'):
     attributess = getattr(Alphatables, id =250)

    if (VisitorName[6]=='H' or 'Q' or 'Z'):
        attributes = getattr(Alphatables, id=251)

    if (VisitorName[6]=='I' or 'R'):
     attributes = getattr(AlphaResults, id=252)

#.................................................................................................
    
    if (VisitorName[7]=='A' or 'S' or 'J'):
     attributess = getattr(Alphatables, id =244)

    if (VisitorName[7]=='B' or 'K' or 'T'):
     attributess = getattr(Alphatables, id =245)

    if (VisitorName[7]=='C' or 'L' or 'U'):
     attributes = getattr(Alphatables, id =246)

    if (VisitorName[7]=='D' or 'M' or 'V'):
     attributes = getattr(AlphaResults, id=247)
    
    if (VisitorName[7]=='E' or 'N' or 'W'):
     attributes = getattr(AlphaResults, id=248)

    if (VisitorName[7]=='F' or 'O' or 'X'):
     attributess = getattr(Alphatables, id =249)

    if (VisitorName[7]=='G' or 'P' or 'Y'):
     attributess = getattr(Alphatables, id =250)

    if (VisitorName[7]=='H' or 'Q' or 'Z'):
        attributes = getattr(Alphatables, id=251)

    if (VisitorName[7]=='I' or 'R'):
     attributes = getattr(AlphaResults, id=252)


#.........................................................................................................   

    if (VisitorName[8]=='A' or 'S' or 'J'):
     attributess = getattr(Alphatables, id =244)

    if (VisitorName[8]=='B' or 'K' or 'T'):
     attributess = getattr(Alphatables, id =245)

    if (VisitorName[8]=='C' or 'L' or 'U'):
     attributes = getattr(Alphatables, id =246)

    if (VisitorName[8]=='D' or 'M' or 'V'):
     attributes = getattr(AlphaResults, id=247)
    
    if (VisitorName[8]=='E' or 'N' or 'W'):
     attributes = getattr(AlphaResults, id=248)

    if (VisitorName[8]=='F' or 'O' or 'X'):
     attributess = getattr(Alphatables, id =249)

    if (VisitorName[8]=='G' or 'P' or 'Y'):
     attributess = getattr(Alphatables, id =250)

    if (VisitorName[8]=='H' or 'Q' or 'Z'):
        attributes = getattr(Alphatables, id=251)

    if (VisitorName[8]=='I' or 'R'):
     attributes = getattr(AlphaResults, id=252)


#................................................................................................... 

    if (VisitorName[9]=='A' or 'S' or 'J'):
     attributess = getattr(Alphatables, id =244)

    if (VisitorName[9]=='B' or 'K' or 'T'):
     attributess = getattr(Alphatables, id =245)

    if (VisitorName[9]=='C' or 'L' or 'U'):
     attributes = getattr(Alphatables, id =246)

    if (VisitorName[9]=='D' or 'M' or 'V'):
     attributes = getattr(AlphaResults, id=247)
    
    if (VisitorName[9]=='E' or 'N' or 'W'):
     attributes = getattr(AlphaResults, id=248)

    if (VisitorName[9]=='F' or 'O' or 'X'):
     attributess = getattr(Alphatables, id =249)

    if (VisitorName[9]=='G' or 'P' or 'Y'):
     attributess = getattr(Alphatables, id =250)

    if (VisitorName[9]=='H' or 'Q' or 'Z'):
        attributes = getattr(Alphatables, id=251)

    if (VisitorName[9]=='I' or 'R'):
     attributes = getattr(AlphaResults, id=252) 

     return render (request, 'results.html', {'attributes': attributes})