import os
import streamlit as st
import pandas as pd
import numpy as np
import plost
st.title('Local Authority Emissions')
st.write('This app will plot the emissions of UK local authorities.')

#create a dataframe from the csv file
df = pd.read_csv('co2-emissions_cleaned.csv')
dfcopy = df.copy(deep=True)



def user_interface():
    """
    This function will ask the user for a list of local authorities, one at a time.
    """
    while True:
        local_authority = st.multiselect('Select local authorities', df['Local Authority'].unique())
        return local_authority
        
def plot_local_authorities(local_authority):
    if local_authority is not None and st.button(label='Plot') is True:
        for authority in local_authority:
            dfcopy = df.loc[df.loc[:, "Local Authority"] == authority, :]
            dfcopy.set_index('Year')
            plost.area_chart(dfcopy, x = str('Year:O'), y = 'Emissions', color = 'Local Authority',opacity=0.5,pan_zoom=None, use_container_width=True)



city = user_interface()
plot_local_authorities(city)


    
