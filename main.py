import streamlit as st
import random as ran
st.title('안녕하세요 이마루입니다 반갑습니다')
for i in range(5):
  a = ran(1,3)
  if a % 2 == 0:
    st.write('감사합니다')
  else:
    st.write('하하호호')

