T=readtable('mycsv.csv')

p=T{:,1}
q=T{:,2}
save('mymat.mat','p','q')
