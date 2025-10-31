# bulgarian-municipal-disaster-plans-2025
This repository contains data compiled and analyzed for the study “How Bulgarian Municipalities Plan for Disasters – An Analysis of the Availability and Content of The Municipal Disaster Protection Plans"
## Overview

The dataset provides comprehensive information on the public accessibility and structure of municipal disaster protection plans across all 265 municipalities in Bulgaria. It includes both a tabular summary of the research results and a geospatial layer for mapping and spatial analysis. The data were compiled through a systematic review of official municipal websites (March–August 2025) and analyzed using an AI-assisted workflow implemented in ChatGPT-5 with Python libraries for text extraction, structuring, and validation.

## Data Files
1. Data_result_table.xlsx

An Excel table containing metadata and results from the systematic search and analysis of municipal disaster protection plans.
Columns:

1. *Name_Bulgarian* - the name of the municipality in Bulgarian language
2. *Name_English* - the name of the municipality in English language
3. *POP_2024* - the total population from the National Statistics Institute data
4. *POP_DENS_2024* - population density for 2024
5. *AREA_KM2* - area of the municipality in sq. km.
6. *PlanAvailab* - the availability of the plan at the moment of the search = 1 = yes, 0 = no
7. *Comment* - comment regarding the availability or other situation
8. *URL* - the web address of the plan if it was discovered

2. Municipalities_plans.geojson

A polygon layer of all Bulgarian municipalities with same attributes as the Excel table.
Source: Eurostat GISCO 2024 (simplified geometry).
Purpose: Enables visualization and spatial analysis of disaster protection plan accessibility and coverage at the municipal level.

Method Summary

Data collection was based on manual and AI-assisted review of official municipal websites. Each municipality was checked for the presence of a disaster protection plan in designated sections (“Documents,” “Strategies,” “Plans,” etc.). The AI analysis, conducted in ChatGPT-5, used Python libraries for text extraction and summarization of available documents.

License

This dataset is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
You are free to share and adapt the material, provided that appropriate credit is given.
