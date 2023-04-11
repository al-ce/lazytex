| Equivalence | Law |
| --------- | --- |
| $\ \ \ \ \ [(p \to q) \ \land \ (q \to r)] \to (p \to r) \ \equiv \ \mathbf{t}$ | --- |
| $\ \equiv \ [(\sim p \ \lor \ q) \ \land \ (q \to r)] \to (p \to r)$ | by implication |
| $\ \equiv \ [(\sim p \ \lor \ q) \ \land \ (\sim q \ \lor \ r)] \to (p \to r)$ | by implication |
| $\ \equiv \ [(\sim p \ \lor \ q) \ \land \ (\sim q \ \lor \ r)] \to (\sim p \ \lor \ r)$ | by implication |
| $\ \equiv \ \sim [(\sim p \ \lor \ q) \ \land \ (\sim q \ \lor \ r)] \ \lor \ (\sim p \ \lor \ r)$ | by implication |
| $\ \equiv \ [\sim (\sim p \ \lor \ q) \ \lor \ \sim (\sim q \ \lor \ r)] \ \lor \ (\sim p \ \lor \ r)$ | by De Morgan's law |
| $\ \equiv \ [(p \ \land \ \sim q) \ \lor \ \sim (\sim q \ \lor \ r)] \ \lor \ (\sim p \ \lor \ r)$ | by De Morgan's law and double negation |
| $\ \equiv \ [(p \ \land \ \sim q) \ \lor \ (q \ \land \ \sim r)] \ \lor \ (\sim p \ \lor \ r)$ | by De Morgan's law and double negation |
| $\ \equiv \ (p \ \land \ \sim q) \ \lor \ (q \ \land \ \sim r) \ \lor \ \sim p \ \lor \ r$ | by associative law |
| $\ \equiv \ \sim p \ \lor \ (p \ \land \ \sim q) \ \lor \ (q \ \land \ \sim r) \ \lor \ r$ | by commutative law |
| $\ \equiv \ [(\sim p \ \lor \ p) \ \land \ (\sim p \ \lor \ \sim q)] \ \lor \ (q \ \land \ \sim r) \ \lor \ r$ | by distributive law |
| $\ \equiv \ [\mathbf{t} \ \land \ (\sim p \ \lor \ \sim q)] \ \lor \ (q \ \land \ \sim r) \ \lor \ r$ | by negation law |
| $\ \equiv \ (\sim p \ \lor \ \sim q) \ \lor \ (q \ \land \ \sim r) \ \lor \ r$ | by identity law |
| $\ \equiv \ (\sim p \ \lor \ \sim q) \ \lor \ r \ \lor \ (q \ \land \ \sim r)$ | by commutative law |
| $\ \equiv \ (\sim p \ \lor \ \sim q) \ \lor \ ((r \ \lor \ q) \ \land \ (r \ \lor \ \sim r))$ | by distributive law |
| $\ \equiv \ (\sim p \ \lor \ \sim q) \ \lor \ [ (r \ \lor \ q) \ \land \ \mathbf{t}]$ | by negation law |
| $\ \equiv \ (\sim p \ \lor \ \sim q) \ \lor \ (r \ \lor \ q)$ | by identity law |
| $\ \equiv \ \sim p \ \lor \ \sim q \ \lor \ r \ \lor \ q$ | by associative law |
| $\ \equiv \ q \ \lor \ \sim q \ \lor \ r \ \lor \ \sim p$ | by commutative law |
| $\ \equiv \ (q \ \lor \ \sim q) \ \lor \ r \ \lor \ \sim p$ | by associative law |
| $\ \equiv \ \mathbf{t} \ \lor \ r \ \lor \ \sim p$ | by negation law |
| $\ \equiv \ \mathbf{t}$ | by universal bound law |
