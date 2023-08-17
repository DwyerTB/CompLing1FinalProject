### CompLing Term Project
# Ru_Text_Sent_Analysis.py
# by
# 12/06/2022

"""
Write a program that takes user input (Russian sentence), translates it to
English and uses VADER to provide a sentiment score then returns the sentiment
score
"""

# Get sentiment analyzer from VADER
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Connect LibreTranslateAPI
from libretranslatepy import LibreTranslateAPI

# If this link becomes outdated, the program will display the error message
# found in the main function's try/except
# (because this link is where the machine translations for this code come from)
lt = LibreTranslateAPI("https://translate.argosopentech.com/")

# Function for translating Russian sentence to English with LibreTranslateAPI
def ru2en_translator(ru_sent):
    """
    Translate Russian sentence to English using LibreTranslateAPI.

    Parameters:
        ru_sent (str): Russian sentence.

    Returns:
        en_sent (str): English sentence.
    """
    
    # Translate Russian text to English and name it 'en_sent'
    en_sent = lt.translate(ru_sent, "ru", "en")

    return en_sent

# Function for translating English sentence to Russian with LibreTranslateAPI
def en2ru_translator(en_sent):
    """
    Translate English sentence to Russian using LibreTranslateAPI.

    Parameters:
        en_sent (str): Russian sentence.

    Returns:
        ru_sent (str): English sentence.
    """
    
    # Translate Russian text to English and name it 'en_sent'
    ru_sent = lt.translate(en_sent, "en", "ru")

    return ru_sent

# Function for using VADER on the English sentence returned above
# use polarity_scores method
def sent_score(sentence):
    """
    Take an English sentence and give sentiment scores using VADER
    SentimentIntensityAnalyzer.

    Parameters:
        sentence (str): English sentence.

    Returns:
        senti_dictionary (dict): Dictionary of sentiment scores (pos, neg,
        neu, and compound) for a sentence.
        # pos = how positive the sentence is
        # neg = how negative it is
        # neu = how neutral it is
        # compound = the overall score for the sentence's sentiment
    """
    senti_dictionary = SentimentIntensityAnalyzer().polarity_scores(sentence)

    return senti_dictionary

# Function for reporting overall sentiment score
def compound_score(dictionary):
    """
    Take compound scores from a sentiment analysis dictionary and return a word.

    Parameters
        dictionary (dict): a sentiment analysis dictionary from the polarity_scores method.

    Returns
        c_score_word (str): an English word
    """

    compound_score = dictionary['compound']

    # overall positive = compound score >= 0.05
    if compound_score >= 0.05:
        c_score_word = 'Positive'
    
    # overall negative = compound score <= -0.05
    elif compound_score <= -0.05:
        c_score_word = 'Negative'
    
    # overall neutral = (compound score > -0.05) and (compound score <= 0.05)
    elif compound_score > -0.05 and compound_score <= 0.05:
        c_score_word = 'Neutral'

    # In case something goes wrong
    else:
        c_score_word = 'I\'m sorry. Something went wrong with the compound score, can you try again?'

    return c_score_word
        
# Main function to greet user, request input, give sentiment scores, and
# explain scores.
def main():

    # Greet user and request input
    greeting = "Hello! I can give you sentiment scores for a Russian sentence."
    quit_instructions = "(When you're ready to be done, just press enter.)"

    # Test that the translation is still working
    # if so, greet user and ask for input and give output,
    # but if not, see exception at end of main function
    try: 
        # Test translation link
        test_sentence = en2ru_translator("I'm a test!")

        # English greeting
        print(greeting)
        
        # Russian greeting
        print(en2ru_translator(greeting))
        
        # English quit instructions
        print(quit_instructions)
        
        # Russian quit instructions
        print(en2ru_translator(quit_instructions))

    
        while True:
            user_text = input()
            
            # Let user close program by pressing Enter
            if user_text == "":
                print("Bye for now!")
                print("Пока")
                break

            else:
                # Translate input into English
                step_one = ru2en_translator(user_text)

                # Get sentiment score dictionary for the English sentence
                step_two = sent_score(step_one)

                # Get compound sentiment score word for the English sentence
                step_two_b = compound_score(step_two)

                # Tell user what we found
                opening = "Here\'s what I found - On a scale of 0 to 1, your sentence was scored: "

                # English then Russian opening
                print(opening)
                print(en2ru_translator(opening))

                # Do a score by score analysis in English then Russian
                pos_score_msg = "for positive sentiment."
                neg_score_msg = "for negative sentiment."
                neu_score_msg = "for neutral sentiment."
                compound_score_msg = "Overall, your sentence's sentiment is "

                print(step_two['pos'])
                print(pos_score_msg)
                print(en2ru_translator(pos_score_msg))

                print(step_two['neg'])
                print(neg_score_msg)
                print(en2ru_translator(neg_score_msg))

                print(step_two['neu'])
                print(neu_score_msg)
                print(en2ru_translator(neu_score_msg))

                print(compound_score_msg)
                print(en2ru_translator(compound_score_msg))
                print(step_two_b)
                print(en2ru_translator(step_two_b))

    # if translation link not working, explain issue and invite user to try again later 
    except ValueError:
        print("I'm sorry; my translation link is broken. Please check back soon!")
        print("Простите, моя ссылка на перевод сломана. Пожалуйста, попробуйте позже!")

main()
