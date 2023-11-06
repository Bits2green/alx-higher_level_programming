#!/usr/bin/python3

def multiple_returns(sentence):
    sentence_length  = len(sentence)
    if sentence_length == 0:
        res = (0, None)
        return res
    else:
        result = (sentence_length, sentence[0:1])
        return result
