# Documentation

## How to use

1. Download the project archive ([.zip]({{ site.github.zip_url }}) OR [.tag.gz]({{ site.github.tar_url }})) and unarchive (unzip) it.
2. Copy the `highlighter/` folder in you project SCSS directory.
3. In your main SCSS file, import the color palette you want tu use, followed by an import to the sorbus file:
```scss
/// In this example we use the Solarized Dark color palette
@import "highlighter/palettes/solarized-dark";
@import "highlighter/sorbus";
```
If you don't import a color palette the default one (`rowan.scss`) is used automatically.

## Included color palettes

To avoid unused data in your project, Sorbus is shipped (by design) with only 4 color palettes:

| Rowan | Monokai | Solarized | Solarized Dark |
|:-----:|:-------:|:---------:|:--------------:|
|       |         |           |                |

**Rowan** is the default one, this means that if you avoid (or forget) to import a color palette it's the one that will be used.

## More color palettes

Want more palettes click on the images below to see palettes at work!  
The palettes SCSS files are located in the `palettes/` folder at the root of this repository.

## Create you own color palette

Want to create your own palette, it's easy, follow these simple steps:

1. After you copied the `highlighter/` folder in you project SCSS directory, go to the subfolder `palettes/`.
2. Copy an existing color palette file and rename it to your preference.
3. Open the file and edit the color HEX values.
4. In your main SCSS file change the color palette you imported by the name of the new color palette you created. And it's done!

To understand utility of each color variables please check the [Styling Guidelines](./styling_guidelines.md).

## Difference with Base16 project (from Chris Kempson)

Sorbus use color palettes (16 colors) for generating the final highlighter theme, this is inspired by the [Base16 project](https://github.com/chriskempson/base16) created by [Chris Kempson](https://github.com/chriskempson).  
But there is **one major difference**, the styling guidelines aren't the same.  
Check [this page](./styling_guidelines.md) to see the Styling guidelines of Sorbus color palettes (there is a comparaison with the Chris Kempson Base16 project guidelines).

## Origin of Sorbus

Sorbus was created to be used with Jekyll (especially Jekyll Github Pages) since Rouge Highlighter is the default code highlighter used by Jekyll, and there is no style file by default.

## Errors / Bugs

You encountered an error, something doesn't work as expected or you have a question, check or open an [issue here](https://github.com/BenSouchet/sorbus/issues).

## Others Ressouces & Useful links

- [Rouge highlighter](https://github.com/rouge-ruby/rouge)
- [base16](https://github.com/chriskempson/base16) project created by [Chris Kempson](https://github.com/chriskempson)

## Author & Maintainer

Sorbus has been created and is currently maintained by [Ben Souchet](https://github.com/BenSouchet).

The code present in this repository is under [MIT license](https://github.com/BenSouchet/sorbus/blob/main/LICENSE).
