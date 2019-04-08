import os
import pickle
import random
from getpass import getpass
def mainmenu():
    os.system('cls')
    print "\n\t\t\t\tMAINMENU\n"
    print "\t\t\t\t~~~~~~~~\n"
    print "\n\t\t1.MANAGING DIRECTOR"
    print "\n\t\t2.CHAIRMAN"
    print "\n\t\t3.SUPERVISORS"
    print "\n\t\t4.RESIDENTS"
    print "\n\t\t5.BUYERS"Andriaajai?tab=repositories
    print "\n\t\t6.OTHERS"
    print "\n\t\t7.BACK"
    print "\n\t\t8.EXIT"
    print "\nEnter your choice"
    c=input()
    if c==1:
        os.system('cls')
        managingdirector()
    elif c==2:
        os.system('cls')
        chairman()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    elif c==3:
        os.system('cls')
        supervisors()
    elif c==4:
        os.system('cls')
        residents()
    elif c==5:
        os.system('cls')
        buyers()
    elif c==6:
        os.system('cls')
        others()
    elif c==7:
        mainmenu()
    elif c==8:
        exit()
    else:
        exit()

def supervisors():
    print "\n\t\t\t\t\tLOGIN WINDOW"
    print "\n\t\t\t\t\t~~~~~ ~~~~~~"
    print "\n\n\n\n\n\t\t\tUsername:",
    a=raw_input()
    print "\n\t\t\t",
    b=getpass()

    if(a=="supervisors" and b=="shb"):
        supmenu()
    else:
        print "Unauthorised entry"
        x=raw_input()
        mainmenu()

def supmenu():
    os.system('cls')
    print "\n\t\t\t\tSUPERVISORS"
    print "\n\t\t\t\t~~~~~~~~~~~"

    print "\n\n\n\t\t1.Status\n\t\t2.News\n\t\t3.Draftbox\n\t\t4.Inbox\n\t\t5.Resident details\n\t\t6.Facilities\n\t\t7.About us\n\t\t8.Back\n\t\t9.Exit\n"
    print "\nEnter your choice"
    m=input()
    if m==1:
        s="supervisors"
        status(s)
    elif m==2:
        n="supervisors"
        news(n)
    elif m==3:
        k="supervisors"
        draftbox(k)
    elif m==4:
        j="supervisors"
        inbox(j)
    elif m==5:
        w="supervisors"
        resdetails(w)
    elif m==6:
        b="supervisors"
        facilities(b)
    elif m==7:
        l="supervisors"
        aboutus(l)
    elif m==8:
        mainmenu()
    elif m==9:
        exit()
    else:
        exit()

def managingdirector():
    print "\n\t\t\t\t\tLOGIN WINDOW"
    print "\n\t\t\t\t\t~~~~~~~~~~~~"
    print "\n\n\n\n\n\t\t\tUsername:",
    a=raw_input()
    print "\n\t\t\t",
    b=getpass()

    if(a=="md" and b=="shb"):
        mdmenu()
    else:
        print "Unauthorised entry"
        x=raw_input()
        mainmenu()

def mdmenu():
    os.system('cls')
    print "\n\t\t\t\tMANAGING DIRECTOR"
    print "\n\t\t\t\t~~~~~~~~ ~~~~~~~~"

    print "\n\n\n\t\t1.Finance\n\t\t2.Status\n\t\t3.Facilities\n\t\t4.Draft box\n\t\t5.Inbox\n\t\t6.News\n\t\t7.Residents details\n\t\t8.About us\n\t\t9.Back\n\t\t10.Exit"
    print "\nEnter your choice"
    m=input()
    if m==1:
        d="managing director"
              finance(d)
    elif m==2:
        s="managing director"
        status(s)
    elif m==3:
        b="managing director"
        facilities(b)
    elif m==4:
        k="managing director"
        draftbox(k)
    elif m==5:
        j="managing director"
        inbox(j)
    elif m==6:
        n="managing director"
        news(n)
    elif m==7:
        w="managing director"
        resdetails(w)
    elif m==8:
        l="managing director"
        aboutus(l)
        print "hfhg"
    elif m==9:
        mainmenu()
    elif m==10:
        exit()
    else:
        exit()

def chairman():
    os.system('cls')
    print "\n\t\t\t\t\tLOGIN WINDOW"
    print "\n\t\t\t\t\t~~~~~~~~~~~~"
    print "\n\n\n\n\n\t\t\tUsername:",
    a=raw_input()
    print "\n\t\t\t",
    b=getpass()

    if(a=="chairman" and b=="shb"):
        chairmanmenu()
    else:
        print "Unauthorised entry"
        x=raw_input()
        os.system('cls')
        mainmenu()

def  chairmanmenu():
    os.system('cls')
    print "\n\t\t\t\t\t\t\t\t\t\tCHAIRMAN\n";
    print "\n\t\t\t\t\t\t\t\t\t\t~~~~~~~~";
    print "\n\n\n\t\t1.Finance\n\t\t2.Status\n\t\t3.Facilities\n\t\t4.Draft box\n\t\t5.Inbox\n\t\t6.News\n\t\t7.Residents details\n\t\t8.About us\n\t\t9.Back\n\t\t10.Exit"
    print "Enter your choice"
    m=input()
    if m==1:
        d="chairman"
              finance(d)
    elif m==2:
        s="chairman"
        status(s)
    elif m==3:
        b="chairman"
        facilities(b)
    elif m==4:
        k="chairman"
        draftbox(k)
    elif m==5:
        j="chairman"
        inbox(j)
    elif m==6:
        n="chairman"
        news(n)
    elif m==7:
        w="chairman"
        resdetails(w)
    elif m==8:
        l="chairman"
        aboutus(l)
    elif m==9:
        mainmenu()
    elif m==10:
        exit()
    else:
        exit()

def residents():
    os.system('cls')
    print "\n\t\t\t\tLOGIN WINDOW"
    print "\n\t\t\t\t~~~~~ ~~~~~~"
    print "\n\n\n\n\n\t\t\tUserid:"
    userid=input()
    print "\n\t\t\t"
    password=getpass()
    f8=open("usedet.txt","r")
    str1=f8.read()
    str1=str1.replace("\n"," ")
        str1=str1.replace("\t"," ")
    l=str1.split(" ")
    for i in range(0,len(l),2):
        if l[i]==str(userid):
            if l[i+1]==password:
                resmenu()
    f8.close()
    f11=open("villausedet.txt","r");
    str2=f11.read()
    str2=str2.replace("\n"," ")
    str2=str2.replace("\t"," ")
    l1=str2.split(" ")
    for j in range(0,len(l1),2):
        if l1[j]==str(userid):
            if l1[j+1]==password:
                resmenu()
    f11.close()
    print "Invalid entry"
    p=raw_input()
    residents()

def resmenu():
    os.system('cls')
    print "\n\t\t\t\tRESIDENTS"
    print "\n\t\t\t\t~~~~~~~~~"

    print "\n\n\n\t\t1.Status\n\t\t2.News\n\t\t3.Draftbox\n\t\t4.Inbox\n\t\t5.Facilities\n\t\t6.Aboutus\n\t\t7.Back\n\t\t8.Exit\n"
    print "Enter your choice"
    p=input()
    if p==1:
        s="residents"
               status(s)
    elif p==2:
        n="residents"
               news(n)
    elif p==3:
        k="residents"
               draftbox(k);
    elif p==4:
        j="residents"
               inbox(j)
    elif p==5:
        b="residents"
               facilities(b)
    #elif p==6:
        #theatre()
    elif p==6:
        l="residents"
               aboutus(l);
    elif p==7:
        mainmenu();
    elif p==8:
        exit()

def buyers():
    os.system('cls')
    print "\n\t\t\t\tBUYERS"
    print "\n\t\t\t\t~~~~~~"
    print "\n\n\n\t\t1.Booking\n\t\t2.Facilities\n\t\t3.Aboutus\n\t\t4.Back\n\t\t5.Exit\n"
    print "Enter your choice"Andriaajai?tab=repositories
    ch=input()
    if ch==1:
        booking()
    elif ch==2:
        b="buyers"
              facilities(b)
    elif ch==3:
        l="buyers"
               aboutus(l)
    elif ch==4:
        mainmenu()
    elif ch==5:
        exit()
    else:
        exit()

def booking():Andriaajai?tab=repositories
    os.system('cls')
    print"\n\t\t\t\tBOOKING WINDOW"
    print"\n\t\t\t\t~~~~~~~ ~~~~~~"
    print"\n\t\t1.Flats\n\t\t2.Villas\n\t\t3.Back\n\t\t4.Exit\n"
    print"Enter your choice"
    l=input()
    if l==1:
        flats()
    elif l==2:
        villas()
    elif l==3:
        buyers()
    elif l==4:
        exit()
def flats():
    count=10
    os.system('cls')Andriaajai?tab=repositories
    print "\n\t\t\t\tBOOKING WINDOW"
    print "\n\t\t\t\t~~~~~~~ ~~~~~~"
    print "\n\n\n\n\n\n\tDo you want to book a flat in our apartments"
    f=raw_input()
    os.system('cls')
    if(f=='y'):
        f6=open("bookid.txt","r+")
        try:    
            p=f6.read(1)
            while p!="":
                if(p=="1"):
                    count=count-1
                p=f6.read(1)
        except EOFError:
            pass
        f6.close()Andriaajai?tab=repositories
    else:
        os.system('cls')
        buyers()
    if(count<=0):
        print "\n\n\n\n\n\n\n\t\t\t   "
        print "Sorry booking over"
        r=raw_input()
        buyers()
    else:
        print "\n\t\t\t\tBOOKING WINDOW"
        print "\n\t\t\t\t~~~~~~~ ~~~~~~"
        print "\n\n\n\n\n\n\n\t\t    No. of slots available are:",count
        k=raw_input()
    os.system('cls')
    print "\n\t\t\t\tBOOKING WINDOW"
    print "\n\t\t\t\t~~~~~~~ ~~~~~~"
    print "\n\n\n\n\n\t\t\t      Do you want to buy"
    l=raw_input()
    if(l=='y'):
        confirm()
    else:
        buyers()

def confirm():
    os.system('cls')
    print "\n\t\t\t\tBOOKING WINDOW"
    print "\n\t\t\t\t~~~~~~~ ~~~~~~"
    print "\n\n\n\t\t1.Enter the details and confirm\n\t\t2.Facilities\n\t\t 3.Back\n\t\t4.Exit"
    print "\nEnter your choice"
    t=input()
    if t==1:
        details()
    elif t==2:
        flatfacilities()
    elif t==3:
        buyers()
    elif t==4:
        exit()

def details():
    os.system('cls')                                                                                                       
    f7=open("res.txt","a+")
    print "\n\t\t\t\tDETAILS"
    print "\n\t\t\t\t~~~~~~~"
    print "\n\n\n"
    print "\t\tName:"
    name=raw_input()
    print "\t\tAddress:"
    address=raw_input()
    print "\t\tMobile No:"
    mob=input()    
    print "\t\tEmail:"
    email=raw_input()
    print "\t\tOccupational Address:"
    occadd=raw_input()
    
    os.system('cls')
    print "\n\t\t\t\tDETAILS"
    print "\n\t\t\t\t~~~~~~~"
    print "\n\n\n"
    print "\t\t1.Company lease\n\t\t2.Family"
    print "\nEnter your choice"
    j=input()
    if j==1:
        ownby="company"
    elif j==2:
        ownby="family"

    os.system('cls')
    print "\n\t\t\t\tDETAILS"
    print "\n\t\t\t\t~~~~~~~"
    print "\n\n\n"

    print "\t\t\tMode of Transaction\n"
    print "\t\t1.Cheque\n\t\t2.Cash"
    print "\nEnter your choice"
    l=input()
    if l==1:
        mot="cheque"
    elif 2:
        mot="cash"

    os.system('cls')
    print "\n\t\t\t\tDETAILS"
    print "\n\t\t\t\t~~~~~~~"
    print "\n\n\n"

    print "\t\t\tAdvance amount:"
    aa=input()
    global de
    de+=aa

    os.system('cls')
    print "\n\t\t\t\tCONFIRM WINDOW"
    print "\n\t\t\t\t~~~~~~~ ~~~~~~"
    print "\n\n\n\t\t1.Confirm\n\t\t2.Back\n\t\t3.Exit"
    print "\nEnter your choice"
    v=input()

    if(v==1):
        f7.write("\n")
        f7.write("Name:")
        f7.write(name)
        f7.write("\n");
        f7.write("Address:")
        f7.write(address)
        f7.write("\n")
        f7.write("Mobile No:")
        f7.write(str(mob))
        f7.write("\n")
        f7.write("Email:")
        f7.write(email)
        f7.write("\n")
        f7.write("Occupational Address:")
        f7.write(occadd)
        f7.write("\n");
        f7.write("Owned by:")
        f7.write(ownby)
        f7.write("\n")
        f7.write("Mode Of Transaction:")
        f7.write(mot)
        f7.write("\n")
        f7.write("Advance Amount:")
        f7.write(str(aa))
        f7.write("|")
        f7.close()
    
        os.system('cls')
        f6=open("bookid.txt","r+")
        try:
            c=f6.read(1)
            while c!="":
                if(c=="0"):
                    y=f6.tell()
                        f6.seek(y-1)
                    f6.write("1")    
                    break
                c=f6.read(1)
        except EOFError:
            pass
        f6.close()
        m=1000
        print "\n\t\t\t\tSKY HIGH BUILDERS"
        print "\n\t\t\t\t~~~ ~~~~ ~~~~~~~~"
        print "\n\n\n\n\n\t\t\t\tYour flat is booked"
        u=raw_input()
    
        os.system('cls')
        print "\n\t\t\t\tSKY HIGH BUILDERS"
        print "\n\t\t\t\t~~~ ~~~~ ~~~~~~~~"
        print "Welcome to your home"
        i=raw_input()
    
        os.system('cls')
        print "\n\t\t\t\tSKY HIGH BUILDERS"
        print "\n\t\t\t\t~~~ ~~~~ ~~~~~~~~"
        print "Your userid is shown below"
        print "\n\n\t\t\t\tUserid:"
    
        q=random.randint(1, 10)
        print m+q
        userid=m+q
        c=raw_input()
    
        os.system('cls')
        print "\n\t\t\t\tSKY HIGH BUILDERS"
        print "\n\t\t\t\t~~~ ~~~~ ~~~~~~~~"
        print "\n\n\n\t\t\t\tPlease enter your password"
        print "\n\n\t\t\t\t"
        password=getpass()
    
        f8=open("usedet.txt","a+")
        f8.write(str(userid))
        f8.write("\t")
        f8.write(password)
        f8.write("\n")
        f8.close()
    
        print "\nPress any key"
        i=raw_input()
        resmenu()

    elif v==2:
        os.system('cls')
        buyers()
    
    else:
        exit()

def flatfacilities():
    os.system('cls')
    print "\t\t\t\tFACILITIES\n"
    print "\t\t\t\t~~~~~~~~~~\n"
        
    print "\t! Air conditioned"
    print "\n"
    print "\t! Fully equipped kitchen"
    print "\n"
    print "\t! En suite bathroom"
    print "\n"
    print "\t! Bathrobes,towels and slippers"
    print "\n"
    print "\t! Living and dining area"
    print "\n"
    print "\t! TV with satellite channel"
    print "\n"
    print "\t! Free wifi"
    print "\n"
    print "\t! Direct dial telephones"
    print "\n"
    print "\t! Ipod docking station"
    print "\n"
    print "\t! Fine selection of king koil beddings"
    print "\n"
    print "\t! DVD player"
    print "\n"
    print "\t! Safety box"
    print "\n"
    print "\t! Laundry"
    print "\n"
    print "\t! Butler service"
    print "\n\n"
    print "Press any key"
    l=raw_input()
    confirm()

def villafacilities():
    os.system('cls')
    print "\t\t\t\tFACILITIES\n"
    print "\t\t\t\t~~~~~~~~~~\n\n"

    print "\t! Private swimming pool"
    print "\n"
    print "\t! Sundeck"
    print "\n"
    print "\t! Air conditioned"
    print "\n"
    print "\t! Fully equipped kitchen"
    print "\n"
    print "\t! En suite bathroom"
    print "\n"
    print "\t! Bathrobes,towels and slippers"
    print "\n"
    print "\t! Living and dining area"
    print "\n"
    print "\t! TV with satellite channel"
    print "\n"
    print "\t! Free wifi"
    print "\n"
    print "\t! Direct dial telephones"
    print "\n"
    print "\t! Ipod docking station"
    print "\n"
    print "\t! Fine selection of king koil beddings"
    print "\n"
    print "\t! DVD player"
    print "\n"
    print "\t! Safety box"
    print "\n"
    print "\t! Laundry"
    print "\n"
    print "\t! Butler service"
    print "\n"
    print "\t! Barbeque equipment for lunch or dinner party"
    print "\n\n"
    
    print "Press any key"
    f=raw_input()
    villaconfirm()

def villas():
    count1=10
    os.system('cls')
    print "\n\t\t\t\tBOOKING WINDOW"
    print "\n\t\t\t\t~~~~~~~ ~~~~~~"
    print "\n\n\n\n\n\n\tDo you want to book a villa in our apartments"
    f=raw_input()
    os.system('cls')
    if(f=='y'):
        f9=open("bookid1.txt","r+")
        try:    
            p=f9.read(1)
            while p!="":
                if(p=="1"):
                    count1=count1-1
                p=f9.read(1)
        except EOFError:
            pass
        f9.close()
    else:
        os.system('cls')
        buyers()
    if(count1<=0):
        print "\n\n\n\n\n\n\n\t\t\t   "
        print "Sorry booking over"
        r=raw_input()
        buyers()
    else:
        print "\n\t\t\t\tBOOKING WINDOW"
        print "\n\t\t\t\t~~~~~~~ ~~~~~~"
        print "\n\n\n\n\n\n\n\t\t    No. of slots available are:",count1
        k=raw_input()
    os.system('cls')
    print "\n\t\t\t\tBOOKING WINDOW"
    print "\n\t\t\t\t~~~~~~~ ~~~~~~"
    print "\n\n\n\n\n\t\t\t      Do you want to buy"
    l=raw_input()
    if(l=='y'):
        villaconfirm()
    else:
        buyers()

def villaconfirm():
    os.system('cls')
    print "\n\t\t\t\tBOOKING WINDOW"
    print "\n\t\t\t\t~~~~~~~ ~~~~~~"
    print "\n\n\n\t\t1.Enter the details and confirm\n\t\t2.Facilities\n\t\t3.Back\n\t\t4.Exit"
    print "\nEnter your choice"
    t=input()
    if t==1:
        villadetails()
    elif t==2:
        villafacilities()
    elif t==3:
        buyers()
    elif t==4:
        exit()

def villadetails():
    os.system('cls')                                                                                                       
    f10=open("villares.txt","a+")
    print "\n\t\t\t\tDETAILS"
    print "\n\t\t\t\t~~~~~~~"
    print "\n\n\n"
    print "\t\tName:"
    name=raw_input()
    print "\t\tAddress:"
    address=raw_input()
    print "\t\tMobile No:"
    mob=input()    
    print "\t\tEmail:"
    email=raw_input()
    print "\t\tOccupational Address:"
    occadd=raw_input()
    
    os.system('cls')
    print "\n\t\t\t\tDETAILS"
    print "\n\t\t\t\t~~~~~~~"
    print "\n\n\n"
    print "\t\t1.Company lease\n\t\t2.Family"
    print "\nEnter your choice"
    j=input()
    if j==1:
        ownby="company"
    elif j==2:
        ownby="family"

    os.system('cls')
    print "\n\t\t\t\tDETAILS"
    print "\n\t\t\t\t~~~~~~~"
    print "\n\n\n"

    print "\t\t\tMode of Transaction\n"
    print "\t\t1.Cheque\n\t\t2.Cash"
    print "\nEnter your choice"
    l=input()
    if l==1:
        mot="cheque"
    elif 2:
        mot="cash"

    os.system('cls')
    print "\n\t\t\t\tDETAILS"
    print "\n\t\t\t\t~~~~~~~"
    print "\n\n\n"

    print "\t\t\tAdvance amount:"
    aa=input()
    global de
    de+=aa

    os.system('cls')
    print "\n\t\t\t\tCONFIRM WINDOW"
    print "\n\t\t\t\t~~~~~~~ ~~~~~~"
    print "\n\n\n\t\t1.Confirm\n\t\t2.Back\n\t\t3.Exit"
    print "\nEnter your choice"
    v=input()

    if(v==1):
        f10.write("\n")
        f10.write("Name:")
        f10.write(name)
        f10.write("\n");
        f10.write("Address:")
        f10.write(address)
        f10.write("\n")
        f10.write("Mobile No:")
        f10.write(str(mob))
        f10.write("\n")
        f10.write("Email:")
        f10.write(email)
        f10.write("\n")
        f10.write("Occupational Address:")
        f10.write(occadd)
        f10.write("\n");
        f10.write("Owned by:")
        f10.write(ownby)
        f10.write("\n")
        f10.write("Mode Of Transaction:")
        f10.write(mot)
        f10.write("\n")
        f10.write("Advance Amount:")
        f10.write(str(aa))
        f10.write("|")
        f10.close()
    
        os.system('cls')
        f9=open("bookid1.txt","r+")
        try:
            c=f9.read(1)
            while c!="":
                if(c=="0"):
                    y=f9.tell()
                        f9.seek(y-1)
                    f9.write("1")    
                    break
                c=f9.read(1)
        except EOFError:
            pass
        f9.close()
        m=2000
        print "\n\t\t\t\tSKY HIGH BUILDERS"
        print "\n\t\t\t\t~~~ ~~~~ ~~~~~~~~"
        print "\n\n\n\n\n\t\t\t\tYour villa is booked"
        u=raw_input()
    
        os.system('cls')
        print "\n\t\t\t\tSKY HIGH BUILDERS"
        print "\n\t\t\t\t~~~ ~~~~ ~~~~~~~~"
        print "Welcome to your home"
        i=raw_input()
    
        os.system('cls')
        print "\n\t\t\t\tSKY HIGH BUILDERS"
        print "\n\t\t\t\t~~~ ~~~~ ~~~~~~~~"
        print "Your userid is shown below"
        print "\n\n\t\t\t\tUserid:"
    
        q=random.randint(1, 10)
        print m+q
        userid=m+q
        c=raw_input()
    
        os.system('cls')
        print "\n\t\t\t\tSKY HIGH BUILDERS"
        print "\n\t\t\t\t~~~ ~~~~ ~~~~~~~~"
        print "\n\n\n\t\t\t\tPlease enter your password"
        print "\n\n\t\t\t\t"
        password=getpass()
    
        f11=open("villausedet.txt","a+")
        f11.write(str(userid))
        f11.write("\t")
        f11.write(password)
        f11.write("\n")
        f11.close()
    
        print "\nPress any key"
        i=raw_input()
        residents()

    elif v==2:
        os.system('cls')
        buyers()
    
    else:
        exit()

def draftbox(k):
    os.system('cls')
    print "\n\t\t\t\tDRAFT BOX"
    print "\n\t\t\t\t~~~~~ ~~~"
    print "\n"
    print "Compose..................."
    print "\n\n\n"

    for i in range(0,84):
        print "-",                                                                                                                                                                                                                                                                                          
    print "\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tDATE:",
    date=raw_input()
    print "\tFrom:",
    print k
    print "\n\tTo:",
    to=raw_input()
    print "\n\n"
    cont=raw_input()

    if to=="chairman":
        f1=open("chairinbox.txt","a")
        f1.write("\n\n\t\t\t\t\t\t\t\t\t\t\t\tDate:")
        f1.write(date)
        f1.write("\n\n\tFrom:")
        f1.write(k)
        f1.write("\n\tTo:")
        f1.write(to)
        f1.write("\n\n")
        f1.write(cont)
        f1.close()

    elif to=="supervisors":
        f2=open("superinbox.txt","a")
        f2.write("\n\n\t\t\t\t\t\t\t\t\t\t\t\tDate:")
        f2.write(date)
        f2.write("\n\n\tFrom:")
        f2.write(k)
        f2.write("\n\tTo:")
        f2.write(to)
        f2.write("\n\n")
        f2.write(cont)
        
    elif to=="residents":
        f3=open("resinbox.txt","a")
        f3.write("\n\n\t\t\t\t\t\t\t\t\t\t\t\tDate:")
        f3.write(date)
        f3.write("\n\n\tFrom:")
        f3.write(k)
        f3.write("\n\tTo:")
        f3.write(to)
        f3.write("\n\n")
        f3.write(cont)

    elif to=="managing director":
        f4=open("mdinbox.txt","a")
        f4.write("\n\n\t\t\t\t\t\t\t\t\t\t\t\tDate:")
        f4.write(date)
        f4.write("\n\n\tFrom:")
        f4.write(k)
        f4.write("\n\tTo:")
        f4.write(to)
        f4.write("\n\n")
        f4.write(cont)

    print "\n\n"
    for i in range(0,84):
        print "-",      

    print "\n\tPress any key",
    x=raw_input()

    if k=="managing director":
        mdmenu()
    elif k=="chairman":
        chairmanmenu()
    elif k=="supervisors":
        supmenu()
    elif k=="residents":
        resmenu()

def facilities(b):
    os.system('cls')
    print "FACILITIES"
    print "~~~~~~~~~~"
    print "> Flats"
    print "> Villas"
    print "> School"
    print "> Gymnasium"
    print "> Car Service"
    print "> Hospital"
    print "> Library"
    print "> Swimming Pool"
    print "> ATM"
    print "> Park"
    print "> Shopping Mall"
    print "> Super Market"
    print "> Theatre"
    print "> Recreation Club"
    print "\n\nPress any key"
    t=raw_input()
    if b=="managing director":
        mdmenu()
    elif b=="chairman":
        chairmanmenu()
    elif b=="supervisors":
        supmenu()
    elif b=="buyers":
        buyers()
    elif b=="others":
        others()
    elif b=="residents":
        resmenu()

def inbox(j):
    os.system('cls')
    print "\n\n\t\t\t\tINBOX"
    print "\n\t\t\t\t~~~~~"
    print "\n"
    if  j=="chairman":
        f1=open("chairinbox.txt","r")
        y=f1.readline()
        while y!="":
            print y
            y=f1.readline()
        f1.close()
        print "Press any key";
        h=raw_input()
        chairmanmenu(); 
    elif  j=="supervisors":
        f2=open("superinbox.txt","r")
        y=f2.readline()
        while y!="":
            print y
            y=f2.readline()
        f2.close() 
        print "Press any key";
        h=raw_input()
        supmenu(); 
    elif  j=="residents":
        f3=open("resinbox.txt","r")
        y=f3.readline()
        while y!="":
            print y
            y=f3.readline()
        f3.close() 
        print "Press any key";
        b=raw_input()
        resmenu()
    elif  j=="managing director":
        f4=open("mdinbox.txt","r")
        y=f4.readline()
        while y!="":
            print y
            y=f4.readline()
        f4.close() 
        print "Press any key";
        h=raw_input()
        mdmenu(); 

def status(s):
    os.system("cls")
    print "\n\t\t\t\tSTATUS"
    print "\n\t\t\t\t~~~~~~"
    print "\n\n"
    f12=open("perola.txt","r")
    j=f12.read()
    print j
    f12.close();

    print "\n\n\n\n\t1.Next\t\t2.Back\n\n\tEnter your choice";
    x=input()

    if(x==1):
        os.system("cls")
        print "\n\t\t\t\tSTATUS"
        print "\n\t\t\t\t~~~~~~"
        print "\n\n"

        f13=open("square.txt","r")
        j1=f13.read()
        print j1
        f13.close()
    
        print "\n\n\n\n\t1.Next\t\t2.Back\n\n\tEnter your choice";
        x2=input()

        if(x2==1):

            os.system("cls")
            print "\n\t\t\t\tSTATUS"
            print "\n\t\t\t\t~~~~~~"
            print "\n\n"

            f14=open("panorama.txt","r")
            j2=f14.read()
            print j1
            f14.close()
            print "\n\n\n"
            print "Press any key"
            n=raw_input()
            if s=="managing director":
                mdmenu()
            elif s=="chairman":
                chairmanmenu()
            elif s=="supervisors":
                supmenu()
            elif s=="residents":
                resmenu()
            elif s=="others":
                others()
        else:
            if s=="managing director":
                mdmenu()
            elif s=="chairman":
                chairmanmenu()
            elif s=="supervisors":
                supmenu()
            elif s=="residents":
                resmenu()
            elif s=="others":
                others()
    else:
        if s=="managing director":
            mdmenu()
        elif s=="chairman":
            chairmanmenu()
        elif s=="supervisors":
            supmenu()
        elif s=="residents":
            resmenu()
        elif s=="others":
            others()

def news(n):
    os.system("cls")
    print "\n\t\t\t\tNEWS"    
    print "\n\t\t\t\t~~~~"
    print "\n\n\n"
    print "ANNUAL INTERFACE MULTIFAMILY TEXAS"
    print "\n"
    print "November 11 2016"
    print "\n\n"
    print "Dallas"
    print "\n"
    print "Daryl Smith, National Marketing Director at Sky High Builders recently participated on a five person panel at the 5th Annual Interface Multifamily Texas Conference, which focused on who is buying, building and financing apartment properties in Dallas, Houston, San Anton Austin, as 5th well as trends in leasing, management and operations,The event also looked at macroeconomic and demographic trends in influencing and impacting the apartment markets in Texas."
    print "\n\n"
    print "Press any key"
    g=raw_input()
    os.system("cls")
    print "\n\t\t\t\tNEWS"
    print "\n\t\t\t\t~~~~"
    print "\n\n\n"
    print "SKY HIGH BUILDERS LAUNCHES UPDATER TO HELP NATIONWIDE CUSYOMERS MOVE"
    print "\n"
    print "December 25 2016"
    print "\n\n"
    print "Dallas,Texas"
    print "\n"
    print "Sky High Builders ,one of the nation's leading multifamily management firms, has partnered with Updater, an automated and guided web application that provides residents with an easier and seamless moving evperiance."
    print "\n\n"
    
    print "'Finding new ways to elevate resident experiance is paramount to Sky High Builders and Updater is a great tool to help us accomplish that,' said Jennifer Staciokas, Sky High's senior vice president of marketing and training.We are thrilled to offer this virtual concierge service that allows us to implement a hassle-free moving experience for residents from the time they choose to live in a Sky High managed community. Updater is an absolute time saver.";
    print "\n"
    print "Press any key";
    j=raw_input();
    if n=="managing director":
        mdmenu()
    elif n=="chairman":
        chairmanmenu()
    elif n=="supervisors":
        supmenu()
    elif n=="residents":
        resmenu()
    elif n=="others":
        others()    
    
def aboutus(l):
    os.system("cls")
    print "\n\t\t\t\tSKY HIGH BUILDERS"
    print "\n\t\t\t\t~~~ ~~~~ ~~~~~~~~"    
    print "\n"

    print "Sky High Builders is a residential real estate developer in Kerala headquatered in Kochi.Started as a partnership firm in 1989 the first project of pinnacle builders was at Gandhinagar, Kochi.Pinnacle is headed by Keith Chapman and Peter Steele.\n\nIts prime activity includes the development of residential and villa projects and also has commercial property developmet.Sky High Builders has 137 projects till date in 10 cities across Kerala.The home builder has completed and handed over 122 residential projects and it has 15 on going residential projects.Sky High Builders has over 1.4 crore sq.ft built-up area in its credit.Over 6600 clients from about 51 countries invested in Skyhigh Builders.\n\nKerala's No.1 builder Sky High is at the top of its game yet again,being one of the first builders in India with the internetional quality certification, ISO 9001:2015.This has been certified to Sky High Builders by Bureau Veritas,an internationally recognised certifying body.It attends to various aspects of quality management ,ensuring that products and services delivered are of the highest quality, consistently meeting  cutomer requirements. A strong customer focus motivation and implication of top management ,the process approach and continual improvement are some of the other quality management principles that the ISO certification addresses.\n\n"
    r=raw_input()

    if l=="managing director":
        mdmenu()
    elif l=="chairman":
        chairmanmenu()
    elif l=="supervisors":
        supmenu()
    elif l=="residents":
        resmenu()
    elif l=="buyers":
        buyers()
    elif l=="others":
        others()

def finance(d):
    os.system("cls")
    if d=="managing director":
        print "\n\t\t\t\tFINANCE WINDOW"
        print "\n\t\t\t\t~~~~~~~ ~~~~~~"
        print "\n\n\n\t\t1.Update\n\t\t2.View\n\t\t3.Back"
        print "\nEnter your choice"
        b=input()
        c="managing director"
        if b==1:
            financeupdate(d)
        elif b==2:
            financeview(d)
        elif b==3:
            mdmenu()
        elif b==4:
            exit()
    else:
        financeview(d)

def financeview(d):
    os.system("cls")
    print "\n\t\t\t\tFINANCE WINDOW"
    print "\n\t\t\t\t~~~~~~~ ~~~~~~"
    print "\n\n\n\n\t\tAVAILABLE FUNDS :Rs.",o
    print "EXPECTED EARNING:Rs.",de
    
    print "\nPress any key"
    x=raw_input()

    if d=="managing director":
        mdmenu()
    elif d=="chairman":
        chairmanmenu()

def financeupdate(d):
    os.system("cls")
    print "\n\t\t\t\tFINANACE UPDATION"
    print "\n\t\t\t\t~~~~~~~~ ~~~~~~~~"

    print "Do you want to update finance details"
    u=raw_input()

    if(u=='y'):
        os.system("cls")
        print "\n\t\t\t\tFINANACE UPDATION"
        print "\n\t\t\t\t~~~~~~~~ ~~~~~~~~"
        print "Enter the new funds"
        m=input()
        #af+=m
        global o
        o+=m
        financeview(d)

        print "\nPress any key"
        x=raw_input()

    if d=="managing director":
        mdmenu()
    elif d=="chairman":
        chairmanmenu()
def others():
    os.system("cls")
    print "\n\t\t\t\tOTHERS"
    print "\n\t\t\t\t~~~~~~"
    print "\n\n\n\t\t1.Status\n\t\t2.News\n\t\t3.Facilities\n\t\t4.About us\n\t\t5.Back\n\t\t6.Exit"
    print "\nEnter your choice"
    q=input()
    if q==1:
        s="others"
        status(s)
    elif q==2:
        n="others"
        news(n)
    elif q==3:
        b="others"
        facilities(b)
    elif q==4:
        l="others"
        aboutus(l)
    elif q==5:
        mainmenu()
    elif q==6:
        exit()

def resdetails(w):
    os.system("cls")
    print "\n\t\t\t\tRESIDENT DETAILS"
    print "\n\t\t\t\t~~~~~~~~ ~~~~~~~"
    print "\n\n\n\t\t1.Flat residents\n\t\t2.Villa residents\n\t\t3.Back\n\t\t4.Exit\n"
    print "Enter your choice"
    p=input()
    if p==1:
        flatres(w)
    elif p==2:
        villares(w)
    elif p==3:
        if w=="managing director":
            mdmenu()
        elif w=="chairman":
            chairmanmenu()
        elif(w=="supervisors"):
            supmenu()
    elif p==4:
        exit()

def flatres(w):
    os.system("cls")
    print "\n\t\t\t\tFLAT RESIDENTS";
    print "\n\t\t\t\t~~~~ ~~~~~~~~~";
    print "\n";
    f7=open("res.txt","r+");
    y=f7.readline()
    while y!="":
        print y
        y=f7.readline()
    f7.close()
    print "Press any key";
    n=raw_input();
    if w=="managing director":
        mdmenu()
    elif w=="chairman":
        chairmanmenu()
    elif w=="supervisors":
        supmenu()

def villares(w):
    os.system("cls")
    print "\n\t\t\t\tVILLA RESIDENTS";
    print "\n\t\t\t\t~~~~~ ~~~~~~~~~";
    print "\n";
    f10=open("villares.txt","r+");
    y=f10.readline()
    while y!="":
        print y
        y=f10.readline()
    f10.close()
    print "Press any key";
    n=raw_input();

    if w=="managing director":
        mdmenu()
    elif w=="chairman":
        chairmanmenu()
    elif w=="supervisors":
        supmenu()


print "my new project"
o=1200000
de=100000
mainmenu()
