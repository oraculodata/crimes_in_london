import streamlit as st
import pandas as pd
import altair as alt

def load_data(csv_file):
    df = pd.read_csv(csv_file, sep=';', parse_dates=['date'])
    return df

def filter_data(df, selected_months):
    if selected_months:
        filtered_df = df[df['date'].dt.strftime('%Y-%m').isin(selected_months)]
    else:
        filtered_df = df
    return filtered_df

def plot_charts(df):
    gender_chart = alt.Chart(df.dropna(subset=['gender'])).mark_bar().encode(
        x='gender',
        y='count()',
        color='gender',
        tooltip=[alt.Tooltip('gender', title='Gender'), alt.Tooltip('count()', title='Count')]
    ).properties(
        width=450,
        height=300
    )
    st.altair_chart(gender_chart)

    age_chart = alt.Chart(df.dropna(subset=['age_range'])).mark_bar().encode(
        x='age_range',
        y='count()',
        color='age_range',
        tooltip=[alt.Tooltip('age_range', title='Age Range'), alt.Tooltip('count()', title='Count')]
    ).properties(
        width=450,
        height=300
    )
    st.altair_chart(age_chart)

    ethnicity_chart = alt.Chart(df.dropna(subset=['self_defined_ethnicity'])).mark_bar().encode(
        x='self_defined_ethnicity',
        y='count()',
        color='self_defined_ethnicity',
        tooltip=[alt.Tooltip('self_defined_ethnicity', title='Self Defined Ethnicity'), alt.Tooltip('count()', title='Count')]
    ).properties(
        width=750,
        height=500
    )
    st.altair_chart(ethnicity_chart)

    outcome_chart = alt.Chart(df.dropna(subset=['outcome'])).mark_bar().encode(
        x='outcome',
        y='count()',
        color='outcome',
        tooltip=[alt.Tooltip('outcome', title='Outcome'), alt.Tooltip('count()', title='Count')]
    ).properties(
        width=750,
        height=500
    )
    st.altair_chart(outcome_chart)

def main():
    st.write("# :cop: Individual stop and search records")

    csv_file = "data/stop_and_search.csv"
    df = load_data(csv_file)

    if df.empty:
        st.warning("No data available.")
        st.stop()

    available_months = sorted(df['date'].dt.strftime('%Y-%m').unique())
    selected_months = st.multiselect("Select months", available_months, default=[available_months[-1]])

    filtered_df = filter_data(df, selected_months)

    if filtered_df.empty:
        st.warning("No data available for the selected months.")
        st.stop()

    plot_charts(filtered_df)

if __name__ == "__main__":
    main()
