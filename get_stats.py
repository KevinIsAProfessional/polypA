#!/usr/bin/env python3
import pandas
import stats
import sys


def get_data(filename):
    df = pandas.read_csv(filename,header=0)

    data = stats.Stats()

    data.num_male = len(df.query('Sex == "M"').index)
    data.num_female = len(df.query('Sex == "F"').index)

    data.num_norm = len(df.query('Cat == 1.0').index) 
    data.num_pre = len(df.query('Cat == 2.0').index) 
    data.num_cancer = len(df.query('Cat == 3.0').index)

    data.num_screening = len(df.query('Reason == "screening"').index)
    data.num_fam_hist = len(df.query('Reason == "FHx"').index)
    data.num_hx_pol = len(df.query('Reason == "Hx Pol"').index)

    data.num_m_norm = len(df.query('Sex == "M"').query("Cat == 1.0"))
    data.num_m_pre = len(df.query('Sex == "M"').query("Cat == 2.0")) 
    data.num_m_cancer = len(df.query('Sex =="M"').query("Cat == 3.0"))

   
    data.num_f_norm =  len(df.query('Sex == "F"').query("Cat == 1.0"))
    data.num_f_pre = len(df.query('Sex == "F"').query("Cat == 2.0")) 
    data.num_f_cancer  = len(df.query('Sex =="F"').query("Cat == 3.0")) 
    
    data.num_m_screening = len(df.query('Sex == "M"').query("Reason == 'screening'"))
    data.num_m_fam_hist = len(df.query('Sex == "M"').query("Reason == 'FHx'")) 
    data.num_m_hx_pol = len(df.query('Sex =="M"').query("Reason == 'Hx Pol'"))
                                                                               
    data.num_f_screening = len(df.query('Sex == "F"').query("Reason == 'screening'"))                                                       
    data.num_f_fam_hist = len(df.query('Sex == "F"').query("Reason == 'FHx'")) 
    data.num_f_hx_pol = len(df.query('Sex =="F"').query("Reason == 'Hx Pol'")) 
                           
    data.num_norm_screening =  len(df.query('Cat == 1.0').query('Reason == "screening"'))
    data.num_norm_fam_hist = len(df.query('Cat == 1.0').query('Reason == "FHx"'))
    data.num_norm_hx_pol =    len(df.query('Cat == 1.0').query('Reason == "Hx Pol"'))


    data.num_pre_screening = len(df.query('Cat == 2.0').query('Reason == "screening"'))
    data.num_pre_fam_hist = len(df.query('Cat == 2.0').query('Reason == "FHx"'))       
    data.num_pre_hx_pol = len(df.query('Cat == 2.0').query('Reason == "Hx Pol"'))

    data.num_cancer_screening = len(df.query('Cat == 3.0').query('Reason == "screening"'))
    data.num_cancer_fam_hist = len(df.query('Cat == 3.0').query('Reason == "FHx"'))        
    data.num_cancer_hx_pol = len(df.query('Cat == 3.0').query('Reason == "Hx Pol"'))

    data.num_patients = len(df.index)  
    
    data.make_stats_file("data_stats.csv")


if __name__=="__main__":
    get_data(sys.argv[1])
