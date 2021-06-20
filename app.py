import streamlit as st
import numpy as np
import pandas as pd

from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder

st.set_page_config(layout='wide')
st.header("ACS PROJECT(EE3302)\nAIM- To check whether a given matrix is orthogonal or not.\n")
st.header("NAME-SWATI MALLICK\nROLL NO-118EE0308")

# st.header("Swati Mallick")
# st.subheader('118EE0308')
# st.markdown('ACS PROJECT(EE3302)')
# st.markdown('To check whether a given matrix is orthogonal or not')
st.write("[More information about the topic](https://docs.google.com/presentation/d/1XQXzOV60eLvaQh0XRO-vuG3Zg1sIwR3SVBhkpjCa7rs/edit?usp=sharing)")


def isOrthogonal(a, n):

    for cols in a.columns:
        a[cols] = a[cols].astype(int)
    a = a.values
     
    trans = [[0 for x in range(n)]
                for y in range(n)]
                 
    for i in range(0, n) :
        for j in range(0, n) :
            trans[i][j] = a[j][i]
             
    prod = [[0 for x in range(n)]
               for y in range(n)]
                
    for i in range(0, n) :
        for j in range(0, n) :
     
            sum = 0
            for k in range(0, n) :
                sum = sum + (a[i][k] *
                             a[j][k])
     
            prod[i][j] = sum
 
    for i in range(0, n) :
        for j in range(0, n) :
 
            if (i != j and prod[i][j] != 0) :
                return False, trans, prod
            if (i == j and prod[i][j] != 1) :
                return False, trans, prod
 
    return True, trans, prod

st.write('\n\n\n\n')
st.write('Give input dimensions of the matrix')
n = st.number_input('dimension of matrix n*n (Orthogonal matrix needs to be a square matrix)', min_value=1, value=1)

if st.checkbox('Feed Input Matrix'):
    st.text('* While entering the values press tab to go to the next input field and press enter after giving the inputs')
    st.text('* If you want to change the dimension of the input matrix then uncheck the checkbox before changing the input dimension')

    input_dataframe = pd.DataFrame(
        '',
        index=[i for i in range(n)],
        columns=['col-'+str(i) for i in range(n)]
    )

    resp = AgGrid(
            input_dataframe, 
        editable=True,
        sortable=False,
        filter=False,
        resizable=False,
        defaultWidth=5,
        fit_columns_on_grid_load=True,
        key='input_frame')
    
    st.write('Given Input Matrix')
    st.write(resp['data'].values)

    if st.button('Check Orthogonality'):
        ans, trans, prod = isOrthogonal(resp['data'], n)
        st.write('Transpose Matrix',np.array(trans))
        st.write('Product Matrix',np.array(prod))
        if not ans:
            st.write('The Prodcuct Matrix is not an identity matrix')
        else:
            st.write('The Prodcut Matrix is an identity matrix')
        
        st.write('Orthogonality of Matrix', ans)

        
