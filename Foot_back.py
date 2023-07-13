import streamlit as st
import pandas as pd
import numpy as np
import Foot_back as Fb
def intro():
    #st.header("🏉FOOTY BETTING🏉")
    st.markdown("<h1 style='text-align: center; color: black;'>🏉FOOTY BETTING🏉</h1>", unsafe_allow_html=True)
    

    st.divider()
    

    with st.expander("Explanation on Downloading CSV"):
        st.text("📱Iphone Instructions: ")
        st.text("Step1. Hold down on link -> tap 'open in new tab'")
        st.text("Step2. scorll down to'Download as CSV' -> Download")
        st.text("Step3. CSV is now located in Files")
        st.text("Step4. Browse files on Streamlit")
        st.text("Step4. CHoose file -> newst file in recent")
        st.text("💻Computer Instructions: ")
        st.text("Step1. Click the link and scorll down to (Download CSV)")
        st.text("Step2. Add CSV file to a location in computer easily accessible ")
        st.text("Step3. Click browse files and add csv file.")
        st.text("Ensure its the current week stats of the players")

    #st.write("CSV file location 👉 [link](https://www.wheeloratings.com/afl_stats.html)👈")
    st.markdown('<center>Download file here <a href="https://www.wheeloratings.com/afl_stats.html">CSV</a></center>', unsafe_allow_html=True)
    st.divider()
    #st.subheader('📦 CSV DROPBOX ')
    st.markdown("<h2 style='text-align: center; color: black;'>📦 CSV DROPBOX 📦</h2>", unsafe_allow_html=True)

def read_data(uploaded_file):
       # Read CSV file
       data = pd.read_csv(uploaded_file)
       return data

def Team1_2_desposals_range(Team1_Risk,lower_lim,upper_lim):
    Dsp = Team1_Risk[(Team1_Risk['Adjusted Disposals'] >= lower_lim) & (Team1_Risk['Adjusted Disposals'] < upper_lim)].sort_values('Adjusted Disposals')
    tabel = Dsp[['Player', 'Adjusted Disposals']]
    st.write(tabel)


def Team1_2_goals_range(Team1_Risk,lower_lim,upper_lim):
    Dsp = Team1_Risk[(Team1_Risk['Adjusted Goals_Avg'] >= lower_lim) & (Team1_Risk['Adjusted Goals_Avg'] < upper_lim)].sort_values('Adjusted Goals_Avg')
    tabel = Dsp[['Player', 'Adjusted Goals_Avg']]
    st.write(tabel)

def sort_team(sorted_data,x):
    y = sorted_data[sorted_data['Team'] == x]
    return y


def data_shown(AFL_selection, sorted_data):
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(AFL_selection[0])
        team1 = sort_team(sorted_data,AFL_selection[0])
        st.write(team1[['Player', 'Goals_Avg', 'Disposals']])



    with col2:
        st.subheader(AFL_selection[1])
        team2 = sort_team(sorted_data,AFL_selection[1])
        st.write(team2[['Player', 'Goals_Avg', 'Disposals']])

    
    ##RISK SLIDER
    st.divider()

    #st.subheader('Choose Risk Level ↕️')
    st.markdown("<h2 style='text-align: center; color: black;'>Choose Risk Level ↕️</h2>", unsafe_allow_html=True)
    
    @st.cache_data(experimental_allow_widgets=True)
    def slider_cached():
        Risk_range = st.slider('Select Risk level', 0.0, 4.0, 0.0)
        return Risk_range
    
    Risk_range = slider_cached()

    
    
    def Risk_str(Risk_range):
        if Risk_range <=  0.75:
            st.subheader('Low Risk')
            Risk = 'Low Risk'
            return Risk
        
        if 0.75 < Risk_range <= 1.25:
            st.subheader('Normal Risk')
            Risk = 'Normal Risk'
            return Risk
        
        if 1.25 < Risk_range <= 2:
            st.subheader("Medium Risk")
            Risk = 'Medium Risk'
            return Risk
        
        if 2 < Risk_range <= 3.5:
            st.subheader("High Risk")
            Risk = 'High Risk'
            return Risk
        
        if Risk_range >3.5:
            st.subheader("Extreme Risk")
            Risk = 'Extreme Risk'
            return Risk
            
    Risk = Risk_str(Risk_range)


    with st.expander("Explanation on Risk Scores"):
        st.text("Goal Avg: adds the (slider value divided by 3) to -1")
        st.text("Disposal Avg: adds the (slider value) to -4.5" )
        st.write("⚠️Disclaimer⚠️")
        st.text("This is designed to improve your odds and not guarantee wins!")

    tab1, tab2 = st.tabs([AFL_selection[0], AFL_selection[1]])
    ##RISK SLIDER


    x = (len(team1))
    z = (len(team2))
    ## GOALS: LOW = -1, NORMAL = -0.5, HIGH = 0, MAD = +0.5
    ## DISP: LOW = -4, NORMAL = -2, HIGH = 0, MAD = +2
    GRF_team1= pd.DataFrame({'Risk': np.full(x,-1+float(Risk_range/3))})
    DRF_team1= pd.DataFrame({'Risk': np.full(x,-4.5+float(Risk_range))})
    GRF_team2= pd.DataFrame({'Risk': np.full(z,-1+float(Risk_range/3))})
    DRF_team2= pd.DataFrame({'Risk': np.full(z,-4.5+float(Risk_range))})

    Team1_Risk = pd.DataFrame({'Player':np.array(team1['Player']),
                            'Adjusted Goals_Avg':np.array(team1['Goals_Avg'])+np.array(GRF_team1['Risk']),
                                'Adjusted Disposals':np.array(team1['Disposals'])+np.array(DRF_team1['Risk'])})

    Team2_Risk = pd.DataFrame({'Player':np.array(team2['Player']),
                            'Adjusted Goals_Avg':np.array(team2['Goals_Avg'])+np.array(GRF_team2['Risk']),
                                'Adjusted Disposals':np.array(team2['Disposals'])+np.array(DRF_team2['Risk'])})

    word_1 = "Selection: "
    word_2 = Risk

    combines_word = f'{word_1}{word_2}'
    team1_name = AFL_selection[0]
    team2_name = AFL_selection[1]
    betslip_banner = '📚 Bet Slip Recomendations 📚'
    team1_slip_name = betslip_banner
    team2_slip_name = betslip_banner
    word_for = ' '
    combines_word1 = f'{team1_name}{word_for}{word_1}{word_2}'
    combines_word2 = f'{team2_name}{word_for}{word_1}{word_2}'

    with tab1:
    
      
        st.markdown("<h3 style='text-align: center; color: black;'>🏉 Goal Averages</h3>", unsafe_allow_html=True)
        st.bar_chart(data=Team1_Risk, x='Player', y='Adjusted Goals_Avg', use_container_width=True)
       
        st.markdown("<h3 style='text-align: center; color: black;'>🤾‍♂️ Disposals Average</h3>", unsafe_allow_html=True)
        st.bar_chart(data=Team1_Risk, x='Player', y='Adjusted Disposals', use_container_width=True)
        st.divider()
       
        st.markdown(f"<h3 style='text-align: center; color: black;'>{team1_slip_name}</h3>", unsafe_allow_html=True)
      
        st.markdown(f"<h3 style='text-align: center; color: black;'>{combines_word1}</h3>", unsafe_allow_html=True)


        col3, col4 = st.columns(2)

        with col3:
            
            st.markdown("<h3 style='text-align: center; color: black;'>15 or more disposals</h3>", unsafe_allow_html=True)
            Fb.Team1_2_desposals_range(Team1_Risk,15,20)
           
            st.markdown("<h3 style='text-align: center; color: black;'>20 or more disposals</h3>", unsafe_allow_html=True)
            Fb.Team1_2_desposals_range(Team1_Risk,20,25)
            
            st.markdown("<h3 style='text-align: center; color: black;'>25 or more disposals</h3>", unsafe_allow_html=True)
            Fb.Team1_2_desposals_range(Team1_Risk,25,40)

        with col4:
            
            st.markdown("<h3 style='text-align: center; color: black;'>1 or more goals</h3>", unsafe_allow_html=True)
            Fb.Team1_2_goals_range(Team1_Risk,1,10)
         
            st.markdown("<h3 style='text-align: center; color: black;'>2 or more goals</h3>", unsafe_allow_html=True)
            Fb.Team1_2_goals_range(Team1_Risk,2,10)
        


    with tab2:
    
  
        st.markdown("<h3 style='text-align: center; color: black;'>🏉 Goal Averages</h3>", unsafe_allow_html=True)
        st.bar_chart(data=Team2_Risk, x='Player', y='Adjusted Goals_Avg', use_container_width=True)
        
        st.markdown("<h3 style='text-align: center; color: black;'>🤾 Disposals Average</h3>", unsafe_allow_html=True)
        st.bar_chart(data=Team2_Risk, x='Player', y='Adjusted Disposals', use_container_width=True)
        
        st.markdown(f"<h3 style='text-align: center; color: black;'>{team2_slip_name}</h3>", unsafe_allow_html=True)
      
        st.markdown(f"<h3 style='text-align: center; color: black;'>{combines_word2}</h3>", unsafe_allow_html=True)

        col5, col6 = st.columns(2)

        with col5:
            st.markdown("<h3 style='text-align: center; color: black;'>15 or more disposals</h3>", unsafe_allow_html=True)
            Fb.Team1_2_desposals_range(Team2_Risk,15,20)
           
            st.markdown("<h3 style='text-align: center; color: black;'>20 or more disposals</h3>", unsafe_allow_html=True)
            Fb.Team1_2_desposals_range(Team2_Risk,20,25)
            
            st.markdown("<h3 style='text-align: center; color: black;'>25 or more disposals</h3>", unsafe_allow_html=True)
            Fb.Team1_2_desposals_range(Team2_Risk,25,40)

        with col6:
            st.markdown("<h3 style='text-align: center; color: black;'>1 or more goals</h3>", unsafe_allow_html=True)
            Fb.Team1_2_goals_range(Team2_Risk,1,10)
         
            st.markdown("<h3 style='text-align: center; color: black;'>2 or more goals</h3>", unsafe_allow_html=True)
            Fb.Team1_2_goals_range(Team2_Risk,2,10)

def run_program(uploaded_file):


    data = read_data(uploaded_file)
    sorted_data = data.sort_values(by='Team', ascending=True)

    st.divider()

    st.markdown("<h2 style='text-align: center; color: black;'>🤼‍♂️ HEAD TO HEAD 🤼‍♂️</h2>", unsafe_allow_html=True)
    
    @st.cache_data(experimental_allow_widgets=True)
    def cached_dropbox():

        all_teams_list = ['Adelaide','Brisbane', 'Carlton', 'Collingwood','Essendon', 'Fremantle','Geelong', 
                        'Gold Coast', 'Greater Western Sydney' , 'Hawthorn', 'Melbourne' , 'North Melbourne', 
                        'Port Adelaide', 'Richmond', 'St Kilda', 'Sydney','West Coast', 'Western Bulldogs' ]

        AFL_selection = st.multiselect(
            ' ',
            all_teams_list )
        return AFL_selection
    
    AFL_selection = cached_dropbox()

    

    if len(AFL_selection)  != 2:
    
        st.markdown("<h3 style='text-align: center; color: black;'>Choose two teams...</h3>", unsafe_allow_html=True)
    else:
        data_shown(AFL_selection, sorted_data)

