SOGLIA_ORE = 1000

aeromobili = [
    {"codice": "I-ABC", "modello": "A320", "ore_volo": 1240, "controlli_ok": True},
    {"codice": "I-DEF", "modello": "B737", "ore_volo": 850, "controlli_ok": False},
    {"codice": "I-GHI", "modello": "ATR72", "ore_volo": 2310, "controlli_ok": True},
    {"codice": "I-LMN", "modello": "A319", "ore_volo": 430, "controlli_ok": True},
    {"codice": "I-OPQ", "modello": "E190", "ore_volo": 1105, "controlli_ok": False},
]

def stampa_riepilogo(aeromobili):
    print("Riepilogo flotta")
    for a in aeromobili:
        stato = "OK" if a["controlli_ok"] else "NON VALIDI"
        print(f'{a["codice"]:<6} {a["modello"]:<6} {a["ore_volo"]:>6} h  controlli: {stato}')


stampa_riepilogo(aeromobili)