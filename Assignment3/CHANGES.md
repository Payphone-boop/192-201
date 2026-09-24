# Assignment 03 — CHANGES

**Name:** Phone Pyae **Student ID:** 6705140070

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---
| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Products were stored as bare tuples. | Created a Product class with name, price, and category. | Classes / encapsulation | Ran the self-test → PASS. |
| 2 | Order items were stored as tuples with product indexes and quantities. | Created an OrderItem class containing a Product and quantity. | Composition / encapsulation | Ran the self-test → PASS. |
| 3 | Membership discounts used if/elif chains for each tier. | Created NoneCustomer, SilverCustomer, GoldCustomer, and PlatinumCustomer subclasses. | Inheritance / polymorphism | Ran the self-test → PASS. |
| 4 | Points used another if/elif chain for membership tiers. | Added points_multiplier() to the customer class family. | Polymorphism | Ran the self-test → PASS. |
| 5 | One large calc() function mixed calculations, printing, magic numbers, and a global variable. | Created an Order class with separate calculation and receipt methods and named constants. | Composition / encapsulation / separation of concerns | Ran the program in Docker with Python 3.12 → PASS. |

## 2 · Short reflection (4–6 sentences)

Which change improved the code the most, and why? Where did keeping the behaviour identical force you to be careful?

> _your reflection..._

 The change that improved the code the most was replacing the membership if/elif chains with a customer class family. Each customer type now has its own discount and points rules, which makes the code easier to understand and avoids repeating tier checks. Creating Product, OrderItem, and Order objects also made the relationships between the data clearer. Keeping the behaviour identical meant I had to be careful not to change the tax, discount, bulk discount, points, or receipt formatting. I checked the final program using the self-test in Docker, and it printed PASS.

## 3 · Prompt log (Level 2 — required)

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | "what to do this" | Explained the assignment requirements and what needed to be changed in Assignment_03.py and CHANGES.md. | Accepted | Compared the explanation with the assignment instructions. |
| 2 | "step by step" | Explained how to start the refactoring with named constants and then continue with the OOP design. | Accepted | Followed the steps in VS Code. |
| 3 | "ok give me all the fixed answer" | Provided the complete OOP refactored version with Product, OrderItem, Customer subclasses, Order, constants, and refactored_main(). | Edited | Ran the program and checked the self-test. |
| 4 | "i want to run it how to do it" | Explained how to run the Python file in VS Code and troubleshoot the Python execution problem. | Accepted | Tried the commands in the terminal. |
| 5 | "ok" / continued troubleshooting | Helped diagnose the Windows Application Control error and checked available Python, WSL, and Docker options. | Accepted | Checked the terminal results. |
| 6 | Docker execution step | Suggested running the assignment using Python 3.12 inside Docker. | Accepted | Ran the Docker command successfully and received PASS. |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [x] No tuples / parallel lists left — products, orders, and items are objects.
- [x] No `if tier == ...` chains — tiers are a class family.
- [x] Calculation methods **return** values and do not `print`; printing is separate.
- [x] Constructors validate state; no leftover `global`; magic numbers are named.
- [x] The change table and reflection above are filled in.
- [x] The prompt log is complete and the ownership statement is signed.
