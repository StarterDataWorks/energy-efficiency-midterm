Problem Framing
I chose the Energy Efficiency dataset which deals with the energy efficiency of buildings. The dataset has 768 rows and nine columns, two targets, but I only considered the target Y1: HEATING LOAD. The columns do not have specific names, but each X represents: Relative Compactness, Surface Area, Wall Area, Roof Area, Overall Height, Orientation, Glazing Area, Glazing Area Distribution, respectively from X1 to X8. The goal is to identify which parts of a building involve the greatest heat loss. Addressing the problem can help improve energy efficiency and reduce climate change risks. The dataset has no null values, nor extreme values, they are float and integer values, for this reason I used regression models and RMSE for evaluations.

Project Structure

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

Target Analysis.
The histplot of the target shows the presence of two peaks in the data distribution, but does not show tails or a bell-shaped structure. This distribution implies no cleaning intervention on the target.

Features Analysis.

Through the correlation matrix, we can see that X5, overall height, is positively correlated (0.89) with the target. Therefore, the height of the buildings affects heat loss; as height increases, the heating load increases. X4, roof area, is negatively correlated (-0.86) with the target, so the greater the roof extension, the lower the loss. 
X1, relative compactness, is positively correlated (0.62) and X2, surface area, is negatively correlated (-0.66). 
I analyzed X7, glazing area, X8, glazing area distribution, and X1, relative compactness, through GROUP BY calculating the mean and median. As the number of windows (X7 and X8) increases, Y1, heating load, increases.
The mean and median of X1 have a fluctuating trend due to the strong negative correlation (-0.99) with X2, surface area.
The analysis with mutual_info_regression shows that the features that most affect the target are: X2, surface area, X1, relative compactness, X3, wall area, and X4, roof area. 
Instead, X6 receives a score of 0.000 and therefore orientation does not affect thermal dispersion.

Predictive Models.

I tried LinearRegressor without fine tuning, DecisiontreeRegressor, RandomForestRegressor, and XGBOOST.
I applied fine tuning to the tree models with the following results:
Decisiontree: max_depth=10
Randomforest: n_estimators=40, max_depth=20
XGBOOST: eta: 0.3, max_depth: 6

Final Model

I applied the RMSE evaluation metric with the following results:

LinearRegression--> RMSE: 2.8593429789437104
DecisionTreeRegressor --> RMSE: 0.5763
RandomForestRegressor --> RMSE: 0.4643
XGBOOST -->  RMSE: 0.3968

The best model is XGBOOST because it has the lowest RMSE value

How to run locally and via Docker

Locally with Pipenv:

1. Clone the repository and navigate to the project directory:
   cd energyef/container
2. Install dependencies:
   pipenv install
3. Run the application:
   pipenv run python logistic.py

Via Docker:
1. Build the Docker image:
   docker build -t energyef-app ./container
2. Run the Docker container:
   docker run -it --rm -p 9696:9696 energyef-app

API usage example

You can test the prediction endpoint by running the test script:
python container/test.py

Or by sending a POST request with curl:
curl -X POST http://localhost:9696/predict \
  -H "Content-Type: application/json" \
  -d '{
    "X1": 0.98,
    "X2": 514.5,
    "X3": 294.0,
    "X4": 110.25,
    "X5": 7.0,
    "X6": 2,
    "X7": 0.0,
    "X8": 0
  }'

Known limitations / next steps

- The project only considers target Y1 (Heating Load) and ignores target Y2 (Cooling Load).
- The dataset is small (768 rows), so testing on a larger dataset with more real-world building features could improve generalization.
- Future steps include adding tuning for more XGBoost parameters (like subsample or colsample_bytree) and serving predictions for both targets simultaneously.