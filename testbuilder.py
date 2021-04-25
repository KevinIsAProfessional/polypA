#!/usr/bin/env python3
import random
import csv
import datetime
import stats

def make_test_files():
    totals = stats.Stats()
    make_patient_file(totals)
    totals.make_stats_file("test_stats.csv")


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

if __name__ == "__main__":
    make_test_files()
