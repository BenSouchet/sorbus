Use Sorbus to easily create a full Rouge Higlighter SCSS Theme by defining only 16 colors!

## How to use

1. Download the project archive ([.zip]({{ site.github.zip_url }}) OR [.tag.gz]({{ site.github.tar_url }})) and unarchive (unzip) it.
1. Copy the `highlighter/` folder in you project SCSS directory.
2. In your main SCSS file, import the color palette you want tu use, followed by an import to the sorbus file:
```scss
/// In this example we use the Solarized Dark color palette
@import "highlighter/base16/solarized-dark";
@import "highlighter/sorbus";
```
If you don't import a color palette the default one (`rowan.scss`) is used automatically.

## Preview
