Problem Framing
Ho scelto il dataset Energy Efficency che si occupa dell'efficenza energetica degli edifici.
IL dataset ha 768 righe e nove colonne, due target, ma ho preso in considerazione solo il target Y1: HEATING LOAD. Le colonne non hanno nomi specifici ma ogni X rappresenta:Relative Compactness,Surface Area,Wall Area,Roof Area,Overall Height,Orientation,Glazing Area,Glazing Area Distribution, rispettivamente da X1 a X8.L'obiettivo è quello di individuare  quali parti di un edificio comportano la maggiore dispersione di calore. Affrontando il problema di può contribuire a migliorae l'efficenza energetica e ridurre i rischi del cambiamento climatico.
Il dataset non presenta valori nulli, nè valori estremi, sono valori float e integer per questo motivo ho usato i modelli di regressione e RMSE per le valutazioni.

Struttura del progetto

energyef
|-- data/
       |--ENB_2012_data.xls
|---- notebook.ipynb
|-----container/
      |----Pipfile
      |----Pipfile.lock
      |----logistic.py
      |----test.py
      |----Dockerfile
|---readme      

EDA

Analisi del target.
IL grafico histplot del target mostra la presenza di due picchi nella distribuzione dei dati , ma non mostra code o una struttura a campana. Questa distribuzione comporta il non intervento di pulitura sul target.

Analisi delle features.

Attraverso la matrice di correlazione si nota che X5,overall height, è correlato (0.89) positivamente con il target.Quindi l'altezza degli edifici influisce sulla dispersione del calore,all'aumentare dell'altezza aumenta heating load. X4, roof area , è correlato negativamente(-0.86) con il target, quindi maggiore è l'estensione del tetto minore sarà la dispersione. 
X1,relative compactness, è correlato positivamente (0.62) e X2,surface area, è correlato negativamente (-0.66). 
Ho analizzato X7, glazing area, X8,glazing area distribution e X1, relative compactness, attraverso GROUP BY calcolando la media e mediana.All'aumentare del numero di vetrate(X7 e X8) aumenta Y1,heating load.
La media e la mediana di X1 hanno un andamento altalenante a causa della forte correlazione negativa(-0.99) con X2,surface area.
L'analisi con mutual_info_regression mostra che le features che influiscono maggiormente sul target sono:
X2,surface area, X1, relative compactness, X3,wall area, e X4, roof area.
Invece X6 riceve un punteggio di 0.000 e quindi l'orientation non influisce sulla dispersione termica.

Modelli predittivi.

Ho provato LinearRegressor senza fine tuning, DecisiontreeRegressor, RandomForestRegressor e XGBOOST.
Ho applicato il fine tuning ai modelli ad albero con i seguenti risultati:
Decisiontree: max_depth=10
Randomforest: n_estimators=40, max_depth=20
XGBOOST: eta: 0.3, max_depth: 6

Modello finale

Ho applicato la metrica di valutazione RMSE con i seguenti risultati:

LinearRegression--> RMSE: 2.8593429789437104
DecisionTreeRegressor --> RMSE: 0.5763
RandomForestRegressor --> RMSE: 0.4643
XGBOOST -->  RMSE: 0.3968

Il modello migliore è XGBOOST perchè ha il valore di RMSE più basso