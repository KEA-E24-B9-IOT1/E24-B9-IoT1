# Krav: 
Man skal kunne sende en besked til løsningen fra Thingsboard så den aktiverer eller deaktiverer et alarmsystem så den blinker kraftigt med lys og giver lyd fra sig hvis den rykker sig når alarmen er slået til.

# Accepttest: 
- Start testprogrammet. 
- Send besked til løsningen om at aktivere alarmen. Vent 30 sekunder uden at flytte løsningen og i denne periode skal alarmen IKKE udløses. 
Prøv nu at flytte løsningen, og bekræft at alarmen går i gang ved at blinke lys og give lyd fra sig. 
- Send besked til løsningen om at deaktivere alarmen, og prøv at flytte løsningen, og kontroller at alarmen ikke udløses når cyklen flyttes. Hvis accepttesten kan udføres 8 ud af 10 gange uden fejl vurderes kravet som godkendt.