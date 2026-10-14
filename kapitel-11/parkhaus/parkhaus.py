# Praxisaufgabe · Die Klasse Parkhaus
# Ein Parkhaus hat eine feste Zahl an Plätzen. Autos fahren ein und aus.
# Die Zahl der belegten Plätze darf nur über Methoden geändert werden.


class Parkhaus:

    def __init__(self, name, plaetze):
        self.name = name
        self.__plaetze = plaetze
        self.__belegt = 0

    def einfahren(self):
        if self.__belegt < self.__plaetze:
            self.__belegt += 1
            return True
        else:
            return False

    def ausfahren(self):
        if self.__belegt > 0:
            self.__belegt -= 1
            return True
        else:
            return False

    def freie_plaetze(self):
        return self.__plaetze - self.__belegt


# Schritt 5: Testen

ph = Parkhaus("Am Markt", 2)

assert ph.einfahren() == True
assert ph.freie_plaetze() == 1

assert ph.einfahren() == True
assert ph.freie_plaetze() == 0

assert ph.einfahren() == False
assert ph.freie_plaetze() == 0

assert ph.ausfahren() == True
assert ph.freie_plaetze() == 1

leeres_ph = Parkhaus("Leer", 2)
assert leeres_ph.ausfahren() == False

print(ph.name, "- freie Plätze:", ph.freie_plaetze())
print("Alle Tests bestanden")



# Schritt 5: Testen
# TODO: Parkhaus "Am Markt" mit 2 Plätzen anlegen, dreimal einfahren, einmal ausfahren,
#       nach jedem Schritt den Rückgabewert und die freien Plätze prüfen.
