# Tests

The [Rouge Highlighter](https://github.com/rouge-ruby/rouge) used tokens, it's with them that we can apply CSS to style the HTML output.

Since Sorbus set the CSS properties for the Rouge tokens, it's important to know why each CSS property is applied to each token.

To determine the best CSS properties for the tokens the idea is to "test" tokens in an IDE, in others words create files correponding to the tokens (one file per token) and check how it's rendered in the best corresponding IDE.

The main goal is to determine the following CSS properties:
- `font-style` (normal or italic)
- `font-weight` (normal or bold)
- `font-decoration` (none or underline)

## Tokens tests infomation

Since all tokens isn't used in one single language the tests are written in multiple languages (C++, Python, Ruby, Json, ...).

| Token code | Token name | Test language | Test file |
|:----------:|:----------:|:-------------:|:---------:|
| .hll | Highlight Line | Json | [File]() |
| .w | Text Whitespace | Json | [File]() |
| .c | Comment | Python | [File]() |
| .cd | Comment Doc | PHP | [File]() |
| .ch | Comment Hashbang | Python | [File]() |
| .cm | Comment Multiline | Python | [File]() |
| .cp | Comment Preproc | Embedded Ruby | [File]() |
| .cpf | Comment PreprocFile | C | [File]() |
| .c1 | Comment Single | CSS | [File]() |
| .cs | Comment Special | Javadoc | [File]() |
| .g | Generic | ***N/A*** | ***N/A*** |
| .gd | Generic Deleted | diff | [File]() |
| .ge | Generic Emph | Markdown | [File]() |
| .gr | Generic Error | ***N/A*** | ***N/A*** |
| .gh | Generic Heading | Markdown | [File]() |
| .gi | Generic Inserted | diff | [File]() |
| .go | Generic Output | ***N/A*** | ***N/A*** |
| .gp | Generic Prompt | ***N/A*** | ***N/A*** |
| .gs | Generic Strong | Markdown | [File]() |
| .gu | Generic Subheading | Markdown | [File]() |
| .gt | Generic Traceback | ***N/A*** | ***N/A*** |
| .gl | Generic Lineno | ***N/A*** | ***N/A*** |
| .k | Keyword | ***N/A*** | ***N/A*** |
| .kc | Keyword Constant | JavaScript | [File]() |
| .kd | Keyword Declaration | JavaScript | [File]() |
| .kn | Keyword Namespace | C++ | [File]() |
| .kp | Keyword Pseudo | Python | [File]() |
| .kr | Keyword Reserved | ruby | [File]() |
| .kt | Keyword Type | C++ | [File]() |
| .kv | Keyword Variable | JavaScript | [File]() |
| .l | Literal | ***N/A*** | ***N/A*** |
| .ld | Literal Date | Visual Basic | [File]() |
| .s | Literal String | Ruby | [File]() |
| .sa | Literal String Affix | Python | [File]() |
| .sb | Literal String Backtick | Ruby | [File]() |
| .sc | Literal String Char | C++ | [File]() |
| .dl | Literal String Delimiter | JavaScript | [File]() |
| .sd | Literal String Doc | Python | [File]() |
| .s2 | Literal String Double | JavaScript | [File]() |
| .se | Literal String Escape | JavaScript | [File]() |
| .sh | Literal String Heredoc | Ruby | [File]() |
| .si | Literal String Interpol | Ruby | [File]() |
| .sx | Literal String Other | Ruby | [File]() |
| .sr | Literal String Regex | Python | [File]() |
| .s1 | Literal String Single | JavaScript | [File]() |
| .ss | Literal String Symbol | Ruby | [File]() |
| .m | Literal Number | ***N/A*** | ***N/A*** |
| .mb | Literal Number Binary | Ruby | [File]() |
| .mf | Literal Number Float | Python | [File]() |
| .mh | Literal Number Hexadecimal | Python | [File]() |
| .mi | Literal Number Integer | C++ | [File]() |
| .il | Literal Number Integer Long | C++ | [File]() |
| .mo | Literal Number Octal | Ruby | [File]() |
| .mx | Literal Number Other | C++ | [File]() |
| .o | Operator | Python | [File]() |
| .ow | Operator Word | Python | [File]() |
| .p | Ponctuation | JavaScript | [File]() |
| .pi | Punctuation Indicator | YAML | [File]() |
| .n | Name | ***N/A*** | ***N/A*** |
| .na | Name Attribute | HTML | [File]() |
| .nb | Name Built-in | CSS | [File]() |
| .bp | Built-in Pseudo | Ruby | [File]() |
| .nc | Name Class | C++ | [File]() |
| .no | Name Constant | CSS | [File]() |
| .nd | Name Decorator | Python | [File]() |
| .ni | Name Entity | HTML | [File]() |
| .ne | Name Exception | Ruby | [File]() |
| .nf | Name Function | Python | [File]() |
| .fm | Name Function Magic | ***N/A*** | ***N/A*** |
| .py | Name Property | CSS | [File]() |
| .nl | Name Label | Json | [File]() |
| .nn | Name Namespace | C++ | [File]() |
| .nx | Name Other | ***N/A*** | ***N/A*** |
| .nt | Name Tag | HTML | [File]() |
| .nv | Name Variable | JavaScript | [File]() |
| .vc | Name Variable Class | Ruby | [File]() |
| .vg | Name Variable Global | Ruby | [File]() |
| .vi | Name Variable Instance | Ruby | [File]() |
| .vm | Name Variable Magic | Batch | [File]() |
| .esc | Escape | C++ | [File]() |
| .err | Error | python | [File]() |
| .x | Other | ***N/A*** | ***N/A*** |

The list of tokens that Sorbus handle is based on theses links:
 - [Rouge List of tokens](https://github.com/rouge-ruby/rouge/wiki/List-of-tokens)
 - [lib/rouge/token.rb](https://github.com/rouge-ruby/rouge/blob/master/lib/rouge/token.rb)

## Results

IDEs used:
 - [Visual Studio Code](https://code.visualstudio.com/) (for: *C++*, *HTML*, *CSS*, *Batch*, *JavaScript*, *YAML*, *diff*, *JSON* and *Visual Basic*)
 - [PhpStorm](https://www.jetbrains.com/phpstorm/) (for: *PHP*)
 - [PyCharm](https://www.jetbrains.com/pycharm/) (for: *Python*)
 - [RubyMine](https://www.jetbrains.com/ruby/) (for; *Ruby*)
 - [Github](https://github.com/) (for: *Markdown*)

| Token code | Visual representation |
|:----------:|:---------------------:|
| .hll |  |
| .w |  |
| .c |  |
| .cd |  |
| .ch |  |
| .cm |  |
| .cp |  |
| .cpf |  |
| .c1 |  |
| .cs |  |
| .g | ***N/A*** |
| .gd |  |
| .ge |  |
| .gr | ***N/A*** |
| .gh |  |
| .gi |  |
| .go | ***N/A*** |
| .gp | ***N/A*** |
| .gs |  |
| .gu |  |
| .gt | ***N/A*** |
| .gl | ***N/A*** |
| .k | ***N/A*** |
| .kc |  |
| .kd |  |
| .kn |  |
| .kp |  |
| .kr |  |
| .kt |  |
| .kv |  |
| .l | ***N/A*** |
| .ld |  |
| .s |  |
| .sa |  |
| .sb |  |
| .sc |  |
| .dl |  |
| .sd |  |
| .s2 |  |
| .se |  |
| .sh |  |
| .si |  |
| .sx |  |
| .sr |  |
| .s1 |  |
| .ss |  |
| .m | ***N/A*** |
| .mb |  |
| .mf |  |
| .mh |  |
| .mi |  |
| .il |  |
| .mo |  |
| .mx |  |
| .o |  |
| .ow |  |
| .p |  |
| .pi |  |
| .n | ***N/A*** |
| .na |  |
| .nb |  |
| .bp |  |
| .nc |  |
| .no |  |
| .nd |  |
| .ni |  |
| .ne |  |
| .nf |  |
| .fm | ***N/A*** |
| .py |  |
| .nl |  |
| .nn |  |
| .nx | ***N/A*** |
| .nt |  |
| .nv |  |
| .vc |  |
| .vg |  |
| .vi |  |
| .vm |  |
| .esc |  |
| .err |  |
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
  puts "Test"
end
```
### `.kt` Keyword Type (C++)
In the example below, the token is the type of the variable `int`
```cpp
int test = 42;
```
### `.kv` Keyword Variable (JavaScript)
In the example below, the token is the function name `test`
```javascript
function test() { return true; }
```
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
name = "Test"
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
    puts "test"
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
  @name = "Test"
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