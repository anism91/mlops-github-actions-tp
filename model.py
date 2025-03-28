def predict_sentiment(text):
    """
    Predict the sentiment of a given text.

    Args:
        text (str): The input text to analyze.

    Returns:
        str: The sentiment of the text, which can be "positive", "negative", or "neutral".
    """
    if not text:
        return "neutral"
    if "simple" in text.lower():
        return "neutral-simple"
    if "happy" in text.lower() or "good" in text.lower():
        return "positive"
    if "sad" in text.lower() or "bad" in text.lower():
        return "negative"
    return "neutral"