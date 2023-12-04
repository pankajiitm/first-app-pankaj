import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="TDS-Week-8",
        page_icon="👋",
    )

    st.write("# Welcome to TDS Week-8 Assignment 👋")

    st.markdown(
    """ This app is for calculating maximum out of three numbers.
    """
)
    number_1 = st.number_input('Insert first number')
    number_2 = st.number_input('Insert second number')
    number_3 = st.number_input('Insert third number')
    max_number = max(number_1, number_2, number_3)
    st.write('The largest number is ', max_number)


if __name__ == "__main__":
    run()
