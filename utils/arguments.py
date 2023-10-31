import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generates a client list.")

    # Flag "-u" for amount of users
    parser.add_argument("-u", "--users", type=int, default=10000,
                        help="Number of users to generate. Defaults to 10 000. Must be a positive integer.")
    
     # Flag "-f" for output file name
    parser.add_argument("-f", "--file", type=str, default="client_list.json",
                        help="Name of the output file. Defaults to 'client_list.json'.")

    return parser.parse_args()