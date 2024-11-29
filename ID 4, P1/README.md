# Krav: 
Når cyklen har stået stille i mere end 3 minutter, og brugeren ikke har slukket permanent for løsningen, sendes beskeder med cyklens placering til Thingsboard, hvis cyklen kommer i bevægelse

# Accepttest: 
- Batteri skal være fuldt opladet 
- Løsningen tændes 
- En kort tur på 1 minut køres 
- Cyklen stilles, men løsningen slukkes ikke, og tiden nulstilles 
- Når der ikke er registreret bevægelse på cyklen i 3 minutter fra 3) skal der inden for 30 sekunder komme en besked på Thingsboard hvis cyklen kommer i bevægelse, og positionen sendes hvert tiende sekund til Thingsboard. Sker dette er kravet opfyldt.