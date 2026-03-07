import pulp
#inicializace modelu
model = pulp.LpProblem("Maximize_Zisku_Notip", pulp.LpMaximize)
#D-dřevěné a S-skleněné stoly
pocet_D = pulp.LpVariable('x1', lowBound=0, cat='Integer')
pocet_S = pulp.LpVariable('x2', lowBound=0, cat='Integer')

model += 200*pocet_D + 350*pocet_S, "Zisk"

model += 1*pocet_D <= 50, "Omezení_dřeva"
model += 1*pocet_S <= 35, "Omezení_skla" 
model += 5*pocet_D + 5*pocet_S <= 300, "Omezení_noh"
model +=0.6*pocet_D + 1.5*pocet_S <= 63, "Omezení_času"

model.solve()
print("--- VÝSLEDKY ---")
print(f"zisk: {pulp.value(model.objective)}")
print(f"pocet_D: {pocet_D.varValue}")
print(f"pocet_S: {pocet_S.varValue}")