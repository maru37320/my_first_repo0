import streamlit as st
st.title('안녕하세요 이마루입니다 반갑습니다')
for i in range(5):
  if i % 2 == 0:
    st.write('감사합니다')
  else:
    st.write('하하호호')

