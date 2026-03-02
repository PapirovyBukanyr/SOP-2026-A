# SOP-2026-A
Sdílený repositář na všechny úkoly skupiny A do předmětu SOP na VUT Brno - FSI

## Struktura repositáře
- `README.md` - soubor s informacemi o repositáři
- `.gitignore` - soubor pro ignorování nepotřebných souborů a složek (např. `__pycache__/`, `.vscode/`, atd. - nesahat, pokud není potřeba/nevíte, co děláte, AI tam za nic nepouštějte!)
- `ukol_1/` - složka pro úkol 1
- `ukol_2/` - složka pro úkol 2
  - `programy/` - složka pro softwarové řešení úkolu 2
  - `kapitoly/` - složka pro textové řešení úkolu 2


## Jak přidat část úkolu
1. Naklonujte repositář do svého počítače pomocí příkazu:
   ```
   git clone https://github.com/PapirovyBukanyr/SOP-2026-A/
Je důležité si ho naklonovat a ne jenom stáhnout ZIP, protože pak to nebude propojené.
2. Vytvořte novou větev pro svůj úkol (např. `ukol1-jmeno`) za pomoci příkazu:
   ```
   git checkout -b ukol1-jmeno
   ```
3. Přidejte své řešení:
    - Jdi do kapitol, přidej kapitolu s odpovídajícím číslem úlohy a tam napiš své řešení. Pokud je to potřeba, přidej i obrázky. Obrázky nenechávej pojmenované defaultně, zbytečně se budeme bít o stejné názvy, ale pojmenuj je nějak rozumně, třeba `ukol2-jmeno-1.png` nebo `ukol2-číslo podúlohy-2.png` a tak dále.
    - Následně přilož kapitolu do hlavního souboru, který je pro druhou úlohu sablona-main.tex, ať se to zkompiluje.
4. Přidejte změny do svého commitu pomocí příkazu:
   ```
   git add .
   ```  
5. Vytvořte commit s popisem změn:
   ```  
    git commit -m "Přidáno řešení úkolu 1 od Jméno Příjmení"
    ```
6. Pushněte svou větev do repositáře:
   ``` 
   git push origin ukol1-jmeno
    ```
    kde `ukol1-jmeno` je název vaší větve, kterou jste vytvořili v kroku 2.
7. Po pushnutí své větve vytvořte pull request (PR) na GitHubu, aby ostatní mohli zkontrolovat vaše řešení a případně ho sloučit do hlavní větve (main).
8. Po schválení PR se nezapomeňte na počítači vrátit do hlavní větve a stáhnout nejnovější změny:
   ```
   git checkout main
   git pull origin main
   ```
   Často se na to zapomíná, právě teď se mi to povedlo...
## Důležité poznámky
- Nezasahujte do kódů druhých, bude to hromada věcí, tak ať je v tom pořádek.
- Pokud máte nějaké otázky nebo potřebujete pomoc, neváhejte se mě zeptat.
- Snažte se dodržovat strukturu repositáře a pojmenování souborů, aby bylo vše přehledné pro všechny členy skupiny.
- Nezapomeňte pravidelně commitovat a pushovat své změny, aby ostatní měli přehled o vašem pokroku a mohli vám případně pomoci s řešením.
- Pokud máte nějaké nápady na zlepšení struktury repositáře nebo způsobu práce, neváhejte je navrhnout a diskutovat s ostatními členy skupiny. Společně můžeme vytvořit efektivní a organizovaný repositář pro všechny úkoly.
