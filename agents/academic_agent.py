"""
Academic Helper Agent
---------------------
Handles: explanations, summaries, and study-related questions.
Future upgrade: connect to RAG or course material retriever.
"""

def handle_query(user_input: str, context: dict = None) -> dict:
    """
    Main function to process academic queries.
    Returns:
        dict: A dictionary containing the response and metadata
    """
    if context is None:
        context = {}
        
    text = user_input.lower()
    response = {
        "response": "",
        "context": context,
        "suggested_actions": []
    }

    # Basic keyword responses (MVP logic)
    if "recursion" in text:
        response["response"] = (
            "Recursion is a programming concept where a function calls itself "
            "until a base condition is met. For example, computing factorial(n) "
            "by calling factorial(n-1)."
        )
        response["suggested_actions"].extend([
            "Show me a code example",
            "Explain base case in recursion"
        ])
    elif "summary" in text or "explain" in text:
        response["response"] = (
            "Here's a concise explanation:\n"
            "Try breaking the topic into smaller sub-points, define each clearly, "
            "and look for real-world examples that reinforce your understanding."
        )
        response["suggested_actions"].extend([
            "Provide an example",
            "Break it down further"
        ])
    else:
        response["response"] = (
            "This looks like an academic query. To help best, please specify a topic or concept."
        )
        response["suggested_actions"].extend([
            "Explain recursion",
            "Help with math problems",
            "Study techniques"
        ])

    return response
