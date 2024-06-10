import folium

goroda_geroi = folium.Map(
    location = [64.6863136, 97.7453061],    # широта и долгота России
    zoom_start = 4
)
saint_petersburg = folium.map.FeatureGroup()
saint_petersburg.add_child(
    folium.features.Marker(
        [59.938676, 30.314494], popup = "ЛЕНИНГРАД. 8 мая 1965 Санкт-Петербург получил почетное звание города героя.", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)
moscow = folium.map.FeatureGroup()
moscow.add_child(
    folium.features.Marker(
        [55.755819, 37.617644], popup = "МОСКВА. 8 мая 1965 Москва получила почетное звание города героя.", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)
volgograd = folium.map.FeatureGroup()
volgograd.add_child(
    folium.features.Marker(
        [48.707067, 44.516975], popup = "ВОЛГОГРАД. 8 мая 1965 Волгоград получил почетное звание города героя.", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)
kiev = folium.map.FeatureGroup()
kiev.add_child(
    folium.features.Marker(
        [50.450441, 30.523550], popup = "КИЕВ. 8 мая 1965 Киев получил почетное звание города героя.", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)
odessa = folium.map.FeatureGroup()
odessa.add_child(
    folium.features.Marker(
        [46.484213, 30.731689], popup = "ОДЕССА. 8 мая 1965 Одесса получил почетное звание города героя.", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)
sevastopol = folium.map.FeatureGroup()
sevastopol.add_child(
    folium.features.Marker(
        [44.616020, 33.524471], popup = "СЕВАСТОПОЛЬ. 8 мая 1965 Севастополь получил почетное звание города героя.", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)
novorossisk = folium.map.FeatureGroup()
novorossisk.add_child(
    folium.features.Marker(
        [44.723771, 37.768813], popup = "НОВОРОССИЙСК. 14 сентября 1973 Новороссийск получил почетное звание города героя.", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)
kerch = folium.map.FeatureGroup()
kerch.add_child(
    folium.features.Marker(
        [45.356219, 36.467378], popup = "КЕРЧЬ. 14 сентября 1973 Керчь получил почетное звание города героя.", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)
minsk = folium.map.FeatureGroup()
minsk.add_child(
    folium.features.Marker(
        [53.902284, 27.561831], popup = "МИНСК. 26 июня 1974 Минск получил почетное звание города героя.", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)
tula = folium.map.FeatureGroup()
tula.add_child(
    folium.features.Marker(
        [54.193122, 37.617348], popup = "ТУЛА. 7 декабря 1976 Тула получил почетное звание города героя.", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)
murmansk = folium.map.FeatureGroup()
murmansk.add_child(
    folium.features.Marker(
         [68.970663, 33.074918], popup = "МУРМАНСК. 6 мая 1985 Мурманск получил почетное звание города героя.", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)
smolensk = folium.map.FeatureGroup()
smolensk.add_child(
    folium.features.Marker(
        [54.782495, 32.048054],  popup = "СМОЛЕНСК. 6 мая 1985 Смоленск получил почетное звание города героя.", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)
spisokgg = [moscow, saint_petersburg, volgograd, kiev, odessa, sevastopol, novorossisk, kerch, minsk, tula, murmansk, smolensk]
# add the feature group to the map  (добавить группу объектов на карту)
for i in spisokgg:
    goroda_geroi.add_child(i)
goroda_geroi.save('gp.html')


#################################################################################################
goroda_vs = folium.Map(
    location = [64.6863136, 97.7453061],    # широта и долгота России
    zoom_start = 4
)
belgo = folium.map.FeatureGroup()
belgo.add_child(
    folium.features.Marker(
        [50.595414, 36.587277],  popup = "БЕЛГОРОД. 27 апреля 2007 Белгород получил почетное звание города воинской славы", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)
kursk = folium.map.FeatureGroup()
kursk.add_child(
    folium.features.Marker(
        [51.730846, 36.193015], popup = "КУРСК. 27 апреля 2007 Курск получил почетное звание города воинской славы", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)
orel = folium.map.FeatureGroup()
orel.add_child(
    folium.features.Marker(
        [52.970756, 36.064358], popup = "ОРЁЛ. 27 апреля 2007 Орёл получил почетное звание города воинской славы", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)
vladikavkaz = folium.map.FeatureGroup()
vladikavkaz.add_child(
    folium.features.Marker(
        [43.024616, 44.681771], popup = "ВЛАДИКАВКАЗ. 8 октября 2007 Владикавказ получил почетное звание города воинской славы", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)

malgo = folium.map.FeatureGroup()
malgo.add_child(
    folium.features.Marker(
        [43.509318, 44.585723], popup = "МАЛГОБЕК. 8 октября 2007 Малгобек получил почетное звание города воинской славы", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)

rghev = folium.map.FeatureGroup()
rghev.add_child(
    folium.features.Marker(
        [56.263017, 34.334419], popup = "РЖЕВ. 8 октября 2007 Ржев получил почетное звание города воинской славы", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)
elnya = folium.map.FeatureGroup()
elnya.add_child(
    folium.features.Marker(
        [54.575911, 33.182743], popup = "ЕЛЬНЯ. 8 октября 2007 город Ельня получил почетное звание города воинской славы", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)
elec = folium.map.FeatureGroup()
elec.add_child(
    folium.features.Marker(
        [52.621938, 38.500446], popup = "ЕЛЕЦ. 8 октября 2007 Елец получил почетное звание города воинской славы", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)

voroneg = folium.map.FeatureGroup()
voroneg.add_child(
    folium.features.Marker(
        [51.660781, 39.200296],  popup = "ВОРОНЕЖ. 16 февраля 2008 Воронеж получил почетное звание города воинской славы", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)

luga = folium.map.FeatureGroup()
luga.add_child(
    folium.features.Marker(
        [58.735207, 29.847945], popup = "ЛУГА. 5 мая 2008 Луга получил почетное звание города воинской славы", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)

polarn = folium.map.FeatureGroup()
polarn.add_child(
    folium.features.Marker(
        [69.197402, 33.437235], popup = "ПОЛЯРНЫЙ. 5 мая 2008 Полярный получил почетное звание города воинской славы", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)

rost_na_don = folium.map.FeatureGroup()
rost_na_don.add_child(
    folium.features.Marker(
        [47.222109, 39.718813], popup = "РОСТОВ-НА-ДОНУ. 5 мая 2008 Ростов-на-Дону получил почетное звание города воинской славы", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
    )
)

tuapse = folium.map.FeatureGroup()
tuapse.add_child(
    folium.features.Marker(
        [44.095245, 39.073382], popup = "ТУАПСЕ. 5 мая 2008 Туапсе получил почетное звание города воинской славы", radius = 5,  # широта и долгота Санкт-Петербурга
        icon = folium.Icon(color = 'red')
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