'''
___________________________________________________________________________
główny plik programu do pozyskiwania EKG

zawiera części:
> akwizycji
> przetwarzania
> zapisu danych
___________________________________________________________________________
UWAGA:
podczas importowania własnych modułów może pojawić się problem:
    <Python Unresolved Import>
Wówczas w .vscode\setting.json wklejamy poniższą linijkę:
    <'python.autoComplete.extraPaths': ["./path-to-your-code"]>
wskazuje ona lokalizację naszych dodatkowych modułów.
___________________________________________________________________________
'''

import pandas as pd
import EKG_acquisition as a
import EKG_processing as p
import EKG_saving as s
import prints

col_names = ['t', 'V'] # podaj nazwy kolumn
data = pd.DataFrame(columns=col_names) # tu będą dane

prints.message('heloł')
data = a.main(data)
data = p.main(data)
s.main(data)