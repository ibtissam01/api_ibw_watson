import streamlit as st
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, CategoriesOptions

# Set up Watson NLU credentials
apikey="Y5hX-s8UJ8PYMSZ40D5AGWqmeyE2T5zLDMXrlf7E4uHc"
url="https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/7fdb634c-d235-4d63-bfbb-0a928698fb41"


authenticator = IAMAuthenticator(apikey)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)

natural_language_understanding.set_service_url(url)


# Streamlit app
def main():
    st.title("Watson NLU API Interface")
    text_input = st.text_area("Enter the text you want to analyze")

    if st.button("Analyze"):
        if text_input:
            st.write("Analyzing...")
            features = {
                "sentiment": {}
        
            }
            response = nlu.analyze(text=text_input, features=features).get_result()

            # Display analysis results
            st.subheader("Sentiment")
            sentiment = response["sentiment"]["document"]["label"]
            st.write(f"Sentiment: {sentiment}")

       

        else:
            st.warning("Please input some text to analyze.")

# Run the app
if __name__ == "__main__":
    main()
