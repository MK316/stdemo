import streamlit as st

# IPA Data from your original dictionary
ipa_data = {
    'p': {'Voicing': 'voiceless', 'Place': 'bilabial', 'Manner': 'stop', 'Oro-nasal': '(oral)', 'Centrality': '(central)'},
    'b': {'Voicing': 'voiced', 'Place': 'bilabial', 'Manner': 'stop', 'Oro-nasal': '(oral)', 'Centrality': '(central)'},
    't': {'Voicing': 'voiceless', 'Place': 'alveolar', 'Manner': 'stop', 'Oro-nasal': '(oral)', 'Centrality': '(central)'},
    'd': {'Voicing': 'voiced', 'Place': 'alveolar', 'Manner': 'stop', 'Oro-nasal': '(oral)', 'Centrality': '(central)'},
    'k': {'Voicing': 'voiceless', 'Place': 'velar', 'Manner': 'stop', 'Oro-nasal': '(oral)', 'Centrality': '(central)'},
    'g': {'Voicing': 'voiced', 'Place': 'velar', 'Manner': 'stop', 'Oro-nasal': '(oral)', 'Centrality': '(central)'},
    # Add the rest of the IPA data...
}

# Function to filter IPA symbols based on user selections with 'ALL' as an option
def filter_symbols(voicing, place, manner, oronasal, centrality):
    # Extract IPA symbols based on the user's selections
    matching_symbols = [symbol for symbol, attributes in ipa_data.items()
                        if (voicing == 'ALL' or attributes['Voicing'] == voicing)
                        and (place == 'ALL' or attributes['Place'] == place)
                        and (manner == 'ALL' or attributes['Manner'] == manner)
                        and (oronasal == 'ALL' or attributes['Oro-nasal'] == oronasal)
                        and (centrality == 'ALL' or attributes['Centrality'] == centrality)]
    
    # Return the matching symbols in the format /p, b, m/
    return f"/{', '.join(matching_symbols)}/" if matching_symbols else "No matching symbols."

# Streamlit Interface
st.title("Sound grouping \nWith phonetic description")

# Horizontal alignment for Voicing options using st.columns()
st.markdown("### 1. Voicing")
col1, col2, col3 = st.columns(3)
with col1:
    voicing = st.radio("Voicing", ['ALL'], key="voicing_all", label_visibility="collapsed")
with col2:
    voicing = st.radio("Voicing", ['voiceless'], key="voicing_voiceless", label_visibility="collapsed")
with col3:
    voicing = st.radio("Voicing", ['voiced'], key="voicing_voiced", label_visibility="collapsed")

# Horizontal alignment for Place options
st.markdown("### 2. Place")
place_columns = st.columns(5)  # Splitting into 5 columns for horizontal layout
place_options = ['ALL', 'bilabial', 'labio-dental', 'labio-velar', 'dental', 'alveolar', 'palato-alveolar', 'palatal', 'velar', 'glottal']
place = st.radio("Place", place_options, index=0, horizontal=True)

# Horizontal alignment for Manner options
st.markdown("### 3. Manner")
manner_columns = st.columns(4)  # Splitting into 4 columns for horizontal layout
manner_options = ['ALL', 'stop', 'fricative', 'affricate', 'approximant']
manner = st.radio("Manner", manner_options, index=0, horizontal=True)

# Horizontal alignment for Oro-nasal options
st.markdown("### 4. Oro-nasal")
oronasal_columns = st.columns(3)
oronasal_options = ['ALL', '(oral)', 'nasal']
oronasal = st.radio("Oro-nasal", oronasal_options, index=0, horizontal=True)

# Horizontal alignment for Centrality options
st.markdown("### 5. Centrality")
centrality_columns = st.columns(3)
centrality_options = ['ALL', '(central)', 'lateral', '(not applicable)']
centrality = st.radio("Centrality", centrality_options, index=0, horizontal=True)

# Submit button
if st.button("Submit"):
    # Call the filter function and display the result
    result = filter_symbols(voicing, place, manner, oronasal, centrality)
    
    # Display the result with larger font
    st.markdown(f"<h1 style='text-align: center; font-size: 200%;'>{result}</h1>", unsafe_allow_html=True)
