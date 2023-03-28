import ipdb
from lib import *

# Test your code below...

r1= Role("Inspector Lee")
r2= Role("Korben Dallas")
r3= Role("Tony Stark")
r4= Role("Padme Amidala")
r5= Role("Rick O'Connell")
r6= Role("Elena Gilbert")

a1= Actor("Jackie Chan")
a2= Actor("Bruce Willis")
a3= Actor("Brendan Fraser")
a4= Actor("Chris Tucker")
a5= Actor("Nina Dobrev")
a6= Actor("Natalie Portman")
a7= Actor("Gary Oldman")
a8= Actor("Robert Downey Jr.")
a9= Actor("Tom Ellis")
a10= Actor("Chris Evans")

au1= Audition("LA", True, r1, a1) 
au2= Audition("ATL", True, r2, a2)
au3= Audition("CHI", True, r3, a8)
au4= Audition("NY", True, r4, a6) 
au5= Audition("SD", True, r5, a3) 
au6= Audition("LA", True, r6, a5) 
au7= Audition("ATL", False, r3 , a1 )
au8= Audition("CHI", False, r4 , a2 )
au9= Audition("NY", False, r5 , a3 )
au10= Audition("SD", False, r6 , a4 )
au11= Audition("LA", False, r3 , a5 )
au12= Audition("ATL", False, r2 , a5 )
au13= Audition("CHI", False, r1 , a6 )
au14= Audition("NY", False, r2 , a8 )
au15= Audition("SD", False, r2 , a7 )
au16= Audition("LA", False, r4 , a10 )
au17= Audition("ATL", False, r1 , a9 )
au18= Audition("CHI", False, r5 , a8 )
au19= Audition("NY", False, r5 , a4 )
au20= Audition("SD", False, r6 , a3 )




# the below line allows us to stop & try stuff!
ipdb.set_trace()