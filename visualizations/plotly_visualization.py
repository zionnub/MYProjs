# -*- coding: utf-8 -*-
"""Plotly_visualization

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mhbEPs6iqeupfhdCI9kCrpmyoOdwJhvK

### **Plotly Visualization**

Using Gapminer data from plotly
"""

import plotly.express as px
gap_df = px.data.gapminder()

gap_df.info()

gap_df.describe()

gap_df.head()

"""Use of assign to crearte a new column in dataframe"""

gap_df = gap_df.assign(gdp=gap_df['pop'] * gap_df['gdpPercap'])

"""Visulaizing latest year data"""

year_df = gap_df[gap_df.year == max(gap_df.year)]
cont_df = year_df.groupby('continent').agg({'gdp': 'sum'})
cont_df.reset_index(inplace=True)

"""### **Different charts using plotly**"""

# Pie chart
fig = px.pie(cont_df, values='gdp', names='continent')
fig.show()
# Bar chart
fig = px.bar(cont_df, color='continent', x='continent', y='gdp')
fig.show()
# Horizontal bar chart - stacked
fig = px.bar(cont_df, color='continent', x='gdp', orientation='h')
fig.show()
# Bubble chart
fig = px.scatter(cont_df.assign(dataType='GDP'), color='continent', x='continent', y='dataType', size='gdp', size_max=50)
fig.show()

"""### **Visualizing data over longer time period**"""

mul_yrs_df = gap_df[gap_df.year > 1985]
mul_yr_cont_df = mul_yrs_df.groupby(['continent', 'year']).agg({'gdp': 'sum'})
mul_yr_cont_df.reset_index(inplace=True)

mul_yr_cont_df.head(10)

# Bar chart
mul_yr_cont_df = mul_yr_cont_df.assign(yrstr=mul_yr_cont_df.year.astype(str))
fig = px.bar(mul_yr_cont_df, color='continent', y='gdp', x='yrstr', barmode='group')
fig.show()
# Horizontal bar chart - stacked
fig = px.bar(mul_yr_cont_df, color='continent', x='gdp', orientation='h', y='yrstr')
fig.show()
# Bubble chart
fig = px.scatter(mul_yr_cont_df, y='continent', x='yrstr', color='continent', size='gdp', size_max=50)
fig.show()

"""**Year wise and continent wise data**"""

fig = px.bar(mul_yr_cont_df, color='continent', y='gdp', x='yrstr', barmode='group')
fig.show()
fig = px.bar(mul_yr_cont_df, color='yrstr', y='gdp', x='continent', barmode='group')
fig.show()

"""**Showing independent continet wise data**"""

fig = px.bar(mul_yr_cont_df, color='continent', facet_col='continent', x='gdp', orientation='h', facet_row='yrstr')
fig.update_yaxes(showticklabels=False)
fig.show()