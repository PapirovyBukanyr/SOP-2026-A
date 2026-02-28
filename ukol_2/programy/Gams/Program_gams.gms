Set i /1,2/;
Parameters potrebny_cas(i) /1 0.6, 2 1.5/, prodejni_cena(i) /1 200,2 350/, pocet_noh(i)/1 5,2 5/,
pocet_skel(i) /1 1,2 0/, pocet_drev(i) /1 0,2 1/;
Variable zisk;
Positive Variable pocet(i);
Equations drevo, sklo, nohy, vyplata, cas;
drevo.. sum(i,pocet_drev(i)*pocet(i))=L=50;
sklo.. sum(i,pocet_skel(i)*pocet(i))=L=35;
nohy.. sum(i,pocet_noh(i)*pocet(i))=L=300;
cas.. sum(i,potrebny_cas(i)*pocet(i))=L=63;
vyplata.. sum(i,prodejni_cena(i)*pocet(i))=E=zisk;

model stoly /all/;
solve stoly maximizing zisk using LP;
display zisk.L, pocet.L;
