
import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
from GetData import get_data,get_count,get_users
from filtor import filter_dataframe
import io



# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Статус почтовой рассылки", page_icon="📨", layout="wide")

def update_data():
    get_data()
    get_count()
    return

def loud_data(df):
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.close()
    output.seek(0)
    return output

hide_bar= """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        visibility:hidden;
        width: 0px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        visibility:hidden;
    }
    </style>
"""

# --- USER AUTHENTICATION ---
names = get_users()

authenticator = stauth.Authenticate(names,"random_cookie_name",'sdsdff',cookie_expiry_days = 0)

name, authentication_status, username = authenticator.login("Вход", "main")

if authentication_status == False:
    st.error("Неверное имя пользователя/пароль")
    st.markdown(hide_bar, unsafe_allow_html=True)

if authentication_status == None:
    st.warning("Пожалуйста, введите свое имя пользователя и пароль")
    st.markdown(hide_bar, unsafe_allow_html=True)


if authentication_status:
    st.button('Обновить', on_click=update_data)
    # # ---- SIDEBAR ----
    st.sidebar.title(f"Добро пожаловать {name}")
############################ КОЛИЧЕСТВО СООБЩЕНИЙ #####################################################################
    count = get_count()
    st.subheader("Статус сообщений")
    df_chart = pd.DataFrame(count)
    st.dataframe(df_chart, use_container_width=True,hide_index=True)

############################ СООБЩЕНИЯ ################################################################################
    Messages = get_data()
    ###about ....
    st.subheader("Сообщения")
    df = pd.DataFrame([message.__dict__ for message in Messages], columns={"system":"Система","to":"Кому",	"subject":"Тема","message":"Сообщение","status":"Статус отправления","datatime":"Дата отправки"})
    df = filter_dataframe(df)
    excel = loud_data(df)
    st.download_button(
        label="Скачать",
        data=excel,
        file_name='output.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    st.dataframe(df, use_container_width=True,hide_index=True)
#######################################################################################################################

    ###---- HIDE STREAMLIT STYLE ----
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    authenticator.logout("Выход", "sidebar")
