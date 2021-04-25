import csv

###########################################################
#    Makes the stats file, stores the stats information   #
###########################################################
    
class Stats:
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

    def generate_percent(self,numerator,denominator):
        return format(numerator/denominator, '.2%')

    def make_stats_file(self, outfile):
        with open(outfile, 'w', newline='') as statsfile:
            fieldnames = ['Category','Subcategory','Number','Percent','Comment']
            writer = csv.DictWriter(statsfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow(self.patients_total())

            writer.writerow(self.norm_total())
            writer.writerow(self.pre_total())
            writer.writerow(self.cancer_total())
            writer.writerow(self.screening_total())
            writer.writerow(self.fam_hist_total())
            writer.writerow(self.hx_pol_total())

            writer.writerow(self.norm_by_screening())
            writer.writerow(self.norm_by_fam_hist())
            writer.writerow(self.norm_by_hx_pol())

            writer.writerow(self.pre_by_screening())
            writer.writerow(self.pre_by_fam_hist())
            writer.writerow(self.pre_by_hx_pol())

            writer.writerow(self.cancer_by_screening())
            writer.writerow(self.cancer_by_fam_hist())
            writer.writerow(self.cancer_by_hx_pol())
            
            writer.writerow(self.male_total())
            writer.writerow(self.norm_by_male())
            writer.writerow(self.pre_by_male())
            writer.writerow(self.cancer_by_male())
            writer.writerow(self.screening_by_male())
            writer.writerow(self.fam_hist_by_male())
            writer.writerow(self.hx_pol_by_male())

            writer.writerow(self.female_total())
            writer.writerow(self.norm_by_female())
            writer.writerow(self.pre_by_female())
            writer.writerow(self.cancer_by_female())
            writer.writerow(self.screening_by_female())
            writer.writerow(self.fam_hist_by_female())
            writer.writerow(self.hx_pol_by_female())

        statsfile.close()

