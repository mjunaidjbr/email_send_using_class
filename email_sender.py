import subprocess

subprocess.run(["pip", "install", "yagmail"])
import yagmail

receiver = "raojunaidjabbar1999@gmail.com"
body = "Hello there from Yagmail"
filename = ["a.txt", "b.txt", "a.py"]
a = "bcv"
b = """{a}"""
html = """<!-- #######  THIS IS A COMMENT - Visible only in the source editor #########-->
<h2>Welcome To The Best Online HTML Web Editor!</h2>
<p style="font-size: 1.5em;">You can <strong style="background-color: #317399; padding: 0 5px; color: #fff;">type your text</strong> directly in the editor or paste it from a Word Doc, PDF, Excel etc.</p>
<p style="font-size: 1.5em;">The <strong>visual editor</strong> on the right and the <strong>source editor</strong> on the left are linked together and the changes are reflected the other one as you type! <img src="https://html5-editor.net/images/smiley.png" alt="smiley" /></p>
<table class="editorDemoTable">
<tbody>
<tr>
<td><strong>Name</strong></td>
<td><strong>City</strong></td>
<td><strong>age</strong></td>
</tr>
<tr>
<td>John</td>
<td>Chicago</td>
<td>23</td>
</tr>
<tr>
<td>Lucy</td>
<td>Wisconsin</td>
<td>19</td>
</tr>
<tr>
<td>Amanda</td>
<td>Madison</td>
<td>22</td>
</tr>
</tbody>
</table>
<p>This is a table you can experiment with.</p>
<p>&nbsp;</p>"""

yag = yagmail.SMTP("raojunaidjabbar1999@gmail.com")
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=[body, html],
    attachments=filename,
)
