"""
Research Assistant Agent
------------------------
Helps students with research paper understanding, literature reviews,
citation formatting, and summarizing technical documents.
"""

from typing import Dict
import random

def handle(message: str, context: Dict = None) -> Dict:
    """
    Main handler for Research Assistant Agent.
    Detects whether the query is about summarization, citation, methodology, or topic search.
    """

    message_lower = message.lower()
    response = ""
    suggestions = []

    # Detect research-related intents
    if any(word in message_lower for word in ["summarize", "summary", "explain paper", "paper summary"]):
        response = (
            "To summarize a research paper effectively:\n"
            "1️⃣ Read the abstract and conclusion first.\n"
            "2️⃣ Identify the problem statement and methods.\n"
            "3️⃣ Note key findings and limitations.\n"
            "4️⃣ Condense it into 5–7 sentences.\n"
            "You can paste a paper abstract here, and I’ll generate a concise summary."
        )
        suggestions = [
            "Summarize this research paper abstract",
            "Highlight main results of this paper",
            "Extract keywords from this research"
        ]

    elif any(word in message_lower for word in ["citation", "reference", "bibliography", "apa", "mla"]):
        response = (
            "I can format citations for you in APA, MLA, or IEEE style.\n"
            "Please provide one or more paper titles, author names, or DOIs.\n"
            "Example: 'Create APA citation for Smith, 2023, Neural Networks and Learning Systems.'"
        )
        suggestions = [
            "APA citation example",
            "MLA format for journal article",
            "Convert this DOI to citation"
        ]

    elif any(word in message_lower for word in ["research topic", "thesis", "dissertation", "idea", "proposal"]):
        response = (
            "Choosing a good research topic:\n"
            "1️⃣ Pick an area you’re genuinely curious about.\n"
            "2️⃣ Narrow it to a clear, solvable problem.\n"
            "3️⃣ Check literature gaps — I can help list recent papers.\n"
            "4️⃣ Make sure it aligns with your field and advisor’s expertise.\n"
            "Would you like me to suggest 3–5 potential research topics?"
        )
        suggestions = [
            "Suggest thesis topics in AI ethics",
            "Show trending topics in cybersecurity",
            "List current gaps in NLP research"
        ]

    elif any(word in message_lower for word in ["methodology", "experiment", "approach", "model", "technique"]):
        response = (
            "Research methodology advice:\n"
            "1️⃣ Define your hypothesis and variables.\n"
            "2️⃣ Choose a method (quantitative, qualitative, or mixed).\n"
            "3️⃣ Explain your sampling and data collection clearly.\n"
            "4️⃣ Ensure reproducibility and ethical compliance.\n"
            "Do you want an example methodology section?"
        )
        suggestions = [
            "Example of methodology for machine learning research",
            "Explain experimental setup section",
            "Tips for reproducible research"
        ]

    elif any(word in message_lower for word in ["journal", "paper search", "database", "find papers", "literature"]):
        response = (
            "For finding research papers:\n"
            "1️⃣ Use Google Scholar, Semantic Scholar, or IEEE Xplore.\n"
            "2️⃣ Filter by year and citation count.\n"
            "3️⃣ Use queries like 'transformer-based NLP 2023'.\n"
            "4️⃣ I can suggest keywords for your topic search.\n"
            "Would you like help finding relevant papers?"
        )
        suggestions = [
            "Find recent papers on LLM safety",
            "Best databases for psychology research",
            "How to use Google Scholar efficiently"
        ]

    else:
        fallback_responses = [
            "Can you clarify your research goal? (e.g., 'Summarize this paper', 'Help me choose a topic')",
            "I can help with summaries, citations, or research topics — what are you working on?",
            "Tell me your research area, and I’ll guide you with methods or key references."
        ]
        response = random.choice(fallback_responses)

    return {
        "agent": "Research Assistant Agent",
        "type": "research",
        "response": response,
        "suggestions": suggestions
    }
