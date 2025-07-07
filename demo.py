import streamlit as st
from io import BytesIO
import docx
import google.generativeai as genai
import time
prompts = {
    "Group Company": "Extract the name of buyer mentioned in the text.Only the BUYER name to be extracted.Format to look for:'Buyer'.",
    "Counterparty": "Extract only the name of the counterparty mentioned in the text.Format to look for :'Seller'.",
    "Trade Date": "Extract the trade date mentioned in the text. It can be found in the format of dd mm yyyy.Date month and year ",
    "Product": "Extract the name of the product mentioned in the text.",
    "Quantity":"Extract the quantity of the product mentioned in the text. Look for terms such as 'MT' and extract the value of quantity.",
    "Grade": "Extract the product grade or quality mentioned in the text.",
    "Delivery Period":"Extract the delivery period that can be found in the text. Delivery period is ideally a date range",
    "Price/Index": "Extract the price and the price index information from the text. It can be found in the format of : 'NYMEX WTI- 5USD/BBL'.",
    "Pricing Date Type": "Extract the pricing date type from the text. Format:'Event Based'.",
    "Event": "Extract the event from the text. Format:'Month of Delivery'."

}

def gemini_output(text,system_prompt, prompts,parameter):
    # for prompt in prompts:
    import pdb
    # pdb.set_trace()
    print(prompts,'here')
    input_prompt= [system_prompt,text, prompts]
    response= model.generate_content(input_prompt)
    st.text_area(parameter, value=response.text)

    # return response.text
# Create a Streamlit app
st.title("Contract Document Reader")

# Add a file uploader widget
uploaded_file = st.file_uploader("Upload a Word document", type="docx")
genai.configure(api_key='AIzaSyCyMQEtlPdNj8Gr5fkhI9p24nF84ZmlMOc')
MODEL_CONFIG= {
    "temperature": 1,
    "top_p":0.95,
    "top_k":3
}
model = genai.GenerativeModel(model_name='gemini-pro',
generation_config=MODEL_CONFIG)
# response = model.generate_content("What is the meaning of life?")
# Check if a file is uploaded
if uploaded_file is not None:
    
    # Read the contents of the uploaded Word document
    docx_data = uploaded_file.getvalue()
    doc = docx.Document(BytesIO(docx_data))

    # Extract text from the Word document
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"

    # Display the contents
    # st.header("Contents of the Word document:")
    st.text_area("Contract data", value=text, height=30)
    sp =f"""You are a helpful AI text extraction assistant."""
    for parameter, prompt in prompts.items():
    # for prompt in prompts:
        gemini_output(text, sp, prompt,parameter)
        time.sleep(1)
    # for parameter, prompt in prompts.items():
    #     st.write(f"**Prompt:** {prompt}")
    #     # Use Gemini to extract the parameter based on the prompt
    #     extracted_data = model.generate_content(prompt)
    #     # extracted_data = extract_parameter_with_gemini(text_input, prompt)
    #     st.write(f"**Extracted {parameter}:** {extracted_data}")


