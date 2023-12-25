import streamlit as st
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1  import Features, CategoriesOptions
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
    input_type = st.selectbox("Select input type", ["Text", "URL"])

    if input_type == "Text":
        text_input = st.text_area("Enter the text you want to analyze")

        if st.button("Analyze"):
            if text_input:
                analyze_text(text_input)
            else:
                st.warning("Please input some text to analyze.")
    elif input_type == "URL":
        url_input = st.text_input("Enter the URL you want to analyze")

        if st.button("Analyze"):
            if url_input:
                analyze_url(url_input)
            else:
                st.warning("Please input a URL to analyze.")

def analyze_text(text):
    st.write("Analyzing...")
    features = {
        "sentiment": {},
        "categories": {},
        "concepts": {},
        "entities": {},
        "keywords": {}
    }
    response = nlu.analyze(text=text, features=features).get_result()
    display_results(response)

def analyze_url(url):
    st.write("Analyzing...")
    features = {
        "sentiment": {},
        "categories": {},
        "concepts": {},
        "entities": {},
        "keywords": {}
    }
    response = nlu.analyze(url=url, features=features).get_result()
    display_results(response)

def display_results(response):
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

# Run the app
if __name__ == "__main__":
    main()
