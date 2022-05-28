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
    protein_file = str(refine_protein)+'_protein.pdb'
    ligand_file = str(refine_protein)+'_ligand.mol2'
    correct = os.system('cd '+str(towards_dir)+' && '+'/root/deltavina/bin/dvrf20.py -r '+ str(protein_file) +' -l '+str(ligand_file))
    score = 0
    try:
        with open(str(towards_dir)+'/output.csv','r') as f:
            f.readline()
            score = f.readline().split(',')[1]
    except:
        pass
    if correct==0:
        counter+=1
        with open('/mnt/processed_data/deltavinarf20_score_coreset.txt','a') as fo:
            fo.write(str(refine_protein)+' '+str(score)+'\n')
    # success_list.append(refine_protein)
# print(counter)
# print(success_list)


    #os.system('/root/deltavina/bin/dvrf20.py -r '+ str(protein_file) +' -l '+str(ligand_file))
    # os.system('cd /root/processed_data')
