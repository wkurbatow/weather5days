
import plotly.express as px
import streamlit as st
from backend import get_data, parse_img
# import plotly.figure_factory as ff

list_all_images = parse_img()

st.title('Прогноз погоди до 5 днів')
st.subheader('Введи назву міста в світі')  
place = st.text_input("Місто:(на любій мові) " , value="Киев")

days = st.slider('Прогноз на скільки днів', min_value=1, 
                 max_value=5, help='Обери період в днях')
option = st.selectbox("Тепрература або погода?",
                      ('Температура','Погода'))


d, content_country, country = get_data(place, days)

st.subheader(f'{option} на наступні {days} днів в {place}: країна{country}')   

if option == 'Температура':
    temp_line = [data["main"]["temp"] for data in content_country]
    figure = px.line(x=d, y=temp_line, labels={"x" : 'Data', "y": "Temperature C" })
    st.plotly_chart(figure)
if option == 'Погода':
    temp_line = [str(data["weather"][0]["id"]) for data in content_country]
    list_images = [list_all_images[i] for i in temp_line]
    image_columns = st.columns(days)
    # render images
    ix_im = 0
    for column in image_columns:
        with column:
            st.image(list_images[ix_im:ix_im+8], use_column_width='auto', clamp=False, channels="RGB", output_format="auto")
            ix_im +=8


   
    # print(temp_line)
    # print(type(temp_line[0]))