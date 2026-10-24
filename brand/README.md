# Katakrush Games brand

The studio mark: a scrappy, nearly flat robot head in rust, with toxic-green "KK" eyes (the second K's arm hanging loose), a green hex-nut antenna, a taped crack on the screen and a zigzag smile. The name is set in Bungee, with the K of "KRUSH" hanging crooked.

| File | Use |
|---|---|
| `katakrush-mark.svg` | The mark, any size (vector) |
| `katakrush-mark-{1024,512,192,180,64,32,16}.png` | The mark on transparent; 180 = Apple touch icon, 32/16 = favicon |
| `katakrush-icon-512.png` | Square on the dark ground (#15181B): Play developer page, social avatars |
| `katakrush-logo-dark-bg.png` | Mark + name, for dark backgrounds |
| `katakrush-logo-light-bg.png` | Mark + name, for light backgrounds |

Colours: rust #B5521F (shade #7E3714, edge #D07A45), toxic green #A6E22E (on light grounds #4E7A12), screen #1B1714, outline #2A1A12, ground #15181B, bone #E6E0D2.

`source/` holds the Python that draws the mark (`final.py` makes `final-dark.svg`; it builds on the round*.py helpers). Run `python final.py <out-dir>` from inside `source/`.
