from data.constants import tokens_dict

def check_tokens(tokens_str):

    if "," in tokens_str:
        tokens = tokens_str.split(",")
    else:
        #If there are no commas, it will be considered that there is only one element
        tokens = [tokens_str]

    normalized_tokens = []

    for token in tokens:
        normalized_token = tokens_dict.get(token.upper(), None)
        if normalized_token and (normalized_token not in normalized_tokens):
            normalized_tokens.append(normalized_token)
    
    return normalized_tokens