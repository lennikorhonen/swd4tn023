from postinumerot import ryhmittele_toimipaikkoihin, etsi_toimipaikan_numerot, muotoile_tuloste


def test_ryhmittele_yksi_postinumero():
    aineisto = {"10120": "TÄHTELÄ"}

    toimipaikat = ryhmittele_toimipaikkoihin(aineisto)

    assert toimipaikat == {"TÄHTELÄ": ["10120"]}


def test_ryhmittele_useita_postinumeroita():
    aineisto = {"10120": "TÄHTELÄ", "10210": "INKOO", "10211": "INKOO"}

    toimipaikat = ryhmittele_toimipaikkoihin(aineisto)

    assert toimipaikat == {
        "TÄHTELÄ": ["10120"],
        "INKOO": ["10210", "10211"]
    }


def test_etsi_toimipaikan_numerot():
    toimipaikat = {
        "TÄHTELÄ": ["10120"],
        "INKOO": ["10210", "10211"]
    }

    assert etsi_toimipaikan_numerot("TÄHTELÄ", toimipaikat) == ["10120"]
    assert etsi_toimipaikan_numerot("INKOO", toimipaikat) == ["10210", "10211"]

    assert etsi_toimipaikan_numerot("NEW YORK", toimipaikat) == []


def test_etsi_toimipaikan_numerot_eri_kirjoitusasuilla():
    toimipaikat = {
        "TÄHTELÄ": ["10120"],
        "INKOO": ["10210", "10211"]
    }

    assert etsi_toimipaikan_numerot("TÄHTELÄ", toimipaikat) == ["10120"]
    assert etsi_toimipaikan_numerot("tähtelä", toimipaikat) == ["10120"]
    assert etsi_toimipaikan_numerot("Tähtelä", toimipaikat) == ["10120"]


def test_muotoile_tuloste_tyhjalle_listalle():
    tuloste = muotoile_tuloste([])

    assert 'ei löytynyt' in tuloste


def test_muotoile_tuloste_monelle_postinumerolle():
    tuloste = muotoile_tuloste(['00100', '00280'])

    assert '00100, 00280' in tuloste
