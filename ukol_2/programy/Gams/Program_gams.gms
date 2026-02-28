* Optimalizace výroby dvou typů stolů
* i = index typu stolu (1, 2)
Set i /1,2/;
* Parametry pro jednotlivé typy stolů
* potrebny_cas(i)  - čas potřebný na výrobu 1 kusu typu i (hodiny)
* prodejni_cena(i) - prodejní cena jednoho stolu typu i
* pocet_noh(i)     - počet nohou na jednom stole typu i
* pocet_skel(i)    - počet skleněných desek na jednom stole typu i
* pocet_drev(i)    - počet dřevěných desek na jednom stole typu i
Parameters potrebny_cas(i) /1 0.6, 2 1.5/, prodejni_cena(i) /1 200,2 350/, pocet_noh(i)/1 5,2 5/,
pocet_skel(i) /1 1,2 0/, pocet_drev(i) /1 0,2 1/;

* Cílová funkce: celkový zisk z prodeje stolů
Variable zisk;

* Rozhodovací proměnná: počet vyrobených stolů jednotlivých typů
Positive Variable pocet(i);

* Přehled omezení modelu
Equations drevo, sklo, nohy, vyplata, cas;

* Omezení na maximální dostupné množství dřeva (50 dřevěných desek)
drevo.. sum(i,pocet_drev(i)*pocet(i))=L=50;

* Omezení na maximální dostupné množství skla (35 skleněných desek)
sklo.. sum(i,pocet_skel(i)*pocet(i))=L=35;

* Omezení na počet nohou (300 kusů)
nohy.. sum(i,pocet_noh(i)*pocet(i))=L=300;

* Časové omezení výroby (maximálně 63 hodin)
cas.. sum(i,potrebny_cas(i)*pocet(i))=L=63;

* Definice zisku jako součtu tržeb za vyrobené stoly
vyplata.. sum(i,prodejni_cena(i)*pocet(i))=E=zisk;

* Definice a řešení modelu lineárního programování
model stoly /all/;
solve stoly maximizing zisk using LP;

* Výpis optimálního zisku a počtu vyrobených stolů
display zisk.L, pocet.L;
