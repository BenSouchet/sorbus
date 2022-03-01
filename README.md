# Sorbus
Sorbus is a SCSS Auto-Theme using [base16 palettes](https://github.com/chriskempson/base16) for the [Rouge Higlighter](https://github.com/rouge-ruby/rouge).

Easily create a full Rouge Higlighter SCSS Theme by only defining 16 colors!

## How to use

1. Copy the `highlighter/` folder in you project SCSS directory
2. In your main SCSS file, import the color palette you want tu use, followed by an import to the sorbus file:
```scss
/// In this example we use the Solarized Dark color palette
@import "highlighter/base16/solarized-dark";
@import "highlighter/sorbus";
```
If you don't import a color palette the default one (`rowan.scss`) will be used automatically.

## Included color palettes

To avoid copy of unused data to your project, by design Sorbus in shipped with only 4 color palettes:
| Rowan | Monokai | Solarized | Solarized Dark |
|:-----:|:-------:|:---------:|:--------------:|
|       |         |           |                |

Rowan is the default color palette, this means that if you avoid (or forget) to import a color palette it's the one that will be used.

## More color palettes

In the `palettes/` folder at the root if this repository you will find lots of cool **base16** color palettes you can use.

## Create you own color palette

1. After you copied the `highlighter/` folder in you project SCSS directory, go to the subfolder `base16/`
2. Copy an existing color palette file and rename it to your preference
3. Open the file and edit the color HEX values
4. In your main SCSS file change the color palette you import by the name of the new color palette you created

## Origin of Sorbus

Sorbus was created to be used with Jekyll (especially Jekyll Github Pages) since Rouge Highlighter is the default code highlighter used by Jekyll, and there is no theme file by default.

## Author / Maintainer

Sorbus has been created and is currently maintained by [Ben Souchet](https://github.com/BenSouchet).

The code present in this repository is under [MIT license](https://github.com/BenSouchet/sorbus/blob/main/LICENSE).
