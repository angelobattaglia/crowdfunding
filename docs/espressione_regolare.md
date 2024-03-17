# Espressione Regolare

Vi è una espressione regolare usata nel route "signup.html" per controllare che la stringa inserita dall'utente sia della forma
corrispondente ad una email tradizionale:

Questa è quella espressione: `"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"`, e questi sono gli ingredienti per prepararla:

- `[a-zA-Z0-9._%+-]+`: Questa parte rappresenta il nome dell'indirizzo email, la parte prima della chiocciola `@`. Indica che può essere composta da qualsiasi carattere minuscolo (`a-z`), maiuscolo (`A-Z`), cifra numerica (`0-9`), punto (`.`), trattino basso (`_`), segno di percentuale (`%`), segno più (`+`), o un trattino (`-`). Il segno `+` indica che un carattere precedentemente menzionato (`[a-zA-Z0-9._%+-]`) può apparire una o più volte.

- `@`: è letteralmente la chiocciolina `@`

- `[a-zA-Z0-9.-]+`: Questa è la parte del dominio a cui è registrata l'email, specificatamente la parte compresa tra il simbolo `@` e il punto (`.`). Può contenere le lettere maiuscole e minuscole comprese tra la A e la Z (`a-zA-Z`), le cifre numeriche tra lo zero e il nove (`0-9`), i punti (`.`), o i trattini (`-`). Il segno `+`, come prima, indica che questi caratteri possono apparire una o più volte.

- `\.`: Questo è per il carattere (`.`). Nell espressioni regolari il carattere "punto" è un carattere speciale che rappresenta tutti i caratteri, dunque, usando il carattere "backslash" (`\`) posso riferirmi all'effettivo carattere "punto".

- `[a-zA-Z]{2,}`: Questa parte si assicura che il "top-level domain" (TLD) dell'email, che è una stringa, quindi `[a-z][A-Z]`, e sia composta da almeno 2 caratteri, ma non ha un limite superiore, specificato dal `{2,}`, ad esempio, posso scrivere: `.superman` nel qual caso questo dominio esistesse.

- `$`: Il simbolo del dollaro americano asserisce la fine dell'input.
