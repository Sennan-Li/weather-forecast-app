import streamlit as st
import plotly.express as px
from data import get_data

st.title("Weather Forecast for the Next Day")
place = st.text_input("Enter your place here").lower().title()
days = st.slider("Forecast days", min_value=1, max_value=5, help="Select the number of days")

option = st.selectbox("Select the data view:", ("Temperature", "Condition"))
st.subheader(f"Forecast Data: {option} for the next {days} days in {place}")


# Get the temp and conditoin data
if place:
    try:
        weather_data = get_data(place, days)

        match option:
            case "Temperature":
                # Create plot
                temperatures = [weather["main"]["temp"] / 10 for weather in weather_data]
                dates = [weather["dt_txt"] for weather in weather_data]
                figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temp(C)"})
                st.plotly_chart(figure)
            case "Condition":
                # Create graph
                conditions = [weather["weather"][0]["description"] for weather in weather_data]
                dates = [weather["dt_txt"] for weather in weather_data]
                image_paths = []
                for index, condition in enumerate(conditions):
                    if "rain" in condition:
                        image_path = "images/rain.png"
                    elif "clear" in condition:
                        image_path = "images/clear.png"
                    elif ("cloud" in condition):
                        image_path = "images/cloud.png"
                    elif "snow" in condition :
                        image_path = "images/snow.png"

                    image_paths.append(image_path)
                st.image(image_paths,caption= dates, width=100)

    except KeyError:
        st.error("Please enter a valid place")