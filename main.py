
try:
    from speech_eng_to_text import Speech_to_text
    import speech_recognition as sr
except ImportError:
    print("speech_eng_to_text.py is missing")

try:

    from textt_processing import text_nlp
except ImportError:
    print("nltk library is missing is missing")


if __name__=='__main__':
    sp = Speech_to_text()
    sp_status,sp_text = sp.gettext()
    print(sp_status,sp_text)
    if sp_status:
        nl = text_nlp()
        nl_status, nl_words = nl.nl_process(sp_text)
        print(nl_status,nl_words)







    else:
        print("Please try again")
