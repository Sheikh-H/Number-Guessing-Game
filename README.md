<h1 align="center">🎯 Python Number Guessing Game</h1>

<p align="center">
  <b>A fun and interactive number guessing game built in Python.</b><br>
  <i>Guess the number, beat the clock, and compete for the top spot on the scoreboard!</i>
</p>

---

<h2>📘 Overview</h2>

<p>
<strong>Python Number Guessing Game</strong> is a console-based game where players attempt to guess a randomly generated number between 0 and 1000.  
It includes a <strong>real-time timer</strong>, <strong>leaderboard system</strong>, and <strong>data persistence</strong> using JSON files.
</p>

<p>
Your task? Guess the number as fast as possible and see your name rise to the top of the leaderboard.
</p>

---

<h2>🎮 Gameplay Flow</h2>

<ol>
  <li>Enter your name to start the game.</li>
  <li>The computer secretly picks a random number between <b>0</b> and <b>1000</b>.</li>
  <li>Keep guessing until you find the number — hints like <code>Go Higher!</code> or <code>Go Lower!</code> guide you.</li>
  <li>Your total time to find the number is recorded and added to the <b>leaderboard</b>.</li>
  <li>Compete with yourself or others to get the fastest time!</li>
</ol>

---

<h2>🧩 Features</h2>

<ul>
  <li>💡 <b>Randomized number generation</b> every playthrough</li>
  <li>⏱️ <b>Real-time timer</b> to measure your guessing speed</li>
  <li>🏆 <b>Leaderboard system</b> saved to <code>score_board.json</code></li>
  <li>🧹 <b>Reset scores</b> with one menu option</li>
  <li>💬 <b>Menu-driven interface</b> for easy navigation</li>
  <li>📂 <b>Automatic data saving</b> using JSON files</li>
  <li>🧠 <b>Digit-only input validation</b> prevents errors during gameplay</li>
</ul>

---

<h2>📂 Folder Structure</h2>

<pre>
Number-Guessing-Game/
│
├── main.py                     # Main game file
├── README.md                   # Project documentation
└── LICENCE                     # (MIT Licence)
</pre>

---

<h2>⚙️ How to Run the Game</h2>

<ol>
  <li>Ensure you have <strong>Python 3</strong> installed on your system.</li>
  <li>Download or clone this repository:</li>
</ol>

<pre><code>git clone https://github.com/Sheikh-H/Number-Guessing-Game.git</code></pre>

<ol start="3">
  <li>Navigate into the folder:</li>
</ol>

<pre><code>cd Number-Guessing-Game</code></pre>

<ol start="4">
  <li>Run the game:</li>
</ol>

<pre><code>python main.py</code></pre>

<p><i>Follow the instructions and see how quickly you can find the number!</i></p>

---

<h2>🧠 How It Works</h2>

<ul>
  <li><b>Random Number:</b> Generated between <code>0</code> and <code>1000</code> using <code>randint()</code>.</li>
  <li><b>Timer:</b> Starts when you begin guessing and stops when you find the correct number.</li>
  <li><b>Leaderboard:</b> Each player's time is stored in a JSON file and displayed in sorted order.</li>
  <li><b>Reset:</b> You can clear all scores at any time via the main menu.</li>
  <li><b>Cross-platform:</b> Works on both Windows and macOS/Linux (auto-detects <code>cls</code> or <code>clear</code>).</li>
</ul>

---

<h2>💻 Technologies Used</h2>

| Library | Purpose |
|----------|----------|
| <code>random</code> | Generates the random number for guessing |
| <code>time</code> | Controls timers and countdowns |
| <code>os</code> | Clears the console screen dynamically |
| <code>sys</code> | Manages text and output control |
| <code>json</code> | Saves and loads player scores persistently |

---

<h2>📊 Leaderboard System</h2>

<p>Scores are stored inside <code>score_board.json</code> as a simple JSON structure:</p>

<pre><code>{
  "scores": [
    {"player": "SHEIKH", "time": "01:23"},
    {"player": "ALICE", "time": "02:15"}
  ]
}
</code></pre>

<p>The leaderboard automatically sorts players by the fastest completion time.</p>

---

<h2>🏁 Example Gameplay</h2>

<pre>
*WELCOME TO THE PYTHON NUMBER GUESSING GAME*

1. Start Game
2. View Scoreboard
3. Reset Scores
4. Exit Game

What would you like to do?
> 1

Taking you to the game now...

We need to put your results on the scoreboard.
What is your name?
> Sheikh

Great 'SHEIKH'! Let's get you started...
The script has thought of a number between 0 and 1000.
Enter your guess:
> 500
Go higher!
> 750
Go lower!
> 650
Go higher!
> 670
You found the number!
SHEIKH! You finished in 01:23
</pre>

---

<h2>🚀 Future Improvements</h2>

<ul>
  <li>🎨 Add color-coded output for hints and results</li>
  <li>📈 Introduce difficulty levels (Easy / Medium / Hard)</li>
  <li>🧾 Add a score history view with timestamps</li>
  <li>💾 Store high scores in a database for multiplayer mode</li>
</ul>

---

<h2>📄 Licence</h2>

<p>
  This project is licenced under the <b>MIT Licence</b> — see the <a href="./LICENCE">LICENCE</a> file for details.
</p>

<pre>
MIT Licence

Copyright (c) 2025 Sheikh Hussain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
</pre>

---

## Footnote

<div align="center" style="border: 1px solid green; padding: 10px; border-radius: 5px;">
	<p>🗣️ Feel free to follow, connect, and chat!</p>
	<a class="header-badge" target="_blank" href="https://github.com/Sheikh-H"><img src="https://img.shields.io/badge/GitHub-376e00?style=flat&logo=github&logoColor=white" alt="GitHub">
	</a><a class="header-badge" target="_blank" href="https://www.linkedin.com/in/sheikh-hussain/"><img src="https://img.shields.io/badge/LinkedIn-376e00?style=flat&logo=LinkedIn&logoColor=white" alt="LinkedIn">
	</a><a class="header-badge" target="_blank" href="mailto:sheikh.hussain1155@gmail.com"><img src="https://img.shields.io/badge/Gmail-376e00?style=flat&logo=gmail&logoColor=white" alt="Gmail">
	</a><a class="header-badge" target="_blank" href="https://sheikh-hussain.onrender.com/"><img src="https://img.shields.io/badge/Portfolio-376e00?style=flat&logo=github&logoColor=white" alt="Portfolio">
	</a>
</div>

<div align="center">
	<a href="https://sheikh-hussain.onrender.com/" target="_blank">By Sheikh Hussain 💚</a>  
</div>

---
