from decipher import helper


def test_parse_html_table():
    text = """<table>
<tr><th>Form</th><th>Syntax</th></tr>
<tr>
<td>Tall</td>
<td>
<pre>
|$  sample
body
</pre>
</td>
</tr>
<tr>
<td>Wide</td>
<td>
<pre>
|$(sample body)
</pre>
</td>
</tr>
<tr>
<td>Irregular</td>
<td>None.</td>
</tr>
</table>
"""
    expected = """Tall: >
    |$  sample
    body
<
Wide: >
    |$(sample body)
<
Irregular: >
    None.
<"""
    table = helper.parse_html_table(text)
    assert table == expected


def test_clean_markdown_expected():
    given = """
Keep

{% table %}

- Form
- Syntax

---

- Tall
- ```hoon
  .=  p
  q
  ```

---

- Wide
- ```hoon
  .=(p q)
  ```

---

- Irregular
- None

{% /table %}

Keep
"""
    result = helper.clean_markdown(given)
    assert (
        result
        == """
Keep

Tall:

```hoon
.=  p
q
```

Wide:

```hoon
.=(p q)
```

Irregular:

- None

Keep
"""
    )


def test_clean_markdown_unexpected():
    given = """
Keep

{% table %}

Keep

{% /table %}

Keep
"""
    result = helper.clean_markdown(given)
    assert result == given
