/* Besøkstelling for vingpt.no (22.11.2026). Én anonym teller per sidevisning til VinGPTs egen
   server: hvilken side, hvor besøket kom fra (søkemotor, KI-assistent, App Store …), mobil eller pc.
   Ingen informasjonskapsler, ingen id, ingen IP lagres. «Do Not Track» respekteres.
   Se personvern/ og sv/integritet/. Mottaker: cache/worker.js, seksjonen BESØK. */
(function () {
  try {
    if (location.hostname !== "vingpt.no" || navigator.doNotTrack === "1" || !navigator.sendBeacon) return;
    var s = location.pathname.replace(/index\.html$/, "");
    if (s.slice(-1) !== "/") s += "/";
    var h = "";
    try { h = new URL(document.referrer).hostname; } catch (e) {}
    var k = "direkte";
    if (h) {
      if (/(^|\.)vingpt\.no$/.test(h)) k = "intern";
      else if (/gemini\.google|bard\.google/.test(h)) k = "gemini";
      else if (/(^|\.)google\./.test(h)) k = "google";
      else if (/(^|\.)bing\./.test(h)) k = "bing";
      else if (/duckduckgo\./.test(h)) k = "duckduckgo";
      else if (/chatgpt\.com|openai\.com/.test(h)) k = "chatgpt";
      else if (/perplexity\./.test(h)) k = "perplexity";
      else if (/claude\.ai|anthropic\./.test(h)) k = "claude";
      else if (/copilot\.|microsoft\./.test(h)) k = "copilot";
      else if (/apple\.com$/.test(h)) k = "apple";
      else if (/facebook\.|instagram\.|(^|\.)fb\./.test(h)) k = "facebook";
      else if (/reddit\./.test(h)) k = "reddit";
      else k = "annen";
    }
    var e = window.matchMedia && matchMedia("(pointer: coarse)").matches ? "mobil" : "pc";
    navigator.sendBeacon("https://vingpt-cache.jensconradi.workers.dev/web", JSON.stringify({ s: s, k: k, e: e }));
  } catch (e) {}
})();
