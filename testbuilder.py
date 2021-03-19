#!/usr/bin/env python3
import random
import csv
import datetime



def buildpatient(date, t):
    t.num_patients += 1
    if(random.randint(0,1) == 0):
        sex = 'M'
        t.num_male += 1
    else:
        sex = 'F'
        t.num_female += 1

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
        t.num_screen += 1
    else:
        reason = 'Hx Pol'
        t.num_hx_pol += 1

    return {'Name' : "Joe Dirt",
            'Sex' : sex,
            'Chart' : '00001',
            'Date' : date,
            'Cat.' : cat,
            'Reason' : reason
            }

class stats:
    num_male = 0
    num_female = 0
    num_norm = 0
    num_pre = 0
    num_cancer = 0
    num_screen = 0
    num_fam_hist = 0
    num_hx_pol = 0
    num_patients = 0
    def print_stats(self):
        print("Number of patients: %d" % self.num_patients)
        print("Number of Male/Female: %d/%d" % (self.num_male, self.num_female))
        print("Number of normal/precancerous/cancerous: %d/%d/%d" % (self.num_norm, self.num_pre, self.num_cancer))
        print("Number of screening/family history/personal history: %d/%d/%d" % (self.num_screen, self.num_fam_hist, self.num_hx_pol))

    def return_stats(self):
        return "Number of patients: %d\n Number of Male/Female: %d/%d\n Number of normal/precancerous/cancerous: %d/%d/%d\nNumber of screening/family history/personal history: %d/%d/%d" % (self.num_patients, self.num_male, self.num_female, self.num_norm, self.num_pre, self.num_cancer, self.num_screen, self.num_fam_hist, self.num_hx_pol)



def main():
    totals = stats()
    num_days = 0
    day_delta = datetime.timedelta(days=1)
    start_date = datetime.date.today()

    with open('test_patients.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name','Sex','Chart','Date','Cat.','Reason']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        while(num_days < 365):
            procedures = random.randint(1,6)
            date = start_date + num_days*day_delta
            for i in range(0,procedures):
                writer.writerow(buildpatient(date, totals))
            num_days += 1

    csvfile.close()

    with open('test_stats.txt', 'w', newline='') as statsfile:
        statsfile.write(totals.return_stats())
    statsfile.close()

if __name__ == "__main__":
    main()
