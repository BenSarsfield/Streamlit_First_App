import streamlit as st
import pandas as pd
import numpy as np

st.title("Life Expectancy")

who = pd.read_csv("who.csv")
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(who)

## Region
Region_select = st.sidebar.selectbox(
    'What Region do you want to take a closer look at?',
    ('Middle East', 'European Union', 'Asia', 'South America',
       'Central America and Caribbean', 'Rest of Europe', 'Africa',
       'Oceania', 'North America')
)

new_filter = who[who['Region'] == Region_select]
st.subheader(f'This is what {Region_select} looks like')
st.write(new_filter)

## Year
Year_select = st.sidebar.slider(
    'Select a Year',
    2000, 2015
)
filter = who[who['Year'] == Year_select]
st.subheader(f'What does the data look like in {Year_select}')
st.write(filter)

## Country

Country_select = st.sidebar.selectbox(
    'What Country do you want to see?',
    ('Turkiye', 'Spain', 'India', 'Guyana', 'Israel', 'Costa Rica',
       'Russian Federation', 'Hungary', 'Jordan', 'Moldova', 'Brazil',
       'Malta', 'Bahamas, The', 'Ukraine', 'Switzerland', 'Norway',
       'Finland', 'Comoros', 'Japan', 'Gabon', 'Ghana', 'Philippines',
       'Congo, Rep.', 'Madagascar', 'Estonia', 'Belize', 'Kazakhstan',
       'Cameroon', 'Zimbabwe', 'Bhutan', 'South Africa', 'Eritrea',
       'Germany', 'Saudi Arabia', 'Kiribati', 'Seychelles', 'Singapore',
       'Togo', 'Denmark', 'Gambia, The', 'Sweden', 'Austria',
       'Kyrgyz Republic', 'Grenada', 'Brunei Darussalam', 'Greece',
       'Uruguay', 'Croatia', 'Romania', 'Central African Republic',
       'Algeria', 'Yemen, Rep.', 'Armenia',
       'St. Vincent and the Grenadines', 'Kenya', 'Micronesia, Fed. Sts.',
       'Antigua and Barbuda', 'Nepal', 'Lithuania', 'Vanuatu',
       'Afghanistan', 'Kuwait', 'Argentina', 'Panama', 'Oman', 'France',
       'Bosnia and Herzegovina', 'Mauritania', 'Somalia', 'Azerbaijan',
       'Maldives', 'Guinea-Bissau', 'Solomon Islands', 'Congo, Dem. Rep.',
       'Namibia', 'Eswatini', 'Nigeria', 'United Arab Emirates',
       'Burundi', 'Tajikistan', 'Honduras', 'Colombia', 'Iceland',
       'Morocco', 'Pakistan', 'Bolivia', 'Cambodia', 'Malaysia',
       'Dominican Republic', 'Italy', 'Vietnam', 'Albania', 'Czechia',
       'Tonga', 'Slovenia', 'Zambia', 'Egypt, Arab Rep.',
       'Papua New Guinea', 'Ireland', 'Chile', 'Syrian Arab Republic',
       'Serbia', 'Belgium', 'Cuba', 'Trinidad and Tobago', 'Botswana',
       'Paraguay', 'Malawi', 'Montenegro', 'Timor-Leste', 'Chad',
       'Sierra Leone', 'Mali', 'Bangladesh', 'Latvia', 'Angola',
       'Jamaica', 'China', 'Tanzania', 'Ecuador', 'Djibouti',
       "Cote d'Ivoire", 'Nicaragua', 'Iraq', 'Myanmar', 'Bahrain',
       'Cabo Verde', 'Uganda', 'St. Lucia', 'Belarus', 'Senegal',
       'Mongolia', 'Haiti', 'Niger', 'Slovak Republic', 'Tunisia',
       'Thailand', 'Samoa', 'Libya', 'Bulgaria', 'Netherlands', 'Liberia',
       'Ethiopia', 'Benin', 'New Zealand', 'Rwanda',
       'Sao Tome and Principe', 'Guatemala', 'Cyprus', 'Venezuela, RB',
       'Portugal', 'Equatorial Guinea', 'Iran, Islamic Rep.', 'Lao PDR',
       'Mexico', 'Lebanon', 'Turkmenistan', 'Indonesia', 'United States',
       'Peru', 'Mozambique', 'United Kingdom', 'Luxembourg', 'Sri Lanka',
       'Uzbekistan', 'Lesotho', 'Guinea', 'Poland', 'Canada', 'Suriname',
       'Mauritius', 'Barbados', 'El Salvador', 'Burkina Faso', 'Qatar',
       'Fiji', 'Australia', 'North Macedonia', 'Georgia')
)
filter_c = who[who['Country'] == Country_select]
st.subheader(f'What does the data look like in {Country_select}')
st.write(filter_c)







