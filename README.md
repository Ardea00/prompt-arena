# 🎯 Prompt Arena

A competitive prompting game for the Meeting 2 hands-on session. **Three minigames, all played on Microsoft Copilot** (the only sanctioned LLM). The app can't see Copilot, so players **paste Copilot's answer back in** and the Arena auto-scores. A shared leaderboard runs on the projector.

## Run it locally

```bash
cd prompt-arena
pip install -r requirements.txt
streamlit run app.py
# if `streamlit` isn't on PATH:  python -m streamlit run app.py
```

Open the **Network URL** Streamlit prints (e.g. `http://172.16.x.x:8501`) and put it on the projector. If you want everyone submitting to the *same* leaderboard, run one instance and share that Network URL on the room Wi-Fi.

## Deploy free on Streamlit Community Cloud

So attendees can reach it from any network (not just the room Wi-Fi):

1. Push this folder to a GitHub repo (see below).
2. Go to **https://share.streamlit.io** → sign in with GitHub → **New app**.
3. Pick the repo, branch `main`, main file **`app.py`** → **Deploy**.
4. You get a public URL like `https://prompt-arena.streamlit.app` — put that on the Arena slide.

> Note: the leaderboard is **in-memory per session**. On a shared cloud deployment each viewer has their own session, so use the **⬇️ Download answers (.md)** button to collect everyone's submissions and build the official leaderboard. For a single shared live board, run it locally on one laptop and share the Network URL instead.

## The three minigames

| # | Game | Goal | How it scores |
|---|------|------|---------------|
| ⛳ | **Prompt Golf** | Make Copilot output an exact target in the **fewest characters** | Exact match → `300 − chars` points; shorter prompt wins |
| 🔓 | **Jailbreak** | Try to break the escalation agent's guardrails | Detects rule-breaks in the pasted reply; breaking "wins" (and teaches why the rule matters) |
| 👻 | **Hallucination Hunt** | Make Copilot **admit it doesn't know** instead of inventing | Rewards honest "not in the folder" answers; flags fabrications |

## How a round works (say this to the room)

1. Pick a game tab, read the challenge card.
2. Type your prompt **into Microsoft Copilot** (Copilot Chat / Teams).
3. Copy Copilot's answer, **paste it back into the Arena**.
4. Hit the score button → points land on the **Leaderboard** tab.

## Why paste-back instead of calling an LLM?

It keeps the game **on Copilot** (compliant, no API keys, works whatever the license situation), and it's **self-scoring** — the page needs no internet and no model of its own. It also makes players *read* Copilot's output, which is the whole point.

## The official leaderboard (download → Claude)

The in-app score is a fast keyword/length **party judge** — fine to drive the live banter, but it can't fairly rank a clever prompt. So on the **Leaderboard** tab there's a **⬇️ Download answers (.md)** button. It exports every submission — player, game, auto-score, and the **raw prompt + Copilot answer**. After the games:

1. Click **Download answers (.md)**.
2. Hand that file to Claude ("build the real leaderboard from this").
3. Claude re-judges the creative entries the keyword scorer under/over-rated and produces the official ranking.

## Notes

- Leaderboard is in-memory (resets when the app restarts). **Reset** button for a fresh round; **Download** first if you want to keep the data.
- ION-themed to match the deck.
