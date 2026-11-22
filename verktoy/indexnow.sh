#!/bin/zsh
# IndexNow (Bing, Yandex, Seznam; ChatGPT-søket bygger på Bing): melder sidene etter hver publisering.
# Nøkkelfila ligger i rota og er offentlig med vilje. Kjør: zsh verktoy/indexnow.sh   (22.11.2026)
NOKKEL=61479dab718ad14d91c8be94b1e5b279
curl -s -o /dev/null -w "IndexNow %{http_code}\n" -X POST https://api.indexnow.org/indexnow -H 'Content-Type: application/json; charset=utf-8' -d '{
 "host":"vingpt.no","key":"'$NOKKEL'","keyLocation":"https://vingpt.no/'$NOKKEL'.txt",
 "urlList":["https://vingpt.no/","https://vingpt.no/sv/","https://vingpt.no/en/",
  "https://vingpt.no/personvern/","https://vingpt.no/sv/integritet/",
  "https://vingpt.no/vilkar/","https://vingpt.no/sv/villkor/","https://vingpt.no/llms.txt"]}'
