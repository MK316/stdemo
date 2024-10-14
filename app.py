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

# Radio buttons for user input, but now only one selection is allowed per group
st.markdown("### 1. Voicing")
voicing = st.radio("Voicing", ['ALL', 'voiceless', 'voiced'], index=0, horizontal=True)

st.markdown("### 2. Place")
place = st.radio("Place", ['ALL', 'bilabial', 'labio-dental', 'labio-velar', 'dental', 'alveolar', 'palato-alveolar', 'palatal', 'velar', 'glottal'], index=0, horizontal=True)

st.markdown("### 3. Manner")
manner = st.radio("Manner", ['ALL', 'stop', 'fricative', 'affricate', 'approximant'], index=0, horizontal=True)

st.markdown("### 4. Oro-nasal")
oronasal = st.radio("Oro-nasal", ['ALL', '(oral)', 'nasal'], index=0, horizontal=True)

st.markdown("### 5. Centrality")
centrality = st.radio("Centrality", ['ALL', '(central)', 'lateral', '(not applicable)'], index=0, horizontal=True)

# Submit button
if st.button("Submit"):
    # Call the filter function and display the result
    result = filter_symbols(voicing, place, manner, oronasal, centrality)
    
    # Display the result with larger font
    st.markdown(f"<h1 style='text-align: center; font-size: 200%;'>{result}</h1>", unsafe_allow_html=True)
