import glob
import os
from turtle import towards

files = open('core_set_protein.txt','r')
wait_list =  [l[:-1] for l in files if l.strip()]
counter = 0
success_list=[]
for refine_protein in wait_list:
    # print('*'*10+str(refine_protein)+'*'*10)
    base_dir ='/mnt/processed_data/coreset'
    towards_dir = os.path.join(base_dir,str(refine_protein))
    score = '\n'
    try:
        with open(str(towards_dir)+'/input.csv','r') as f:
            f.readline()
            score = f.readline().split(',')[1:]
            score = ','.join(score)
            with open('/mnt/processed_data/vina_feature_test.txt','a') as fo:
                fo.write(str(refine_protein)+' '+str(score))
    except:
        pass
    # if correct==0:
    #     counter+=1
    
    # success_list.append(refine_protein)
# print(counter)
# print(success_list)


    #os.system('/root/deltavina/bin/dvrf20.py -r '+ str(protein_file) +' -l '+str(ligand_file))
    # os.system('cd /root/processed_data')
