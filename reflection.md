# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

Things that were broken at the start:
1. When I typed in a number, there was text that said, "Press Enter to apply". However, when I pressed Enter, nothing happened. I would think that pressing Enter would be the same as pressing the Submit Guess button.
2. The hint is incorrect. They are switched around. My first guess is 50 and it told me to go higher. Eventually, I guessed 100 and it still told me to go higher, even though it said "Guess a number between 1 and 100." Turns out, the secret number is 1. On the other hand, guessing a number lower than the secret number gives a "Go LOWER" message instead of the expected, "Go HIGHER" message.
3. Clicking on New Game just changes the secret number. It doesn't clear the history. Even changing the difficulty does not clear the history. In other words, there is no way to start a new game other than restarting the app or refreshing the page. The attempts of the previous round roll over. Clicking the New Game button does not clear the win or lose message either. Even if there's still attempts leftover, the game no longer accepts inputs even though the secret number has changed.
4. The difficulty and the range of numbers do not match. Easy says that it has a range of 1 to 20, yet the game said to guess a number between 1 and 100. Normal is said to have a range of 1 to 100 while hard has a range of 1 to 50, which doesn't make sense as it should be the other way around. All of the difficulty levels are the same. There is no real difference between easy, normal, and hard. The number of attempts allowed seem to be arbitrary too.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
