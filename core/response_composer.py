"""
Response Composer
-----------------
Combines multi-agent outputs, adds clarity, and ensures consistent tone.
If multiple agents return responses, this module merges and summarizes.
"""

from core.model_router import query_model

def compose_response(intent, agent_output):
    """Composes final AI response with structured data."""
    if not agent_output.get("response"):
        # Use fallback AI models to generate one
        ai_fallback_response = query_model(
            f"User intent: {intent}\nQuery: {agent_output.get('input', '')}\n"
            f"Context: {agent_output.get('context', {})}"
        )
        agent_output["response"] = ai_fallback_response

    return {
        "intent": intent,
        "agent": agent_output.get("agent", "unknown"),
        "response": agent_output.get("response", "No valid response generated."),
        "metadata": {
            "source": agent_output.get("source", "multi-model router"),
        },
    }

def merge_multiple(responses: dict) -> str:
    """Optional: combine multiple agent responses into a coherent summary."""
    composed = "\n\n---\n\n".join([f"{k.upper()}:\n{v}" for k, v in responses.items()])
    return f"Combined Multi-Agent Summary:\n\n{composed}"
