import random
import uuid
from .num_random import generate_number
from .file_ops import load_json

currencies_list = load_json("currencies_list.json")

def generate_client_list(length, tokens=[]):
    client_list = []

    for _ in range(length):
        _uuid = uuid.uuid4()
        client_id = str(_uuid)  # User IDs start from '1'
        # Generate a random number between 1 and 10

        if tokens:
            num_tokens_accounts = len(tokens)
        else:
            num_tokens_accounts = random.randint(1, 10)

        accounts = []
        random_token_list = []

        for j in range(num_tokens_accounts):
            if tokens:
                token_name = tokens[j]
                for token_list in currencies_list:
                    if token_name == token_list[0]:
                        minimun = token_list[1]
                        maximun = token_list[2]
                        account_tokens = generate_number(
                            minimun, maximun, currency=token_name)
                        accounts.append((token_name, account_tokens))
                        break
            else:
                random_token = random.randint(0, len(currencies_list)-1)
                if random_token not in random_token_list:
                    token_list = currencies_list[random_token]
                    token_name = token_list[0]
                    minimun = token_list[1]
                    maximun = token_list[2]

                    # Generate a random number between 1e-9 and 1e9
                    account_tokens = generate_number(
                        minimun, maximun, currency=token_name)

                    accounts.append((token_name, account_tokens))
                random_token_list.append(random_token)

        client_data = {
            client_id: accounts,
        }

        client_list.append(client_data)

    return client_list