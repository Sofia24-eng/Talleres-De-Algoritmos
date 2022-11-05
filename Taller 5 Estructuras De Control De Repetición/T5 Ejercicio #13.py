est_pntj_alto=0
est_pntj_bajo=0
puntaje_max=0
puntaje_min=0
prom_pntj=0
porc_inf_prom=0
porc_sup_prom=0
inf_prom=0
sup_prom=0
def facultad_ing(admision: [(str, float)]):
    for nombre, puntaje in admision:
      if(puntaje>est_pntj_alto):
        est_pntj_alto=puntaje
      if(puntaje>est_pntj_bajo and puntaje<est_pntj_alto):
        est_pntj_bajo=puntaje
      puntaje_max=puntaje_max+est_pntj_alto
      puntaje_min=puntaje_min+est_pntj_bajo
      prom_pntj=(puntaje/len(facultad_ing))
      if(puntaje<prom_pntj):
        inf_prom=inf_prom+1
        porc_inf_prom=(inf_prom/len(facultad_ing))
      if(puntaje>prom_pntj):
        sup_prom=sup_prom+1
        porc_sup_prom=(sup_prom/len(facultad_ing))        
    return est_pntj_alto, est_pntj_bajo, puntaje_max, puntaje_min, prom_pntj, porc_inf_prom, porc_sup_prom