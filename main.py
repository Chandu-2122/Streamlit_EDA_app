#importing necessary libraries
import numpy as np
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


#creating the sidebar
def add_sidebar():
    with st.sidebar.header(':rainbow[Dataset]'):
        uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type = ['csv'])
    return uploaded_file
        
#main function
def main():
     #setting the page configuration parameters
    st.set_page_config(
        #title of the page
        page_title="EDA App",
        
        #icon
        page_icon="📊",
        
        #layout
        layout = "wide",
        
        #initial state of sidebar
        initial_sidebar_state="expanded"
    )
    
    #displaying the sidebar
    uploaded_file = add_sidebar()
    
    with st.container():
        #title of the web app

        st.title(':rainbow[The EDA app] 📊')
        st.write('This is the Exploratory Data Analysis app created in Streamlit using the ydata_profiling''' )

        #creating the pandas profiling report
        if uploaded_file is not None:
            
            #store dataset in cache
            @st.cache_data
            #function to load the dataset
            def load_csv():
                csv = pd.read_csv(uploaded_file)
                return csv
            
            #load the dataset
            dataset = load_csv()
            
            #building a profiling report
            pr = ProfileReport(dataset, explorative = True)
            
            #displaying the dataset
            st.header('**:rainbow[Dataset]**')
            st.write(dataset)
            st.write('---')
            
            #displaying the profiling report
            st.header('**:rainbow[Exploratory Data Analysis]**')
            st_profile_report(pr)
            
        #build the profiling report on example dataset
        else:
            st.info('Awaiting for the CSV file to be uploaded...')
            
            #button to use the example dataset
            if st.button('Use Example Dataset'):
                
                #store the example dataset
                @st.cache_data
                #function to load the example dataset
                def load_example_dataset():
                    #100x4ndarray shape
                    data = pd.DataFrame(np.random.rand(100,4),
                                        columns=['first', 'second', 'third', 'fourth'])
                    return data
                #load the example dataset
                example_dataset = load_example_dataset()
                
                #building a profiling report
                example_ds_pr = ProfileReport(example_dataset, explorative = True)
                
                #displaying the dataset
                st.header('**:rainbow[Example Dataset]**')
                st.write(example_dataset)
                st.write('---')
                
                #displaying the profiling report
                st.header('**:rainbow[Exploratory Data Analysis]**')
                st_profile_report(example_ds_pr)
   

if __name__ == '__main__':
    main()