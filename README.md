# Wastewater as an early Indicator for Short-Term Forecasting COVID-19 Hospitalization in Germany

This repository belongs to the publication Wastewater as an early Indicator for Short-Term Forecasting COVID-19 Hospitalization in Germany by Botz et al. 
If you have questions please reach out to Jonas Botz (jonas.botz@scai.fraunhofer.de)

It is structured as follows:

-- data (needs to be added) 

here the data for the analysis can be stored. Data can be accessed from https://github.com/robert-koch-institut/Abwassersurveillance_AMELAG and https://github.com/robert-koch-institut/COVID-19-Hospitalisierungen_in_Deutschland

-- notebooks 
  - correlation_analysis.ipynb (correlation analysis between wastewater viral load and hospitalization rates)
  - classical_models_predictions.ipynb (linear regression, ridge regression, and ARIMA models for short-term forecasting hospitalization rates (autoregressive and with wastewater viral load))
  - tree_models_prediction.ipynb (Random Forest and XGBoost for short-term forecasting hospitalization rates (autoregressive and with wastewater viral load and cross-modal))
  - tree_models_regional.ipynb (Random Forest and XGBoost for short-term forecasting hospitalization rates with regional data from 5 federal states)

-- output (needs to be added)

if you run the notebooks, the outputs (mae and mapes as well as mean mape and mean mae including 95% CI) will be stored automatically as CSV.

In the study, we further analyzed diagnosis data from CGM. Since these data are not publicly available, we did not include the analysis scripts here. The analysis, however, was performed in alignment with the correlation analysis of the hospitalization data.
