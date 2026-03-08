import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

A = np.array([[1, 1, 1, 0],
              [2, 1, 0, 1]])
b = np.array([80, 100])

def solve_simplex_combinations(A, b):
    m, n = A.shape
    results = []
    
    cols = list(range(n))
    combos = list(combinations(cols, m))
    
    print("-" * 40)
    print("VYPOČET BÁZICKÝCH ŘEŠENÍ")
    print("-" * 40)
    print(f"Matice A:\n{A}")
    print(f"Vektor b: {b}")
    print("-" * 40)
    
    for i, combo in enumerate(combos):
        B = A[:, combo]
        
        print(f"Kombinace {i+1}: Sloupce {combo}")
        print(f"Submatice B:\n{B}")
        
        try:
            x_sol = np.linalg.solve(B, b)
        except np.linalg.LinAlgError:
            print("Matice je singulární, nemá inverzi.\n")
            continue
        
        full_x = np.zeros(n)
        for idx, val in zip(combo, x_sol):
            full_x[idx] = val
            
        print(f"Řešení (v bázických proměnných): {x_sol}")
        print(f"Výsledný vektor v R^4: {full_x}")
        
        if np.all(full_x >= 0):
            status = "VYHOVUJE"
            results.append(full_x)
        else:
            status = "NEVYHOVUJE (záporné souřadnice)"
        
        print(f"Status: {status}\n")

    return np.array(results)

valid_points = solve_simplex_combinations(A, b)

if len(valid_points) > 0:
    plt.scatter(valid_points[:, 0], valid_points[:, 1], color='red', zorder=5, label='Přípustná řešení')
    
    for i, p in enumerate(valid_points):
        plt.text(p[0]+0.1, p[1]+0.1, f"[{p[0]:.1f}, {p[1]:.1f}]")

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Graf vybraných bázických řešení')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.savefig('ukol_3\\solution_plot.png')
    print("Graf byl uložen jako solution_plot.png")
else:
    print("Žádná řešení nevyhověla podmínkám.")