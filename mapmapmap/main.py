import folium

goroda_geroi = folium.Map(
    location = [64.6863136, 97.7453061],    # широта и долгота России
    zoom_start = 4
)
saint_petersburg = folium.map.FeatureGroup()
saint_petersburg.add_child(
    folium.features.CircleMarker(
        [59.938676, 30.314494], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)
moscow = folium.map.FeatureGroup()
moscow.add_child(
    folium.features.CircleMarker(
        [55.755819, 37.617644], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)
volgograd = folium.map.FeatureGroup()
volgograd.add_child(
    folium.features.CircleMarker(
        [48.707067, 44.516975], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)
kiev = folium.map.FeatureGroup()
kiev.add_child(
    folium.features.CircleMarker(
        [50.450441, 30.523550], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)
odessa = folium.map.FeatureGroup()
odessa.add_child(
    folium.features.CircleMarker(
        [46.484213, 30.731689], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)
sevastopol = folium.map.FeatureGroup()
sevastopol.add_child(
    folium.features.CircleMarker(
        [44.616020, 33.524471], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)
novorossisk = folium.map.FeatureGroup()
novorossisk.add_child(
    folium.features.CircleMarker(
        [44.723771, 37.768813], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)
kerch = folium.map.FeatureGroup()
kerch.add_child(
    folium.features.CircleMarker(
        [45.356219, 36.467378], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)
minsk = folium.map.FeatureGroup()
minsk.add_child(
    folium.features.CircleMarker(
        [53.902284, 27.561831], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)
tula = folium.map.FeatureGroup()
tula.add_child(
    folium.features.CircleMarker(
        [54.193122, 37.617348], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)
murmansk = folium.map.FeatureGroup()
murmansk.add_child(
    folium.features.Marker(
         [68.970663, 33.074918], tooltip = 'Мурманск'
    )
)
smolensk = folium.map.FeatureGroup()
smolensk.add_child(
    folium.features.CircleMarker(
        [54.782495, 32.048054], radius = 5, tooltip = 'Смоленск', # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)
spisokgg = [moscow, saint_petersburg, volgograd, kiev, odessa, sevastopol, novorossisk, kerch, minsk, tula, murmansk, smolensk]
# add the feature group to the map  (добавить группу объектов на карту)
for i in spisokgg:
    goroda_geroi.add_child(i)
goroda_geroi.save('name.html')


#################################################################################################
goroda_vs = folium.Map(
    location = [64.6863136, 97.7453061],    # широта и долгота России
    zoom_start = 4
)
belgo = folium.map.FeatureGroup()
belgo.add_child(
    folium.features.CircleMarker(
        [50.36, 36.36], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)
kursk = folium.map.FeatureGroup()
kursk.add_child(
    folium.features.CircleMarker(
        [51.43, 36.11], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)
orel = folium.map.FeatureGroup()
orel.add_child(
    folium.features.CircleMarker(
        [52.58, 36.05], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)
vladikavkaz = folium.map.FeatureGroup()
vladikavkaz.add_child(
    folium.features.CircleMarker(
        [43.01, 44.41], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

malgo = folium.map.FeatureGroup()
malgo.add_child(
    folium.features.CircleMarker(
        [43.3032, 44.3508], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

rghev = folium.map.FeatureGroup()
rghev.add_child(
    folium.features.CircleMarker(
        [56.1556, 34.1939], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)
elnya = folium.map.FeatureGroup()
elnya.add_child(
    folium.features.CircleMarker(
        [54.34, 33.10], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)
elec = folium.map.FeatureGroup()
elec.add_child(
    folium.features.CircleMarker(
        [52.37, 38.28], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

voroneg = folium.map.FeatureGroup()
voroneg.add_child(
    folium.features.CircleMarker(
        [51.4018, 39.1238], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

luga = folium.map.FeatureGroup()
luga.add_child(
    folium.features.CircleMarker(
        [58.44, 29.51], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

polarn = folium.map.FeatureGroup()
polarn.add_child(
    folium.features.CircleMarker(
        [69.1154, 33.2722], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

rost_na_don = folium.map.FeatureGroup()
rost_na_don.add_child(
    folium.features.CircleMarker(
        [47.1426, 39.4238], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

tuapse = folium.map.FeatureGroup()
tuapse.add_child(
    folium.features.CircleMarker(
        [44.06, 39.05], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

velluki = folium.map.FeatureGroup()
velluki.add_child(
    folium.features.CircleMarker(
        [56.2024, 30.3148], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

velnovg = folium.map.FeatureGroup()
velnovg.add_child(
    folium.features.CircleMarker(
        [58.3130, 31.1630], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

dmitr = folium.map.FeatureGroup()
dmitr.add_child(
    folium.features.CircleMarker(
        [56.3448, 37.5204], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

vazm = folium.map.FeatureGroup()
vazm.add_child(
    folium.features.CircleMarker(
        [55.1237,34.1706], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

kronsht = folium.map.FeatureGroup()
kronsht.add_child(
    folium.features.CircleMarker(
        [60, 29.46], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

narfom = folium.map.FeatureGroup()
narfom.add_child(
    folium.features.CircleMarker(
        [55.23,36.44], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

pskov = folium.map.FeatureGroup()
pskov.add_child(
    folium.features.CircleMarker(
        [57.49, 28.20], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

kozel = folium.map.FeatureGroup()
kozel.add_child(
    folium.features.CircleMarker(
        [52.0214, 35.4617], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

arh = folium.map.FeatureGroup()
arh.add_child(
    folium.features.CircleMarker(
        [64.33, 40.32], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

volokol = folium.map.FeatureGroup()
volokol.add_child(
    folium.features.CircleMarker(
        [56.02, 35.5809], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

bransk = folium.map.FeatureGroup()
bransk.add_child(
    folium.features.CircleMarker(
        [53.15, 34.22], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

nalch = folium.map.FeatureGroup()
nalch.add_child(
    folium.features.CircleMarker(
        [43.2907, 43.3625], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

viborg = folium.map.FeatureGroup()
viborg.add_child(
    folium.features.CircleMarker(
        [60.4238, 28.4459], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

kalnadon = folium.map.FeatureGroup()
kalnadon.add_child(
    folium.features.CircleMarker(
        [48.41, 43.32], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

vladivost = folium.map.FeatureGroup()
vladivost.add_child(
    folium.features.CircleMarker(
        [43.0654, 131.5307], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

tihvin = folium.map.FeatureGroup()
tihvin.add_child(
    folium.features.CircleMarker(
        [59.3839, 33.3232], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

tver = folium.map.FeatureGroup()
tver.add_child(
    folium.features.CircleMarker(
        [56.5128, 35.5518], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

anapa = folium.map.FeatureGroup()
anapa.add_child(
    folium.features.CircleMarker(
        [44.5338, 37.1903], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

kolpino = folium.map.FeatureGroup()
kolpino.add_child(
    folium.features.CircleMarker(
        [59.45, 30.36], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

stosk = folium.map.FeatureGroup()
stosk.add_child(
    folium.features.CircleMarker(
        [51.1753, 37.5006], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

kovrov = folium.map.FeatureGroup()
kovrov.add_child(
    folium.features.CircleMarker(
        [56.2138, 41.1911], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

lomon = folium.map.FeatureGroup()
lomon.add_child(
    folium.features.CircleMarker(
        [59.5439, 29.4635], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

petropavkam = folium.map.FeatureGroup()
petropavkam.add_child(
    folium.features.CircleMarker(
        [53.01, 158.39], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

tangarog = folium.map.FeatureGroup()
tangarog.add_child(
    folium.features.CircleMarker(
        [47.14, 38.54], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

maloyar = folium.map.FeatureGroup()
maloyar.add_child(
    folium.features.CircleMarker(
        [55.0052, 36.2818], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

mogh = folium.map.FeatureGroup()
mogh.add_child(
    folium.features.CircleMarker(
        [55.30, 36.02], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

habar = folium.map.FeatureGroup()
habar.add_child(
    folium.features.CircleMarker(
        [48.2812, 135.0524], radius = 5,  # широта и долгота Санкт-Петербурга
        ccolor = 'red', fill_color = 'Red'
    )
)

strussa = folium.map.FeatureGroup()
strussa.add_child(
    folium.features.CircleMarker(
        [57.5939, 31.2138], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

grozn = folium.map.FeatureGroup()
grozn.add_child(
    folium.features.CircleMarker(
        [43.19, 45.42], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

gatch = folium.map.FeatureGroup()
gatch.add_child(
    folium.features.CircleMarker(
        [59.5764, 30.1283], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

petrozav = folium.map.FeatureGroup()
petrozav.add_child(
    folium.features.CircleMarker(
        [61.4648, 34.21], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

feodos = folium.map.FeatureGroup()
feodos.add_child(
    folium.features.CircleMarker(
        [45.0368, 35.3779], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

meriupol = folium.map.FeatureGroup()
meriupol.add_child(
    folium.features.CircleMarker(
        [47.0750, 37.3350], radius = 5,  # широта и долгота Санкт-Петербурга
        color = 'red', fill_color = 'Red'
    )
)

melit = folium.map.FeatureGroup()
melit.add_child(
    folium.features.CircleMarker(
        [46.8489, 35.3653], radius = 5,
        color = 'red', fill_color = 'Red'
    )
)
spisokvs = [belgo, kursk, orel, vladikavkaz, malgo, rghev, elnya, elec, voroneg, luga, polarn, rost_na_don, tuapse, velluki, velnovg, dmitr, vazm, kronsht, narfom, pskov, kozel, arh, volokol, bransk, nalch, viborg, kalnadon, vladivost, tihvin, tver, anapa, kolpino, stosk, kovrov, lomon, petropavkam, tangarog, maloyar, mogh, habar, strussa, grozn, gatch, petrozav, feodos, meriupol, melit]
# add the feature group to the map  (добавить группу объектов на карту)
#sdfghjkl;lkjhgvfcx
for i in spisokvs:
    goroda_vs.add_child(i)
goroda_vs.save('vs.html')