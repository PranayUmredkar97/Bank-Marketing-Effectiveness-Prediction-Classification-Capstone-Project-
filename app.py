import pandas as pd
import numpy as np
import streamlit as st
import xgboost
import pickle
import sklearn

pipe = pickle.load(open('pipe.pkl','rb'))

job = ['management',
 'technician',
 'entrepreneur',
 'blue-collar',
 'unknown',
 'retired',
 'admin.',
 'services',
 'self-employed',
 'unemployed',
 'housemaid',
 'student']

marital = ['married', 'single', 'divorced']

education = ['tertiary', 'secondary', 'unknown', 'primary']

day = [1, 2, 3]

contact = ['unknown', 'cellular', 'telephone']

month = ['may',
 'jun',
 'jul',
 'aug',
 'oct',
 'nov',
 'dec',
 'jan',
 'feb',
 'mar',
 'apr',
 'sep']

poutcome = ['unknown', 'failure', 'other', 'success']

default = [0, 1]

housing = [1, 0]

loan = [1, 0]

campaign = [1,2,3,5,4,6,7,8,9,10,11,12,13,19,14,24,16,32,18,22,15,17,25,21,43,51,63,41,26,28,55,50,38,
            23,20,29,31,37,30,46,27,58,33,35,34,36,39,44]

previous = [0,3,1,4,2,11,16,6,5,10,12,7,18,9,21,8,14,15,26,37,13,25,20,27,17,23,38,29,24,51,275,22,19,
            30,58,28,32,40,55,35,41]

st.title('Term Deposit Bank Service Predictor')

col1, col2 = st.columns(2)

with col1:
    job_type = st.selectbox('Select Job Type',sorted(job))

with col2:
    marital_status = st.selectbox('Select Marital status', sorted(marital))

col3, col4 = st.columns(2)

with col3:
    education_type = st.selectbox('Select Education', sorted(education))

with col4:
    contact_type = st.selectbox('Select Contact Type', sorted(contact))

date = st.selectbox('Select date(1 for 1-10,2 for 11-20 and 3 for 21-31)',sorted(day))

col6, col7 = st.columns(2)

with col6:
    months = st.selectbox('Select Month',sorted(month))

with col7:
    previous_outcome = st.selectbox('Select Previous Outcome', sorted(poutcome))

col8, col9, col10 = st.columns(3)

with col8:
    default_credit = st.selectbox('Select default credit (1:YES,0:NO)',default)

with col9:
    housing_loan = st.selectbox('Select Housing Loan (1:YES,0:NO)',housing)

with col10:
     Personal_loan = st.selectbox('Select Personal Loan (1:YES,0:NO)',loan)

col11, col12 = st.columns(2)

with col11:
     contact_campaign = st.selectbox('Select number of time client contacted during campaign', sorted(campaign))

with col12:
     contact_before_campaign = st.selectbox('Select number of time client contacted before campaign', sorted(previous))

col13, col14, col15 = st.columns(3)

with col13:
    age = st.number_input('Select Age')

with col14:
    balance = st.number_input('Select Account Balance')

with col15:
    duration = st.number_input('Select Call duration')

if st.button('Predict'):
    pass

    input_df = pd.DataFrame({'age':[age],'job':[job_type],'marital':[marital_status],'education':[education_type],
                             'default':[default_credit],'balance':[balance],'housing':[housing_loan],'loan':[Personal_loan],
                             'contact':[contact_type],'day':[date],'month':[months],'duration':[duration],
                             'campaign':[contact_campaign],'previous':[contact_before_campaign],'poutcome':[previous_outcome]})

    st.table(input_df)
    result = pipe.predict(input_df)
    st.text('1 : Will Subscribe, 0: Will not Subscribe')
    st.header('Predicted Output - '  + str(result))