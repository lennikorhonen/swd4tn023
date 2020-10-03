from postitoimipaikka import hae_postinumerot


def ryhmittele_toimipaikkoihin(postinumerot):
    toimipaikat = {}
    for numero, nimi in postinumerot.items():
        if nimi in toimipaikat:
            toimipaikat[nimi].append(numero)
        else:
            toimipaikat[nimi] = [numero]

    return toimipaikat


def etsi_toimipaikan_numerot(toimipaikan_nimi, toimipaikat):
    nimi_isolla = toimipaikan_nimi.strip().upper()
    if nimi_isolla in toimipaikat:
        return toimipaikat[nimi_isolla]
    else:
        return []


def muotoile_tuloste(numerot):
    if numerot:
        return 'Postinumerot: ' + ', '.join(numerot)
    else:
        return 'Postitoimipaikkaa ei löytynyt :('


def main():
    postinumerot = hae_postinumerot()

    toimipaikat = ryhmittele_toimipaikkoihin(postinumerot)

    etsittava = input('Kirjoita postitoimipaikka: ')

    numerot = etsi_toimipaikan_numerot(etsittava, toimipaikat)

    tuloste = muotoile_tuloste(numerot)

    print(tuloste)


if __name__ == '__main__':
    main()
