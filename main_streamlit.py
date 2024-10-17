import streamlit as st
from score_keeper.keeper import Keeper
from score_keeper.score import *
import pandas as pd
import numpy as np
import datetime


st.set_page_config(page_title='Score Keeper', page_icon='🎯')
st.title('Score Keeper 🎯')

if 'data_loaded' not in st.session_state:
    st.session_state.data_loaded = False
    st.session_state.keeper = Keeper()
    st.session_state.data = pd.DataFrame()


def load_btn_click():
    st.session_state.keeper.get_data_from_file()
    st.session_state.data = st.session_state.keeper.data
    st.session_state.data_loaded = True


def filter_data_st(data, semester_from, semester_to, subjects, date_from, date_to, grade_from, grade_to):
    data = data[(data['Semester'] >= semester_from) & (data['Semester'] <= semester_to)]

    if subjects:
        data = data[data['Subject'].isin(subjects)]

    data['Date'] = pd.to_datetime(data['Date'])
    data = data[(data['Date'] >= pd.to_datetime(date_from)) & (data['Date'] <= pd.to_datetime(date_to))]
    data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')

    data = data[(data['Grade'] >= grade_from) & (data['Grade'] <= grade_to)]
    return data

def make_data_equal(df_to_use):
    df_to_use['Date'] = pd.to_datetime(df_to_use['Date']).dt.date
    st.session_state.keeper.data = df_to_use
    st.session_state.data = df_to_use
    return 0

def rerun():
    st.rerun(scope='app')

if not st.session_state.data_loaded:
    st.button('Load Data', on_click=load_btn_click)
else:
    with st.container():
        if st.session_state.keeper.data.empty:
            st.write('No data available.')
        else:
            st.subheader('Data')
            st.dataframe(st.session_state.data, width=800, height=600)


if st.session_state.data_loaded and not st.session_state.keeper.data.empty:
    with st.container():
        if 'under_df_subheader_text' in st.session_state:
            st.subheader(st.session_state.under_df_subheader_text)
            if st.session_state.under_df_subheader_text == 'Show stats':
                copy = st.session_state.data.copy()
                st.session_state.data['Date'] = pd.to_datetime(st.session_state.data['Date'])
                st.dataframe(st.session_state.data.describe().loc[['count', 'mean', 'min', '25%', '50%', '75%', 'max']],
                             width=600, height=300)
                st.session_state.data = copy
            elif st.session_state.under_df_subheader_text == 'Plot grades distribution':
                st.pyplot(plot_grades_bar_distribution(st.session_state.data, return_fig=True))
            elif st.session_state.under_df_subheader_text == 'Plot avg per grade semester':
                st.pyplot(plot_avg_grade_per_semester(st.session_state.data, return_fig=True))


    with st.container():
        st.sidebar.subheader('Filter Data')

        with st.sidebar.form(key='filter_form'):
            col1, col2 = st.columns(2)

            with col1:
                semester_filter_from = st.number_input('Semester From',
                                                       value=st.session_state.keeper.data.Semester.min())
                date_filter_from = st.date_input('Date From',
                                                 value=pd.to_datetime(st.session_state.keeper.data.Date.min()).date())
                grade_filter_from = st.number_input('Grade From',
                                                    value=st.session_state.keeper.data.Grade.min(), step=0.5)

            with col2:
                semester_filter_to = st.number_input('Semester To',
                                                     value=st.session_state.keeper.data.Semester.max())
                date_filter_to = st.date_input('Date To',
                                               value=pd.to_datetime(st.session_state.keeper.data.Date.max()).date())
                grade_filter_to = st.number_input('Grade To', value=st.session_state.keeper.data.Grade.max(), step=0.5)

            subject_filter = st.multiselect("Select Subjects",
                                            sorted(st.session_state.keeper.data.Subject.unique()))

            submitted = st.form_submit_button('Filter Data!')

            if submitted:
                st.session_state.data = filter_data_st(
                    st.session_state.keeper.data,
                    semester_filter_from,
                    semester_filter_to,
                    subject_filter,
                    date_filter_from,
                    date_filter_to,
                    grade_filter_from,
                    grade_filter_to
                )
                rerun()


    with st.sidebar.form('Actions'):
        st.subheader('Actions')
        action = st.radio('What do you want to do?',
                                  ['Show stats', 'Plot grades distribution', 'Plot avg per grade semester'])
        action_button = st.form_submit_button('Action!')
        if action_button:
            st.session_state.under_df_subheader_text = action
            rerun()

    with st.sidebar.form('Add Data'):
        st.subheader('Add Data')
        semester = st.number_input('Semester', min_value=1, max_value=14)
        grade = st.select_slider('Grade', options=np.arange(2, 5.5, 0.5), value=3.5)
        subject = st.text_input('Subject')
        add_data_button = st.form_submit_button('Add Data!')
        if add_data_button:
            if not subject:
                st.warning('Please enter a subject!')
            else:
                new_record = pd.DataFrame([{
                    "Date": datetime.datetime.now().date(),
                    "Semester": semester,
                    "Subject": subject,
                    "Grade": grade
                }])

                df = pd.concat([st.session_state.keeper.data, new_record], ignore_index=True)
                make_data_equal(df)
                rerun()
