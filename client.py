# client.py (robust, updated)
import asyncio
import json
import os
import nest_asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.shared.exceptions import McpError

nest_asyncio.apply()

async def run_symptom_analysis(user_input: str):
    server_path = os.path.join(os.getcwd(), "server.py")
    server_params = StdioServerParameters(command="python", args=[server_path])

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            async def call_tool_safe(name: str, args: dict):
                res = await session.call_tool(name, arguments=args)
                block = res.content[0].text if res.content else None
                try:
                    return json.loads(block) if isinstance(block, str) and block.strip().startswith(("{","[")) else block
                except Exception:
                    return block

            # Step 1: Extract symptoms
            symptoms_text = await call_tool_safe("extract_symptoms", {"user_input": user_input})

            # Step 2: Extract details (new tool)
            details_text = await call_tool_safe("extract_details", {"user_input": user_input})

            # Step 3: Match diseases using BOTH symptoms and details
            diseases_text = await call_tool_safe("match_diseases", {
                "symptoms": symptoms_text or "",
                "details": details_text or ""
            })

            # Step 4: Get advice for matched diseases
            advice_text = await call_tool_safe("get_advice", {"diseases": diseases_text or ""})

            return symptoms_text, details_text, diseases_text, advice_text

if __name__ == "__main__":
    user_input = input("Describe your symptoms: ").strip()
    if user_input:
        results = asyncio.run(run_symptom_analysis(user_input))
        symptoms, details, diseases, advice = results
        print("\n=== Results ===")
        print(f"Symptoms: {symptoms}")
        print(f"Details: {details}")
        print(f"Diseases: {diseases}")
        print(f"Advice: {advice}")
    else:
        print("No input provided.")
