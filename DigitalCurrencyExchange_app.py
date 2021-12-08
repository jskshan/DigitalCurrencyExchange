import time

import streamlit as st

import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Digital Currency Exchange",
    page_icon="random",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("Digital Currency Exchange")

sExchangePlatform = st.selectbox("Exchange Platform", ("Pionex", "ACE"))
st.write('You selected:', sExchangePlatform)

nInputTWD = st.text_input("TWD Dollar", "100000")
st.write("TWD Dollar : ", nInputTWD)

dInputExchangeRate = st.text_input("{0} Exchange Rate".format(sExchangePlatform), "27.942")
st.write("{0} Exchange Rate : ".format(sExchangePlatform), dInputExchangeRate)

dOutputExchangeRate = st.text_input("MAX Exchange Rate", "28.049")
st.write("MAX Exchange Rate : ", dOutputExchangeRate)

if st.button("Compute"):
    nInputExchangeFee = 0 #15
    nOutputExchangeFee = 15
    
    nSendUSDTFee = 1
    
    nInputTWD = int(nInputTWD)
    dInputExchangeRate = float(dInputExchangeRate)
    dOutputExchangeRate = float(dOutputExchangeRate)
    
    if sExchangePlatform == "ACE":
        nSendUSDTFee = 0
        nInputFee = 0.1
        nOutputFee = 0.1
        
        dIuputUSDT = (nInputTWD / dInputExchangeRate) * (1 - (nInputFee / 100))
        dSendUSDT = dIuputUSDT - nSendUSDTFee
        
        dOutputTWD = (dSendUSDT * dOutputExchangeRate) * (1 - (nOutputFee / 100)) - nInputExchangeFee - nOutputExchangeFee
        dRewardRate = round(((dOutputTWD - nInputTWD) / nInputTWD) * 100, 2)
    elif sExchangePlatform == "Pionex":
        nExchangeCount = 100000 // 30000
        
        if (100000 % 30000) > 0:
            nExchangeCount = nExchangeCount + 1
        
        nInputFee = nExchangeCount * 20
        nOutputFee = 0.1
        
        dIuputUSDT = (nInputTWD - nInputFee) / dInputExchangeRate
        dSendUSDT = dIuputUSDT - nSendUSDTFee
        
        dOutputTWD = (dSendUSDT * dOutputExchangeRate) * (1 - (nOutputFee / 100)) - nInputExchangeFee - nOutputExchangeFee
        dRewardRate = round(((dOutputTWD - nInputTWD) / nInputTWD) * 100, 2)
    st.write("Result:")
    st.write("Output TWD Dollar : {0}".format(dOutputTWD))
    st.write("Reward Rate = {0}%".format(dRewardRate))
else:
    st.write("Result:")