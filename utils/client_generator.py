import random
import uuid
from .num_random import generate_number
from .file_ops import load_json

currencies_list = load_json("currencies_list.json")

def generate_client_list(length):
    client_list = []

    for i in range(length):
        _uuid = uuid.uuid4()
        client_id = str(_uuid)  # User IDs start from '1'
        # Generate a random number between 1 and 10
        num_tokens_accounts = random.randint(1, 10)

        accounts = []
        random_token_list = []

        for j in range(num_tokens_accounts):
            random_token = random.randint(0, len(currencies_list)-1)
            if random_token not in random_token_list:
                token_list = currencies_list[random_token]
                token_name = token_list[0]

                # Generate a random number between 1e-9 and 1e9
                account_tokens = generate_number(
                    token_list[1], token_list[2], currency=token_name)

                accounts.append((token_name, account_tokens))
            random_token_list.append(random_token)

        client_data = {
            client_id: accounts,
        }

        client_list.append(client_data)

    return client_list