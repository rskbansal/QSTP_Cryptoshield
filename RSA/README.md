# RSA
## Euler's Totient Function
The Euler's Totient Function is defined as the number of positive integers less than or equal to n that are relatively prime to n. It is denoted by phi(n). The formula for phi(n) is as follows:
```math
\begin{align}
\phi(n)=\phi\big(p_1^{e_1}\ldots p_k^{e_k}\big)&=\phi\big(p_1^{e_1}\big)\ldots\phi\big(p_k^{e_k}\big) \\ &=p_1^{e_1}\left( 1-\frac1{p_1}\right) \cdots p_k^{e_k} \left( 1-\frac1{p_k} \right) \\ &= \big(p_1^{e_1}\ldots p_k^{e_k}\big) \left( 1-\frac1{p_1} \right) \cdots \left( 1-\frac1{p_k} \right) \\ &= n\left( 1-\frac1{p_1} \right) \cdots \left( 1-\frac1{p_k} \right).\ _\square
\end{align}
```
where p1, p2, ..., pk are the prime factors of n.
