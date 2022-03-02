# Styling Guidelines (for color palettes)

In this page find info about how colors are used, which syntactic elements are linked to which colors.  
In other words understand what SCSS variables are used for.  

## Correlation table

| Base16 | Variable name | Color Example | Used for |
|:------:|:-------------:|:-------------:|:--------:|
| $base00 | $bgr | <img src="https://via.placeholder.com/150/002b36?text=+"> | Block Background |
| $base01 | $hgh | <img src="https://via.placeholder.com/150/073642?text=+"> | Highlighted Line(s) |
| $base02 | $sel | <img src="https://via.placeholder.com/150/586e75?text=+"> | Selected Line(s) |
| $base03 | $com | <img src="https://via.placeholder.com/150/657b83?text=+"> | Comments |
| $base04 | $lin | <img src="https://via.placeholder.com/150/839496?text=+"> | Lines Numbers |
| $base05 | $def | <img src="https://via.placeholder.com/150/93a1a1?text=+"> | Default Text, Delimiters |
| $base06 | $lgh | <img src="https://via.placeholder.com/150/eee8d5?text=+"> | Lighter Default Text, used when default text is selected (Not often used) |
| $base07 | $ins | <img src="https://via.placeholder.com/150/5dc02f?text=+"> | Diff Inserted (usually green or greenish) |
| $base08 | $err | <img src="https://via.placeholder.com/150/dc322f?text=+"> | Errors, Diff Deleted (usually red or redish) |
| $base09 | $esc | <img src="https://via.placeholder.com/150/cb4b16?text=+"> | Escaped Characters, Regex, Interpoled Strings, Character Entities |
| $base0A | $key | <img src="https://via.placeholder.com/150/b58900?text=+"> | Constant Keywords, Reserved Keywords, Pseudo Keywords |
| $base0B | $opr | <img src="https://via.placeholder.com/150/859900?text=+"> | Operators, Word Operators |
| $base0C | $str | <img src="https://via.placeholder.com/150/2aa198?text=+"> | Strings, DocStrings |
| $base0D | $var | <img src="https://via.placeholder.com/150/268bd2?text=+"> | Variable Names, Attributes Names  |
| $base0E | $nam | <img src="https://via.placeholder.com/150/6c71c4?text=+"> | Built-In, Namespace Names, Class Names, Decorator Names, Exception Names, Function Names |
| $base0F | $num | <img src="https://via.placeholder.com/150/d33682?text=+"> | Numbers |

## Why differences with Base16
Base16 is a project defining and structuring the concept of color scheme base on 16 colors, basically color palette composed of 16 colors to be use for interfaces, editors, softwares...

The original idea is great, (this is why Sorbus use 16 colors palettes) **BUT** there is some elements that make it not interesting to use.
The main one is the fact that **three** of the sixteen colors aren't really used (base06, base07 & base0F), so they are no longer really 16 colors palettes.
