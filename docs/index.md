Easily create a full Rouge Higlighter SCSS Theme by defining only 16 colors 🎨
You just created a Jekyll website (or Github Pages), this project will bring your `code block` to live 🎉.

## How to use

1. Download the project archive ([.zip]({{ site.github.zip_url }}) OR [.tag.gz]({{ site.github.tar_url }})) and unarchive (unzip) it.
2. Copy the `highlighter/` folder in you project SCSS directory.
3. In your main SCSS file, import the color palette you want tu use, followed by an import to the sorbus file:
```scss
/// In this example we use the Solarized Dark color palette
@import "highlighter/base16/solarized-dark";
@import "highlighter/sorbus";
```
If you don't import a color palette the default one (`rowan.scss`) is used automatically.

## Documentation
The full documentation is available [here](./documentation.md).

## Color Palettes Preview
Click on the images below to see multiple live examples.
