# 🌟 HackerRank Software Engineer Certification  
Practice & Preparation Hub 🌟

![HackerRank Badge](https://img.shields.io/badge/HackerRank-Software%20Engineer%20Certification-blue?style=for-the-badge&logo=hackerrank&logoColor=white&labelColor=2E2E2E)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=for-the-badge)
![Last Updated](https://img.shields.io/badge/Updated-January%202026-success?style=for-the-badge)

Welcome to my personal preparation repository for the **HackerRank Software Engineer Certification** (role-based assessment)!

This repo is designed to help you (and me!) understand exactly what kinds of questions appear, how they are structured, and what skills are being tested — **without spoiling full solutions**.

> **Goal**: Prepare smartly → understand patterns → build confidence → pass with flying colors! 🚀

## 📊 Certification at a Glance

| Aspect              | Details                                      |
|---------------------|----------------------------------------------|
| **Format**          | 2–4 questions (usually 1–2 coding + SQL + API) |
| **Duration**        | 90–120 minutes                               |
| **Scoring**         | Partial credit possible                      |
| **Languages**       | Python, Java, C#, JavaScript, C++, etc.      |
| **Main Skills**     | Greedy / Sorting • SQL Window Functions • REST API Basics |

## ✨ What's Inside This Repo

### 1. Conference Schedule  
**Classic Greedy – Maximum Non-Overlapping Presentations**

**Icon**: 🗓️📅  
**Category**: Greedy Algorithms · Interval Scheduling · Activity Selection  

You are given:  
- `scheduleStart[]` – array of start times  
- `scheduleEnd[]` – array of end times  

**Task**: Find the **maximum number** of presentations one person can attend without any overlap.

**Important Rules**  
✅ End time of one == start time of next → **allowed**  
✅ Must attend **entire** presentation  
❌ No overlapping intervals

**Constraints** (typical)  
- 1 ≤ n ≤ 100,000  
- 0 ≤ start[i] < end[i] ≤ 1,000,000,000

**Winning Strategy Hint**  
Sort by **earliest ending time** → greedily select next possible session

---

### 2. SQL Section – Real-World Patterns

**Icon**: 🗄️📊  
**Category**: Database Queries · Window Functions · Aggregation

**Most common question types seen**:

- Second-highest / Nth-highest salary per department  
- Ranking employees / events within groups (DENSE_RANK, ROW_NUMBER, RANK)  
- Counting errors, conflicts, duplicates per user / department  
- Aggregates + HAVING clauses  
- Running totals / cumulative sums  
- Comparing consecutive rows (LAG / LEAD)

**Frequently used tables**:

- `employees` (employee_id, name, department, salary)  
- `presentations` / `events` (id, start_time, end_time, employee_id)  
- `logs` (log_id, employee_id, event_type, timestamp)

**Pro Tip**: Master `DENSE_RANK()`, `PARTITION BY`, and `HAVING COUNT(*) > 1`

---

### 3. REST API Implementation

**Icon**: 🌐🔌  
**Category**: Backend Development · API Design · HTTP Basics

**Typical Task**  
Implement a simple endpoint like:
Best of luck with your HackerRank Software Engineer Certification!
You’ve got this! 💪✨
Feel free to star ⭐, fork, or open a PR with your own notes, variations, or tips.
Last updated: January 2026
Prepared with ❤️ by Tanushree
