medida = float(input('uma distancia entre metros:'))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida * 1/10
hm = medida * 1/100
km = medida * 1/1000
print('A medida de {}m corresponde a {}dm, {}cm,{}mm,{}dam, {}hm e {}km'.format(medida,dm,cm,mm,dam,hm,km))