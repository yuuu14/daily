


## input descrption, params, returns,
## generate code
## exec answers with user-defined test cases

import streamlit as st
import pandas as pd
import pprint
import time

from llm_template import Param, formatted_prompt


st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)

if "prompt" not in st.session_state:
    st.session_state.prompt = ""

if "code" not in st.session_state:
    st.session_state.code = ""
 
with col1:
    function_name = st.text_input(label="Function name")
    print(function_name)

    description = st.text_area(label="Description", height=200)
    st.write("Parameters")
    df_params = st.data_editor(
        data=pd.DataFrame(columns=["name", "type", "description"]),
        key="params",
        num_rows="dynamic", 
        use_container_width=True
    )
    st.write("Returns")
    df_returns = st.data_editor(
        data=pd.DataFrame(columns=["name", "type", "description"]),
        key="returns",
        num_rows="dynamic", 
        use_container_width=True
    )

    generate_prompt = st.container()
    with generate_prompt:
        if st.button("Generate Prompt"):
            parameters = [
                Param(
                    name=n,
                    type=t,
                    description=d,
                ) for (n, t, d) in df_params.itertuples(index=False)
            ]
            returns = [
                Param(
                    name=n,
                    type=t,
                    description=d,
                ) for (n, t, d) in df_returns.itertuples(index=False)
            ]
            st.session_state.prompt = formatted_prompt(
                function_name, description, parameters, returns
            )


with col2:
    st.write("Prompt")
    if st.session_state.prompt:
        st.code(st.session_state.prompt)

    # st.code(body=st.session_state["code"])
    # st.write(st.session_state["params"])
    # res = exec(st.session_state.code)
    # st.write(res)

with col3:
    st.write("Code")
    

    
    

# inputs, returns