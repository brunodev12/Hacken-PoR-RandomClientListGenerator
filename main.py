from utils.client_generator import generate_client_list
from utils.file_ops import save_json
from utils.arguments import parse_arguments
from utils.check_arguments import check_tokens

def run():
    args = parse_arguments()

    if args.users <= 0:
        raise Exception("The number of users must be a positive integer.")
    
    if not args.file.endswith('.json'):
        raise Exception("The output file name must end with '.json'.")
    
    if args.tokens:
        tokens = check_tokens(args.tokens)
        if tokens==[]:
            raise Exception("Token not found.")
    else:
        tokens = []

    client_list = generate_client_list(args.users, tokens=tokens)

    save_json(client_list, args.file)

    return client_list

# Ensures that the code block within it is only executed when the script is run directly,
# and not when it's imported as a module in another script.
if __name__ == "__main__":
    run()