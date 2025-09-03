import asyncio
import os
from mcp.types import Tool, TextContent
from langchain_tavily import TavilySearch
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("symptom-ai")

# ---------------------
# API keys
# ---------------------
os.environ["GOOGLE_API_KEY"] = "AIzaSyCspSZkzS23r1ZrEl2Vym4H6QEHjRetaBg"
os.environ["TAVILY_API_KEY"] = "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"

# LLM & Search
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
search_tool = TavilySearch(max_results=3)

# ---------------------
# Helper
# ---------------------
def safe_extract_text(search_results):
    if not search_results:
        return ""
    if isinstance(search_results, str):
        return search_results
    if isinstance(search_results, list):
        return " ".join(
            item.get("content", "") if isinstance(item, dict) else str(item)
            for item in search_results
        )
    return str(search_results)

# ---------------------
# MCP Tools
# ---------------------
@mcp.tool()
async def extract_symptoms(user_input: str) -> str:
    """Extract symptoms from user free text input."""
    messages = [
        SystemMessage(content=(
            "You are a medical symptom extractor. "
            "From the user's input, extract a list of distinct symptoms as lowercase phrases. "
            "Output only a comma-separated list."
        )),
        HumanMessage(content=user_input)
    ]
    response = llm.invoke(messages).content.strip()
    return response


@mcp.tool()
async def extract_details(user_input: str) -> str:
    """Extract relevant details from user free text input."""
    messages = [
        SystemMessage(content=(
            "You are a medical relevant details extractor. "
            "From the user's input, extract a list of details as lowercase phrases that can help diagnose the case "
            "(e.g., travel history, lifestyle, habits, or recent events). "
            "Output only a comma-separated list."
        )),
        HumanMessage(content=user_input)
    ]
    response = llm.invoke(messages).content.strip()
    return response


@mcp.tool()
async def match_diseases(symptoms: str, details: str) -> str:
    """Match symptoms and details to possible diseases, return explanations."""
    if not symptoms:
        return "No symptoms identified."

    query = f"Possible diseases for symptoms: {symptoms} with details: {details}"
    search_text = safe_extract_text(search_tool.invoke(query))

    messages = [
        SystemMessage(content=(
            "You are a highly experienced family medicine doctor. "
            "Analyze the symptoms together with the provided details (such as travel, habits, hydration, etc.). "
            "Respond with empathy and professionalism. "
            "Output strictly:\n\n"
            "=== Possible Diseases ===\n"
            "- Disease1: explanation.\n"
            "- Disease2: explanation.\n"
        )),
        HumanMessage(content=f"Symptoms: {symptoms}\nDetails: {details}\nWeb info: {search_text}")
    ]
    return llm.invoke(messages).content


@mcp.tool()
async def get_advice(diseases: str) -> str:
    """Provide medical advice for diseases."""
    if not diseases:
        return "No advice available."

    query = f"Treatments, precautions, and urgent signs for: {diseases}"
    search_text = safe_extract_text(search_tool.invoke(query))

    messages = [
        SystemMessage(content=(
            "You are a medical assistant. "
            "For each disease provide:\n"
            "=== Advice for DISEASE ===\n"
            "- Step 1: explanation\n- Step 2: explanation"
        )),
        HumanMessage(content=f"Diseases: {diseases}\nWeb info: {search_text}")
    ]
    return llm.invoke(messages).content


# ---------------------
# Run Server
# ---------------------
if __name__ == "__main__":
    mcp.run()
