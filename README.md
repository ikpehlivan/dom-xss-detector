\# DOM XSS Detector



DOM XSS Detector is a lightweight static analysis tool designed to identify potential DOM-based Cross-Site Scripting (DOM XSS) vulnerabilities in JavaScript code.



It scans JavaScript files for **dangerous source-to-sink flows** commonly used in DOM XSS attacks.



This tool is intended for:



\- Security Researchers

\- Bug Bounty Hunters

\- Penetration Testers

\- Application Security Engineers



---



\## Features



\- Detects common **DOM XSS Sources**

\- Detects dangerous **DOM XSS Sinks**

\- Highlights potential **source → sink flows**

\- Supports scanning:

&nbsp; - Single JavaScript files

&nbsp; - Entire directories

\- Lightweight and fast

\- No external dependencies



---



\## Detection Logic



The tool searches for patterns where **user-controllable sources** may flow into **dangerous sinks**.



---



\### Sources



Examples of attacker-controlled sources:

location

location.href

location.search

location.hash

document.URL

document.documentURI

document.referrer

window.name



---



\### Sinks



Potentially dangerous sinks:

innerHTML

outerHTML

document.write

document.writeln

eval

setTimeout

setInterval

Function

insertAdjacentHTML



If both a source and sink appear in suspicious contexts, the tool highlights them as potential **DOM XSS candidates**.



---

\## Installation



Clone the repository:



```bash

git clone https://github.com/ikpehlivan/dom-xss-detector

cd dom-xss-detector



Usage

Scan a single JavaScript file:

python domxss.py app.js



Scan an entire directory:

python domxss.py ./js/

Example Output

Scanning: app.js

----------------------------------------

\[HIGH] Possible DOM XSS

Line 12

Source: \['location.search']

Sink: \['innerHTML']

Example Vulnerable Code

var q = location.search;

document.getElementById("output").innerHTML = q;

```



No dependencies required.

