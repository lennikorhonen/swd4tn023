## Sisällysluettelo

# Johdanto koneoppimiseen

Koneoppimisessa on kyse siitä, että datan avulla tietokone voidaan opettaa ratkaisemaan ongelmia tietyssä toimintaympäristössä ilman varsinaista ohjelmointia. Dataa kyseisestä ongelmakentästä täytyy kuitenkin olla paljon, jotta *koneoppimismalli* voidaan kouluttaa. Ongelmakentän tulee myös olla tarkasti rajattu, eikä samalla datalla koulutettua mallia voida siirtää toisen ongelman ratkaisuun. Termiä *tekoäly* tunnutaan käyttävän monesti myös synonyyminä koneoppimisesta ja toisaalta mikä tahansa tavallinen ohjelmoitu algoritmi saatetaan nykyään luokitella valtamediassa "tekoälyksi". 

Yksinkertaisia ongelmia voi mallintaa lineaarisilla funktioilla. Kerätyn datan perusteella, voimme laskea lineaariselle *tavoitefunktiolle (objective function)* painokertoimet ja tehdä ennusteen uudelle datapisteelle. Rakennetun mallin hyvyyttä voidaan mitata esimerkiksi [Root Mean Square Error](https://en.wikipedia.org/wiki/Root-mean-square_deviation):lla (eli lasketaan toteutumien ja ennustefunktion antamien arvojen erotusten (keltaiset viivat kuvassa) neliöiden summa, jaetaan se toteutumien määrällä (3 kpl kuvassa) ja otetaan neliöjuuri tästä).
![lineaarinen tavoitefunktio, hävikkifunktio (loss function), optimointifunktio (gradient descent), ](img/lineaarinen_tavoitefunktio.png)

Usein reaalimaailman asiat ja ilmiöt ovat sen verran monimutkaisia, että lineaarinen ennustemalli olisi hyvin epätarkka. Tällöin voidaan käyttää sen sijaan epälineaarista tavoitefunktiota.
![epälineaarinen tavoitefunktio, ylisovittaminen (overfitting)](img/epalineaarinen_tavoitefunktio.png)

Edelliset ennustemallit ovat vielä ihmiselle helposti ymmärrettäviä. Kuitenkin vielä epälineaarisia ennustemalleja parempi on yleensä neuroverkkoihin pohjautuva ennustemalli. Neuroverkkoa voi ajatella samanlaisena (mutta monimutkaisena) matemaattisena funktiona, jossa on painokertoimet kuten lineaarisessa ja epälineaarisessa tavoitefunktiossa. Neuroverkoissa painokertointen määrittäminen vain on korkeamman asteen matematiikkaa. Tämä matemaattinen mallinnustapa on saanut inspiraationsa ihmisaivojen neuroverkoista, jotka aktivoituvat (painottuvat) niiden käytön mukaan. Neuroverkkojen yhteydessä puhutaan myös syväoppimisesta (deep learning), mikä viittaa neuroverkon kerrosten syvyyteen. Neuroverkkoja voi käyttää varsin sujuvasti ymmärtämättä niiden tarkkaa matemaattista toteutusta. Kuitenkin neuroverkkojen toimintaa (ja mallin hyvyyttä) säädetään ns. *hyperparametrien* avulla, joiden tehokas käyttö edellyttää jonkin verran ymmärrystä neuroverkkojen toiminnasta.
![neuroverkko](img/neuroverkko.png) 

## Miten kone oppii

![koneoppimisen tavat](img/koneoppimisen_tavat.png) 

Koneen opettamiseen on kolme erilaista tapaa, **ohjattu oppiminen, ohjaamaton oppiminen ja vahvistusoppiminen**. Eri tavat soveltuvat erikaltaisten ongelmien ratkaisemiseen.  

**Ohjatussa oppimisessa (supervised learning)** annamme koneelle ison joukon *merkittyä dataa (labelled data)*. Konelle voidaan siis antaa esimerkiksi 1000 kuvaa, joissa esiintyy kissa (tai rikkoutunut putki tai syöpäkasvaimen esivaihe). Tai koneelle voidaan antaa lauseita, joiden on luokiteltu sisältävän vaikka 50% "politiikkaa" ja 30% "luonnonsuojelua". Datan merkitseminen pitää tyypillisesti tehdä manuaalisena käsityönä. Kun kone on siis ajanut esimerkiksi 1000 kissakuvaa neuroverkkoon, niin se osaa tämän rakentamansa *mallin* avulla tunnistaa esiintyykö jossain tuntemattomassa kuvassa kissa. Koulutuksen aikana voidaan säätää mallin *hyperparametereja*, jotka vaikuttavat siitä kuinka hyvä mallista tulee. (Tekoäly bisneksen uudet työkalut, 2019).

**Ohjaamattomassa oppimisessa (unsupervised learning)** koneelle annetaan vain joukko dataa ja koneen annetaan itse tunnistaa datasta samankaltaisuuksia ja jakaa data joukkoihin. Mallin *hyperparametreja* säätämällä kone saadaan painottamaan datan luokittelussa erilaisia asioita. Ohjaamattoman oppimisen hyvä puoli on se, ettei dataa tarvitse luokitella itse, mutta toisaalta ohjaamaton oppiminen soveltuu vain rajattuihin ongelmiin, kuten poikkeavuuksien löytämiseen, asiakaryhmien luokitteluun jne. Ohjaamattoman oppimisen eräs mielenkiintoinen sovellutus on *K-Nearest Neighbours-algoritmiin* perustuva suosittelu. Jos esimerkiksi verkkokaupan asiakkaat on luokiteltu erilaisiin ryhmiin, niin uusi asiakas voidaan hänen käyttäytymisensä perusteella luokitella kuuluvaksi tiettyyn ryhmään ja suositella hänelle esimerkiksi samoja tuotteita, joita muut sen ryhmän asiakkaat ovat ostaneet. (Tekoäly bisneksen uudet työkalut, 2019).

![Ohjaamaton oppiminen](img/ohjaamaton_oppiminen.png) 

Ohjattu ja ohjaamaton oppiminen toimivat siis alla olevassa kuvassa esitettyjen vaiheiden mukaisesti. 
![koneoppimisen vaiheet](img/koneoppimisen_vaiheet.png) 

**Vahvistusoppimisessa (reinforcement learning)** koneen annetaan itse kokeilla ja tehdä virheitä "keppi ja porkkana"-mallilla. Vahvistusoppimista varten rakennetaan simulaatioympäristö, jossa koneelle annetaan pisteitä sen toiminnasta. Vahvistusoppiminen toimii hyvin esimerkiksi erilaisten pelien, vaikkapa shakin, kouluttamisessa. Tietokone voi pelata miljoonia pelejä itseään vastaan ja "simulaatioympäristö" antaa palautetta yksinkertaisimmillaan vain siitä, voittiko kone pelin. Monessa oikean maailman ongelmassa palautesykli koneen tekemien valintojen ja onnistumisen välillä voi olla hyvin pitkä (helposti vaikka useita viikkoja), jolloin kone oppii hyvin hitaasti. Samaten simulaatioympäristön rakentaminen voi olla haastavaa. Käytännön maailmassa itseajavia autoja pyritään kouluttamaan vahvistusoppimisen avulla. Ihminen voi siis esimerkiksi istua auton kyydissä ja antaa jatkuvasti pisteitä koneen tekemistä valinnoista.

![koneoppimisen vaiheet](img/vahvistusoppiminen.png)

### Kuvadatan muokkaaminen

Jotta kone voi oppia esimerkiksi kuvadatasta, pitää kuvadata muokata koneen ymmärtämään matriisimuotoon. Yksinkertainen esimerkki mustavalkoisesta hymynaamakuvasta voisi olla jotain alla olevan kaltaista. Eri harmaan sävyt kuvassa (0-255) on siis esitetty numeroina. Jokainen matriisin solu vastaa yhtä pikseliä kuvassa.

![Hymynaama](img/hymynaama.png)

## Koneoppiminen käytännössä

Koneoppimiseen liitty useita kirjastoja ja työkaluja, joilla kaikilla on oma roolinsa koneoppimismallien rakentamisessa tai havainnollistamisessa.

1. [Python](https://www.python.org/) on ohjelmointikieli, jolla on kirjoitettu lukuisia koneoppimiseen liittyviä kirjastoja ja rajapintoja. Suurin osa koneoppimisohjelmista ohjelmoidaan Pythonilla. 
1. [Jupyter Notebook](https://jupyter.org/) on työkalu, jolla voi kirjoittaa koodia, tehdä dokumentointia, piirtää graafeja jne. Se on vähän kuin steroideja syönyt tekstieditori. Selkeyttää ja visualisoi koneoppimismallien rakentamista. 
1. [TensorFlow](https://www.tensorflow.org/) on kirjasto ensisijaisesti *moniulotteisten taulukoiden (~tensoreiden)* käsittelyyn eli tensorilaskentaan. TensorFlow:n ympärille on rakentunut vähitellen kokonainen koneoppimiseen liittyvä ekosysteemi. TensorFlown *operaatioilla* (esim tf.add()) voidaan muokata tensoreita. Tensorit kulkevat *graafien* läpi, jotka muokkaavat tensoreita operaatioilla. Usein edellisen operaation läpikäyneestä ulostulo-tensorista tulee seuraavaan operaation sisäänmeno-tensori. Graafit tulee ajaa TensorFlow *sessiossa*, joskin uudessa [TensorFlow 2:ssa](https://www.tensorflow.org/guide/effective_tf2) ei enää. [TensorFlown käsitteiden](https://colab.research.google.com/notebooks/mlcc/tensorflow_programming_concepts.ipynb) ja käytön opettelu vaatii hieman aikaa. TensorFlown omat tutoriaalit löytyvät [täältä](https://www.tensorflow.org/tutorials). [PyTorch](https://pytorch.org/) on kilpaileva vaihtoehto TensorFlow:lle. 
1. [Keras](https://keras.io/) on melko korkean abstraktiotason (=helppokäyttöinen) kirjastorajapinta neuroverkkojen rakentamiseen ja siten sitä käytetään esimerkiksi kuvantunnistuksen yhteydessä. Nykyisin Keras sisältyy suoraan TensorFlow:hun.
1.  [Pandas](https://pandas.pydata.org/) on työkalu erityisesti kolumni-muotoisen datan käsittelyyn. Pandas:lla voi ladata dataa (esim CSV-tiedostoista) ja esittää sitä myös graafeina. 
1. [Numpy](https://numpy.org/) on kirjasto numeroiden käsittelyyn Pythonilla.
1. [Scikit-learn](https://scikit-learn.org/stable/) on kirjasto metriikoiden laskemiseen ja tulostamiseen datasta.
1. [Matplotlib](https://matplotlib.org/) on kirjasto datasettien visualisointiin.
1. [Google Colaboratory](https://colab.research.google.com/notebooks/intro.ipynb) on selaimessa pyörivä ympäristö, jossa voi ajaa yllä kuvattuja työkaluja asentamatta niitä itse. Colaboratoryssä tehtyjä Notebookkeja voi jakaa Google driven kautta helposti muille. 
1. [Ibm:n Watson Assistant](https://www.ibm.com/cloud/watson-assistant/) on esimerkiksi yksi koneoppimiseen perustuva helposti käytettävä ja kehittynyt luonnollisen kielen tulkintaan keskittyvä palvelu, jonka voi konfiguroida omiin tarpeisiinsa jopa ilman ohjelmointitaitoja.

Jos yllä olevat koneoppimiskirjastot haluaa asentaa oikeasti omalle koneelleen, eikä vain pyörittää niitä selaimessa, niin esimerkiksi [tässä blogissa](https://medium.com/@margaretmz/anaconda-jupyter-notebook-tensorflow-and-keras-b91f381405f8) on siihen hyvät ohjeet.

Yleisesti on todettava, että koneoppimiskirjastojen rajapinnat eivät ole vielä valitettavasti kehittyneet aivan yhtä korkealle abstraktiotasolle (ja helppokäyttöisiksi) kuin esimerkikiksi webohjelmointiin liittyvät kirjastot. Kuten muussakin ohjelmoinnissa, hyvä tapa lähteä liikkeelle koneoppimismallien rakentamisessa on pyrkiä etsimään esimerkki, joka tekee melkein saman asian jota itse yrittää tehdä ja sitten muokata esimerkkiä omiin tarpeisiin sopivaksi. Internetistä löytyy paljon esimerkiksi Googlen Colaboratoryllä tehtyjä esimerkkipohjia erilaisiin koneoppimisskenaarioihin.

Tällä kurssilla havainnollistetaan koneoppimista käytännössä seuraavien Colaboratory notebookkien avulla:

1. [Pandas-kirjaston perusteet](https://colab.research.google.com/notebooks/mlcc/intro_to_pandas.ipynb#scrollTo=av6RYOraVG1V) <!--datasettinä https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv-->
1. [TensorFlow:n peruskäsitteet](https://colab.research.google.com/notebooks/mlcc/tensorflow_programming_concepts.ipynb)
1. [Lineaarisen mallin rakentamienn TensorFlow 1:lla](https://colab.research.google.com/drive/1gdnOajkVQ66tupq5peMEDoQE3ubkgOl6#scrollTo=ajVM7rkoYXeL)
1. [Neuroverkon rakentaminen TensoFlow 1:lla](https://colab.research.google.com/notebooks/mlcc/intro_to_neural_nets.ipynb#scrollTo=AGOM1TUiKNdz)

Lisäksi sivutaan lyhyesti näitä esimerkkiä:
1. [Kuvadatan käsittelyä Keraksella ja TensorFlow2:lla](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb) ja [tämä on toinen ehkä vielä parempi step-by-step tutoriaali kuvadatasta ja Keraksesta](https://codelabs.developers.google.com/codelabs/tensorflow-lab2-computervision/#0)
1. [Facebookin detectron kuvantunnistuskirjaston käyttämistä käytännössä](https://colab.research.google.com/drive/16jcaJoc6bCFAQ96jDe2HwtXj7BMD_-m5)
1. [Kuvadatasta kissojen ja koirien tunnistamista](https://colab.research.google.com/github/google/eng-edu/blob/master/ml/pc/exercises/image_classification_part1.ipynb)
1. [Kasvojentunnistusta kuvista](https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/05.14-Image-Features.ipynb)

Koneoppimista voi opiskella lisää esimerkiksi Googlen [Machine Learning Crash Coursella](https://developers.google.com/machine-learning/crash-course/).


## Tehtävät

### Seminaaritehtävä 1 (täydennetään seminaarivaiheessa):
Kouluta koneoppimismalli jostain datasta ja laadi sillä ennusteita. Voi liittyä ohjelmistoprojekti 2:seen mieluusti.

### Lähteet:
* Kananen H., Puolitaival H., Tekoäly bisneksen uudet työkalut, Alma Talent, 2019.
