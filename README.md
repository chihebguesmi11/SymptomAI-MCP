# SymptomAI-MCP: Symptom Checker with Model Context Protocol  

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-success?logo=fastapi)
![LLM](https://img.shields.io/badge/LLM-Large%20Language%20Model-purple)
![AI Agent](https://img.shields.io/badge/Agentic%20AI-Emerging%20Paradigm-ff69b4)
![Gemini](https://img.shields.io/badge/Gemini-Google%20DeepMind-4285F4?logo=google)
![HTML](https://img.shields.io/badge/HTML-5-E34F26?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-3-1572B6?logo=css3&logoColor=white)
![JSON-RPC](https://img.shields.io/badge/Protocol-JSON--RPC-lightgrey)

---

## Overview  
This project demonstrates an end-to-end architecture using the **Model Context Protocol (MCP)** integrated with **FastAPI** to prototype a **Symptom Checker AI Assistant**. The system connects a browser-based frontend with an MCP-powered backend, illustrating how agentic AI workflows can be modularized and extended with tools.  

The project is designed as both a **learning resource** for MCP and a **practical health AI prototype**.  

---
## Architecture  

**Flow:**  
Browser → FastAPI → MCP Client ⇆ MCP Server (Tools) → Results  

- **Browser (Frontend)**: Collects user input.  
- **FastAPI (Backend)**: Handles HTTP routes, acts as entry point.  
- **MCP Client**: Async bridge between FastAPI and MCP.  
- **MCP Server**: Hosts modular tools (Extractor, Matcher, Advisor).  
- **Results Layer**: Outputs structured health insights (Symptoms, Diseases, Advice).  

The repository includes an **animated architecture GIF** visualizing the system flow.  

---

## Protocols and Standards Used  
- **HTTP/REST** → Communication between Browser and FastAPI.  
- **Python async** → For MCP client bridging.  
- **JSON-RPC over stdio** → Protocol for MCP client-server communication.  
- **MCP (Model Context Protocol)** → Standard for tool orchestration.  

---

## Technologies and Frameworks  
- **FastAPI** (backend web framework, async-first).  
- **MCP** (Model Context Protocol for AI tool orchestration).  
- **Python 3.10+** (core runtime).  
- **Matplotlib + NumPy** (visualization and architecture animation).  
- **ImageIO** (GIF generation).  
- **HTML5 video and images** (frontend UI banner integration).  

---

## Features  
- End-to-end **MCP architecture demo** with FastAPI.  
- Browser-based input and results rendering.  
- Modular **MCP server tools** (Extractor, Matcher, Advisor).  
- **Animated architecture diagram** for clear visualization.  
- Applied to a **Symptom Checker prototype**:  
  - Symptom extraction  
  - Disease matching  
  - Advice generation  
  - Web search with TAVILY
 
  ---
## Repository Structure  

# Project Structure

This project is organized into the following key directories and files:

```
.
├── app.py                   # The main FastAPI application entry point.
├── mcp_client/              # Contains the implementation for the MCP client.
├── mcp_server/              # Houses the MCP server, including various tools and the LLM (Large Language Model) integration.
├── static/                  # Stores static frontend assets, such as images and video.
├── templates/               # Contains the HTML templates for the frontend.
├── mcp_architecture_gif.gif   # An animated visualization of the MCP architecture.
└── README.md                # The main README file for this repository.
```





