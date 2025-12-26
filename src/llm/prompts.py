"""
prompts.py - Simple prompt templates for investment analysis
"""

INVESTMENT_ANALYSIS_PROMPT = """You are an expert real estate investment analyst at Golden Mile Properties.

PROPERTY DETAILS:
{property_details}

ML MODEL PREDICTIONS:
{ml_predictions}

RELEVANT MARKET CONTEXT:
{rag_context}

TASK: Provide a comprehensive investment analysis with:

1. INVESTMENT SUMMARY (2-3 sentences)
2. KEY DRIVERS (bullet points of what's driving the value)
3. RISK FACTORS (bullet points of potential risks)
4. RECOMMENDATION (Buy/Hold/Avoid with confidence level)
5. NEXT STEPS (specific actions for the investor)

IMPORTANT:
- Base your analysis on the provided ML predictions
- Reference specific facts from the market context
- Acknowledge data limitations when applicable
- Use ₹ for Indian Rupees
- Keep it professional but concise

OUTPUT FORMAT (JSON):
{{
  "investment_summary": "string",
  "key_drivers": ["string", "string"],
  "risk_factors": ["string", "string"],
  "recommendation": "string",
  "confidence": "high/medium/low",
  "next_steps": ["string", "string"]
}}
"""

SIMPLE_PROMPT = """Analyze this property investment:

Property: {property_details}
Predicted Price: ₹{predicted_price:,.0f} (₹{price_per_sqft:,.0f}/sqft)
Predicted Yield: {yield_pct}%

Context:
{rag_context}

Provide brief analysis in JSON format."""

PROMPTS = {
    "detailed": INVESTMENT_ANALYSIS_PROMPT,
    "simple": SIMPLE_PROMPT
}
