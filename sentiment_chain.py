from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langfuse import observe

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

prompt = PromptTemplate(
    input_variables=["review"],
    template="""
You are a Product Review Analyzer.

Analyze the review and return ONLY valid JSON.

{{
  "sentiment": "Positive/Negative/Mixed",
  "sentiment_score": 0.0,
  "key_points": ["string"],
  "summary": "string"
}}

Rules:
1. Use only information present in the review.
2. Do not add external assumptions.
3. Return valid JSON only.

Review:
{review}
"""
)

@observe()
def analyze_review(review):

    chain = prompt | llm

    response = chain.invoke({
        "review": review
    })

    return response.content