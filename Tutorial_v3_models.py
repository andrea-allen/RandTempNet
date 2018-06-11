#generates the randomisations

import sys
import RandTempNet as rn
import itertools as it
from pickle import dump

#General analysis of a dataset
#  lks_data (link_timeline()): object to analyse
#  dt (int): length of a time step
#  filename (string): name of the data file
def analysis_dat(lks_data,dt,ti=-1,tf=0,filename="analysis.pdf"):
    #conversions
    seq_data = rn.link_timeline_to_snapshot_sequence(lks_data,dt,ti,tf)
    tij_data = rn.snapshot_sequence_to_tij(seq_data)
    list_lk = lks_data.links()
    #data analysis
    #--activity timeline
    data_TL = rn.activity_timeline(seq_data)
    #--activity
    data_a = rn.activities(lks_data).values()
    #--activity durations
    data_alpha = list(it.chain(*rn.activity_durations(tij_data,dt).values()))
    #--inactivity durations
    data_dalpha = list(it.chain(*rn.inactivity_durations(tij_data,dt).values()))
    #--degrees
    data_k = rn.degrees(list_lk).values()
    #--strengths
    data_s = rn.strengths(lks_data).values()
    #--weights
    data_w = rn.weights(lks_data).values()
    #--number fo contacts
    data_n = rn.number_of_contacts(lks_data).values()
    #--contact durations
    data_tau = list(it.chain(*rn.contact_durations(lks_data).values()))
    #--intercontact durations
    data_dtau = list(it.chain(*rn.intercontact_durations(lks_data).values()))
    #save
    sortie = open(filename,'w')
    output = {"data_TL":data_TL,
              "data_a":data_a,
              "data_alpha":data_alpha,
              "data_dalpha":data_dalpha,
              "data_k":data_k,
              "data_s":data_s,
              "data_w":data_w,
              "data_n":data_n,
              "data_tau":data_tau,
              "data_dtau":data_dtau}
    dump(output,sortie)
    sortie.close()
#------------------------------------------

tij_data = rn.read_tij("tij_PS.dat")
dt = 20
ti = 0
tf = 172800
lks_data_1 = rn.tijtau_to_link_timeline(rn.tij_to_tijtau(tij_data,dt))

analysis_dat(lks_data_1,dt,ti,tf,"analysis_init.dat")

nsim = 100

for n in range(nsim):
   print n
   lks_data = rn.P__n_pTheta(lks_data_1)
   analysis_dat(lks_data,dt,ti,tf,"analysis_n_pTheta_%03d.dat" % n)

   lks_data = rn.P__L_pTheta(lks_data_1)
   analysis_dat(lks_data,dt,ti,tf,"analysis_L_pTheta_%03d.dat" % n)

   lks_data = rn.P__pTheta_k(lks_data_1)
   analysis_dat(lks_data,dt,ti,tf,"analysis_pTheta_k_%03d.dat" % n)

   lks_data = rn.P__pTheta(lks_data_1)
   analysis_dat(lks_data,dt,ti,tf,"analysis_pTheta_%03d.dat" % n)

   lks_data = rn.P__pttau(lks_data_1,dt)
   analysis_dat(lks_data,dt,ti,tf,"analysis_pttau_%03d.dat" % n)

   lks_data = rn.P__pitau_pidtau_t1(lks_data_1)
   analysis_dat(lks_data,dt,ti,tf,"analysis_pitau_pidtau_t1_%03d.dat" % n)

   lks_data = rn.P__pitau_pidtau(lks_data_1,ti,tf,dt)
   analysis_dat(lks_data,dt,ti,tf,"analysis_pitau_pidtau_%03d.dat" % n)

   lks_data = rn.P__pitau_t1_tw(lks_data_1,dt)
   analysis_dat(lks_data,dt,ti,tf,"analysis_pitau_t1_tw_%03d.dat" % n)

   lks_data = rn.P__pitau(lks_data_1,ti,tf,dt)
   analysis_dat(lks_data,dt,ti,tf,"analysis_pitau_%03d.dat" % n)

   lks_data = rn.P__L_ptau(lks_data_1,ti,tf,dt)
   analysis_dat(lks_data,dt,ti,tf,"analysis_L_ptau_%03d.dat" % n)