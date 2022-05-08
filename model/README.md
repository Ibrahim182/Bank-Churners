# Bank-Churners
-------------------
## Making some analysis in data then preprocessing and apply xgboost with

<p>I used in this project these libraries</p>
<ul>
  <li>Pandas</li>
  <li>Numpy</li>
  <li>Seaborn</li>
  <li>Sklearn</li>
  <li>SimpleImputer</li>
  <li>datasist</li>
  <li>XGBClassifier</li>
  <li>StandardScaler</li>
  <li>GridSearchCV</li>
  <li>joblib</li>
</ul>

<p>Steps in preprocessing the data</p>
<ul>
  <li>Dealing with missing values</li>
  <li>Convert Categories data</li>
  <li>Detect outliers</li>
  <li>Over sample</li>
  <li>Scale the data</li>
  <li>Hyperparameter tuning</li>
  <li>Apply model</li>
</ul>

<h1 style="text-align:center; font-size:100px; color:#BC3232">Conclusion</h1>

- The data contain 16% of customers who have churned so the data is imbalanced
- The proportion of gender count is almos the same (52.9% Male and 47.1% Female)
- Female who have churned are more than male
- Married presons and single almost same as in number of leaving our service.
- Graduate clients are the most type leave our service.
- People with income less than $ 40k are the most category of leaving service.
- People with card type Blue are the most type of leaving service.
- People with dependent count equal 3 are the most of leaveing service
- Most people leave our service after 36 months
- Most people who stay inactive for 3 months leave our service
- Lower credit limit means high probability to leave service
- Lower open to buy mean high probability to leave service
- People with 2700 and less Transaction Amount about half of them leave our service
- More than half of people who never use card leave service
