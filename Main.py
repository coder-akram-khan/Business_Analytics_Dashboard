import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards
from st_aggrid import AgGrid

# Set Streamlit page configuration
st.set_page_config("Business Analytics Dashboard", page_icon="", layout="wide")

# --- DATA LOADING & TRANSFORMATION ---
def load_data():
    """Loads and prepares the dataset."""
    df = pd.read_csv("dataset.csv")
    return df

# --- SIDEBAR FILTERS ---
def sidebar_filters(df):
    """Creates sidebar filters for the dashboard."""
    st.sidebar.header("Filter")
    department = st.sidebar.multiselect(
        label="Filter Department", options=df["Department"].unique(), default=df["Department"].unique()
    )
    country = st.sidebar.multiselect(
        label="Filter Country", options=df["Country"].unique(), default=df["Country"].unique()
    )
    businessunit = st.sidebar.multiselect(
        label="Filter Business Unit", options=df["BusinessUnit"].unique(), default=df["BusinessUnit"].unique()
    )
    return department, country, businessunit

# --- DATA FILTERING ---
def filter_data(df, department, country, businessunit):
    """Filters the data based on selected options."""
    df_selection = df.query(
        "Department in @department & Country in @country & BusinessUnit in @businessunit"
    )
    return df_selection

# --- METRICS SECTION ---
def display_metrics(df_selection):
    """Displays key metrics on the dashboard."""
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Employees", value=df_selection['id'].nunique(), delta="Unique IDs")
    col2.metric("Total Annual Salary", value=f"{df_selection.AnnualSalary.sum():,.0f}", delta="Total Salary")
    col3.metric("Max Salary", value=f"{df_selection.AnnualSalary.max():,.0f}", delta="Maximum Salary")
    style_metric_cards(background_color="#071021", border_left_color="#1f66bd")

def display_extended_metrics(df_selection):
    """Displays extended metrics on the dashboard."""
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Avg. Salary", value=f"{df_selection['AnnualSalary'].mean():,.2f}", delta="Average Salary")
    col2.metric("Median Age", value=f"{df_selection['Age'].median():.0f}", delta="Median Age")
    col3.metric("Total Bonus", value=f"{df_selection['Bonus'].sum():,.2f}", delta="Total Bonus")
    col4.metric("Total Departments", value=df_selection['Department'].nunique(), delta="Unique Departments")
    style_metric_cards(background_color="#071021", border_left_color="#1f66bd")

# --- CHARTS & VISUALIZATIONS ---
def plot_pie_chart(df_selection):
    """Plots a pie chart of annual salary by department."""
    fig = px.pie(df_selection, values="AnnualSalary", names="Department", title="Annual Salary by Department")
    fig.update_traces(textinfo="percent+label", textposition="inside")
    return fig

def plot_bar_chart(df_selection):
    """Plots a bar chart of annual salary by department."""
    fig = px.bar(df_selection, y="AnnualSalary", x="Department", text_auto=".2s", title="Annual Salary by Department")
    return fig

def plot_heatmap(df_selection):
    """Plots a correlation heatmap."""
    corr = df_selection[["AnnualSalary", "Bonus", "Age"]].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

def plot_geographic_map(df_selection):
    """Plots a geographical map of employee distribution."""
    fig = px.scatter_geo(
        df_selection, locations="Country", locationmode="country names",
        size="AnnualSalary", hover_name="City", title="Employee Distribution by Country"
    )
    return fig

def plot_time_series(df_selection):
    """Plots a time series of annual salary over time."""
    df_selection["HireDate"] = pd.to_datetime(df_selection["HireDate"])
    df_time = df_selection.groupby("HireDate").sum().reset_index()
    fig = px.line(df_time, x="HireDate", y="AnnualSalary", title="Annual Salary Over Time")
    return fig

def plot_treemap(df_selection):
    """Plots a treemap of employee distribution by department and job title."""
    fig = px.treemap(df_selection, path=['Department', 'JobTitle'], values='AnnualSalary', title='Employee Distribution Treemap')
    return fig

def display_table(df_selection):
    """Displays a table of the filtered data."""
    with st.expander("Database Table"):
        selected_cols = st.multiselect(
            "Filter Dataset", df_selection.columns,
            default=["EEID", "FullName", "JobTitle", "Department", "AnnualSalary", "Country", "City"]
        )
        st.dataframe(df_selection[selected_cols], use_container_width=True)
        

        # Download button for filtered data

        csv = df_selection.to_csv(index=False).encode('utf-8')

        st.download_button(

            label="Download Filtered Data as CSV",

            data=csv,

            file_name='filtered_data.csv',

            mime='text/csv',

            key='download-csv'

        )

# --- HOME PAGE LOGIC ---
def home_page(df):
    """Displays content for the Home page."""
    left_col, right_col = st.columns(2)

    with left_col:
        st.markdown("### Key Metrics")
        display_metrics(df)
        display_extended_metrics(df)

        st.markdown("### Visualizations")
        pie_chart = plot_pie_chart(df)
        st.plotly_chart(pie_chart, use_container_width=True)

        bar_chart = plot_bar_chart(df)
        st.plotly_chart(bar_chart, use_container_width=True)

        st.markdown("### Correlation Heatmap")
        plot_heatmap(df)

    with right_col:
        st.markdown("### Time Series Analysis")
        time_series_chart = plot_time_series(df)
        st.plotly_chart(time_series_chart, use_container_width=True)

        st.markdown("### Geographic Distribution")
        geo_map = plot_geographic_map(df)
        st.plotly_chart(geo_map, use_container_width=True)

        st.markdown("### Employee Distribution Treemap")
        treemap = plot_treemap(df)
        st.plotly_chart(treemap, use_container_width=True)

# --- MAIN FUNCTION ---
def main():
    """Main function to run the Streamlit app."""
    df = load_data()
    department, country, businessunit = sidebar_filters(df)
    df_selection = filter_data(df, department, country, businessunit)

    home_page(df_selection)
    display_table(df_selection)

if __name__ == "__main__":
    main()