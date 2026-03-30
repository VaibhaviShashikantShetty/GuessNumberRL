# Guess Number RL Environment

## 📌 Overview
This project implements a simple reinforcement learning environment where an agent tries to guess a secret number within a limited number of attempts.

The environment provides feedback after each guess and assigns rewards based on performance.

---

## 🧠 Environment Description

- The agent must guess a number between **1 and 10**
- After each guess, feedback is given:
  - `"too low"`
  - `"too high"`
  - `"correct"`

---

## 🎯 Reward Function

- Correct guess → `+10`
- Close guess (difference = 1) → `+2`
- Incorrect guess → `-1`

This encourages efficient and accurate guessing.

---

## 🔄 Episode Flow

1. Environment resets with a random number
2. Agent makes guesses
3. Environment updates range (`low`, `high`)
4. Episode ends when:
   - Correct guess OR
   - Maximum attempts reached

---

## 📦 Project Structure
