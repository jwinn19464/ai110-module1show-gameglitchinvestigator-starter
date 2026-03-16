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
I used the Chat feature in VSCode. I also fed an error message for pytest into Gemini and learned how to properly run a command for using pytest on the terminal.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
An AI suggestion that was correct is to swap the text when it came to telling the user to go either higher or lower. Furthermore, it was able to pinpoint the lines responsible for the bug. After reading the explanationa and changing the code, I verified the result by launching the app and testing it on the site.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
An incorrect AI suggestion came up when I was putting in a FIXME comment to mark where a bug was. However, VSCode gave an incorrect suggestion, "    # FIXME: The range is currently hardcoded to 1-100 regardless of difficulty. This should be updated to return different ranges based on the selected difficulty level. This is now fixed by returning different low and high values based on the difficulty."
Although it is correct about having to change the hardcoding, it is incorrect in that it claims that it is fixed by returning different values based on difficulty. It has not actually been fixed.
Also, when I asked it to help me write pytest cases for bugs #2 and #3, it ignored bug #3 and instead wrote test cases addressing bug #4. I verified by reading the code myself as well as checking what I fed into the model.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I confirmed the bug was resolved by looking at the game’s state transition during a 'New Game' action. By monitoring st.session_state, I made sure that the app successfully clears previous attempts and history while resetting the status to 'playing.' This allows each person to start the game all over again,preventing old win/loss states from interfering with the new round's logic.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran a pytest case in the test_game_logic.py file for resetting the state of the game to verify that it cleared previous round data. The test set a fake state as an edge case with status="lost", non-empty history, and a previous score, then called reset_game_state. It showed state was fully reset (attempts 1, empty history, score 0, status playing, new secret), proving the reset logic works.

- Did AI help you design or understand any tests? How?
Yes. AI helped me to translate the bug descriptions that I wrote above into concrete state assertions and test names (e.g., “clears history” and “allows new round after loss”). With that, I now understand how to create and run tests more efficiently and effectively.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing in the original app because the app was generating a new random number on every rerun of Streamlit, which happens when the page refreshes.
The problem is resolved by saving the number in st.session_state, which tells Streamlit to remember it even when the page refreshes.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
By default, Streamlit does not remember what has been done previously. Every time someone clicks a button, moves a slider, or does anything in general, Streamlit reruns the entire script from line 1 to the end. It forgets everything that happened a second ago.
Since the app forgets everything on every rerun, session states are needed for the information to persist, rather than be deleted every time the app restarts.
- What change did you make that finally gave the game a stable secret number?
I changed the code to initialize the secret number only once and store it in session state. Then I used st.session_state.secret for guessing. This prevented random re-generation on each rerun and made the game stable.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  One strategy that I would like to reuse in future labs would be to use AI to help me test code by using it to generate pytest cases as I do not know how to use pytest yet. Another strategy would be to reference specific lines when using VS Code chat, in order to give it context when trying to fix a problem. Furthermore, I should make a new chat session for each bug in order to keep the AI focused on one problem at a time.

- What is one thing you would do differently next time you work with AI on a coding task?
I would go ahead and plan my project in advance. Then, I would use AI mainly as a tool to speed up production. Furthermore, going forward, I am going to feed the AI one problem at a time so that it maintains its focus.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
Despite the influx of influencers and youtube videos depicting AI as something that can generate great, production-ready code in an instant, AI generated code is still very flawed and buggy -- even if the AI itself thinks that it's production-ready. Therefore, I need to approach AI generated code with a more critical eye.
