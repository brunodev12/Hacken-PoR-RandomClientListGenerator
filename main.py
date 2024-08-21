from utils.client_generator import generate_client_list
from utils.file_ops import save_csv
from utils.arguments import parse_arguments
from utils.check_arguments import check_tokens


def run():
    args = parse_arguments()

    if args.users <= 0:
        raise Exception("The number of users must be a positive integer.")
    
    if not args.file.endswith('.csv'):
        raise Exception("The output file name must end with '.csv'.")
    
    if args.tokens:
        tokens = check_tokens(args.tokens)
        if tokens==[]:
            raise Exception("Token not found.")
    else:
        tokens = []
    
    if args.uuid in ("y","yes"):
        uuid_format = True
    else:
        uuid_format = False

    client_list = generate_client_list(args.users, tokens, uuid_format)

    save_csv(client_list, args.file)

    return client_list


if __name__ == "__main__":
    run()