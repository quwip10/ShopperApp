# aheidenreich
# 9-13-19

# imports
import argparse
import ShopperApp


# Main
my_parser = argparse.ArgumentParser()

# add an argument
my_parser.add_argument(
        "-i", "--interactive",
        help="opens program in interactive mode",
        action="store_true")
args = my_parser.parse_args()

if args.interactive:
    ShopperApp.get_item_object()
