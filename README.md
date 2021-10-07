# Ein Monorepo des Toolings unserer WG

Das Repo ist wie folgt aufgebaut:

- [`generate_trash_message`](./generate_trash_message) rechnet zyklisch anhand eines Anfangspunktes und der WG-Größe aus wer gerade Mülldienst hat
- [`send_to_wg`](./send_to_wg) sendet alles, was man gerade reinpiped, in die WG-Telegramgruppe.
- [`send_trash_message`](./send_trash_message.sh) ist glue der `generate_trash_message` sowie `send_to_wg` zusammenhält.

## Installation und Konfiguration

Siehe die einzelnen Ordner.

## Deployment

### Müllbenachrichtigung Telegram

Cronjob für [`send_trash_message`](./send_trash_message.sh) erstellen, ich kann [crontab.guru](https://crontab.guru/) empfehlen!

Ich lasse es zum Beispiel jeden Montag um 8 Uhr Morgens laufen, sprich `0 8 * * 1`

## LICENSE

Do What The Fuck You Want To Public License
