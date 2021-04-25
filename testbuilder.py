#!/usr/bin/env python3
import random
import csv
import datetime

def make_test_files():
    totals = stats()
    make_patient_file(totals)
    make_stats_file(totals)


###########################################################
#    Makes the patient files, fill out the stats info     #
###########################################################

def make_patient_file(totals):
    num_days = 0
    day_delta = datetime.timedelta(days=1)
    start_date = datetime.date.today()

    with open('test_patients.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name','Sex','Chart','Date','Cat','Reason']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        while(num_days < 365):
            procedures = random.randint(1,6)
            date = start_date + num_days*day_delta
            for i in range(0,procedures):
                writer.writerow(buildpatient(date, totals))
            num_days += 1

    csvfile.close()


def buildpatient(date, t):
    t.num_patients += 1

# Generate random values for the test patients file
    if(random.randint(0,1) == 0):
        sex = 'M'
    else:
        sex = 'F'

    cat = random.randint(1,3)
    if(cat == 1):
        t.num_norm += 1
    elif(cat == 2):
        t.num_pre += 1
    else:
        t.num_cancer += 1

    reason = random.randint(0,3)
    if(reason == 0):
        reason = 'FHx'
        t.num_fam_hist += 1
    elif(reason == 1):
        reason = 'screening'
        t.num_screening += 1
    else:
        reason = 'Hx Pol'
        t.num_hx_pol += 1

# Tally up results for the test stats file
    if(sex == "M"):
        t.num_male += 1
        if(reason == "FHx"):
            t.num_m_fam_hist += 1
            if(cat == 1):
                t.num_m_norm += 1
                t.num_norm_fam_hist += 1
            elif(cat == 2):
                t.num_m_pre += 1
                t.num_pre_fam_hist += 1
            else:
                t.num_m_cancer += 1
                t.num_cancer_fam_hist += 1 

        elif(reason == "screening"):
            t.num_m_screening += 1
            if(cat == 1):
                t.num_m_norm += 1
                t.num_norm_screening += 1
            elif(cat == 2):
                t.num_m_pre += 1
                t.num_pre_screening += 1
            else:
                t.num_m_cancer += 1
                t.num_cancer_screening += 1
        else:
            t.num_m_hx_pol += 1
            if(cat == 1):
                t.num_m_norm += 1
                t.num_norm_hx_pol += 1
            elif(cat == 2):
                t.num_m_pre += 1
                t.num_pre_hx_pol += 1
            else:
                t.num_m_cancer += 1
                t.num_cancer_hx_pol += 1

    if(sex == "F"):
        t.num_female += 1
        if(reason == "FHx"):
            t.num_f_fam_hist += 1
            if(cat == 1):
                t.num_f_norm += 1
                t.num_norm_fam_hist += 1
            elif(cat == 2):
                t.num_f_pre += 1
                t.num_pre_fam_hist += 1
            else:
                t.num_f_cancer += 1
                t.num_cancer_fam_hist += 1 

        elif(reason == "screening"):
            t.num_f_screening += 1
            if(cat == 1):
                t.num_f_norm += 1
                t.num_norm_screening += 1
            elif(cat == 2):
                t.num_f_pre += 1
                t.num_pre_screening += 1
            else:
                t.num_f_cancer += 1
                t.num_cancer_screening += 1
        else:
            t.num_f_hx_pol += 1
            if(cat == 1):
                t.num_f_norm += 1
                t.num_norm_hx_pol += 1
            elif(cat == 2):
                t.num_f_pre += 1
                t.num_pre_hx_pol += 1
            else:
                t.num_f_cancer += 1
                t.num_cancer_hx_pol += 1

    return {'Name' : "Joe Dirt",
            'Sex' : sex,
            'Chart' : '00001',
            'Date' : date,
            'Cat' : cat,
            'Reason' : reason
            }

###########################################################
#    Makes the stats file, stores the stats information   #
###########################################################

def make_stats_file(totals):
    with open('test_stats.csv', 'w', newline='') as statsfile:
        fieldnames = ['Category','Subcategory','Number','Percent','Comment']
        writer = csv.DictWriter(statsfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow(totals.patients_total())

        writer.writerow(totals.norm_total())
        writer.writerow(totals.pre_total())
        writer.writerow(totals.cancer_total())
        writer.writerow(totals.screening_total())
        writer.writerow(totals.fam_hist_total())
        writer.writerow(totals.hx_pol_total())

        writer.writerow(totals.norm_by_screening())
        writer.writerow(totals.norm_by_fam_hist())
        writer.writerow(totals.norm_by_hx_pol())

        writer.writerow(totals.pre_by_screening())
        writer.writerow(totals.pre_by_fam_hist())
        writer.writerow(totals.pre_by_hx_pol())

        writer.writerow(totals.cancer_by_screening())
        writer.writerow(totals.cancer_by_fam_hist())
        writer.writerow(totals.cancer_by_hx_pol())
        
        writer.writerow(totals.male_total())
        writer.writerow(totals.norm_by_male())
        writer.writerow(totals.pre_by_male())
        writer.writerow(totals.cancer_by_male())
        writer.writerow(totals.screening_by_male())
        writer.writerow(totals.fam_hist_by_male())
        writer.writerow(totals.hx_pol_by_male())

        writer.writerow(totals.female_total())
        writer.writerow(totals.norm_by_female())
        writer.writerow(totals.pre_by_female())
        writer.writerow(totals.cancer_by_female())
        writer.writerow(totals.screening_by_female())
        writer.writerow(totals.fam_hist_by_female())
        writer.writerow(totals.hx_pol_by_female())

    statsfile.close()
    
class stats:
    num_male = 0
    num_female = 0

    num_norm = 0
    num_pre = 0
    num_cancer = 0

    num_screening = 0
    num_fam_hist = 0
    num_hx_pol = 0

    num_m_norm = 0
    num_m_pre = 0
    num_m_cancer = 0
   
    num_f_norm = 0
    num_f_pre = 0
    num_f_cancer = 0
    
    num_m_screening = 0
    num_m_fam_hist = 0
    num_m_hx_pol = 0

    num_f_screening = 0
    num_f_fam_hist = 0
    num_f_hx_pol = 0

    num_norm_fam_hist = 0
    num_norm_screening = 0
    num_norm_hx_pol = 0

    num_pre_fam_hist = 0
    num_pre_screening = 0
    num_pre_hx_pol = 0

    num_cancer_fam_hist = 0
    num_cancer_screening = 0
    num_cancer_hx_pol = 0

    num_patients = 0

    def makerow(self, category='',subcategory='',number=0,percent='',comment=''):
        return {"Category" : category,
                "Subcategory" : subcategory,
                "Number" : number,
                "Percent" : percent,
                "Comment" : comment 
                }
    

    def patients_total(self):
        return self.makerow('Total',number=self.num_patients,comment='Total number of patients')

    def male_total(self):
        return self.makerow('Males',number=self.num_male,percent=self.generate_percent(self.num_male,self.num_patients),comment='Male/Total')

    def female_total(self):
        return self.makerow('Females','',number=self.num_female,percent=self.generate_percent(self.num_female,self.num_patients),comment='Female/Total')
    
    def norm_total(self):
        return self.makerow('Normal','',number=self.num_norm,percent=self.generate_percent(self.num_norm,self.num_patients),comment='Normal/Total')
    
    def pre_total(self):
        return self.makerow('Precancerous','',number=self.num_pre,percent=self.generate_percent(self.num_pre,self.num_patients),comment='Precancerous/Total')

    def cancer_total(self):
        return self.makerow('Cancerous','',number=self.num_cancer,percent=self.generate_percent(self.num_cancer,self.num_patients),comment='Cancerous/Total')
    
    def screening_total(self):
        return self.makerow('Screening','',number=self.num_screening,percent=self.generate_percent(self.num_screening,self.num_patients),comment='Screening/Total')

    def fam_hist_total(self):
        return self.makerow('Family History','',number=self.num_fam_hist,percent=self.generate_percent(self.num_fam_hist,self.num_patients),comment='Family History/Total')

    def hx_pol_total(self):
        return self.makerow('History of Polyps','',number=self.num_hx_pol,percent=self.generate_percent(self.num_hx_pol,self.num_patients),comment='History of Polyps/Total')
    
    def norm_by_male(self):
        this_ones_number = self.num_m_norm
        this_ones_name = 'Normal'
        return self.makerow('Males',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_male),comment='%s/Male'%(this_ones_name))
        
    def pre_by_male(self):
        this_ones_number = self.num_m_pre
        this_ones_name = 'Precancerous'
        return self.makerow('Males',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_male),comment='%s/Male'%(this_ones_name))

    def cancer_by_male(self):
        this_ones_number = self.num_m_cancer
        this_ones_name = 'Cancerous'
        return self.makerow('Males',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_male),comment='%s/Male'%(this_ones_name))

    def screening_by_male(self):
        this_ones_number = self.num_m_screening
        this_ones_name = 'Screening'
        return self.makerow('Males',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_male),comment='%s/Male'%(this_ones_name))

    def fam_hist_by_male(self):
        this_ones_number = self.num_m_fam_hist
        this_ones_name = 'Family History'
        return self.makerow('Males',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_male),comment='%s/Male'%(this_ones_name))
    
    def hx_pol_by_male(self):
        this_ones_number = self.num_m_hx_pol
        this_ones_name = 'History of Polyps'
        return self.makerow('Males',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_male),comment='%s/Male'%(this_ones_name))

    def norm_by_female(self):
        this_ones_number = self.num_f_norm
        this_ones_name = 'Normal'
        return self.makerow('Females',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_female),comment='%s/Female'%(this_ones_name))
        
    def pre_by_female(self):
        this_ones_number = self.num_f_pre
        this_ones_name = 'Precancerous'
        return self.makerow('Females',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_female),comment='%s/Female'%(this_ones_name))

    def cancer_by_female(self):
        this_ones_number = self.num_f_cancer
        this_ones_name = 'Cancerous'
        return self.makerow('Females',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_female),comment='%s/Female'%(this_ones_name))

    def screening_by_female(self):
        this_ones_number = self.num_f_screening
        this_ones_name = 'Screening'
        return self.makerow('Females',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_female),comment='%s/Female'%(this_ones_name))

    def fam_hist_by_female(self):
        this_ones_number = self.num_f_fam_hist
        this_ones_name = 'Family History'
        return self.makerow('Females',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_female),comment='%s/Female'%(this_ones_name))
    
    def hx_pol_by_female(self):
        this_ones_number = self.num_f_hx_pol
        this_ones_name = 'History of Polyps'
        return self.makerow('Females',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_female),comment='%s/Female'%(this_ones_name))


    def norm_by_screening(self):
        this_ones_number = self.num_norm_screening
        this_ones_name = 'Screening'
        return self.makerow('Normal',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_female),comment='%s/Normal'%(this_ones_name))
        
    def norm_by_fam_hist(self):
        this_ones_number = self.num_norm_fam_hist
        this_ones_name = 'Family History'
        return self.makerow('Normal',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_female),comment='%s/Normal'%(this_ones_name))
        
    def norm_by_hx_pol(self):
        this_ones_number = self.num_norm_hx_pol
        this_ones_name = 'History of Polyps'
        return self.makerow('Normal',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_female),comment='%s/Normal'%(this_ones_name))
        

    def pre_by_screening(self):
        this_ones_number = self.num_pre_screening
        this_ones_name = 'Screening'
        return self.makerow('Precancerous',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_female),comment='%s/Precancerous'%(this_ones_name))
        
    def pre_by_fam_hist(self): 
        this_ones_number = self.num_pre_fam_hist
        this_ones_name = 'Family History'
        return self.makerow('Precancerous',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_female),comment='%s/Precancerous'%(this_ones_name))
        
    def pre_by_hx_pol(self):
        this_ones_number = self.num_pre_hx_pol
        this_ones_name = 'History of Polyps'
        return self.makerow('Precancerous',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_female),comment='%s/Precancerous'%(this_ones_name))
        

    def cancer_by_screening(self):
        this_ones_number = self.num_cancer_screening
        this_ones_name = 'Screening'
        return self.makerow('Cancerous',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_female),comment='%s/Cancerous'%(this_ones_name))
        
    def cancer_by_fam_hist(self):
        this_ones_number = self.num_cancer_fam_hist
        this_ones_name = 'Family History'
        return self.makerow('Cancerous',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_female),comment='%s/Cancerous'%(this_ones_name))

    def cancer_by_hx_pol(self):
        this_ones_number = self.num_cancer_hx_pol
        this_ones_name = 'History of Polyps'
        return self.makerow('Cancerous',this_ones_name,number=this_ones_number,percent=self.generate_percent(this_ones_number,self.num_female),comment='%s/Cancerous'%(this_ones_name))
    

    def gender_totals(self):
        return
#        male_percent = self.generate_percent(self.num_male,self.num_patients)
#        female_percent = self.generate_percent(self.num_female,self.num_patients)
#        gender_report = "Number of Male patients:\n%d\n" % (self.num_male)
#        gender_report += "Percentage of patients that are male:\n%s\n" % (male_percent)
#        gender_report += "Number of Female patients:\n%d\n" % (self.num_female)
#        gender_report += "Percentage of patients that are female:\n%s\n" % (female_percent)
#        return gender_report

    def generate_percent(self,numerator,denominator):
        return format(numerator/denominator, '.2%')


    def print_stats(self):
        print("Number of patients: %d" % self.num_patients)
        print("Number of Male/Female: %d/%d" % (self.num_male, self.num_female))
        print("Number of normal/precancerous/cancerous: %d/%d/%d" % (self.num_norm, self.num_pre, self.num_cancer))
        print("Number of screening/family history/personal history: %d/%d/%d" % (self.num_screening, self.num_fam_hist, self.num_hx_pol))

    def return_stats(self):
        return "Number of patients: %d\n Number of Male/Female: %d/%d\n Number of normal/precancerous/cancerous: %d/%d/%d\nNumber of screening/family history/personal history: %d/%d/%d" % (self.num_patients, self.num_male, self.num_female, self.num_norm, self.num_pre, self.num_cancer, self.num_screening, self.num_fam_hist, self.num_hx_pol)



if __name__ == "__main__":
    make_test_files()
