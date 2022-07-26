
from turtle import width
import streamlit as st
from recommandation import cleaning
import pandas as pd
import streamlit.components.v1 as stc 
from Data import list_skills ,job

list_skills1=pd.DataFrame(list_skills)
job1=pd.DataFrame(job)
def main():
    clean=cleaning()
    menu=["Home","recommendation"]
    choice=st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
        st.title("Welcome to your recommender candidats system")
        #st.subheader("take a look of your DB resume")
        #st.dataframe(career_builder.head(5))
        st.subheader("check all the CV's ")
        st.dataframe(list_skills1.head(5))
        st.subheader("check all the Job_Description ")
        st.dataframe(job1.head(5))
    elif choice == "recommendation":
        st.title("Recommender system")
        search_term = st.text_area("Put your Job Description",height=100)
        #st.text_input("Put your Job Description")
        if st.button("Recommendation"):
            if search_term is not None:
                results = clean.recommandation(search_term)
                
                #st.write(results)
                st.json(results)
    else:
        pass
if __name__ == '__main__':
	main()
