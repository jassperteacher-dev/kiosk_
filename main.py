import streamlit as st

# 메뉴 구성
menu_data = {
    "식사류": {"순대국밥": 10000, "내장국밥": 10000, "얼큰국밥": 11000, "고기만": 10000},
    "안주류": {"모둠순대": 15000, "머리고기": 18000, "술국": 15000},
    "음료/주류": {"콜라": 2000, "사이다": 2000, "소주": 5000, "맥주": 5000}
}

# 장바구니
cart = []
if cart not in st.session_state:
  st.session_state['cart'] = []

# 화면 레이아웃
col_menu, col_cart = columns([0.7,0.3])

with col_menu :
    tab1, tab2, tab3 = st.tabs["식사류","안주류","음료/주류"]

# 결제
