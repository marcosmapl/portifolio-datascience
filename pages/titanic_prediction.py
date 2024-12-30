import numpy as np
import pandas as pd
import streamlit as st
import pickle

from xgboost import XGBClassifier

st.title("Predicting the chance of survival in the Titanic disaster")

class_list = ["C1", "C2", "C3"]
max_fare = {
    class_list[0]: 515.0,
    class_list[1]: 75.0,
    class_list[2]: 70.0
}
sex_list = ["Female", "Male"]
embarked_list = ["Cherbourg", "Queenstown", "Southampton"]
title_list = ["Capt.", "Col.", "Don.", "Dr.", "Lady.", "Major.", "Master", "Miss", "Mlle.", "Mme.", "Mr.", "Mrs.", "Other", "Rev.", "Sir."]

form_col, suv_col = st.columns(2)
with form_col:
    st.header("Passenger Information")
    line1 = st.columns([.2, .8])
    with line1[0]:
        st.selectbox(
                label="Title",
                options=title_list,
                index=0,
                key="ptitle"
            )
    
    with line1[1]:
        st.text_input(
            label="Passenger", 
            placeholder="Fullname",
            key="pname"
        )

    line2 = st.columns([.2, .28, .22, .3])
    with line2[0]:
        st.selectbox(
            label="Class",
            options=class_list,
            index=0,
            key="pclass"
        )
        
    with line2[1]:
        st.selectbox(
            label="Sex",
            options=sex_list,
            index=0,
            key="psex"
        )

    with line2[2]:
        st.number_input(
            "Age",
            min_value=0,
            max_value=100,
            value=50,
            key="page"
        )        

    with line2[3]:
        st.number_input(
            "Fare",
            min_value=0.0,
            max_value=max_fare[st.session_state["pclass"]],
            value=max_fare[st.session_state["pclass"]] / 2,
            key="pfare"
        )
        
    line3 = st.columns([.2, .34, .23, .23, ])
    with line3[0]:
        st.selectbox(
            label="Cabin Floor",
            options=("S", "A", "B", "C", "D", "E", "F", "G"),
            index=0,
            key="pcabin"
        )
        
    with line3[1]:
        st.selectbox(
            label="Embarked",
            options=embarked_list,
            index=0,
            key="pembarked"
        )
        
    with line3[2]:
        st.slider(
            "Nº of Siblings/Spouses",
            min_value=0,
            max_value=10,
            value=1,
            step=1,
            key="psibs"
        )
        
    with line3[3]:
        st.slider(
            "Nº of Parents/Children",
            min_value=0,
            max_value=8,
            value=1,
            step=1,
            key="pchild"
        )
    
    btn_line = st.columns([.5, .5])
    with btn_line[1]:
        if st.button("Predict", icon="🎻", type="primary"):
            data = [
                int(st.session_state["pclass"].replace("C", "")),
                st.session_state["page"],
                st.session_state["psibs"],
                st.session_state["pchild"],
                st.session_state["pfare"],
                1 if st.session_state["psex"] == sex_list[0] else 0,
                1 if st.session_state["psex"] == sex_list[1] else 0,
                embarked_list.index(st.session_state["pembarked"]),
                1 if st.session_state["pembarked"] == embarked_list[0] else 0,
                1 if st.session_state["pembarked"] == embarked_list[1] else 0,
                1 if st.session_state["pembarked"] == embarked_list[2] else 0,
                title_list.index(st.session_state["ptitle"]),
                1 if st.session_state["ptitle"] == title_list[0] else 0,
                1 if st.session_state["ptitle"] == title_list[1] else 0,
                1 if st.session_state["ptitle"] == title_list[2] else 0,
                1 if st.session_state["ptitle"] == title_list[3] else 0,
                1 if st.session_state["ptitle"] == title_list[4] else 0,
                1 if st.session_state["ptitle"] == title_list[5] else 0,
                1 if st.session_state["ptitle"] == title_list[6] else 0,
                1 if st.session_state["ptitle"] == title_list[7] else 0,
                1 if st.session_state["ptitle"] == title_list[8] else 0,
                1 if st.session_state["ptitle"] == title_list[9] else 0,
                1 if st.session_state["ptitle"] == title_list[10] else 0,
                1 if st.session_state["ptitle"] == title_list[11] else 0,
                1 if st.session_state["ptitle"] == title_list[12] else 0,
                1 if st.session_state["ptitle"] == title_list[13] else 0,
                1 if st.session_state["ptitle"] == title_list[14] else 0,
                st.session_state["psibs"] + st.session_state["pchild"],
                1 if (st.session_state["psibs"] + st.session_state["pchild"]) == 1 else 0,
                1 if st.session_state["page"] < 12 else 0,
                1 if st.session_state["page"] > 50 else 0,
            ]

            st.session_state["passenger"] = data
            xgb = pickle.load(open("data/xgb_titanic.pkl", "rb"))
            probs = xgb.predict_proba([st.session_state["passenger"]])[0]
            st.session_state["suv_prob"] = probs[1]
        
with suv_col:
    suv_prob = 0
    img_str = "img/titanic.jpeg"
    category_str = ""
    desc_str = ""
    if st.session_state.get("suv_prob", None):
        suv_prob = st.session_state.get("suv_prob", 0)
        
        if suv_prob < .21:
            img_str = "img/titanic-suv0.jpg"
            category_str = "Very Low"
            desc_str = "Survival was extremely unlikely. This group represents the lowest chances of escaping the disaster, possibly due to factors such as location on the ship, economic class, or lack of rescue priority."
        elif suv_prob < .41:
            img_str = "img/titanic-suv1.jpg"
            category_str = "Low"
            desc_str = "Low probability of survival. Individuals in this range had reduced chances, but there was still a limited possibility of being rescued."
        elif suv_prob < .61:
            img_str = "img/titanic-suv2.jpg"
            category_str = "Moderate"
            desc_str = "Survival was possible. This range represents a balance between risk and opportunity. Survival depended on specific circumstances, such as quick access to lifeboats or assistance during the sinking."
        elif suv_prob < .81:
            img_str = "img/titanic-suv3.jpg"
            category_str = "High"
            desc_str = "High probability of survival. Individuals in this range were likely in more favorable situations, such as having rescue priority (women, children, or first-class passengers)."
        else:
            img_str = "img/titanic-suv4.jpg"
            category_str = "Very High"
            desc_str = "Survival was almost certain. This group includes those with the highest chances of escaping, often due to strategic location, immediate assistance, or top rescue priority."
    
    st.header(f"Chance of survival: {round(suv_prob, 2):.2f}%")
    img_cols = st.columns([.05, .9, .05])
    with img_cols[1]:
        st.image(img_str, width=600)
    st.subheader(category_str)
    st.text(desc_str)

