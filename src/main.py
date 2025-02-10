import re

def validate_credit_card(card_number):
    card_number = card_number.replace(" ", "")
    
    card_patterns = {
        "MasterCard": r"^5[1-5][0-9]{14}$",
        "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
        "American Express": r"^3[47][0-9]{13}$",
        "Diners Club": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
        "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$",
        "EnRoute": r"^(2014|2149)[0-9]{11}$",
        "JCB": r"^(?:2131|1800|35\d{3})\d{11}$",
        "Voyager": r"^8699[0-9]{11}$",
        "HiperCard": r"^(606282\d{10}(\d{3})?)|(3841\d{15})$",
        "Aura": r"^50[0-9]{14,17}$"
    }
    
    for card_type, pattern in card_patterns.items():
        if re.match(pattern, card_number):
            return f"Valid: {card_type} card"
    
    return "Invalid card number"

card_number = input("Please enter your credit card number: ")
print(validate_credit_card(card_number))