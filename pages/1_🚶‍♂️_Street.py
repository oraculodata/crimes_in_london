import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster, MousePosition

st.set_page_config(layout="wide")

@st.cache_data()
def load_data_from_csv(selected_months):
    try:
        df = pd.read_csv('data/street.csv', delimiter=';')

        if selected_months:
            df = df[df['month'].isin(selected_months)]

        return df
    except Exception as e:
        st.error(f"An error occurred while loading data from the CSV file: {e}")
        return None

def main():
    try:
        df_months = load_data_from_csv(selected_months=None)
        available_months = sorted(df_months['month'].unique(), reverse=True)

        st.write("# :walking: Crimes at street")

        selected_months = st.multiselect("Select months", available_months, default=[available_months[0]])
        df = load_data_from_csv(selected_months)

        if df is None:
            return

        if 'latitude' not in df.columns or 'longitude' not in df.columns:
            st.error("Latitude and/or longitude columns are missing in the dataset.")
            return

        df_geo = df.dropna(subset=['latitude', 'longitude'])
        df_geo = df_geo[(df_geo['latitude'] != '') & (df_geo['longitude'] != '')]

        if df_geo.empty:
            st.warning("No data available for the selected months after filtering out rows with empty latitude or longitude.")
            return

        selected_locations = st.sidebar.multiselect("Select locations", df_geo['location'].unique())
        selected_crime_types = st.sidebar.multiselect("Select crime types", df_geo['crime_type'].unique())

        latitudes = df_geo['latitude'].astype(float).tolist()
        longitudes = df_geo['longitude'].astype(float).tolist()

        latitude_centro = sum(latitudes) / len(latitudes)
        longitude_centro = sum(longitudes) / len(longitudes)

        mapa = folium.Map(location=[latitude_centro, longitude_centro], zoom_start=8, tiles="openstreetmap")

        marker_cluster = MarkerCluster().add_to(mapa)

        filtered_df = df_geo
        if selected_locations:
            filtered_df = filtered_df[filtered_df["location"].isin(selected_locations)]
        if selected_crime_types:
            filtered_df = filtered_df[filtered_df["crime_type"].isin(selected_crime_types)]

        combined_data = filtered_df[['latitude', 'longitude', 'crime_type', 'location']].values.tolist()

        for data in combined_data:
            popup_info = f"""
            <div style="display: flex; flex-direction: row;">
                <div style="margin-right: 10px;"><b>Crime:</b> {data[2]}</div>
                <div><b>Location:</b> {data[3]}</div>
            </div>
            """
            latitude, longitude = float(data[0]), float(data[1])
            folium.Marker(
                location=[latitude, longitude],
                icon=None,
                popup=folium.Popup(popup_info, max_width=400),
            ).add_to(marker_cluster)

        st_folium(mapa, width=1000)
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
