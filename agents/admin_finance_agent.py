"""
Admin & Finance Agent
---------------------
Handles: scholarships, budgeting, and administrative assistance.
Future upgrade: connect to real APIs or document parsers.
"""

def handle_query(user_input: str, context: dict = None) -> str:
    """
    Processes queries related to university admin, fees, or scholarships.
    """
    text = user_input.lower()

    if "scholarship" in text:
        return (
            "Here are some suggestions:\n"
            "• Look for university-specific merit or need-based scholarships.\n"
            "• Use keywords like 'CS undergraduate scholarship' on your university site.\n"
            "• Contact the Financial Aid Office for open applications."
        )
    elif "budget" in text or "money" in text or "expenses" in text:
        return (
            "To build a simple student budget:\n"
            "1. List your monthly income (stipend, allowance, part-time work).\n"
            "2. Subtract fixed costs (rent, food, transport).\n"
            "3. Allocate 10% to savings if possible."
        )
    elif "form" in text or "register" in text:
        return (
            "Administrative forms usually require your student ID and department info. "
            "Download forms from the official student portal and fill them in using Adobe Acrobat."
        )
    else:
        return (
            "I can help with scholarships, budgeting, or form filling. What do you need help with?"
        )
