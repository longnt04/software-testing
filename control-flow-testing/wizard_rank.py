def get_wizard_title(mana: int, attack: int) -> str:

    if 10 <= mana < 50:
        mana_level = "thap"
    elif 50 <= mana <= 79:
        mana_level = "trung"
    else:
        mana_level = "cao"
   

    if 1 <= attack <= 4:
        attack_level = "yeu"
    elif 5 <= attack <= 8:
        attack_level = "trung"
    else:
        attack_level = "manh"
   
    
    if mana_level == "trung" and attack_level == "trung":
        res = "Phap su Tap su"
    elif mana_level == "trung" and attack_level == "manh":
        res = "Phap su Chop nhoang"
    elif mana_level == "cao" and attack_level == "trung":
        res = "Phap su Tri tue"
    elif mana_level == "cao" and attack_level == "manh":
        res = "Phap su Toan nang"
    else:
        res = "Nguoi thuong"

    return res
