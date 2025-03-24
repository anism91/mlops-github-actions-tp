from model import predict_sentiment

def test_predict_positive():
    """
    Test the predict_sentiment function for a positive sentiment.
    """
    assert predict_sentiment("I am happy today") == "positive"

def test_predict_negative():
    """
    Test the predict_sentiment function for a negative sentiment.
    """
    assert predict_sentiment("I feel sad") == "negative"

def test_predict_neutral():
    """
    Test the predict_sentiment function for a neutral sentiment.
    """
    assert predict_sentiment("The sky is blue") == "neutral"

def test_predict_simple():
    """
    Test the predict_sentiment function for the word 'simple'.
    """
    assert predict_sentiment("This is a simple test") == "neutral-simple"