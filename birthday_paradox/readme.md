# Day 2: Birthday Paradox

## Concept

The Birthday Paradox states that in a group of just **23 people**, there's a **greater than 50% chance** that **two people share the same birthday** — despite there being 365 possible birthdays.

This counterintuitive result arises due to the number of pairwise comparisons increasing rapidly with group size.

## Simulation Approach

- Randomly generate birthdays for a group of `n` people.
- Repeat this for many simulations.
- Count how often at least two people share a birthday.
- Estimate the probability by taking the ratio of such events.

## Output

The program prints approximate probabilities for group sizes from 5 to 50 in steps of 5.

## Reference

This is an empirical simulation — actual probabilities can be derived mathematically and are well-documented in probability theory.
