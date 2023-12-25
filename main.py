import streamlit as st
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, CategoriesOptions
import streamlit as st
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Set up Watson NLU credentials
apikey = "YOUR_API_KEY"
url = "YOUR_SERVICE_URL"

authenticator = IAMAuthenticator(apikey)
nlu = NaturalLanguageUnderstandingV1(version='2021-09-01', authenticator=authenticator)
nlu.set_service_url(url)

# Streamlit app
def main():
    st.title("Watson NLU API Interface")
    text_input = st.text_area("Enter the text you want to analyze")

    if st.button("Analyze"):
        if text_input:
            st.write("Analyzing...")
            features = {
                "sentiment": {},
                "categories": {},
                "concepts": {},
                "entities": {},
                "keywords": {}
            }
            response = nlu.analyze(text=text_input, features=features).get_result()

            # Display analysis results
            st.subheader("Sentiment")
            sentiment = response["sentiment"]["document"]["label"]
            st.write(f"Sentiment: {sentiment}")

            st.subheader("Categories")
            categories = response["categories"]
            for category in categories:
                label = category["label"]
                st.write(f"- {label}")

            st.subheader("Entities")
            entities = response["entities"]
            for entity in entities:
                name = entity["text"]
                entity_type = entity["type"]
                st.write(f"- {name} ({entity_type})")

            st.subheader("Keywords")
            keywords = response["keywords"]
            for keyword in keywords:
                text = keyword["text"]
                relevance = keyword["relevance"]
                st.write(f"- {text} (Relevance: {relevance})")

        else:
            st.warning("Please input some text to analyze.")

# Run the app
if __name__ == "__main__":
    main()
