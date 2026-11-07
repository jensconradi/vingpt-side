#!/usr/bin/env python3
"""Bygger forsidene (no, sv, en) + sitemap.xml + llms.txt fra én mal.
Kjør `python3 bygg.py` etter tekstendringer, commit resultatet. 06.11.2026."""
import datetime as dt, html, json
from pathlib import Path

ROT = Path(__file__).parent
IK = json.loads((ROT / "ikoner.json").read_text())
DOM = "https://vingpt.no"
NO_APP = "https://apps.apple.com/no/app/id6796675360?pt=129246957&ct=nettside&mt=8"
SE_APP = "https://apps.apple.com/se/app/id6821568888?pt=129246957&ct=nettside&mt=8"
NO_SKJERM = [("1-utforsk", "Hylla i din butikk, rangert", "Hovedskjermen: rødviner under 300 kr på hylla i din butikk, rangert etter vurdering"),
             ("4-sommelier", "Spør sommelieren om maten", "Sommelieren svarer med viner som står i din butikk"),
             ("3-vinkart", "Skann vinkartet på restauranten", "Vinkartet fotografert og rangert"),
             ("2-vinkort", "Vurdering, pris og lager per flaske", "Vinkortet med vurdering, pris og flasker på lager"),
             ("5-alkoholfritt", "Alkoholfritt, sortert på farge", "Alkoholfrie viner rangert"),
             ("6-butikk", "Velg butikken din", "Butikkvelgeren")]
SV_SKJERM = [("1-utforska", "Lagret i din butik, rankat", "Startskärmen: röda viner i lager i din butik, rankade efter betyg"),
             ("4-sommelier", "Fråga sommeliern om maten", "Sommeliern svarar med viner som finns i din butik"),
             ("3-vinlista", "Skanna vinlistan på restaurangen", "Vinlistan fotograferad och rankad"),
             ("2-vinkort", "Betyg, pris och lager per flaska", "Vinkortet med betyg, pris och flaskor i lager"),
             ("5-overraska", "Överraska mig", "Överraska mig-vyn")]
EN_SKJERM = [("1-utforsk", "Your store's shelf, ranked", "Home screen: red wines under 300 kr on the shelf of your store, ranked by rating"),
             ("4-sommelier", "Ask the sommelier about the food", "The sommelier answers with wines your store has in stock"),
             ("3-vinkart", "Scan the restaurant wine list", "A photographed wine list, ranked"),
             ("2-vinkort", "Rating, price and stock per bottle", "Wine card with rating, price and bottles in stock"),
             ("5-alkoholfritt", "Alcohol-free, sorted by colour", "Alcohol-free wines ranked"),
             ("6-butikk", "Pick your store", "The store picker")]

SIDER = {
"no": dict(
  sti="", lang="nb", locale="nb_NO", app=NO_APP, appid="6796675360", bilder="bilder/no", skjermer=NO_SKJERM, hjem="./",
  tittel="VinGPT — den beste vinen din polbutikk har inne",
  beskrivelse="Velg din Vinmonopol-butikk og se alt den har på hylla, rangert etter vurderinger fra tusenvis av vinelskere. Spør sommelieren på vanlig norsk. Skann vinkartet på restauranten. iPhone-app.",
  og_tittel="VinGPT — hva er den beste vinen din polbutikk har inne?",
  og_beskrivelse="Alt på hylla i din butikk, sortert etter hva tusenvis av folk faktisk synes. Spør: «rødvin til lam under 250 kr».",
  og_bilde="/godvin/kort.jpg",
  nav=[("#funksjoner", "Funksjoner"), ("#faq", "Spørsmål")],
  lofte="Hva er den beste vinen <em>din polbutikk</em> har inne?",
  ingress="Velg din Vinmonopol-butikk og se alt som står på hylla, rangert etter vurderinger fra tusenvis av andre vinelskere. Spør på vanlig norsk: «rødvin til lam under 250 kr». På restauranten: ta bilde av vinkartet.",
  knapp="Hent i App Store", krav="iPhone med iOS 17 eller nyere · sommelieren krever Apple Intelligence · <a href=\"mailto:support.vingpt@vingpt.no?subject=VinGPT%20p%C3%A5%20Android&amp;body=Si%20ifra%20hvis%20VinGPT%20kommer%20p%C3%A5%20Android.\">Android? Si ifra</a>",
  merker=["Hele butikkutvalget", "Flasketall live", "Sommelier på norsk", "Uavhengig av Vinmonopolet", "Også i Sverige"],
  funk_h="Hva kan VinGPT hjelpe med?", funk_i="Ikke hele Norge. Butikken du faktisk går til, og det som står der nå.",
  kort=[("Hylla i din butikk, rangert", "Det som står i butikken du går til, sortert etter vurdering. Filtrer på pris, vintype, land og hva maten er."),
        ("Flasketall live", "Trykk «Sjekk lager» og se hvor mange flasker butikken har akkurat nå. Utsolgt? Appen viser nærmeste butikk som har den."),
        ("Spør sommelieren", "«Noe godt til taco under 200?» Svaret er viner som står i din butikk, med begrunnelse per flaske. Kjører på telefonen, ingenting sendes bort."),
        ("Skann vinkartet", "Ta bilde av vinkartet på restauranten og se vinene rangert innenfor det du vil betale. Bildet leses på telefonen."),
        ("Alkoholfritt, sortert på farge", "Rødt, hvitt, rosé og bobler uten alkohol, rangert som alt annet. Slå på bryteren i avansert søk."),
        ("Favoritter uten konto", "Merk viner du vil huske. De følger din egen iCloud til neste telefon, uten innlogging.")],
  slik_h="Slik fungerer det",
  steg=[("Velg butikk", "Den du handler i, eller den nærmeste nå."), ("Se hylla rangert", "Topp ti først, resten på «Vis flere». Filtrer på pris og type."), ("Spør eller skann", "Still et spørsmål til sommelieren, eller ta bilde av vinkartet.")],
  se_h="Se appen",
  galleri=[("1-utforsk", "Hovedskjermen: rødviner under 300 kr på hylla i din butikk, rangert etter vurdering"), ("4-sommelier", "Sommelieren svarer på «rødvin til biff under 300 kr» med viner fra din butikk"), ("3-vinkart", "Skannet vinkart fra en restaurant, rangert etter vurdering innenfor prisramme"), ("5-alkoholfritt", "Alkoholfrie viner sortert på rødt, hvitt, rosé og bobler")],
  band_h="Neste gang du står på polet", band_p="Åpne appen, velg butikken, se hva som er best på hylla.",
  faq_h="Vanlige spørsmål",
  faq=[("Hvor kommer vurderingene fra?", "Fra tusenvis av vanlige vindrikkere som har gitt vinen en karakter, ikke fra én anmelder. Appen viser snittet og hvor mange som står bak det, og viser aldri et tall den ikke har."),
       ("Hvorfor viser appen en annen beholdning enn butikken har?", "Lagerlisten («hvilke varer fører butikken») caches i inntil ett døgn og merkes med når den sist ble sjekket. <strong>Flasketall</strong> hentes derimot alltid live når du trykker «Sjekk lager» på en vin. Dra ned i listen for å oppdatere hele lagerlisten."),
       ("Hvorfor mangler en vin vurdering?", "Vurderinger finnes for de mest omsatte vinene i butikkutvalget. Viner i bestillingsutvalget og helt ferske årganger kan mangle — appen viser da «Ingen vurdering funnet» i stedet for å gjette."),
       ("Sommelieren svarte rart eller feil", "Sommelieren kjører på Apples språkmodell på telefonen (krever iPhone 15 Pro eller nyere med Apple Intelligence). Den kan kun anbefale varer som faktisk finnes i sortimentet, og begrunnelsene ved hver vin kommer fra Vinmonopolets egne beskrivelser. Blir et svar likevel feil, trykk tommel ned og fortell hva som var galt — det hjelper oss mye."),
       ("Krever appen konto?", "Nei. Ingen innlogging, ingen registrering. Favoritter følger din egen iCloud automatisk."),
       ("Er VinGPT en del av Vinmonopolet?", "Nei. VinGPT er en uavhengig app uten tilknytning til Vinmonopolet. Appen selger ikke alkohol og har ingen kjøpsfunksjon."),
       ("Finnes appen i Sverige?", "Ja, med Systembolagets butikker: <a href=\"sv/\">VinGPT för Sverige</a>."),
       ("Finnes appen på Android?", "Ikke ennå, bare iPhone. Vil du ha den på Android? <a href=\"mailto:support.vingpt@vingpt.no?subject=VinGPT%20p%C3%A5%20Android&amp;body=Si%20ifra%20hvis%20VinGPT%20kommer%20p%C3%A5%20Android.\">Si ifra på e-post</a>, så gir vi beskjed hvis den kommer. Det hjelper oss også å se om det er verdt å lage."),
       ("Utgiver", "VinGPT utgis av Siphon AS (org.nr. 998 610 672), Jacob Aalls gate 14A, 0368 Oslo."),
       ("Kontakt", "Tilbakemeldinger og feilrapporter: <a href=\"mailto:support.vingpt@vingpt.no\">support.vingpt@vingpt.no</a><br>(eller bruk «Send tilbakemelding» i appen — da følger versjon og katalogdato med automatisk).")],
  bunn=[("personvern/", "Personvernerklæring")], bunn_tekst="VinGPT er uavhengig av Vinmonopolet og selger ikke alkohol.",
  org_navn="VinGPT", land="NO", kategori="LifestyleApplication",
),
"sv": dict(
  sti="sv/", lang="sv", locale="sv_SE", app=SE_APP, appid="6821568888", bilder="../bilder/sv", skjermer=SV_SKJERM, hjem="./",
  tittel="VinGPT — det bästa vinet i lager på ditt Systembolag",
  beskrivelse="Välj din Systembolagsbutik och se vinerna i lager där, rankade efter betyg från tusentals vinälskare. Fråga sommeliern på vanlig svenska. Fotografera vinlistan på restaurangen. iPhone-app.",
  og_tittel="VinGPT — vilket är det bästa vinet i lager på ditt Systembolag?",
  og_beskrivelse="Allt i lager i din butik, sorterat efter vad tusentals människor faktiskt tycker. Fråga: ”rött vin till lamm under 150 kr”.",
  og_bilde="/bilder/sv/1-utforska.jpg",
  nav=[("#funksjoner", "Funktioner"), ("#faq", "Frågor")],
  lofte="Vilket är det bästa vinet i lager <em>på ditt Systembolag</em>?",
  ingress="Välj din Systembolagsbutik och se vinerna som finns i lager där, rankade efter betyg från tusentals andra vinälskare. Fråga på vanlig svenska: ”rött vin till lamm under 150 kr”. På restaurangen: fotografera vinlistan.",
  knapp="Hämta i App Store", krav="iPhone med iOS 17 eller senare · sommeliern kräver Apple Intelligence · <a href=\"mailto:support.vingpt@vingpt.no?subject=VinGPT%20p%C3%A5%20Android&amp;body=S%C3%A4g%20till%20om%20VinGPT%20kommer%20p%C3%A5%20Android.\">Android? Säg till</a>",
  merker=["Hela butikssortimentet", "Lager direkt", "Sommelier på svenska", "Oberoende av Systembolaget", "Även i Norge"],
  funk_h="Vad kan VinGPT hjälpa till med?", funk_i="Inte hela Sverige. Butiken du faktiskt går till, och det som finns där nu.",
  kort=[("Lagret i din butik, rankat", "Det som finns i butiken du går till, sorterat efter betyg. Filtrera på pris, vintyp, land och vad du ska äta."),
        ("Lager direkt", "Tryck ”Kolla lager” och se hur många flaskor butiken har just nu. Slut? Appen visar butiker i närheten som har vinet."),
        ("Fråga sommeliern", "”Något gott till tacos under 120 kr?” Svaret är viner som finns i din butik, med motivering per flaska. Körs i telefonen, inget skickas iväg."),
        ("Skanna vinlistan", "Fotografera vinlistan på restaurangen och se vinerna rankade inom det du vill betala. Bilden läses i telefonen."),
        ("Alkoholfritt, sorterat på färg", "Rött, vitt och rosé utan alkohol, rankat som allt annat. Slå på knappen i avancerad sökning."),
        ("Favoriter utan konto", "Markera viner du vill komma ihåg. De följer ditt eget iCloud till nästa telefon, utan inloggning.")],
  slik_h="Så fungerar det",
  steg=[("Välj butik", "Den du handlar i, eller den närmaste just nu."), ("Se lagret rankat", "Topp tio först, resten under ”Visa fler”. Filtrera på pris och typ."), ("Fråga eller skanna", "Ställ en fråga till sommeliern, eller fotografera vinlistan.")],
  se_h="Se appen",
  galleri=[("1-utforska", "Startskärmen: röda viner i lager i din butik, rankade efter betyg"), ("4-sommelier", "Sommeliern svarar på ”nötkött, kraftigt och fylligt” med viner från din butik"), ("3-vinlista", "Skannad vinlista från en restaurang, rankad efter betyg inom prisklass"), ("5-overraska", "Överraska mig: ett slumpat vin bland de bäst betygsatta i lager i din butik")],
  band_h="Nästa gång du står på Systembolaget", band_p="Öppna appen, välj butiken, se vad som är bäst i lager.",
  faq_h="Vanliga frågor",
  faq=[("Varifrån kommer betygen?", "Från tusentals vanliga vindrickare som har betygsatt vinet, inte från en enskild recensent. Appen visar snittet och hur många som står bakom det, och visar aldrig en siffra den inte har."),
       ("Varför visar appen ett annat lager än butiken har?", "Lagerlistan (vilka viner butiken har i lager) uppdateras löpande och visar när den senast kollades. Listan säger om ett vin finns i lager, men inte hur många flaskor. <strong>Antalet flaskor</strong> hämtas direkt från Systembolaget när du trycker ”Kolla lager” på vinkortet. Dra nedåt i listan för att uppdatera lagerlistan."),
       ("Varför saknar ett vin betyg?", "Betyg finns för de flesta viner i butikernas sortiment. Viner i beställningssortimentet och helt nya årgångar kan sakna betyg — då står det att vinet saknar betyg, i stället för att appen gissar."),
       ("Sommeliern svarade konstigt eller fel", "Sommeliern använder Apples språkmodell direkt på telefonen (kräver iPhone 15 Pro eller senare med Apple Intelligence). Den kan bara föreslå viner som finns i Systembolagets sortiment, och motiveringen vid varje vin kommer från Systembolagets egna beskrivningar. Blir ett svar ändå fel, tryck tummen ned och berätta vad som blev fel — det hjälper oss mycket."),
       ("Behöver jag ett konto?", "Nej. Ingen inloggning och ingen registrering. Favoriter följer ditt eget iCloud automatiskt."),
       ("Är VinGPT en del av Systembolaget?", "Nej. VinGPT är en fristående app som inte är ansluten till Systembolaget. Appen säljer inte alkohol och har ingen köpfunktion."),
       ("Finns appen i Norge?", "Ja, med Vinmonopolets butiker: <a href=\"../\">VinGPT for Norge</a>."),
       ("Finns appen för Android?", "Inte än, bara för iPhone. Vill du ha den på Android? <a href=\"mailto:support.vingpt@vingpt.no?subject=VinGPT%20p%C3%A5%20Android&amp;body=S%C3%A4g%20till%20om%20VinGPT%20kommer%20p%C3%A5%20Android.\">Säg till via e-post</a>, så hör vi av oss om den kommer. Det hjälper oss också att se om det är värt att bygga."),
       ("Utgivare", "VinGPT ges ut av Siphon AS (org.nr. 998 610 672), Jacob Aalls gate 14A, 0368 Oslo, Norge."),
       ("Kontakt", "Feedback och felrapporter: <a href=\"mailto:support.vingpt@vingpt.no\">support.vingpt@vingpt.no</a><br>(eller använd ”Skicka feedback” i appen — då följer version och katalogdatum med automatiskt).")],
  bunn=[("integritet/", "Integritetspolicy")], bunn_tekst="VinGPT är oberoende av Systembolaget och säljer inte alkohol.",
  org_navn="VinGPT", land="SE", kategori="LifestyleApplication",
),
"en": dict(
  sti="en/", lang="en", locale="en_GB", app=NO_APP, appid="6796675360", bilder="../bilder/no", skjermer=EN_SKJERM, hjem="./",
  tittel="VinGPT — the best wine your Vinmonopolet or Systembolaget store has in stock",
  beskrivelse="Pick your Vinmonopolet (Norway) or Systembolaget (Sweden) store and see everything on its shelf, ranked by ratings from thousands of wine lovers. Ask the on-device sommelier, scan a restaurant wine list. iPhone app.",
  og_tittel="VinGPT — what is the best wine your local Vinmonopolet or Systembolaget has in stock?",
  og_beskrivelse="Everything on the shelf of your store, ranked by what thousands of people actually think. Ask: “red wine for lamb under 250 kr”.",
  og_bilde="/godvin/kort.jpg",
  nav=[("#funksjoner", "Features"), ("#faq", "FAQ")],
  lofte="What is the best wine <em>your local store</em> has in stock?",
  ingress="Pick your Vinmonopolet store in Norway or Systembolaget store in Sweden and see everything on the shelf, ranked by ratings from thousands of other wine lovers. Ask in plain language: “red wine for lamb under 250 kr”. At the restaurant: photograph the wine list.",
  knapp="Get it on the App Store", krav="iPhone with iOS 17 or later · the sommelier needs Apple Intelligence · app interface in Norwegian (Norway) or Swedish (Sweden) · <a href=\"mailto:support.vingpt@vingpt.no?subject=VinGPT%20on%20Android&amp;body=Let%20me%20know%20if%20VinGPT%20comes%20to%20Android.\">Android? Tell us</a>",
  merker=["The whole store range", "Live bottle counts", "On-device sommelier", "Independent of the monopolies", "Norway and Sweden"],
  funk_h="What VinGPT helps with", funk_i="Not the whole country. The store you actually go to, and what is on its shelf right now.",
  kort=[("Your store's shelf, ranked", "What is in the store you go to, sorted by rating. Filter by price, wine type, country and what you are eating."),
        ("Live bottle counts", "Tap “Check stock” to see how many bottles the store has right now. Sold out? The app shows the nearest store that has it."),
        ("Ask the sommelier", "“Something good for tacos under 200?” The answer is wines that are in your store, with a reason per bottle. Runs on the phone, nothing is sent anywhere."),
        ("Scan the wine list", "Photograph the restaurant's wine list and see the wines ranked within what you want to pay. The image is read on the phone."),
        ("Alcohol-free, sorted by colour", "Red, white, rosé and sparkling without alcohol, ranked like everything else. Flip the switch in advanced search."),
        ("Favourites without an account", "Mark wines you want to remember. They follow your own iCloud to your next phone, no sign-in.")],
  slik_h="How it works",
  steg=[("Pick a store", "The one you shop in, or the nearest right now."), ("See the shelf ranked", "Top ten first, the rest under “Show more”. Filter by price and type."), ("Ask or scan", "Ask the sommelier a question, or photograph the wine list.")],
  se_h="See the app",
  galleri=[("1-utforsk", "Home screen: red wines under 300 kr on the shelf of your store, ranked by rating"), ("4-sommelier", "The sommelier answering “red wine for steak under 300 kr” with wines from your store"), ("3-vinkart", "A scanned restaurant wine list, ranked by rating within a price range"), ("5-alkoholfritt", "Alcohol-free wines sorted into red, white, rosé and sparkling")],
  band_h="Next time you are at the store", band_p="Open the app, pick the store, see what is best on the shelf.",
  faq_h="Frequently asked questions",
  faq=[("Which countries does VinGPT work in?", "Norway, with every Vinmonopolet store, and Sweden, with every Systembolaget store. They are two separate apps on the App Store: <a href=\"" + NO_APP + "\">VinGPT for Norway</a> (Norwegian interface) and <a href=\"" + SE_APP + "\">VinGPT for Sweden</a> (Swedish interface). Wine names, ratings and prices are the same whatever language you speak."),
       ("Where do the ratings come from?", "From thousands of ordinary wine drinkers who have rated the wine, not from a single critic. The app shows the average and how many people stand behind it, and never shows a number it does not have."),
       ("Why does the app show different stock than the store has?", "The stock list (which wines the store carries) is cached for up to a day and marked with when it was last checked. <strong>Bottle counts</strong>, however, are always fetched live when you tap “Check stock” on a wine. Pull down the list to refresh the whole stock list."),
       ("Why does a wine have no rating?", "Ratings exist for the most sold wines in the store range. Wines in the order-only range and brand-new vintages may lack one — the app then says “No rating found” instead of guessing."),
       ("The sommelier answered oddly or wrongly", "The sommelier runs on Apple's language model on the phone (needs iPhone 15 Pro or later with Apple Intelligence). It can only recommend products that actually exist in the range, and the reasoning next to each wine comes from the monopoly's own descriptions. If an answer is still wrong, tap thumbs down and tell us what was off — it helps a lot."),
       ("Does the app need an account?", "No. No sign-in, no registration. Favourites follow your own iCloud automatically."),
       ("Is VinGPT part of Vinmonopolet or Systembolaget?", "No. VinGPT is an independent app with no ties to either monopoly. The app does not sell alcohol and has no purchase function."),
       ("Is there an Android version?", "Not yet, iPhone only. Want it on Android? <a href=\"mailto:support.vingpt@vingpt.no?subject=VinGPT%20on%20Android&amp;body=Let%20me%20know%20if%20VinGPT%20comes%20to%20Android.\">Tell us by email</a> and we will let you know if it happens. It also helps us see whether it is worth building."),
       ("Publisher", "VinGPT is published by Siphon AS (Norwegian org. no. 998 610 672), Jacob Aalls gate 14A, 0368 Oslo, Norway."),
       ("Contact", "Feedback and bug reports: <a href=\"mailto:support.vingpt@vingpt.no\">support.vingpt@vingpt.no</a><br>(or use “Send feedback” in the app — the version and catalogue date come along automatically).")],
  bunn=[("../personvern/", "Privacy policy (Norwegian)"), ("../sv/integritet/", "Privacy policy (Swedish)")], bunn_tekst="VinGPT is independent of Vinmonopolet and Systembolaget and does not sell alcohol.",
  org_navn="VinGPT", land="NO", kategori="LifestyleApplication",
),
}
SPRAK = [("no", "Norsk", ""), ("sv", "Svenska", "sv/"), ("en", "English", "en/")]


def rel(fra, til):
    """Relativ lenke fra sida `fra` (sti) til rotsti `til`."""
    return ("../" if fra else "") + til if til else ("../" if fra else "./")


def aktuell(ja):
    return ' aria-current="page"' if ja else ""


def skjerm_html(d):
    bilder = []
    prikker = []
    for i, (fil, tekst, alt) in enumerate(d["skjermer"]):
        ekstra = ' class="aktiv"' if i == 0 else ' loading="lazy"'
        bilder.append(f'<img src="{d["bilder"]}/{fil}.jpg" alt="{html.escape(alt)}" data-tekst="{html.escape(tekst)}"{ekstra}>')
        akt = ' class="aktiv"' if i == 0 else ""
        prikker.append(f'<button type="button" data-i="{i}" aria-label="{html.escape(tekst)}"{akt}></button>')
    return (f'<div class="telefon"><div class="skjermer">{"".join(bilder)}</div>'
            f'<p class="bildetekst" aria-live="polite">{html.escape(d["skjermer"][0][1])}</p>'
            f'<div class="prikker">{"".join(prikker)}</div></div>')


def jsonld(d):
    url = f"{DOM}/{d['sti']}"
    app = {
        "@context": "https://schema.org", "@type": "MobileApplication", "name": "VinGPT",
        "operatingSystem": "iOS 17", "applicationCategory": d["kategori"], "inLanguage": d["lang"],
        "url": url, "installUrl": d["app"], "description": d["beskrivelse"],
        "countriesSupported": "NO, SE", "image": DOM + d["og_bilde"],
        "author": {"@type": "Organization", "name": "Siphon AS", "address": {"@type": "PostalAddress", "streetAddress": "Jacob Aalls gate 14A", "postalCode": "0368", "addressLocality": "Oslo", "addressCountry": "NO"}, "email": "support.vingpt@vingpt.no"},
    }
    import re
    def ren(t): return html.unescape(re.sub(r"<[^>]+>", "", t))
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": d["lang"],
           "mainEntity": [{"@type": "Question", "name": ren(q), "acceptedAnswer": {"@type": "Answer", "text": ren(a)}} for q, a in d["faq"]]}
    return "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in (app, faq))


def bygg(kode):
    d = SIDER[kode]
    sti = d["sti"]
    css = ("../" if sti else "") + "felles.css?v=20261106c"
    url = f"{DOM}/{sti}"
    hreflang = "".join(f'<link rel="alternate" hreflang="{SIDER[k]["lang"]}" href="{DOM}/{SIDER[k]["sti"]}">\n' for k in SIDER)
    hreflang += f'<link rel="alternate" hreflang="x-default" href="{DOM}/en/">\n'
    nav_ankre = "".join(f'<a class="anker" href="{h}">{t}</a>' for h, t in d["nav"])
    sprak = "".join(
        f'<a lang="{SIDER[k]["lang"]}" hreflang="{SIDER[k]["lang"]}" href="{rel(sti, s)}"{aktuell(k == kode)}>{n}</a>'
        for k, n, s in SPRAK)
    merker = "".join(f"<li>{m}</li>" for m in d["merker"])
    kort = "".join(f'<div>{IK["kort"][i]}<h3>{h}</h3><p>{p}</p></div>' for i, (h, p) in enumerate(d["kort"]))
    steg = "".join(f"<li><strong>{h}</strong>{p}</li>" for h, p in d["steg"])
    galleri = "".join(f'<img src="{d["bilder"]}/{f}.jpg" alt="{html.escape(a)}" loading="lazy">\n' for f, a in d["galleri"])
    faq = "".join(f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in d["faq"])
    bunn = "".join(f'<a href="{h}">{t}</a> · ' for h, t in d["bunn"])
    bunn += " · ".join(f'<a href="{rel(sti, s)}" lang="{SIDER[k]["lang"]}">{n}</a>' for k, n, s in SPRAK if k != kode)
    knapp = f'<a class="appstore" href="{html.escape(d["app"])}">{IK["appstore"]}{d["knapp"]}</a>'
    return f"""<!doctype html>
<html lang="{d['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{d['tittel']}</title>
<meta name="description" content="{html.escape(d['beskrivelse'])}">
<link rel="canonical" href="{url}">
{hreflang}<meta property="og:title" content="{html.escape(d['og_tittel'])}">
<meta property="og:description" content="{html.escape(d['og_beskrivelse'])}">
<meta property="og:image" content="{DOM}{d['og_bilde']}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="{d['locale']}">
<meta property="og:site_name" content="VinGPT">
<meta name="twitter:card" content="summary_large_image">
<meta name="apple-itunes-app" content="app-id={d['appid']}, affiliate-data=pt=129246957&ct=smartbanner">
<meta name="theme-color" content="#150709">
<link rel="stylesheet" href="{css}">
{jsonld(d)}</head>
<body>
<main>

<div class="topp">
<a class="merke" href="{d['hjem']}">{IK['merke']}<span class="merkenavn">VinGPT</span></a>
<nav>{nav_ankre}<span class="sprak">{sprak}</span></nav>
</div>

<header class="hero">
<div>
<h1 class="lofte">{d['lofte']}</h1>
<p>{d['ingress']}</p>
{knapp}
<p class="krav">{d['krav']}</p>
<ul class="merker">{merker}</ul>
</div>
{skjerm_html(d)}
</header>

<section id="funksjoner">
<h2 class="seksjon">{d['funk_h']}</h2>
<p class="ingress">{d['funk_i']}</p>
<div class="kort">
{kort}
</div>
</section>

<section>
<h2 class="seksjon">{d['slik_h']}</h2>
<ol class="steg">
{steg}
</ol>
</section>

<section>
<h2 class="seksjon">{d['se_h']}</h2>
<div class="bilder">
{galleri}</div>
</section>

<section class="band">
<p class="lofte">{d['band_h']}</p>
<p>{d['band_p']}</p>
{knapp}
</section>

<section id="faq" class="faq">
<h2 class="seksjon">{d['faq_h']}</h2>
{faq}</section>

<footer>
{bunn}<br>
{d['bunn_tekst']}
</footer>
</main>
<script>
(function(){{var b=document.querySelectorAll(".skjermer img"),p=document.querySelectorAll(".prikker button"),t=document.querySelector(".bildetekst"),tel=document.querySelector(".telefon"),i=0,k;
if(b.length<2)return;
function vis(n){{b[i].classList.remove("aktiv");p[i].classList.remove("aktiv");i=n%b.length;b[i].classList.add("aktiv");p[i].classList.add("aktiv");t.textContent=b[i].dataset.tekst;}}
function start(){{if(!matchMedia("(prefers-reduced-motion: reduce)").matches)k=setInterval(function(){{vis(i+1)}},3500);}}
function stopp(){{clearInterval(k);}}
p.forEach(function(x){{x.addEventListener("click",function(){{stopp();vis(+x.dataset.i);start();}});}});
tel.addEventListener("mouseenter",stopp);tel.addEventListener("mouseleave",start);start();}})();
</script>
</body>
</html>
"""


def sitemap():
    i_dag = dt.date.today().isoformat()
    sider = [("", "nb"), ("sv/", "sv"), ("en/", "en"), ("personvern/", None), ("sv/integritet/", None)]
    ut = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for sti, lang in sider:
        ut.append(f"<url><loc>{DOM}/{sti}</loc><lastmod>{i_dag}</lastmod>")
        if lang:
            for k in SIDER:
                ut.append(f'<xhtml:link rel="alternate" hreflang="{SIDER[k]["lang"]}" href="{DOM}/{SIDER[k]["sti"]}"/>')
            ut.append(f'<xhtml:link rel="alternate" hreflang="x-default" href="{DOM}/en/"/>')
        ut.append("</url>")
    ut.append("</urlset>")
    return "\n".join(ut) + "\n"


LLMS = f"""# VinGPT

> VinGPT is an independent iPhone app that shows which wines a specific Vinmonopolet store (Norway) or Systembolaget store (Sweden) has on its shelf right now, ranked by ratings from thousands of wine drinkers, with live bottle counts, an on-device sommelier that answers questions like "red wine for lamb under 250 kr" using only wines that store carries, and a scanner that ranks a restaurant's wine list. It does not sell alcohol and is not affiliated with Vinmonopolet or Systembolaget.

Key facts
- No Android version yet; interested users can email support.vingpt@vingpt.no.
- Platform: iPhone, iOS 17 or later. The sommelier and wine-list scan use Apple Intelligence on the phone (iPhone 15 Pro or later); nothing is sent to a server.
- Two editions: Norway (Norwegian interface, all Vinmonopolet stores) and Sweden (Swedish interface, all Systembolaget stores). Same data model, same ratings.
- Ratings: average rating and number of ratings from thousands of ordinary wine drinkers; the app never shows a number it does not have.
- Stock: the store's stock list is cached up to a day and marked with its check time; bottle counts are fetched live on request.
- Filters: price, wine type, country, district, food pairing, alcohol-free (red, white, rosé, sparkling).
- No account, no sign-in. Favourites sync through the user's own iCloud.
- Telemetry is anonymous aggregated counters without any device identifier; see the privacy policy.
- Publisher: Siphon AS, org. no. 998 610 672, Jacob Aalls gate 14A, 0368 Oslo, Norway. Support: support.vingpt@vingpt.no

Pages
- Norwegian front page: {DOM}/
- Swedish front page: {DOM}/sv/
- English front page: {DOM}/en/
- Privacy policy (Norwegian): {DOM}/personvern/
- Privacy policy (Swedish): {DOM}/sv/integritet/
- App Store Norway: https://apps.apple.com/no/app/id6796675360
- App Store Sweden: https://apps.apple.com/se/app/id6821568888

Typical questions VinGPT answers
- What is the best red wine under 300 kr that my local Vinmonopolet store has in stock?
- Which wine on this restaurant wine list is the best value?
- Which alcohol-free sparkling wines does my Systembolaget store carry?
- Does the store near me have this wine, and how many bottles?
"""

ROBOTS = f"""User-agent: *
Allow: /

Sitemap: {DOM}/sitemap.xml
"""

if __name__ == "__main__":
    for kode in SIDER:
        ut = ROT / SIDER[kode]["sti"] / "index.html"
        ut.parent.mkdir(exist_ok=True)
        ut.write_text(bygg(kode))
        print("skrev", ut.relative_to(ROT))
    (ROT / "sitemap.xml").write_text(sitemap())
    (ROT / "llms.txt").write_text(LLMS)
    (ROT / "robots.txt").write_text(ROBOTS)
    print("skrev sitemap.xml, llms.txt, robots.txt")
