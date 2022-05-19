

def stringToSentiment(text):
    return TextBlob(text).sentiment.polarity

def main():
    print(stringToSentiment('i love you'))



if __name__ == "__main__":
    from textblob import TextBlob
    main()