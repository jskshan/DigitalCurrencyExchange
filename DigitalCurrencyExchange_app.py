import time

import streamlit as st

import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Digital Currency(USDT) Exchange",
    page_icon="random",
    layout="centered",
    initial_sidebar_state="collapsed",
)

dIuputUSDT = 0.0

st.title("Digital Currency(USDT) Exchange")

sExchangePlatform = st.selectbox("Exchange Platform", ("Pionex", "ACE"))
st.write("Your Selecte : ", sExchangePlatform)

nInputTWD = st.text_input("TWD Dollar", "100000")
nInputTWD = int(nInputTWD)
st.write("TWD Dollar : {0}".format(nInputTWD))

dInputExchangeRate = st.text_input("{0} Exchange Rate".format(sExchangePlatform), "27.942")
dInputExchangeRate = round(float(dInputExchangeRate), 3)

if sExchangePlatform == "ACE":
    dInputFee = 0.1
    
    dIuputUSDT = (nInputTWD / dInputExchangeRate) * (1 - (dInputFee / 100))
elif sExchangePlatform == "Pionex":
    nExchangeCount = 100000 // 30000
        
    if (100000 % 30000) > 0:
        nExchangeCount = nExchangeCount + 1
    
    dInputFee = nExchangeCount * 20
    nOutputFee = 0.1
    
    dIuputUSDT = (nInputTWD - dInputFee) / dInputExchangeRate

st.write("{0} Exchange Rate : {1}, USDT Amount : {2}".format(sExchangePlatform, dInputExchangeRate, dIuputUSDT))

dOutputExchangeRate = st.text_input("MAX Exchange Rate", "28.049")
dOutputExchangeRate = round(float(dOutputExchangeRate), 3)

if sExchangePlatform == "ACE":
    nSendUSDTFee = 0
    dOutputFee = 0.1
elif sExchangePlatform == "Pionex":
    nSendUSDTFee = 1
    dOutputFee = 0.1

dRecieveUSDT = dIuputUSDT - nSendUSDTFee

st.write("Recieve USDT : {0}, MAX Exchange Rate : {1}".format(dRecieveUSDT, dOutputExchangeRate))

if st.button("Compute"):
    dOutputTWD = (dRecieveUSDT * dOutputExchangeRate) * (1 - (dOutputFee / 100))
    dRewardRate = round(((dOutputTWD - nInputTWD) / nInputTWD) * 100, 2)
        
    st.write("Result:")
    st.write("Output TWD Dollar : {0}".format(dOutputTWD))
    st.write("Reward Rate = {0}%".format(dRewardRate))
else:
    st.write("Result:")