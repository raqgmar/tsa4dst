# README

## Project Overview
This repository contains scripts, data, and documentation for a Master's thesis focused on **time-series prediction using Support Vector Regression (SVR)** and hybrid **LSTM-MLP models**. 
The research targets the prediction of geomagnetic storms, analyzing key variables like the Dst index and solar wind data, sourced from NASA, NOAA, and the Kyoto Dst Index. 
The purpose of this study is to understand how solar storms affect Earth's geomagnetic field using statistical and machine learning techniques.

### Structure
- **Anexos/**  Contains additional documents, including an EDA PDF report. 
- **RESULTADOS/**  Final results from all model training and evaluations across different prediction horizons (2h, 4h, 6h).
- **TFM_data/**  Includes the datasets from SVR and related models used for training and evaluation.
- **./**: Scripts / notebooks and presentation, pdf and pptx.
  - **00_download_data.ipynb**  Script for downloading datasets from various sources like NOAA and NASA. This script is generalizable for other projects.
  - **00_02_obtencion_ecuaciones_regresion.ipynb**   Provides the regression equations and processes used in predictive models.
  - **01_01_EDA_storms_data_source.ipynb**  Explores raw data related to solar wind and Dst indices, with a focus on storms.
  - **03_*_vDef_SVR_Xh_ahead.ipynb**  These notebooks handle SVR models trained to predict geomagnetic storms at various time intervals (2h, 4h, and 6h ahead).
  - **04_*_LSTM-MLP_Xh.ipynb**  Implements comparative hybrid models using LSTM and MLP to forecast the storm-related variables for the same time intervals (2h, 4h, 6h ahead).
  - **05_analisis_resultados_y_graficas_completar.ipynb**  Scripts for result visualization and performance analysis.
  - **06_01_INTERPRETABILIDAD_SVR.ipynb**  Analysis focused on the interpretability of SVR models
  - **Presentación_TFM_RGM_TECI_2024M09.pdf**  The final presentation for the Master’s thesis, including key findings and methodologies.
  - **garmar_raq_TFM_PredTS_SVR.pdf**  The actual master's thesis. Detailed documentation for the theoretical and practical application of SVR and other models in the prediction of geomagnetic storms.

### Issues
- **Multicollinearity Problem**: A significant issue was identified with multicollinearity in the regression models, which impacted the interpretability of some regression equations. The models' predictive performance was strong, but interpretation suffered due to this issue.
- **Error in Final Report**: There are three identical tables in the final report, which was a mistake. Since the final version of the thesis was submitted and graded (9.1/10, GPA 3.64), these tables were not corrected.

### How to Use
WARNING: This is not a modular / reusable repo, this is a showcase for this specific master's thesis. However, if you are interested in replicating it:
- Run `00_download_data.ipynb` to obtain necessary datasets.
- Analyze storm data using the EDA notebooks, starting with `01_01_EDA_storms_data_source.ipynb`.
- Train SVR and hybrid models using the notebooks in the `03_*` and `04_*` directories.
- Use `05_analisis_resultados_y_graficas_completar.ipynb` for visualizations and final performance evaluations.

### Version Control
- All files have been updated to **version 3** (July 2024), with major revisions to data processing and visualization. The final results **version F4** are summarized in the attached reports.
