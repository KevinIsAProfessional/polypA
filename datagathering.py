#!/usr/bin/env python3
import pandas as pd
import sys

df = pd.read_csv(sys.argv[1], header=0)

totalcount = len(df.index)
mcount = df.query('Sex == "M"')['Reason'].count()
fcount = df.query('Sex == "F"')['Reason'].count()

#noncancercount = len(df.query('Cat == 1.0').index)
#precancercount = len(df.query('Cat == 2.0 | Cat == 3.0 | Cat == 4.0').index)
#cancercount = len(df.query('Cat == 5.0 | Cat == 6.0').index)

noncancercount = len(df.query('Cat == 1.0').index)
precancercount = len(df.query('Cat == 2.0').index)
cancercount = len(df.query('Cat == 3.0').index)
############################################################
# Reason for getting screened, by gender
############################################################

screeningdf = df.query('Reason == "screening"')
FHdf = df.query('Reason == "FHx"')
poldf = df.query('Reason == "Hx Pol"')

print('\033[1m' + "Reason for getting screened, by gender" + '\033[0m\n')
screeningcount = len(screeningdf.index)
mscreeningcount = len(screeningdf.query('Sex == "M"').index)
fscreeningcount = len(screeningdf.query('Sex == "F"').index)

print("Screening counts and percentages:\n\tM: %d, %4.2f\n\tF: %d, %4.2f\n\tTotal: %d\n"%
        (mscreeningcount, mscreeningcount/mcount, 
        fscreeningcount, fscreeningcount/fcount,
        screeningcount))

print('')

FHcount = len(FHdf.index)
mFHcount = len(FHdf.query('Sex == "M"').index)
fFHcount = len(FHdf.query('Sex == "F"').index)

print("FH counts and percentages:\n\tM: %d, %4.2f\n\tF: %d, %4.2f\n\tTotal: %d\n"%
        (mFHcount, mFHcount/mcount,
        fFHcount, fFHcount/fcount,
        FHcount))

polcount = len(poldf.index)
mpolcount = len(poldf.query('Sex == "M"').index)
fpolcount = len(poldf.query('Sex == "F"').index)

print("Hx pol counts and percentages:\n\tM: %d, %4.2f\n\tF: %d, %4.2f\n\tTotal: %d\n"%
        (mpolcount, mpolcount/mcount,
        fpolcount, fpolcount/fcount,
        polcount))


############################################################
# Cat of Screening, by Reason for getting screened
############################################################

print('\033[1m' + "Cat of screening, by Reason for getting screened" + '\033[0m\n')

noncancerscreeningcount = len(screeningdf.query('Cat == 1.0'))
precancerscreeningcount = len(screeningdf.query('Cat == 2.0 | Cat == 3.0 | Cat == 4.0'))
cancerscreeningcount = len(screeningdf.query('Cat == 5.0 | Cat == 6.0'))

print("Screening counts and percents:\n\tNoncancerous: %d, %4.2f \n\tPrecancerous: %d, %4.2f \n\tCancerous: %d, %4.2f \n\tPrecancer and Cancerous: %d, %4.2f \n" % (noncancerscreeningcount, 
    noncancerscreeningcount/screeningcount, 
    precancerscreeningcount, 
    precancerscreeningcount/screeningcount, 
    cancerscreeningcount, 
    cancerscreeningcount/screeningcount, 
    precancerscreeningcount+cancerscreeningcount, 
    (precancerscreeningcount+cancerscreeningcount)/screeningcount))


noncancerFHcount = len(FHdf.query('Cat == 1.0'))
precancerFHcount = len(FHdf.query('Cat == 2.0 | Cat == 3.0 | Cat == 4.0'))
cancerFHcount = len(FHdf.query('Cat == 5.0 | Cat == 6.0'))

print("FH counts and percents:\n\tNoncancerous: %d, %4.2f \n\tPrecancerous: %d, %4.2f \n\tCancerous: %d, %4.2f \n\tPrecancer and Cancerous: %d, %4.2f \n" % (noncancerFHcount, 
    noncancerFHcount/FHcount, 
    precancerFHcount, 
    precancerFHcount/FHcount, 
    cancerFHcount, 
    cancerFHcount/FHcount, 
    precancerFHcount+cancerFHcount, 
    (precancerFHcount+cancerFHcount)/FHcount))


noncancerpolcount = len(poldf.query('Cat == 1.0'))
precancerpolcount = len(poldf.query('Cat == 2.0 | Cat == 3.0 | Cat == 4.0'))
cancerpolcount = len(poldf.query('Cat == 5.0 | Cat == 6.0'))

print("Hx pol counts and percents:\n\tNoncancerous: %d, %4.2f \n\tPrecancerous: %d, %4.2f \n\tCancerous: %d, %4.2f \n\tPrecancer and Cancerous: %d, %4.2f \n" % (noncancerpolcount, 
    noncancerpolcount/polcount, 
    precancerpolcount, 
    precancerpolcount/polcount, 
    cancerpolcount, 
    cancerpolcount/polcount, 
    precancerpolcount+cancerpolcount, 
    (precancerpolcount+cancerpolcount)/polcount))


############################################################
# Cat of Screening, by Gender 
############################################################

print('\033[1m' + "Cat of screening, by gender" + '\033[0m\n')

mgenderdf = df.query('Sex == "M"')
fgenderdf = df.query('Sex == "F"')

malenoncancercount = len(mgenderdf.query('Cat == 1.0 | Cat == 7.0 | Cat == 8.0'))
maleprecancercount = len(mgenderdf.query('Cat == 2.0 | Cat == 3.0 | Cat == 4.0'))
malecancercount = len(mgenderdf.query('Cat == 5.0 | Cat == 6.0'))

print("\033[1m" + "Male: " + "\033[0m" + "counts and percents\n\tNoncancerous: %d, %4.2f \n\tPrecancerous: %d, %4.2f \n\tCancerous: %d, %4.2f \n\tPrecancer and Cancerous: %d, %4.2f \n" % 
    (malenoncancercount, malenoncancercount/mcount, #noncancer
    maleprecancercount, maleprecancercount/mcount,  #precancer
    malecancercount, malecancercount/mcount,        #cancer 
    maleprecancercount+malecancercount, 
    (maleprecancercount+malecancercount)/mcount))


femalenoncancercount = len(fgenderdf.query('Cat == 1.0 | Cat == 7.0 | Cat == 8.0'))
femaleprecancercount = len(fgenderdf.query('Cat == 2.0 | Cat == 3.0 | Cat == 4.0'))
femalecancercount = len(fgenderdf.query('Cat == 5.0 | Cat == 6.0'))

print('\033[1m' + "Female: " + '\033[0m' + "counts and percents\n\tNoncancerous: %d, %4.2f \n\tPrecancerous: %d, %4.2f \n\tCancerous: %d, %4.2f \n\tPrecancer and Cancerous: %d, %4.2f \n" % 
    (femalenoncancercount, femalenoncancercount/fcount, #noncancer
    femaleprecancercount, femaleprecancercount/fcount,  #precancer
    femalecancercount, femalecancercount/fcount,        #cancer 
    femaleprecancercount+femalecancercount, 
    (femaleprecancercount+femalecancercount)/fcount))

##################################################
# Printing the results
##################################################
print('\033[1m' + 'Numbers:' + '\033[0m')
print("%d people were screened\n"%totalcount)
print("%d of the screenings were Male.\n%d of the screenings were Female."%(mcount, fcount))
print("")
print("%d of the patients were average risk"%screeningcount)
print("%d of the patients had a family history"%FHcount)
print("%d of the patients had a history of polyps"%polcount)
print("")
print("%d of the screenings came back normal"%noncancercount)
print("%d of the screenings had adenomas"%precancercount)
print("%d of the screenings had adenocarcinoma"%cancercount)
print("\n\n")
print('\033[1m' + 'Statistics:' + '\033[0m')
print(format(noncancercount/totalcount, '.2%') + " of patients had normal results")
print(format(precancercount/totalcount, '.2%') + " of patients had adenoma")
print(format(cancercount/totalcount, '.2%') + " of patients had adennocarcinoma")
print('')
print(format(noncancerscreeningcount/screeningcount, '.2%') + " of patients that came in who were average risk had normal results")
print(format(precancerscreeningcount/screeningcount, '.2%') + " of patients that came in who were average risk had adenoma")
print(format(cancerscreeningcount/screeningcount, '.2%') + " of patients that came in who were average risk had adenocarcinoma")
print('')
print(format(noncancerFHcount/FHcount, '.2%') + " of patients that came in who were average risk had normal results")
print(format(precancerFHcount/FHcount, '.2%') + " of patients that came in who were average risk had adenoma")
print(format(cancerFHcount/FHcount, '.2%') + " of patients that came in who were average risk had adenocarcinoma")
print('')
print(format(noncancerpolcount/polcount, '.2%') + " of patients that came in who were average risk had normal results")
print(format(precancerpolcount/polcount, '.2%') + " of patients that came in who were average risk had adenoma")
print(format(cancerpolcount/polcount, '.2%') + " of patients that came in who were average risk had adenocarcinoma")
print('')
print(format(mscreeningcount/mcount,'.2%') + " of men who were screened were of average risk")
print(format(mFHcount/mcount,'.2%') + " of men who were screened had a family history")
print(format(mpolcount/mcount,'.2%') + " of men who were screened had a history of polyps")
print('')
print(format(malenoncancercount/mcount,'.2%') + " of men who were screened came back normal")
print(format(maleprecancercount/mcount,'.2%') + " of men who were screened had adenomas")
print(format(malecancercount/mcount,'.2%') + " of men who were screened had adenocarcinoma")
print('')
print(format(femalenoncancercount/fcount,'.2%') + " of women who were screened came back normal")
print(format(femaleprecancercount/fcount,'.2%') + " of women who were screened had adenomas")
print(format(femalecancercount/fcount,'.2%') + " of women who were screened had adenocarcinoma")
print('')
print(format(fscreeningcount/fcount,'.2%') + " of women who were screened were of average risk")
print(format(fFHcount/fcount,'.2%') + " of women who were screened had a family history")
print(format(fpolcount/fcount,'.2%') + " of women who were screened had a history of polyps")
print('')
