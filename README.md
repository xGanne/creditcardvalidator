# Credit Card Validator

This script validates credit card numbers for various card types based on their specific patterns. The supported card types are:

- MasterCard
- Visa
- American Express
- Diners Club
- Discover
- EnRoute
- JCB
- Voyager
- HiperCard
- Aura

## How to Use

1. Clone the repository or download the script.
2. Run the script using Python.
3. Enter your credit card number when prompted.

The script will check the entered credit card number against the patterns for each supported card type and will return whether the card number is valid and which type of card it is.

## Example

```sh
$ python src/main.py
Please enter your credit card number: 4111111111111111
Valid: Visa card
