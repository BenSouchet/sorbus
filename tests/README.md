# Tests Tokens Representation

The [Rouge Highlighter](https://github.com/rouge-ruby/rouge) used tokens, it's with them that we can apply CSS to style the HTML output.

Since Sorbus set the CSS properties for the Rouge tokens, it's important to know why each CSS property is applied to each token.

To determine the best CSS properties for the tokens the idea is to "test" tokens in an IDE, in others words create files correponding to the tokens (one file per token) and check how it's rendered in the best corresponding IDE.

The main goal is to determine the following CSS properties:
- `font-style` (normal or italic)
- `font-weight` (normal or bold)
- `font-decoration` (none or underline)

## Tests infomation

Since all tokens isn't used in one single language the tests are written in multiple languages (C++, Python, Ruby, Json, ...).

| Token code | Token name | Test language | Test file |
|:----------:|:----------:|:-------------:|:---------:|
| .hll | Highlight Line | Json | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/json/hll.json) |
| .w | Text Whitespace | Json | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/json/w.json) |
| .c | Comment | Python | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/python/c.py) |
| .cd | Comment Doc | PHP | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/php/cd.php) |
| .ch | Comment Hashbang | Python | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/python/ch.py) |
| .cm | Comment Multiline | C++ | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/cpp/cm.cpp) |
| .cp | Comment Preproc | C++ | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/cpp/cp.cpp) |
| .cpf | Comment PreprocFile | C++ | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/cpp/cpf.cpp) |
| .c1 | Comment Single | C++ | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/cpp/c1.cpp) |
| .cs | Comment Special | Java | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/java/cs.java) |
| .g | Generic | ***N/A*** | ***N/A*** |
| .gd | Generic Deleted | diff | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/diff/gd.diff) |
| .ge | Generic Emph | Markdown | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/markdown/ge.md) |
| .gr | Generic Error | ***N/A*** | ***N/A*** |
| .gh | Generic Heading | Markdown | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/markdown/gh.md) |
| .gi | Generic Inserted | diff | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/diff/gi.diff) |
| .go | Generic Output | ***N/A*** | ***N/A*** |
| .gp | Generic Prompt | ***N/A*** | ***N/A*** |
| .gs | Generic Strong | Markdown | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/markdown/gs.md) |
| .gu | Generic Subheading | Markdown | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/markdown/gu.md) |
| .gt | Generic Traceback | ***N/A*** | ***N/A*** |
| .gl | Generic Lineno | ***N/A*** | ***N/A*** |
| .k | Keyword | ***N/A*** | ***N/A*** |
| .kc | Keyword Constant | JavaScript | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/javascript/kc.js) |
| .kd | Keyword Declaration | JavaScript | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/javascript/kd.js) |
| .kn | Keyword Namespace | C++ | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/cpp/kn.cpp) |
| .kp | Keyword Pseudo | Python | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/python/kp.py) |
| .kr | Keyword Reserved | ruby | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/ruby/kr.rb) |
| .kt | Keyword Type | C++ | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/cpp/kt.cpp) |
| .kv | Keyword Variable | ***N/A*** | ***N/A*** |
| .l | Literal | ***N/A*** | ***N/A*** |
| .ld | Literal Date | Visual Basic | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/visual-basic/ld.vb) |
| .s | Literal String | Ruby | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/ruby/s.rb) |
| .sa | Literal String Affix | Python | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/python/sa.py) |
| .sb | Literal String Backtick | Ruby | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/ruby/sb.rb) |
| .sc | Literal String Char | C++ | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/cpp/sc.cpp) |
| .dl | Literal String Delimiter | JavaScript | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/javascript/dl.js) |
| .sd | Literal String Doc | Python | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/python/sd.py) |
| .s2 | Literal String Double | JavaScript | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/javascript/s2.js) |
| .se | Literal String Escape | JavaScript | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/javascript/se.js) |
| .sh | Literal String Heredoc | Ruby | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/ruby/sh.rb) |
| .si | Literal String Interpol | Ruby | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/ruby/si.rb) |
| .sx | Literal String Other | Ruby | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/ruby/sx.rb) |
| .sr | Literal String Regex | Python | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/python/sr.py) |
| .s1 | Literal String Single | JavaScript | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/javascript/s1.js) |
| .ss | Literal String Symbol | Ruby | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/ruby/ss.rb) |
| .m | Literal Number | ***N/A*** | ***N/A*** |
| .mb | Literal Number Binary | Ruby | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/ruby/mb.rb) |
| .mf | Literal Number Float | Python | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/python/mf.py) |
| .mh | Literal Number Hexadecimal | JavaScript | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/javascript/mh.js) |
| .mi | Literal Number Integer | C++ | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/cpp/mi.cpp) |
| .il | Literal Number Integer Long | C++ | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/cpp/il.cpp) |
| .mo | Literal Number Octal | Ruby | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/ruby/mo.rb) |
| .mx | Literal Number Other | C++ | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/cpp/mx.cpp) |
| .o | Operator | Python | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/python/o.py) |
| .ow | Operator Word | Python | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/python/ow.py) |
| .p | Ponctuation | JavaScript | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/javascript/p.js) |
| .pi | Punctuation Indicator | YAML | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/yaml/pi.yaml) |
| .n | Name | ***N/A*** | ***N/A*** |
| .na | Name Attribute | HTML | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/html/na.html) |
| .nb | Name Built-in | CSS | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/css/nb.css) |
| .bp | Built-in Pseudo | Ruby | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/ruby/bp.rb) |
| .nc | Name Class | C++ | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/cpp/nc.cpp) |
| .no | Name Constant | CSS | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/css/no.css) |
| .nd | Name Decorator | Python | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/python/nd.py) |
| .ni | Name Entity | HTML | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/html/ni.html) |
| .ne | Name Exception | Python | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/python/ne.py) |
| .nf | Name Function | Python | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/python/nf.py) |
| .fm | Name Function Magic | ***N/A*** | ***N/A*** |
| .py | Name Property | CSS | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/css/py.css) |
| .nl | Name Label | Json | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/json/nl.json) |
| .nn | Name Namespace | C++ | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/cpp/nn.cpp) |
| .nx | Name Other | ***N/A*** | ***N/A*** |
| .nt | Name Tag | HTML | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/html/nt.html) |
| .nv | Name Variable | PHP | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/php/nv.php) |
| .vc | Name Variable Class | Ruby | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/ruby/vc.rb) |
| .vg | Name Variable Global | Ruby | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/ruby/vg.rb) |
| .vi | Name Variable Instance | Ruby | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/ruby/vi.rb) |
| .vm | Name Variable Magic | Batch | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/batch/vm.bat) |
| .esc | Escape | C++ | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/cpp/esc.cpp) |
| .err | Error | python | [File](https://github.com/BenSouchet/sorbus/blob/main/tests/python/err.py) |
| .x | Other | ***N/A*** | ***N/A*** |

The list of tokens that Sorbus handle is based on theses links:
 - [Rouge List of tokens](https://github.com/rouge-ruby/rouge/wiki/List-of-tokens)
 - [lib/rouge/token.rb](https://github.com/rouge-ruby/rouge/blob/master/lib/rouge/token.rb)

## IDEs Representation

IDEs used:
 - [CLion](https://www.jetbrains.com/clion) (for: *C++*)
 - [Github](https://github.com/) (for: *Markdown*)
 - [IntelliJ IDEA](https://www.jetbrains.com/idea)  (for: *Java*)
 - [PhpStorm](https://www.jetbrains.com/phpstorm/) (for: *PHP*)
 - [PyCharm](https://www.jetbrains.com/pycharm/) (for: *Python*)
 - [RubyMine](https://www.jetbrains.com/ruby/) (for: *Ruby*)
 - [Visual Studio Code](https://code.visualstudio.com/) (for: *Batch*, *YAML*, *diff*, *JSON* and *Visual Basic*)
 - [WebStorm](https://www.jetbrains.com/webstorm) (for: *HTML*, *CSS*, *JavaScript*)

Theme used: [**Monokai Pro**](https://monokai.pro/)

/!\ Diclaimer: Project not affiliate (or sponsored) by any brand (nor Jetbrains, VS Code, Monokai, ...). Simply for the best setup using an IDE designed for the corresponding language is way more accurate.

| Token code | Visual representation |
|:----------:|:---------------------:|
| .hll | <img width="336" alt="Result image of token Highlight Line" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/json/vscode/hll.png"> |
| .w | <img width="336" alt="Result image of token Text Whitespace" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/json/vscode/w.png"> |
| .c | <img width="336" alt="Result image of token Comment" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/python/pycharm/c.png"> |
| .cd | <img width="336" alt="Result image of token Comment Doc" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/php/phpstorm/cd.png"> |
| .ch | <img width="336" alt="Result image of token Comment Hashbang" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/python/pycharm/ch.png"> |
| .cm | <img width="336" alt="Result image of token Comment Multiline" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/cpp/clion/cm.png"> |
| .cp | <img width="336" alt="Result image of token Comment Preproc" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/cpp/clion/cp.png"> |
| .cpf | <img width="336" alt="Result image of token Comment PreprocFile" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/cpp/clion/cpf.png"> |
| .c1 | <img width="336" alt="Result image of token Comment Single" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/cpp/clion/c1.png"> |
| .cs | <img width="336" alt="Result image of token Comment Special" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/java/intellijidea/cs.png"> |
| .g | ***N/A*** |
| .gd | <img width="336" alt="Result image of token Generic Deleted" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/diff/vscode/gd.png"> |
| .ge | <img width="336" alt="Result image of token Generic Emph" src=""> |
| .gr | ***N/A*** |
| .gh | <img width="336" alt="Result image of token Generic Heading" src=""> |
| .gi | <img width="336" alt="Result image of token Generic Inserted" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/diff/vscode/gi.png"> |
| .go | ***N/A*** |
| .gp | ***N/A*** |
| .gs | <img width="336" alt="Result image of token Generic Strong" src=""> |
| .gu | <img width="336" alt="Result image of token Generic Subheading" src=""> |
| .gt | ***N/A*** |
| .gl | ***N/A*** |
| .k | ***N/A*** |
| .kc | <img width="336" alt="Result image of token Keyword Constant" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/javascript/webstorm/kc.png"> |
| .kd | <img width="336" alt="Result image of token Keyword Declaration" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/javascript/webstorm/kd.png"> |
| .kn | <img width="336" alt="Result image of token Keyword Namespace" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/cpp/clion/kn.png"> |
| .kp | <img width="336" alt="Result image of token Keyword Pseudo" src=""> |
| .kr | <img width="336" alt="Result image of token Keyword Reserved" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/ruby/mineruby/kr.png"> |
| .kt | <img width="336" alt="Result image of token Keyword Type" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/cpp/clion/kt.png"> |
| .kv | ***N/A*** |
| .l | ***N/A*** |
| .ld | <img width="336" alt="Result image of token Literal Date" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/visualbasic/vscode/ld.png"> |
| .s | <img width="336" alt="Result image of token Literal String" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/ruby/mineruby/s.png"> |
| .sa | <img width="336" alt="Result image of token Literal String Affix" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/python/pycharm/sa.png"> |
| .sb | <img width="336" alt="Result image of token Literal String Backtick" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/ruby/mineruby/sb.png"> |
| .sc | <img width="336" alt="Result image of token Literal String Char" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/cpp/clion/sc.png"> |
| .dl | <img width="336" alt="Result image of token Literal String Delimiter" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/javascript/webstorm/dl.png"> |
| .sd | <img width="336" alt="Result image of token Literal String Doc" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/python/pycharm/sd.png"> |
| .s2 | <img width="336" alt="Result image of token Literal String Double" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/javascript/webstorm/s2.png"> |
| .se | <img width="336" alt="Result image of token Literal String Escape" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/javascript/webstorm/se.png"> |
| .sh | <img width="336" alt="Result image of token Literal String Heredoc" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/ruby/mineruby/sh.png"> |
| .si | <img width="336" alt="Result image of token Literal String Interpolation" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/ruby/mineruby/si.png"> |
| .sx | <img width="336" alt="Result image of token Literal String Other" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/ruby/mineruby/sx.png"> |
| .sr | <img width="336" alt="Result image of token Literal String Regex" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/python/pycharm/sr.png"> |
| .s1 | <img width="336" alt="Result image of token Literal String Single" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/javascript/webstorm/s1.png"> |
| .ss | <img width="336" alt="Result image of token Literal String Symbol" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/ruby/mineruby/ss.png"> |
| .m | ***N/A*** |
| .mb | <img width="336" alt="Result image of token Literal Number Binary" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/ruby/mineruby/mb.png"> |
| .mf | <img width="336" alt="Result image of token Literal Number Float" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/python/pycharm/mf.png"> |
| .mh | <img width="336" alt="Result image of token Literal Number Hexadecimal" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/javascript/webstorm/mh.png"> |
| .mi | <img width="336" alt="Result image of token Literal Number Integer" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/cpp/clion/mi.png"> |
| .il | <img width="336" alt="Result image of token Literal Number Integer Long" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/cpp/clion/il.png"> |
| .mo | <img width="336" alt="Result image of token Literal Number Octal" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/ruby/mineruby/mo.png"> |
| .mx | <img width="336" alt="Result image of token Literal Number Other" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/cpp/clion/mx.png"> |
| .o | <img width="336" alt="Result image of token Operator" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/python/pycharm/o.png"> |
| .ow | <img width="336" alt="Result image of token Operator Word" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/python/pycharm/ow.png"> |
| .p | <img width="336" alt="Result image of token Ponctuation" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/javascript/webstorm/p.png"> |
| .pi | <img width="336" alt="Result image of token Punctuation Indicator" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/yaml/vscode/pi.png"> |
| .n | ***N/A*** |
| .na | <img width="336" alt="Result image of token Name Attribute" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/html/webstorm/na.png"> |
| .nb | <img width="336" alt="Result image of token Name Built-in" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/css/webstorm/nb.png"> |
| .bp | <img width="336" alt="Result image of token Built-in Pseudo" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/ruby/mineruby/bp.png"> |
| .nc | <img width="336" alt="Result image of token Name Class" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/cpp/clion/nc.png"> |
| .no | <img width="336" alt="Result image of token Name Constant" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/css/webstorm/no.png"> |
| .nd | <img width="336" alt="Result image of token Name Decorator" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/python/pycharm/nd.png"> |
| .ni | <img width="336" alt="Result image of token Name Entity" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/html/webstorm/ni.png"> |
| .ne | <img width="336" alt="Result image of token Name Exception" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/python/pycharm/ne.png"> |
| .nf | <img width="336" alt="Result image of token Name Function" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/python/pycharm/nf.png"> |
| .fm | ***N/A*** |
| .py | <img width="336" alt="Result image of token Name Property" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/css/webstorm/py.png"> |
| .nl | <img width="336" alt="Result image of token Name Label" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/json/vscode/nl.png"> |
| .nn | <img width="336" alt="Result image of token Name Namespace" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/cpp/clion/nn.png"> |
| .nx | ***N/A*** |
| .nt | <img width="336" alt="Result image of token Name Tag" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/html/webstorm/nt.png"> |
| .nv | <img width="336" alt="Result image of token Name Variable" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/php/phpstorm/nv.png"> |
| .vc | <img width="336" alt="Result image of token Name Variable Class" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/ruby/mineruby/vc.png"> |
| .vg | <img width="336" alt="Result image of token Name Variable Global" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/ruby/mineruby/vg.png"> |
| .vi | <img width="336" alt="Result image of token Name Variable Instance" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/ruby/mineruby/vi.png"> |
| .vm | <img width="336" alt="Result image of token Name Variable Magic" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/batch/vscode/vm.png"> |
| .esc | <img width="336" alt="Result image of token Escape" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/cpp/clion/esc.png"> |
| .err | <img width="336" alt="Result image of token Error" src="https://raw.githubusercontent.com/BenSouchet/sorbus/main/tests/results/python/pycharm/err.png"> |
| .x | ***N/A*** |

# Github Representation

See also how Github display these tokens.

### `.hll` Highlight Line (***N/A***)
*Not available in Github Flavored Markdown (GFM)*
### `.w` Text Whitespace (Json)
In the example below, the token is the whitespace between `:` and `42`
```json
{
    "test": 42
}
```
### `.c` Comment (Python)
In the example below, the token is the comment line starting by `#`
```python
# Test
```
### `.cd` Comment Doc (PHP)
In the example below, the token is the doc comment line starting by `/**` and ending by `*/`
```php
<?php
    /** Test */
?>
```
### `.ch` Comment Hashbang (Python)
In the example below, the token is the hashbang line starting by `#!`
```python
#!/usr/bin/env python
```
### `.cm` Comment Multiline (Python)
In the example below, the token is the comment block between `/*` and `*/`
```python
/*
 Test
*/
```
### `.cp` Comment Preproc (C++)
In the example below, the token is the syntax `#include`
```cpp
#include <iostream>
```
### `.cpf` Comment PreprocFile (C++)
In the example below, the token is the header files `<test1.h>` and `"test2.h"`
```cpp
#include <test1.h>
#include "test2.h"
```
### `.c1` Comment Single (C++)
In the example below, the token is the comment line starting by `// `
```cpp
// Test
```
### `.cs` Comment Special (Java)
In the example below, the token is the special comment word `@param`
```java
/**
* @param  test  simply a param to test
*/
```
### `.g` Generic (***N/A***)
*Currently no test available*
### `.gd` Generic Deleted (diff)
In the example below, the token is the whole line
```diff
- This is a long line to properly see the style.
```
### `.ge` Generic Emph (Markdown)
In the example below, the token is the word `*test*` (normally rendered in italic)  
*Test*
### `.gr` Generic Error (***N/A***)
*Currently no test available*
### `.gh` Generic Heading (Markdown)
# Test
### `.gi` Generic Inserted (diff)
In the example below, the token is the whole line
```diff
+ This is a long line to properly see the style.
```
### `.go` Generic Output (***N/A***)
*Currently no test available*
### `.gp` Generic Prompt (***N/A***)
*Currently no test available*
### `.gs` Generic Strong (Markdown)
In the example below, the token is the word `**test**` (normally rendered in bold)  
**Test**
### `.gu` Generic Subheading (Markdown)
In the example below, the token is the header `**test**` (normally rendered in bold, with big font-size)
## Test
### `.gt` Generic Traceback (***N/A***)
*Currently no test available*
### `.gl` Generic Lineno (***N/A***)
*Currently no test available*
### `.k` Keyword (***N/A***)
*Currently no test available*
### `.kc` Keyword Constant (JavaScript)
In the example below, the token is the constant keyword `true`
```javascript
var test = true;
```
### `.kd` Keyword Declaration (JavaScript)
In the example below, the token is the keyword to declare variable `var`
```javascript
var test;
```
### `.kn` Keyword Namespace (C++)
In the example below, the token is the namespace keyword `namespace`
```cpp
namespace test { int test_val = 500; }
```
### `.kp` Keyword Pseudo (Python)
In the example below, the token is the pseudo keyword `None`
```python
test = None
```
### `.kr` Keyword Reserved (Ruby)
In the example below, the token is the reserved keyword `end`
```ruby
def test
  puts 'Test'
end
```
### `.kt` Keyword Type (C++)
In the example below, the token is the type of the variable `int`
```cpp
int test = 42;
```
### `.kv` Keyword Variable (JavaScript)
*Currently no test available*
### `.l` Literal (***N/A***)
*Currently no test available*
### `.ld` Literal Date (Visual Basic)
In the example below, the token is the literal date between `#`
```vb
Dim someDateAndTime As Date = #8/13/2002 12:14 PM#
```
### `.s` Literal String (Ruby)
 the example below, the token is the string `'Test string'`
```ruby
test = 'Test string'
```
### `.sa` Literal String Affix (Python)
In the example below, the token is the character bbefore the string `f`
```python
test = 'foo'
f'{test} , bar, {test}bar'
```
### `.sb` Literal String Backtick (Ruby)
In the example below, the token is the backtick string ` `` `
```ruby
test = `ls`
```
### `.sc` Literal String Char (C++)
In the example below, the token is the character string `'T'`
```cpp
char test = 'T';
char test_code = 84;
```
### `.dl` Literal String Delimiter (JavaScript)
In the example below, the token is the single quote `'`  
This token seems to be used only on **JavaScript** ([issue](https://github.com/rouge-ruby/rouge/issues/1786))
```javascript
var test = 'test';
```
### `.sd` Literal String Doc (Python)
In the example below, the token is the docstring `"""Test of a docstring"""`
```python
def test():
    """Test of a docstring"""
    return True
```
### `.s2` Literal String Double (JavaScript)
In the example below, the token is the double quoted string `"test"`
```javascript
var test = "test";
```
### `.se` Literal String Escape (JavaScript)
In the example below, the token is the string escape `\'`
```javascript
let test = 'It\'s a test';
```
### `.sh` Literal String Heredoc (Ruby)
In the example below, the token is the Heredoc block starting with `<<-HEREDOC` and ending with `HEREDOC`
```ruby
test = <<-HEREDOC
  This is
  a sample
  text.
HEREDOC
```
### `.si` Literal String Interpol (Ruby)
In the example below, the token is the interpolated string part `#{name}`
```ruby
name = 'Test'
puts "Hello, #{name}!"
```
### `.sx` Literal String Other (Ruby)
In the example below, the token is the special string `%q{foo}`
```ruby
puts %q{foo}
```
### `.sr` Literal String Regex (Python)
In the example below, the token is the regex string `r'[\w\.-]+@[\w\.-]+'`
```python
email_regex = r'[\w\.-]+@[\w\.-]+'
```
### `.s1` Literal String Single (JavaScript)
In the example below, the token is the string `'test'`
```javascript
var test = 'test';
```
### `.ss` Literal String Symbol (Ruby)
In the example below, the token is the special string `:test`
```ruby
puts :test.to_s
```
### `.m` Literal Number (***N/A***)
*Currently no test available*
### `.mb` Literal Number Binary (Ruby)
In the example below, the token is the binary number `0b1011`
```ruby
test = 0b1011
```
### `.mf` Literal Number Float (Python)
In the example below, the token is the float number `4.0`
```python
test = 4.0
```
### `.mh` Literal Number Hexadecimal (JavaScript)
In the example below, the token is the hexadecimal number `0xFF`
```javascript
let x = 0xFF;
```
### `.mi` Literal Number Integer (C++)
In the example below, the token is the integer number `42`
```cpp
int test = 42;
```
### `.il` Literal Number Integer Long (C++)
In the example below, the token is the long number `2147483647l` ending with `l`
```cpp
long test = 2147483647l;
```
### `.mo` Literal Number Octal (Ruby)
In the example below, the token is the octal number `0377`
```ruby
test = 0377
```
### `.mx` Literal Number Other (C++)
In the example below, the token is the complex syntax `(10.0, 2.0)`
```cpp
#include <complex>
std::complex<double> test(10.0, 2.0);
```
### `.o` Operator (Python)
In the example below, the token are the operators `*`, `+`, `-`, and `/`
```python
test = (((0.2 * 10) + 0.1) - 6) / 10
```
### `.ow` Operator Word (Python)
In the example below, the token is the operator word `and`
```python
if True and 1 == 1:
    pass
```
### `.p` Ponctuation (JavaScript)
In the example below, the token are the ponctuation symbols `{`, `;` and `}`
```javascript
function test() { return true; }
```
### `.pi` Punctuation Indicator (YAML)
In the example below, the token is the punctuation indicator `:`
```yaml
test:
  person1:
    age: 22
    location: Madrid
  person2:
    age: 24
    location: Rome
```
### `.n` Name (***N/A***)
*Currently no test available*
### `.na` Name Attribute (HTML)
In the example below, the token is the attribute name `class`
```html
<p class="test"></p>
```
### `.nb` Name Built-in (CSS)
In the example below, the token is the built-in name `inline-block`
```css
.test { display: inline-block; }
```
### `.bp` Built-in Pseudo (Ruby)
In the example below, the token is the keyword `self`
```ruby
class Test
  def self.print_test
    puts 'test'
  end
end
```
### `.nc` Name Class (C++)
In the example below, the token is the class name `Test`
```cpp
class Test { int test; };
```
### `.no` Name Constant (CSS)
In the example below, the token is the constant `blue`
```css
.test { color: blue; }
```
### `.nd` Name Decorator (Python)
In the example below, the token is the decorator syntax `@testDecorator`
```python
def testDecorator(func):
    return func

@testDecorator
def testFunc():
    return True
```
### `.ni` Name Entity (HTML)
In the example below, the token is the special entity `&nbsp;`
```html
<p>&nbsp;</p>
```
### `.ne` Name Exception (Python)
In the example below, the token are the exceptions names `OSError`, `ValueError` and `BaseException`
```python
try:
    test = 42
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not assign integer to variable.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```
### `.nf` Name Function (Python)
In the example below, the token is the function name `test`
```python
def test():
    return True
```
### `.fm` Name Function Magic (***N/A***)
*Not use in Rouhe Highlighter*
### `.py` Name Property (CSS)
In the example below, the token is property name `margin`
```css
.test { margin: 0; }
```
### `.nl` Name Label (Json)
In the example below, the token is the label name `"test"`
```json
{
    "test": 42
}
```
### `.nn` Name Namespace (C++)
In the example below, the token is the namespace name `test`
```cpp
namespace test { int test_val = 500; }
```
### `.nx` Name Other (***N/A***)
*Currently no test available*
### `.nt` Name Tag (HTML)
In the example below, the token is the tag name `style`
```html
<style></style>
```
### `.nv` Name Variable (PHP)
In the example below, the token is the variable `$test`
```php
<?php
    $test;
?>
```
### `.vc` Name Variable Class (Ruby)
In the example below, the token is class variable `@@shared`
```ruby
class Test
  @@shared = 1
end
```
### `.vg` Name Variable Global (Ruby)
In the example below, the token is the global variable `$LOAD_PATH`
```ruby
$LOAD_PATH.uniq!
```
### `.vi` Name Variable Instance (Ruby)
In the example below, the token is instance variable `@name`
```ruby
class Person
  @name = 'Test'
end
```
### `.vm` Name Variable Magic (Batch)
In the example below, the token is the value magic variable `%~p0`
```batch
set _SCRIPT_PATH=%~p0
```
### `.esc` Escape (C++)
In the example below, the token is the ecaped character `\n`
```cpp
char* test = "hello\nworld!";
```
### `.err` Error (Python)
In the example below, the token is the whole line (normally rendered with an red wavy underline)
```python
!.....................
```
### `.x` Other (***N/A***)
*Currently no test available*
