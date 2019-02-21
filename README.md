# mutualFundAnalysis

Given a list of months and corresponding data `get_instrument_wise_exposure_month_by_month` function writes monthly
instrument wise exposure in security_wise_exposure.csv

* Data loading script: loadData.py
* Analysis script: analyseFunds.py

# Data fields description
* Instruments.csv
  * Name of the Instrument,ISIN,Industry/Rating
* Mutual fund file like ABSLTR96.csv
  * ISIN Jan 19,Quantity Jan 19,Market value Jan 19 (in lac),% to net asset Jan 19
  * In repetition of 4 months
* List of fund files
  * ABSLTR96.csv
  * MOLTE.csv
* Final_security_wise_exposure in security_wise_exposure.csv
