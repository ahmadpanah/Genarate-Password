# UTF-8
import random
import string
import sys
reload(sys)
sys.setdefaultencoding('UTF8')
def random_number():
    pwnumber=input("Number of Password:")
    pwlength=input("Lengh of Each Password:")
    if  pwlength<=10: # You Can Change it !
        for i in range(pwnumber):
            number=string.join(random.sample(string.digits+string.letters,pwlength)).replace(' ','')
            print number
    else :
        print "Oh . Max Number of Create Password is 10 ! Try Again."
        random_number()
if __name__=="__main__":
    random_number()