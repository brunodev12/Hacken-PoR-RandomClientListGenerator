import random
import uuid
import hashlib
import os
from .num_random import generate_number
from .file_ops import load_json

currencies_list = load_json("currencies_list.json")

def generate_client_list(length:int, tokens:list=[], uuid_format:bool=False):
    client_list = []

    for _ in range(length):
        if uuid_format:
            id_ = uuid.uuid4()
        else:
            random_data = os.urandom(32)                # 32 bytes = 256 bits
            hash_object = hashlib.sha256(random_data)
            id_ = hash_object.hexdigest()
        client_id = str(id_)


        if tokens:
            num_tokens_accounts = len(tokens)
        else:
            num_tokens_accounts = random.randint(1, 10)

        random_token_list = []
        client_data = {'hash': client_id}

        for j in range(num_tokens_accounts):
            if tokens:
                token_name = tokens[j]
                for token_list in currencies_list:
                    if token_name == token_list[0]:
                        minimun = token_list[1]
                        maximun = token_list[2]
                        account_tokens = generate_number(
                            minimun, maximun, currency=token_name)
                        client_data[token_name] = account_tokens
                        break
            else:
                random_token = random.randint(0, len(currencies_list)-1)
                if random_token not in random_token_list:
                    token_list = currencies_list[random_token]
                    token_name = token_list[0]
                    minimun = token_list[1]
                    maximun = token_list[2]

                    account_tokens = generate_number(
                        minimun, maximun, currency=token_name)
                    client_data[token_name] = account_tokens
                random_token_list.append(random_token)


        client_list.append(client_data)

    return client_list