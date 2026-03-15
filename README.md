<div align="center">

<img src="op.png" width="80">

<h1 style="color:#3b82f6;">DevPulse</h1>

<h3 style="color:#555;">
AI-Powered Code Intelligence CLI
</h3>

<p>
<b>Understand Your Codebase Instantly ⚡</b><br>
DevPulse analyzes repositories, detects patterns, and helps developers improve productivity.
</p>

<p>

<img src="https://img.shields.io/badge/python-≥3.8-blue?logo=python&logoColor=white">
<img src="https://img.shields.io/badge/interface-CLI-green">
<img src="https://img.shields.io/badge/analysis-code_quality-purple">
<img src="https://img.shields.io/badge/output-JSON_%2B_Human-blueviolet">
<img src="https://img.shields.io/badge/license-MIT-yellow">

</p>

<img src="assets/demo.gif" width="800">

</div>

<hr>

<h2 style="color:#10b981;">🧠 What is DevPulse?</h2>

<p>

<b style="color:#3b82f6;">DevPulse</b> is a <b>developer productivity tool</b> designed to analyze source code repositories and provide insights about code structure, quality, and project activity.

</p>

<blockquote>
<b>Goal:</b> Help developers understand their codebase faster.
</blockquote>

<p>DevPulse scans projects and produces:</p>

<ul>
<li><b style="color:#2563eb;">Repository statistics</b></li>
<li><b style="color:#2563eb;">Programming language breakdown</b></li>
<li><b style="color:#2563eb;">TODO / FIXME tracking</b></li>
<li><b style="color:#2563eb;">Code quality indicators</b></li>
<li><b style="color:#2563eb;">Developer productivity insights</b></li>
</ul>

<p><b>Built for:</b></p>

<ul>
<li>👨‍💻 Individual developers</li>
<li>🌍 Open source maintainers</li>
<li>🏢 Development teams</li>
<li>🎓 Students learning large codebases</li>
</ul>

<hr>

<h2 style="color:#f59e0b;">🚀 Quick Start</h2>

<h3>Install from PyPI</h3>

<pre>
pip install devpulse-tool
</pre>

<h3>Scan a project</h3>

<pre>
devpulse scan .
</pre>

<h3>Example Output</h3>

<pre>
Scanning project...

Files scanned: 82

Languages detected
- Python: 76%
- Markdown: 15%
- JSON: 9%

TODO items: 12
Code health score: 8.1 / 10
</pre>

<hr>

<h2 style="color:#6366f1;">⚡ CLI Commands</h2>

<h4>Scan repository</h4>

<pre>
devpulse scan .
</pre>

<h4>Analyze code quality</h4>

<pre>
devpulse analyze .
</pre>

<h4>Developer productivity metrics</h4>

<pre>
devpulse dashboard
</pre>

<h4>Generate AI commit message</h4>

<pre>
devpulse ai-commit
</pre>

<hr>

<h2 style="color:#10b981;">✨ Features</h2>

<h3>📊 Repository Analysis</h3>

<p>DevPulse scans project files to detect:</p>

<ul>
<li>Programming languages</li>
<li>File distribution</li>
<li>Project complexity</li>
</ul>

<h3>🧾 TODO &amp; FIXME Detection</h3>

<p>Automatically detects developer notes:</p>

<pre>
# TODO
# FIXME
# HACK
</pre>

<p>Useful for tracking unfinished work.</p>

<h3>📈 Code Quality Insights</h3>

<ul>
<li>Repository structure</li>
<li>Comment density</li>
<li>TODO accumulation</li>
<li>Project organization</li>
</ul>

<h3>🤖 AI Developer Tools</h3>

<p>Future AI features include:</p>

<ul>
<li>AI commit message generation</li>
<li>Automated code review hints</li>
<li>Developer productivity metrics</li>
</ul>

<hr>

<h2 style="color:#ef4444;">🏗 Architecture</h2>

<pre>
devpulse/
│
├── cli.py
│     CLI entry point
│
├── scanner.py
│     repository scanning engine
│
├── analyzer.py
│     code analysis engine
│
├── dashboard.py
│     developer statistics
│
├── ai_commit.py
│     AI commit message generator
│
└── utils.py
      helper utilities
</pre>

<h3>Core Modules</h3>

<table>
<tr>
<th>Module</th>
<th>Purpose</th>
</tr>

<tr>
<td><b>scanner</b></td>
<td>scans files and directories</td>
</tr>

<tr>
<td><b>analyzer</b></td>
<td>calculates project metrics</td>
</tr>

<tr>
<td><b>dashboard</b></td>
<td>visualizes repository stats</td>
</tr>

<tr>
<td><b>ai_commit</b></td>
<td>generates commit messages</td>
</tr>

<tr>
<td><b>utils</b></td>
<td>shared helper logic</td>
</tr>

</table>

<hr>

<h2 style="color:#8b5cf6;">⚙️ How DevPulse Works</h2>

<h3>1️⃣ Repository Scanning</h3>

<ul>
<li>File types</li>
<li>Language detection</li>
<li>Project structure</li>
</ul>

<h3>2️⃣ Code Analysis</h3>

<ul>
<li>TODO counts</li>
<li>File statistics</li>
<li>Complexity indicators</li>
<li>Codebase health score</li>
</ul>

<h3>3️⃣ Insight Generation</h3>

<ul>
<li>Language breakdown</li>
<li>Developer productivity metrics</li>
<li>Improvement suggestions</li>
</ul>

<hr>

<h2 style="color:#3b82f6;">📊 Example Output</h2>

<pre>
Project: devpulse

Files scanned: 56

Languages
Python: 88%
Markdown: 12%

TODO items: 7
FIXME items: 2

Code Quality Score: 8.3 / 10
</pre>

<hr>

<h2 style="color:#f43f5e;">🧩 Plugin Architecture</h2>

<p>DevPulse supports future plugins.</p>

<pre>
devpulse/plugins/

security_scanner.py
performance_analyzer.py
dependency_audit.py
documentation_generator.py
</pre>

<p>Plugins will hook into the analysis pipeline.</p>

<hr>

<h2 style="color:#10b981;">🧪 Testing</h2>

<pre>
pytest
</pre>

<p>Coverage includes:</p>

<ul>
<li>CLI functionality</li>
<li>Scanning engine</li>
<li>Analyzer module</li>
</ul>

<hr>

<h2 style="color:#f59e0b;">📦 Development Setup</h2>

<h4>Clone repository</h4>

<pre>
git clone https://github.com/manucian-official/devpulse.git
</pre>

<h4>Enter directory</h4>

<pre>
cd devpulse
</pre>

<h4>Install dev mode</h4>

<pre>
pip install -e .
</pre>

<h4>Run CLI</h4>

<pre>
devpulse scan .
</pre>

<hr>

<h2 style="color:#6366f1;">🧭 DevPulse Vision</h2>

<p>DevPulse aims to become a <b>Developer Intelligence Platform</b>.</p>

<ul>
<li>AI code review assistant</li>
<li>Commit quality scoring</li>
<li>Repository health dashboard</li>
<li>GitHub integration</li>
<li>Developer productivity analytics</li>
</ul>

<p><b>Long-term goal:</b></p>

<blockquote>
Transform raw source code into actionable developer insights.
</blockquote>

<hr>

<h2 style="color:#22c55e;">🤝 Contributing</h2>

<ol>
<li>Fork the repository</li>
<li>Create a new branch</li>
<li>Implement your feature</li>
<li>Submit a pull request</li>
</ol>

<hr>

<h2 style="color:#eab308;">📄 License</h2>

<p>MIT License</p>

<hr>

<div align="center">

<h3>⭐ Support the Project</h3>

<p>If DevPulse helps you analyze code faster, consider giving the project a star.</p>

<h2 style="color:#3b82f6;">DevPulse</h2>

<b>Code Intelligence for Developers</b>

</div>
