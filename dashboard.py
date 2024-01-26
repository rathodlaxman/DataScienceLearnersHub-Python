import dash
from dash import dcc, html
import plotly.express as px

# Example data
data = px.data.gapminder().query("continent == 'Asia'")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='Gapminder Dashboard'),
    
    # Dropdown for selecting a country
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in data['country'].unique()],
        value='India',  # Default selected value
        multi=False
    ),

    # Line plot for GDP per Capita over time
    dcc.Graph(
        id='gdp-line-plot'
    )
])

# Define callback to update the line plot based on dropdown selection
@app.callback(
    dash.dependencies.Output('gdp-line-plot', 'figure'),
    [dash.dependencies.Input('country-dropdown', 'value')]
)
def update_line_plot(selected_country):
    filtered_data = data[data['country'] == selected_country]
    fig = px.line(filtered_data, x='year', y='gdpPercap', title=f'GDP Per Capita Over Time in {selected_country}')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
