#import logging
#from __future__ import print_function
import snap7, os, time
#from StringIO import StringIO
# for setup the Logo connection please follow this link
# http://snap7.sourceforge.net/logo.html


#logging.basicConfig(level=logging.INFO)

# Siemens LOGO devices Logo 8 is the default
Logo_7 = True

#logger = logging.getLogger(__name__)
hammermill = snap7.logo.Logo()
unload = snap7.logo.Logo()
control = snap7.logo.Logo()
conveyor = snap7.logo.Logo()

hammermill.connect("192.168.0.220",0x2300,0x0300)
unload.connect("192.168.0.221",0x2200,0x0300)
control.connect("192.168.0.222",0x2300,0x0300)
conveyor.connect("192.168.0.223",0x2200,0x0300)

while (1):
    time.sleep(.5)
    
    print("Hammermill Cabinet")
    print("I1  - " + str(hammermill.read("V1024.0")) + "  Q1 -  " + str(hammermill.read("V1064.0")))
    print("I2  - " + str(hammermill.read("V1024.1")) + "  Q2 -  " + str(hammermill.read("V1064.1")))
    print("I3  - " + str(hammermill.read("V1024.2")) + "  Q3 -  " + str(hammermill.read("V1064.2")))
    print("I4  - " + str(hammermill.read("V1024.3")) + "  Q4 -  " + str(hammermill.read("V1064.3")))
    print("I5  - " + str(hammermill.read("V1024.4")) + "  Q5 -  " + str(hammermill.read("V1064.4")))
    print("I6  - " + str(hammermill.read("V1024.5")) + "  Q6 -  " + str(hammermill.read("V1064.5")))
    print("I7  - " + str(hammermill.read("V1024.6")) + "  Q7 -  " + str(hammermill.read("V1064.6")))
    print("I8  - " + str(hammermill.read("V1024.7")) + "  Q8 -  " + str(hammermill.read("V1064.7")))
    print("I9  - " + str(hammermill.read("V1025.0")) + "  Q9 -  " + str(hammermill.read("V1065.0")))
    print("I10 - " + str(hammermill.read("V1025.1")) + "  Q10 - " + str(hammermill.read("V1065.1")))
    print("I11 - " + str(hammermill.read("V1025.2")) + "  Q11 - " + str(hammermill.read("V1065.2")))
    print("I12 - " + str(hammermill.read("V1025.3")) + "  Q12 - " + str(hammermill.read("V1065.3")))
    print("I13 - " + str(hammermill.read("V1025.4")))
    print("I14 - " + str(hammermill.read("V1025.5")))







   
