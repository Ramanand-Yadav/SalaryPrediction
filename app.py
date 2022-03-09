# %%writefile app.py
import streamlit as st 
import pickle
from PIL import Image
import base64
import pandas as pd
import numpy as np


model = pickle.load(open('modelSalary.pkl', 'rb'))


def getData():
  st.write("print")



  # full Name 
  name = st.text_input("Enter Your full Name")

  # fulwgt
  fulwgt = st.number_input("Enter final Weight",min_value=13769, max_value=1484705)
  # st.write(fulwgt)

  # educationNumeric
  education_num = st.number_input("enter education b/w 1 to 16", min_value=1, max_value=16)
  # st.write(education_num)
  
  # Gender
  gen_display = ('Female','Male')
  gen_options = list(range(len(gen_display)))
  sex = st.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])
  sex = int(sex)
  # st.write(sex)

  # capital_gain
  capital_gain = st.number_input("Capital Gain",min_value=0, max_value=99999)
  capital_gain = int(capital_gain)
  # st.write(capital_gain)

  # capital_loss
  capital_loss = st.number_input("Capital Loss", min_value=0, max_value=4356)
  capital_loss = int(capital_loss)
  # st.write(capital_loss)

  # educationLevel
  edu_display = ('Low','Medium','High')
  edu_options = list(range(len(edu_display)))
  education_numCat = st.selectbox("Education Level",edu_options, format_func=lambda x: edu_display[x])
  education_numCat = int(education_numCat)
  # st.write(education_numCat)


  # hour_Per_week
  hour_display = ('Low', 'Medium', 'VeryHigh', 'High')
  hour_options = list(range(len(hour_display)))
  hour_per_weekCat = st.selectbox("Work Hour Per Week", hour_options,format_func=lambda x : hour_display[x])
  hour_per_weekCat = int(hour_per_weekCat)
  # st.write(hour_per_weekCat)

  # Occupation
  occu_display = ('LowSkill', 'HighSkill')
  occu_options = list(range(len(occu_display)))
  Occupa_cat = st.selectbox("type of Occupation", occu_options,format_func=lambda x : occu_display[x])
  Ocuupa_cat = int(Occupa_cat)
  # st.write(Ocuupa_cat)

  # AgeCat
  age_display = ('Young', 'MiddleAge', 'Old')
  age_options = list(range(len(age_display)))
  ageCat = st.selectbox("Age Category", age_options,format_func=lambda x :age_display[x])
  ageCat = int(ageCat)
  # st.write(ageCat)

  # Marital_status
  m_display = ('Single', 'Married')
  m_options = list(range(len(m_display)))
  MaritalStatusCat = st.selectbox("Marital Status", m_options,format_func=lambda x : m_display[x])
  MaritalStatusCat = int(MaritalStatusCat)
  # st.write(MaritalStatusCat)


  # Race_cat
  race_display = ('Others', 'White')
  race_options = list(range(len(race_display)))
  Race_cat = st.selectbox("Race or Enthicity", race_options,format_func=lambda x : race_display[x])
  Race_cat = int(Race_cat)
  # st.write(Race_cat)

  # workclas 
  work_display = ('Others', 'Private', 'Goverment', 'SelfEmployee')
  work_options = list(range(len(work_display)))
  WorfClass_cat = st.selectbox("chose your Work type", work_options,format_func=lambda x : work_display[x])
  # st.write(WorfClass_cat)


  # native country
  country_display = ('Others', 'United States')
  country_options = list(range(len(country_display)))
  native_country_cat = st.selectbox("Native Country", country_options,format_func=lambda x : country_display[x])
  native_country_cat = int(native_country_cat)
  # st.write(native_country_cat)


  # FEAR = [f0, f1, 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']

  # f12 = [[capital_loss, MaritalStatusCat, education_numCat, education_num, fulwgt, Occupa_cat, hour_per_weekCat, ageCat, capital_gain, WorfClass_cat, native_country_cat, sex, Race_cat]] 

  features = [fulwgt,education_num,sex,capital_gain,capital_loss,education_numCat,hour_per_weekCat,Occupa_cat,ageCat,MaritalStatusCat,Race_cat,WorfClass_cat,native_country_cat]

  dataf = pd.DataFrame({'fulwgt':fulwgt,'education_num':education_num, 'sex':sex, 'capital_gain':capital_gain,
                        'capital_loss':capital_loss, 'education_numCat':education_numCat,
                        'hour_per_weekCat':hour_per_weekCat, 'Occupa_cat':Occupa_cat, 
                        'ageCat':ageCat,'MaritalStatusCat':MaritalStatusCat, 'Race_cat':Race_cat, 'WorfClass_cat':WorfClass_cat,
                        'native_country_cat':native_country_cat}, index=[0])
  # st.write(dataf)
  print(dataf)
  if st.button("Submit"):
    prediction = model.predict(dataf)
    lc = [str(i) for i in prediction]
    ans = int("".join(lc))
    # st.write(ans)
    print(ans)
    if ans == 0:
        st.error(
            "Hello: " + name +" || "
            'According to our Calculations, your earning less than 50K. **Best Of Luck**.'
        )
    else:
        st.success(
            "Hello: " + name +" || "
            'Hurray!! According to our calculations, Your are earning more than 50k.'
        )




@st.cache(suppress_st_warning=True)
def readImage():
  """function for loading image"""
  # this is for image
  file_ = open("/content/img.gif", "rb")
  contents = file_.read()
  data_url = base64.b64encode(contents).decode("utf-8")
  file_.close()
  st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',unsafe_allow_html=True)


def run():

  
  # readImage()
  """function for loading image"""
  # this is for image
  file_ = open("/content/img.gif", "rb")
  contents = file_.read()
  data_url = base64.b64encode(contents).decode("utf-8")
  file_.close()
  st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',unsafe_allow_html=True)

  st.title("""
  Salary Prediction using Machine Learning
  **The major aim of this project is to predict which of the employee will get salary more than 50K.**
""")
  
  getData()
  






# st.write("Salary")
run()