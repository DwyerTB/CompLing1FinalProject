# CompLing1FinalProject

Ru_Text_Sent_Analysis_ver14.py
Made with Python 3.10.6 in IDLE 3.10.6
Packages used: vaderSentiment, SentimentIntensityAnalyzer and libretranslatepy, LibreTranslateAPI

Purpose of Program / Reason for Development
This program was written for Computational Linguistics 1 Term Project. Its purpose is to provide sentiment analysis of a Russian sentence. This can be used to check tone of text for emails, essays, etc. to guide a user on how they may come across in their writing.

Program Overview
This program provides a set of sentiment scores (level of positive, negative, and neutral sentiment from 0 to 1 and an overall sentiment rating of positive, negative, or neutral based on those scores) for a sentence in Russian. It takes user input in the form of text (a Russian sentence in Cyrrilic characters). It outputs a score for each of the three sentiment categories and informs the user of the scale (0 to 1) and the overall sentiment (positive, negative, or neutral). All user interaction is through text in both English and Russian. The program will continue taking input until the user quits by hitting ‘Enter.’

Basic Structure and Related Limitations
This program works by taking Russian text and translating it to English with LibreTranslateAPI and then using VADER sentiment analysis (SentimentIntensityAnalyzer and polarity_scores from vaderSentiment). If the translation link for the API is no longer reachable, the user will receive a message informing them that the link is broken and encouraging them to try again soon (the message will display in English and Russian). The program is currently only effective for Russian text in Cyrrilic characters and for one sentence at a time. It will accept other languages and/or longer text, but the sentiment analysis will be less accurate.

Future Iterations
Future iterations can include: more accurate machine translation, language specific sentiment analysis (rather than having to translate into English first), more languages supported, and the ability to more accurately process text longer than one sentence.
