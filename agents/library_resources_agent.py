"""
Library & Resources Agent
-------------------------
Helps students find relevant academic materials such as textbooks,
research papers, journals, and online learning resources.
Can also recommend digital tools for specific subjects or tasks.
"""

from typing import Dict
import random

def handle(message: str, context: Dict = None) -> Dict:
    """
    Main handler for Library & Resources Agent.
    Detects resource lookup and recommendation-type queries.
    """

    message_lower = message.lower()
    response = ""
    suggestions = []

    # Textbook or reading material requests
    if any(word in message_lower for word in ["textbook", "book", "reading material", "reference"]):
        response = (
            "📚 Here are some textbook recommendations based on common student requests:\n"
            "• *Introduction to Algorithms* – Cormen et al. (CS)\n"
            "• *Operating System Concepts* – Silberschatz et al. (CS)\n"
            "• *Principles of Microeconomics* – Mankiw (Economics)\n"
            "• *Campbell Biology* – Reece et al. (Biology)\n"
            "Would you like me to filter by subject or provide online PDF/library links?"
        )
        suggestions = [
            "Find textbooks for data structures",
            "Suggest books for psychology basics",
            "List open-access engineering textbooks"
        ]

    # Journal or research article lookup
    elif any(word in message_lower for word in ["journal", "research paper", "academic article", "publication", "citation"]):
        response = (
            "🔎 Research Resource Options:\n"
            "• [Google Scholar](https://scholar.google.com)\n"
            "• [Semantic Scholar](https://www.semanticscholar.org)\n"
            "• [arXiv](https://arxiv.org)\n"
            "• [DOAJ – Open Access Journals](https://doaj.org)\n"
            "I can also help you craft a search query — e.g., 'machine learning in education'."
        )
        suggestions = [
            "Find journals about AI in healthcare",
            "Get citation for published paper",
            "List open-access education research"
        ]

    # Online learning & resource platforms
    elif any(word in message_lower for word in ["online course", "tutorial", "learning site", "video lecture"]):
        response = (
            "💻 Learning Resources:\n"
            "• Coursera – Academic university courses\n"
            "• edX – Verified certifications\n"
            "• YouTube EDU – Free video lectures\n"
            "• Khan Academy – Foundational learning\n"
            "Would you like me to list free vs paid options?"
        )
        suggestions = [
            "Find online course for statistics",
            "Suggest tutorials for Python beginners",
            "List top AI courses on Coursera"
        ]

    # Citation or bibliography assistance
    elif any(word in message_lower for word in ["citation", "bibtex", "reference format", "apa", "mla", "chicago style"]):
        response = (
            "📝 Citation Support:\n"
            "You can use these tools for formatting:\n"
            "• [ZoteroBib](https://zbib.org)\n"
            "• [CiteThisForMe](https://www.citethisforme.com)\n"
            "• [Mendeley Reference Manager](https://www.mendeley.com)\n"
            "Need me to format a citation example in APA or MLA?"
        )
        suggestions = [
            "Format this citation in APA style",
            "Generate BibTeX entry for my research paper",
            "Suggest citation management tools"
        ]

    # Digital tool recommendations
    elif any(word in message_lower for word in ["tools", "app", "software", "plugin"]):
        response = (
            "🧰 Useful Academic Tools:\n"
            "• Notion / Obsidian – Note management\n"
            "• Zotero – Citation and research organization\n"
            "• Grammarly – Writing improvement\n"
            "• Overleaf – LaTeX collaboration\n"
            "Would you like me to suggest domain-specific apps (e.g., math, writing, research)?"
        )
        suggestions = [
            "Suggest apps for research writing",
            "Find tools for note-taking and referencing",
            "List best study organization software"
        ]

    else:
        fallback = [
            "Would you like to find textbooks, journals, or online courses?",
            "I can recommend academic materials or digital tools for your field.",
            "Need help finding research sources or citation formats?"
        ]
        response = random.choice(fallback)

    return {
        "agent": "Library & Resources Agent",
        "type": "library_resources",
        "response": response,
        "suggestions": suggestions
    }
