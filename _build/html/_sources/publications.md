# Publications 

 Ce document présente une liste de publications ayant bénéficié du programme HQI.

  ```{important} 
 La plupart des publications sont référencées sur le portail <a href="https://haltools.archives-ouvertes.fr/Public/afficheRequetePubli.php?projet_anr=ANR-22-PNCQ-0002&CB_auteur=oui&CB_titre=oui&CB_DOI=oui&CB_resume=oui&langue=Francais&tri_exp=annee_publi&tri_exp2=typdoc&tri_exp3=date_publi&ordre_aff=TA&CB_rubriqueDiv=oui&Fen=Aff&css=../css/VisuCondense.css">HAL HQI-R&D Support</a> et <a href="https://haltools.archives-ouvertes.fr/Public/afficheRequetePubli.php?projet_anr=ANR-22-PNCQ-0001&CB_auteur=oui&CB_titre=oui&CB_DOI=oui&CB_resume=oui&langue=Francais&tri_exp=annee_publi&tri_exp2=typdoc&tri_exp3=date_publi&ordre_aff=TA&CB_rubriqueDiv=oui&Fen=Aff&css=../css/VisuCondense.css">HAL HQI-Acquisition</a>. Cependant, certaines publications étant mal référencées, vous trouverez ici les preprints ArXiV.
 ``` 
## Langage de programmation

### A programming language characterizing quantum polynomial time

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2212.06656v1)

**Date de publication :** 13/12/2022

**Auteur(s) :**
- Emmanuel Hainry
- Romain Péchoux
- Mário Silva

**Résumé :**
We introduce a first-order quantum programming language, named FOQ, whose
terminating programs are reversible. We restrict FOQ to a strict and tractable
subset, named PFOQ, of terminating programs with bounded width, that provides a
first programming language-based characterization of the quantum complexity
class FBQP. Finally, we present a tractable semantics-preserving algorithm
compiling a PFOQ program to a quantum circuit of size polynomial in the number
of input qubits.

### Quantum Expectation Transformers for Cost Analysis

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2201.09361v1)

**Date de publication :** 23/01/2022

**Auteur(s) :**
- Martin Avanzini
- Georg Moser
- Romain Péchoux
- Simon Perdrix
- Vladimir Zamdzhiev

**Résumé :**
We introduce a new kind of expectation transformer for a mixed
classical-quantum programming language. Our semantic approach relies on a new
notion of a cost structure, which we introduce and which can be seen as a
specialisation of the Kegelspitzen of Keimel and Plotkin. We show that our
weakest precondition analysis is both sound and adequate with respect to the
operational semantics of the language. Using the induced expectation
transformer, we provide formal analysis methods for the expected cost analysis
and expected value analysis of classical-quantum programs. We illustrate the
usefulness of our techniques by computing the expected cost of several
well-known quantum algorithms and protocols, such as coin tossing, repeat until
success, entangled state preparation, and quantum walks.

### Qimaera: Type-safe (Variational) Quantum Programming in Idris

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2111.10867v1)

**Date de publication :** 21/11/2021

**Auteur(s) :**
- Liliane-Joy Dandy
- Emmanuel Jeandel
- Vladimir Zamdzhiev

**Résumé :**
Variational Quantum Algorithms are hybrid classical-quantum algorithms where
classical and quantum computation work in tandem to solve computational
problems. These algorithms create interesting challenges for the design of
suitable programming languages. In this paper we introduce Qimaera, which is a
set of libraries for the Idris 2 programming language that enable the
programmer to implement (variational) quantum algorithms where the full power
of the elegant Idris language works in synchrony with quantum programming
primitives that we introduce. The two key ingredients of Idris that make this
possible are (1) dependent types which allow us to implement unitary (i.e.
reversible and controllable) quantum operations; and (2) linearity which allows
us to enforce fine-grained control over the execution of quantum operations
that ensures compliance with the laws of quantum mechanics. We demonstrate that
Qimaera is suitable for variational quantum programming by providing
implementations of the two most prominent variational quantum algorithms --
QAOA and VQE. To the best of our knowledge, this is the first implementation of
these algorithms that has been achieved in a type-safe framework.

### Addition and Differentiation of ZX-diagrams

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2202.11386v5)

**Date de publication :** 23/02/2022

**Auteur(s) :**
- Emmanuel Jeandel
- Simon Perdrix
- Margarita Veshchezerova

**Résumé :**
The ZX-calculus is a powerful framework for reasoning in quantum computing.
It provides in particular a compact representation of matrices of interests. A
peculiar property of the ZX-calculus is the absence of a formal sum allowing
the linear combinations of arbitrary ZX-diagrams. The universality of the
formalism guarantees however that for any two ZX-diagrams, the sum of their
interpretations can be represented by a ZX-diagram. We introduce a general,
inductive definition of the addition of ZX-diagrams, relying on the
construction of controlled diagrams. Based on this addition technique, we
provide an inductive differentiation of ZX-diagrams.
  Indeed, given a ZX-diagram with variables in the description of its angles,
one can differentiate the diagram according to one of these variables.
Differentiation is ubiquitous in quantum mechanics and quantum computing (e.g.
for solving optimization problems). Technically, differentiation of ZX-diagrams
is strongly related to summation as witnessed by the product rules.
  We also introduce an alternative, non inductive, differentiation technique
rather based on the isolation of the variables. Finally, we apply our results
to deduce a diagram for an Ising Hamiltonian.

### LOv-Calculus: A Graphical Language for Linear Optical Quantum Circuits

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2204.11787v1)

**Date de publication :** 25/04/2022

**Auteur(s) :**
- Alexandre Clément
- Nicolas Heurtel
- Shane Mansfield
- Simon Perdrix
- Benoît Valiron

**Résumé :**
We introduce the LOv-calculus, a graphical language for reasoning about
linear optical quantum circuits with so-called vacuum state auxiliary inputs.
We present the axiomatics of the language and prove its soundness and
completeness: two LOv-circuits represent the same quantum process if and only
if one can be transformed into the other with the rules of the LOv-calculus. We
give a confluent and terminating rewrite system to rewrite any
polarisation-preserving LOv-circuit into a unique triangular normal form,
inspired by the universal decomposition of Reck et al. (1994) for linear
optical quantum circuits.

### Perceval: A Software Platform for Discrete Variable Photonic Quantum Computing

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2204.00602v3)

**Date de publication :** 01/04/2022

**Auteur(s) :**
- Nicolas Heurtel
- Andreas Fyrillas
- Grégoire de Gliniasty
- Raphaël Le Bihan
- Sébastien Malherbe
- Marceau Pailhas
- Eric Bertasi
- Boris Bourdoncle
- Pierre-Emmanuel Emeriau
- Rawad Mezher
- Luka Music
- Nadia Belabas
- Benoît Valiron
- Pascale Senellart
- Shane Mansfield
- Jean Senellart

**Résumé :**
We introduce Perceval, an open-source software platform for simulating and
interfacing with discrete-variable photonic quantum computers, and describe its
main features and components. Its Python front-end allows photonic circuits to
be composed from basic photonic building blocks like photon sources, beam
splitters, phase-shifters and detectors. A variety of computational back-ends
are available and optimised for different use-cases. These use state-of-the-art
simulation techniques covering both weak simulation, or sampling, and strong
simulation. We give examples of Perceval in action by reproducing a variety of
photonic experiments and simulating photonic implementations of a range of
quantum algorithms, from Grover's and Shor's to examples of quantum machine
learning. Perceval is intended to be a useful toolkit for experimentalists
wishing to easily model, design, simulate, or optimise a discrete-variable
photonic experiment, for theoreticians wishing to design algorithms and
applications for discrete-variable photonic quantum computing platforms, and
for application designers wishing to evaluate algorithms on available
state-of-the-art photonic quantum computers.

## Physique

### Efficient and robust estimation of many-qubit Hamiltonians

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2205.09567v2)

**Date de publication :** 19/05/2022

**Auteur(s) :**
- Daniel Stilck França
- Liubov A. Markovich
- V. V. Dobrovitski
- Albert H. Werner
- Johannes Borregaard

**Résumé :**
Characterizing the interactions and dynamics of quantum mechanical systems is
an essential task in the development of quantum technologies. We propose an
efficient protocol based on the estimation of the time derivatives of few qubit
observables using polynomial interpolation for characterizing the underlying
Hamiltonian dynamics and Markovian noise of a multi-qubit device. For finite
range dynamics, our protocol exponentially relaxes the necessary time
resolution of the measurements and quadratically reduces the overall sample
complexity compared to previous approaches. Furthermore, we show that our
protocol can characterize the dynamics of systems with algebraically decaying
interactions. The implementation of the protocol requires only the preparation
of product states and single-qubit measurements. Furthermore, we develop a
shadow tomography method for quantum channels that is of independent interest.
This protocol can be used to parallelize to learn the Hamiltonian, rendering it
applicable for the characterization of both current and future quantum devices.

### Efficient learning of ground & thermal states within phases of matter

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2301.12946v2)

**Date de publication :** 30/01/2023

**Auteur(s) :**
- Emilio Onorati
- Cambyse Rouzé
- Daniel Stilck França
- James D. Watson

**Résumé :**
We consider two related tasks: (a) estimating a parameterisation of a given
Gibbs state and expectation values of Lipschitz observables on this state; and
(b) learning the expectation values of local observables within a thermal or
quantum phase of matter. In both cases, we wish to minimise the number of
samples we use to learn these properties to a given precision.
  For the first task, we develop new techniques to learn parameterisations of
classes of systems, including quantum Gibbs states of non-commuting
Hamiltonians with exponential decay of correlations and the approximate Markov
property. We show it is possible to infer the expectation values of all
extensive properties of the state from a number of copies that not only scales
polylogarithmically with the system size, but polynomially in the observable's
locality -- an exponential improvement. This set of properties includes
expected values of quasi-local observables and entropies.
  For the second task, we develop efficient algorithms for learning observables
in a phase of matter of a quantum system. By exploiting the locality of the
Hamiltonian, we show that $M$ local observables can be learned with probability
$1-\delta$ to precision $\epsilon$ with using only
$N=O\big(\log\big(\frac{M}{\delta}\big)e^{polylog(\epsilon^{-1})}\big)$ samples
-- an exponential improvement on the precision over previous bounds. Our
results apply to both families of ground states of Hamiltonians displaying
local topological quantum order, and thermal phases of matter with exponential
decay of correlations. In addition, our sample complexity applies to the worse
case setting whereas previous results only applied on average.
  Furthermore, we develop tools of independent interest, such as robust shadow
tomography algorithms, Gibbs approximations to ground states, and
generalisations of transportation cost inequalities for Gibbs states.

### Provably Efficient Learning of Phases of Matter via Dissipative Evolutions

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2311.07506v1)

**Date de publication :** 13/11/2023

**Auteur(s) :**
- Emilio Onorati
- Cambyse Rouzé
- Daniel Stilck França
- James D. Watson

**Résumé :**
The combination of quantum many-body and machine learning techniques has
recently proved to be a fertile ground for new developments in quantum
computing. Several works have shown that it is possible to classically
efficiently predict the expectation values of local observables on all states
within a phase of matter using a machine learning algorithm after learning from
data obtained from other states in the same phase. However, existing results
are restricted to phases of matter such as ground states of gapped Hamiltonians
and Gibbs states that exhibit exponential decay of correlations. In this work,
we drop this requirement and show how it is possible to learn local expectation
values for all states in a phase, where we adopt the Lindbladian phase
definition by Coser \& P\'erez-Garc\'ia [Coser \& P\'erez-Garc\'ia, Quantum 3,
174 (2019)], which defines states to be in the same phase if we can drive one
to other rapidly with a local Lindbladian. This definition encompasses the
better-known Hamiltonian definition of phase of matter for gapped ground state
phases, and further applies to any family of states connected by short unitary
circuits, as well as non-equilibrium phases of matter, and those stable under
external dissipative interactions. Under this definition, we show that $N =
O(\log(n/\delta)2^{polylog(1/\epsilon)})$ samples suffice to learn local
expectation values within a phase for a system with $n$ qubits, to error
$\epsilon$ with failure probability $\delta$. This sample complexity is
comparable to previous results on learning gapped and thermal phases, and it
encompasses previous results of this nature in a unified way. Furthermore, we
also show that we can learn families of states which go beyond the Lindbladian
definition of phase, and we derive bounds on the sample complexity which are
dependent on the mixing time between states under a Lindbladian evolution.

### Many-body entropies and entanglement from polynomially-many local measurements

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2311.08108v1)

**Date de publication :** 14/11/2023

**Auteur(s) :**
- Benoît Vermersch
- Marko Ljubotina
- J. Ignacio Cirac
- Peter Zoller
- Maksym Serbyn
- Lorenzo Piroli

**Résumé :**
Randomized measurements (RMs) provide a practical scheme to probe complex
many-body quantum systems. While they are a very powerful tool to extract local
information, global properties such as entropy or bipartite entanglement remain
hard to probe, requiring a number of measurements or classical post-processing
resources growing exponentially in the system size. In this work, we address
the problem of estimating global entropies and mixed-state entanglement via
partial-transposed (PT) moments, and show that efficient estimation strategies
exist under the assumption that all the spatial correlation lengths are finite.
Focusing on one-dimensional systems, we identify a set of approximate
factorization conditions (AFCs) on the system density matrix which allow us to
reconstruct entropies and PT moments from information on local subsystems.
Combined with the RM toolbox, this yields a simple strategy for entropy and
entanglement estimation which is provably accurate assuming that the state to
be measured satisfies the AFCs, and which only requires polynomially-many
measurements and post-processing operations. We prove that the AFCs hold for
finite-depth quantum-circuit states and translation-invariant matrix-product
density operators, and provide numerical evidence that they are satisfied in
more general, physically-interesting cases, including thermal states of local
Hamiltonians. We argue that our method could be practically useful to detect
bipartite mixed-state entanglement for large numbers of qubits available in
today's quantum platforms.

## Machine learning/optimisation

### Trainability and Expressivity of Hamming-Weight Preserving Quantum Circuits for Machine Learning

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2309.15547v1)

**Date de publication :** 27/09/2023

**Auteur(s) :**
- Léo Monbroussou
- Jonas Landman
- Alex B. Grilo
- Romain Kukla
- Elham Kashefi

**Résumé :**
Quantum machine learning has become a promising area for real world
applications of quantum computers, but near-term methods and their scalability
are still important research topics. In this context, we analyze the
trainability and controllability of specific Hamming weight preserving quantum
circuits. These circuits use gates that preserve subspaces of the Hilbert
space, spanned by basis states with fixed Hamming weight $k$. They are good
candidates for mimicking neural networks, by both loading classical data and
performing trainable layers. In this work, we first design and prove the
feasibility of new heuristic data loaders, performing quantum amplitude
encoding of $\binom{n}{k}$-dimensional vectors by training a n-qubit quantum
circuit. Then, we analyze more generally the trainability of Hamming weight
preserving circuits, and show that the variance of their gradients is bounded
according to the size of the preserved subspace. This proves the conditions of
existence of Barren Plateaus for these circuits, and highlights a setting where
a recent conjecture on the link between controllability and trainability of
variational quantum circuits does not apply.

### Solving Higher Order Binary Optimization Problems on NISQ Devices: Experiments and Limitations

**Lien de l'article :** [iccs](https://www.iccs-meeting.org/archive/iccs2023/papers/140770216.pdf)

**Date de publication :** 26/06/2023

**Auteur(s) :**
- Valentin Gilbert
- Julien Rodriguez
- Stephane Louise
- Renaud Sirdey

**Résumé :**
With the recent availability of Noisy Intermediate-Scale Quantum devices, the potential of quantum computers to impact the field of
combinatorial optimization lies in quantum variational and annealing-based
methods. This paper further compares Quantum Annealing (QA) and the
Quantum Approximate Optimization Algorithm (QAOA) in solving Higher
Order Binary Optimization (HOBO) problems. This case study considers the
hypergraph partitioning problem, which is used to generate custom HOBO
problems. Our experiments show that D-Wave systems quickly reach limits
solving dense HOBO problems. Although the QAOA demonstrates better
performance on exact simulations, noisy simulations reveal that the gate
error rate should remain under 10<sup>-5</sup> to match D-Wave systems’ performance,
considering equal compilation overheads for both device.

## Cryptographie/cryptanalyse

### Variational Loop Vertex Expansion

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2312.00712v2)

**Date de publication :** 01/12/2023

**Auteur(s) :**
- Vasily Sazonov

**Résumé :**
Loop Vertex Expansion (LVE) was developed to construct QFT models with local
and non-local interactions. Using LVE, one can prove the analyticity in the
finite cardioid-like domain in the complex plain of the coupling constant of
the free energies and cumulants of various vector, matrix, or tensor-type
models. Here, applying the idea of choosing the initial approximation depending
on the coupling constant, we construct the analytic continuation of the free
energy of the quartic matrix model beyond the standard LVE cardioid over the
branch cut and for arbitrary large couplings.

### Even-Cycle Detection in the Randomized and Quantum CONGEST Model

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2402.12018v1)

**Date de publication :** 19/02/2024

**Auteur(s) :**
- Pierre Fraigniaud
- Mael Luce
- Frederic Magniez
- Ioan Todinca

**Résumé :**
We show that, for every $k\geq 2$, $C_{2k}$-freeness can be decided in
$O(n^{1-1/k})$ rounds in the \CONGEST{} model by a randomized Monte-Carlo
distributed algorithm with one-sided error probability $1/3$. This matches the
best round-complexities of previously known algorithms for $k\in\{2,3,4,5\}$ by
Drucker et al. [PODC'14] and Censor-Hillel et al. [DISC'20], but improves the
complexities of the known algorithms for $k>5$ by Eden et al. [DISC'19], which
were essentially of the form $\tilde O(n^{1-2/k^2})$. Our algorithm uses
colored BFS-explorations with threshold, but with an original \emph{global}
approach that enables to overcome a recent impossibility result by Fraigniaud
et al. [SIROCCO'23] about using colored BFS-exploration with \emph{local}
threshold for detecting cycles.
  We also show how to quantize our algorithm for achieving a round-complexity
$\tilde O(n^{\frac{1}{2}-\frac{1}{2k}})$ in the quantum setting for deciding
$C_{2k}$ freeness. Furthermore, this allows us to improve the known quantum
complexities of the simpler problem of detecting cycles of length \emph{at
most}~$2k$ by van Apeldoorn and de Vos [PODC'22]. Our quantization is in two
steps. First, the congestion of our randomized algorithm is reduced, to the
cost of reducing its success probability too. Second, the success probability
is boosted using a new quantum framework derived from sequential algorithms,
namely Monte-Carlo quantum amplification.

### A Functional Analysis Approach to Symbolic Regression

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2402.06299v1)

**Date de publication :** 09/02/2024

**Auteur(s) :**
- Kirill Antonov
- Roman Kalkreuth
- Kaifeng Yang
- Thomas Bäck
- Niki van Stein
- Anna V Kononova

**Résumé :**
Symbolic regression (SR) poses a significant challenge for randomized search
heuristics due to its reliance on the synthesis of expressions for input-output
mappings. Although traditional genetic programming (GP) algorithms have
achieved success in various domains, they exhibit limited performance when
tree-based representations are used for SR. To address these limitations, we
introduce a novel SR approach called Fourier Tree Growing (FTG) that draws
insights from functional analysis. This new perspective enables us to perform
optimization directly in a different space, thus avoiding intricate symbolic
expressions. Our proposed algorithm exhibits significant performance
improvements over traditional GP methods on a range of classical
one-dimensional benchmarking problems. To identify and explain limiting factors
of GP and FTG, we perform experiments on a large-scale polynomials benchmark
with high-order polynomials up to degree 100. To the best of the authors'
knowledge, this work represents the pioneering application of functional
analysis in addressing SR problems. The superior performance of the proposed
algorithm and insights into the limitations of GP open the way for further
advancing GP for SR and related areas of explainable machine learning.

### (Quantum) complexity of testing signed graph clusterability

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2311.10480v1)

**Date de publication :** 17/11/2023

**Auteur(s) :**
- Kuo-Chin Chen
- Simon Apers
- Min-Hsiu Hsieh

**Résumé :**
This study examines clusterability testing for a signed graph in the
bounded-degree model. Our contributions are two-fold. First, we provide a
quantum algorithm with query complexity $\tilde{O}(N^{1/3})$ for testing
clusterability, which yields a polynomial speedup over the best classical
clusterability tester known [arXiv:2102.07587]. Second, we prove an
$\tilde{\Omega}(\sqrt{N})$ classical query lower bound for testing
clusterability, which nearly matches the upper bound from [arXiv:2102.07587].
This settles the classical query complexity of clusterability testing, and it
shows that our quantum algorithm has an advantage over any classical algorithm.

### Quantum speedups for linear programming via interior point methods

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2311.03215v2)

**Date de publication :** 06/11/2023

**Auteur(s) :**
- Simon Apers
- Sander Gribling

**Résumé :**
We describe a quantum algorithm based on an interior point method for solving
a linear program with $n$ inequality constraints on $d$ variables. The
algorithm explicitly returns a feasible solution that is $\varepsilon$-close to
optimal, and runs in time $\sqrt{n} \cdot
\mathrm{poly}(d,\log(n),\log(1/\varepsilon))$ which is sublinear for tall
linear programs (i.e., $n \gg d$). Our algorithm speeds up the Newton step in
the state-of-the-art interior point method of Lee and Sidford [FOCS~'14]. This
requires us to efficiently approximate the Hessian and gradient of the barrier
function, and these are our main contributions.
  To approximate the Hessian, we describe a quantum algorithm for the
\emph{spectral approximation} of $A^T A$ for a tall matrix $A \in \mathbb R^{n
\times d}$. The algorithm uses leverage score sampling in combination with
Grover search, and returns a $\delta$-approximation by making
$O(\sqrt{nd}/\delta)$ row queries to $A$. This generalizes an earlier quantum
speedup for graph sparsification by Apers and de Wolf~[FOCS~'20]. To
approximate the gradient, we use a recent quantum algorithm for multivariate
mean estimation by Cornelissen, Hamoudi and Jerbi [STOC '22]. While a naive
implementation introduces a dependence on the condition number of the Hessian,
we avoid this by pre-conditioning our random variable using our quantum
algorithm for spectral approximation.

### Quantum walks, the discrete wave equation and Chebyshev polynomials

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2402.07809v1)

**Date de publication :** 12/02/2024

**Auteur(s) :**
- Simon Apers
- Laurent Miclo

**Résumé :**
A quantum walk is the quantum analogue of a random walk. While it is
relatively well understood how quantum walks can speed up random walk hitting
times, it is a long-standing open question to what extent quantum walks can
speed up the spreading or mixing rate of random walks on graphs. In this
expository paper, inspired by a blog post by Terence Tao, we describe a
particular perspective on this question that derives quantum walks from the
discrete wave equation on graphs. This yields a description of the quantum walk
dynamics as simply applying a Chebyshev polynomial to the random walk
transition matrix. This perspective decouples the problem from its quantum
origin, and highlights connections to earlier (non-quantum) work and the use of
Chebyshev polynomials in random walk theory as in the Varopoulos-Carne bound.
We illustrate the approach by proving a weak limit of the quantum walk dynamics
on the lattice. This gives a different proof of the quadratically improved
spreading behavior of quantum walks on lattices.

### Quantum security of subset cover problems

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2210.15396v2)

**Date de publication :** 27/10/2022

**Auteur(s) :**
- Samuel Bouaziz--Ermann
- Alex B. Grilo
- Damien Vergnaud

**Résumé :**
The subset cover problem for $k \geq 1$ hash functions, which can be seen as
an extension of the collision problem, was introduced in 2002 by Reyzin and
Reyzin to analyse the security of their hash-function based signature scheme
HORS.
  The security of many hash-based signature schemes relies on this problem or a
variant of this problem (e.g. HORS, SPHINCS, SPHINCS+, $\dots$).
  Recently, Yuan, Tibouchi and Abe (2022) introduced a variant to the subset
cover problem, called restricted subset cover, and proposed a quantum algorithm
for this problem. In this work, we prove that any quantum algorithm needs to
make $\Omega\left((k+1)^{-\frac{2^{k}}{2^{k+1}-1}}\cdot
N^{\frac{2^{k}-1}{2^{k+1}-1}}\right)$ queries to the underlying hash functions
with codomain size $N$ to solve the restricted subset cover problem, which
essentially matches the query complexity of the algorithm proposed by Yuan,
Tibouchi and Abe.
  We also analyze the security of the general $(r,k)$-subset cover problem,
which is the underlying problem that implies the unforgeability of HORS under a
$r$-chosen message attack (for $r \geq 1$). We prove that a generic quantum
algorithm needs to make $\Omega\left(N^{k/5}\right)$ queries to the underlying
hash functions to find a $(1,k)$-subset cover.
  We also propose a quantum algorithm that finds a $(r,k)$-subset cover making
$O\left(N^{k/(2+2r)}\right)$ queries to the $k$ hash functions.

### The special case of cyclotomic fields in quantum algorithms for unit groups

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2303.03978v1)

**Date de publication :** 07/03/2023

**Auteur(s) :**
- Razvan Barbulescu
- Adrien Poulalion

**Résumé :**
Unit group computations are a cryptographic primitive for which one has a
fast quantum algorithm, but the required number of qubits is $\tilde O(m^5)$.
In this work we propose a modification of the algorithm for which the number of
qubits is $\tilde O(m^2)$ in the case of cyclotomic fields. Moreover, under a
recent conjecture on the size of the class group of $\mathbb{Q}(\zeta_m +
\zeta_m^{-1})$, the quantum algorithms is much simpler because it is a hidden
subgroup problem (HSP) algorithm rather than its error estimation counterpart:
continuous hidden subgroup problem (CHSP). We also discuss the (minor) speed-up
obtained when exploiting Galois automorphisms thanks to the Buchmann-Pohst
algorithm over $\mathcal{O}_K$-lattices.


## Caractérisation/correction d'erreur

### Efficient learning of the structure and parameters of local Pauli noise channels

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2307.02959v1)

**Date de publication :** 06/07/2023

**Auteur(s) :**
- Cambyse Rouzé
- Daniel Stilck França

**Résumé :**
The unavoidable presence of noise is a crucial roadblock for the development
of large-scale quantum computers and the ability to characterize quantum noise
reliably and efficiently with high precision is essential to scale quantum
technologies further. Although estimating an arbitrary quantum channel requires
exponential resources, it is expected that physically relevant noise has some
underlying local structure, for instance that errors across different qubits
have a conditional independence structure. Previous works showed how it is
possible to estimate Pauli noise channels with an efficient number of samples
in a way that is robust to state preparation and measurement errors, albeit
departing from a known conditional independence structure.
  We present a novel approach for learning Pauli noise channels over n qubits
that addresses this shortcoming. Unlike previous works that focused on learning
coefficients with a known conditional independence structure, our method learns
both the coefficients and the underlying structure. We achieve our results by
leveraging a groundbreaking result by Bresler for efficiently learning Gibbs
measures and obtain an optimal sample complexity of O(log(n)) to learn the
unknown structure of the noise acting on n qubits. This information can then be
leveraged to obtain a description of the channel that is close in diamond
distance from O(poly(n)) samples. Furthermore, our method is efficient both in
the number of samples and postprocessing without giving up on other desirable
features such as SPAM-robustness, and only requires the implementation of
single qubit Cliffords. In light of this, our novel approach enables the
large-scale characterization of Pauli noise in quantum devices under minimal
experimental requirements and assumptions.

### Information-theoretic generalization bounds for learning from quantum data

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2311.05529v1)

**Date de publication :** 09/11/2023

**Auteur(s) :**
- Matthias Caro
- Tom Gur
- Cambyse Rouzé
- Daniel Stilck França
- Sathyawageeswar Subramanian

**Résumé :**
Learning tasks play an increasingly prominent role in quantum information and
computation. They range from fundamental problems such as state discrimination
and metrology over the framework of quantum probably approximately correct
(PAC) learning, to the recently proposed shadow variants of state tomography.
However, the many directions of quantum learning theory have so far evolved
separately. We propose a general mathematical formalism for describing quantum
learning by training on classical-quantum data and then testing how well the
learned hypothesis generalizes to new data. In this framework, we prove bounds
on the expected generalization error of a quantum learner in terms of classical
and quantum information-theoretic quantities measuring how strongly the
learner's hypothesis depends on the specific data seen during training.
  To achieve this, we use tools from quantum optimal transport and quantum
concentration inequalities to establish non-commutative versions of decoupling
lemmas that underlie recent information-theoretic generalization bounds for
classical machine learning.
  Our framework encompasses and gives intuitively accessible generalization
bounds for a variety of quantum learning scenarios such as quantum state
discrimination, PAC learning quantum states, quantum parameter estimation, and
quantumly PAC learning classical functions. Thereby, our work lays a foundation
for a unifying quantum information-theoretic perspective on quantum learning.

### Lower Bounds on Learning Pauli Channels

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2301.09192v1)

**Date de publication :** 22/01/2023

**Auteur(s) :**
- Omar Fawzi
- Aadil Oufkir
- Daniel Stilck França

**Résumé :**
Understanding the noise affecting a quantum device is of fundamental
importance for scaling quantum technologies. A particularly important class of
noise models is that of Pauli channels, as randomized compiling techniques can
effectively bring any quantum channel to this form and are significantly more
structured than general quantum channels. In this paper, we show fundamental
lower bounds on the sample complexity for learning Pauli channels in diamond
norm with unentangled measurements. We consider both adaptive and non-adaptive
strategies. In the non-adaptive setting, we show a lower bound of
$\Omega(2^{3n}\epsilon^{-2})$ to learn an $n$-qubit Pauli channel. In
particular, this shows that the recently introduced learning procedure by
Flammia and Wallman is essentially optimal. In the adaptive setting, we show a
lower bound of $\Omega(2^{2.5n}\epsilon^{-2})$ for
$\epsilon=\mathcal{O}(2^{-n})$, and a lower bound of
$\Omega(2^{2n}\epsilon^{-2} )$ for any $\epsilon > 0$. This last lower bound
even applies for arbitrarily many sequential uses of the channel, as long as
they are only interspersed with other unital operations.

### Robust sparse IQP sampling in constant depth

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2307.10729v4)

**Date de publication :** 20/07/2023

**Auteur(s) :**
- Louis Paletta
- Anthony Leverrier
- Alain Sarlette
- Mazyar Mirrahimi
- Christophe Vuillot

**Résumé :**
Between NISQ (noisy intermediate scale quantum) approaches without any proof
of robust quantum advantage and fully fault-tolerant quantum computation, we
propose a scheme to achieve a provable superpolynomial quantum advantage (under
some widely accepted complexity conjectures) that is robust to noise with
minimal error correction requirements. We choose a class of sampling problems
with commuting gates known as sparse IQP (Instantaneous Quantum
Polynomial-time) circuits and we ensure its fault-tolerant implementation by
introducing the tetrahelix code. This new code is obtained by merging several
tetrahedral codes (3D color codes) and has the following properties: each
sparse IQP gate admits a transversal implementation, and the depth of the
logical circuit can be traded for its width. Combining those, we obtain a
depth-1 implementation of any sparse IQP circuit up to the preparation of
encoded states. This comes at the cost of a space overhead which is only
polylogarithmic in the width of the original circuit. We furthermore show that
the state preparation can also be performed in constant depth with a single
step of feed-forward from classical computation. Our construction thus exhibits
a robust superpolynomial quantum advantage for a sampling problem implemented
on a constant depth circuit with a single round of measurement and
feed-forward.


## Chimie

### Greedy Gradient-free Adaptive Variational Quantum Algorithms on a Noisy Intermediate Scale Quantum Computer

**Lien de l'article :** [ArXiv](https://arxiv.org/abs/2306.17159)

**Date de publication :** 29/06/2023

**Auteur(s) :**
- César Feniou
- Baptiste Claudon
- Muhammad Hassan
- Axel Courtat
- Olivier Adjoua
- Yvon Maday
- Jean-Philip Piquemal

**Résumé :**
Hybrid quantum-classical adaptive Variational Quantum Eigensolvers (VQE) already hold the potential to outperform classical computing for simulating quantum many-body systems. However, their practical implementation on current quantum processing units (QPUs) is very challenging due to the noisy evaluation of a polynomially scaling number of observables, undertaken for operator selection and optimisation of a high-dimensional cost function. To overcome this, we propose new techniques to execute adaptive algorithms on a 25-qubit error-mitigated QPU coupled to a GPU-accelerated HPC simulator. Targeting physics applications, we compute the ground state of a 25-body Ising model using the newly introduced Greedy Gradient-free Adaptive VQE (CGA-VQE) requiring only five circuit measurements per iteration, regardless of the number of qubits and size of the operator pool. Towards chemistry, we combine the GGA-VQE and Overlap-ADAPT-VQE algorithms to approximate a molecular system ground state. We show that the QPU successfully executes the algorithms and yields the correct choice of parametrised unitary operators. While the QPU evaluation of the resulting ansatz wave-function is polluted by hardware noise, a single final evaluation of the sought-after observables on a classical GPU-accelerated/noiseless simulator allows the recovery of the correct approximation of the ground state, thus highlighting the need for hybrid quantum-classical observable measurement.

### Overlap-ADAPT-VQE: Practical Quantum Chemistry on Quantum Computers via Overlap-Guided Compact Ansätze

**Lien de l'article :** [ArXiv](https://arxiv.org/abs/2301.10196)

**Date de publication :** 24/01/2023

**Auteur(s) :**
- César Feniou
- Muhammad Hassan
- Diata Traoré
- Emmanuel Giner
- Yvon Maday
- Jean-Philip Piquemal

**Résumé :**
ADAPT-VQE is a robust algorithm for hybrid quantum-classical simulations of quantum chemical systems on near-term quantum computers. While its iterative process systematically reaches the ground state energy, ADAPT-VQE is sensitive to local energy minima, leading to over-parameterized ansätze. We introduce the Overlap-ADAPT-VQE to grow wave-functions by maximizing their overlap with any intermediate target wave-function that already captures some electronic correlation. By avoiding building the ansatz in the energy landscape strewn with local minima, the Overlap-ADAPT-VQE produces ultra-compact ansätze suitable for high-accuracy initializations of a new ADAPT procedure. Spectacular advantages over ADAPT-VQE are observed for strongly correlated systems including massive savings in circuit depth. Since this compression strategy can also be initialized with accurate Selected-Configuration Interaction (SCI) classical target wave-functions, it paves the way for chemically accurate simulations of larger systems, and strengthens the promise of decisively surpassing classical quantum chemistry through the power of quantum computing. 

### Sparse Quantum State Preparation for Strongly Correlated Systems

**Lien de l'article :** [ArXiv](https://arxiv.org/abs/2311.03347)

**Date de publication :** 06/11/2023

**Auteur(s) :**
- César Feniou
- Olivier Adjoua
- Baptiste Claudon
- Julien Zylberman
- Emmanuel Giner
- Jean-Philip Piquemal

**Résumé :**
Quantum Computing allows, in principle, the encoding of the exponentially scaling many-electron wave function onto a linearly scaling qubit register, offering a promising solution to overcome the limitations of traditional quantum chemistry methods. An essential requirement for ground state quantum algorithms to be practical is the initialisation of the qubits to a high-quality approximation of the sought-after ground state. Quantum State Preparation (QSP) allows the preparation of approximate eigenstates obtained from classical calculations, but it is frequently treated as an oracle in quantum information. In this study, we conduct QSP on the ground state of prototypical strongly correlated systems, up to 28 qubits, using the Hyperion GPU-accelerated state-vector emulator. Various variational and non-variational methods are compared in terms of their circuit depth and classical complexity. Our results indicate that the recently developed Overlap-ADAPT-VQE algorithm offers the most advantageous performance for near-term applications. 

### Dilute measurement-induced cooling into many-body ground states

**Lien de l'article :** [ArXiv](https://arxiv.org/abs/2311.05258)

**Date de publication :** 09/11/2023

**Auteur(s) :**
- Josias Langbehn
- Kyrylo Snizhko
- Igor Gornyi
- Giovanna Morigi
- Yuval Gefen
- Christiane P. Koch

**Résumé :**
Cooling a quantum system to its ground state is important for the characterization of non-trivial interacting systems, and in the context of a variety of quantum information platforms. In principle, this can be achieved by employing measurement-based passive steering protocols, where the steering steps are predetermined and are not based on measurement readouts. However, measurements, i.e., coupling the system to auxiliary quantum degrees of freedom, is rather costly, and protocols in which the number of measurements scales with system size will have limited practical applicability. Here, we identify conditions under which measurement-based cooling protocols can be taken to the dilute limit. For two examples of frustration-free one-dimensional spin chains, we show that steering on a single link is sufficient to cool these systems into their unique ground states. We corroborate our analytical arguments with finite-size numerical simulations and discuss further applications. 

## Algorithme/circuit

### Formal Methods for Quantum Programs: A Survey

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2109.06493v2)

**Date de publication :** 14/09/2021

**Auteur(s) :**
- Christophe Chareton
- Sébastien Bardin
- Dongho Lee
- Benoît Valiron
- Renaud Vilmart
- Zhaowei Xu

**Résumé :**
While recent progress in quantum hardware open the door for significant
speedup in certain key areas (cryptography, biology, chemistry, optimization,
machine learning, etc), quantum algorithms are still hard to implement right,
and the validation of such quantum programs is achallenge. Moreover, importing
the testing and debugging practices at use in classical programming is
extremely difficult in the quantum case, due to the destructive aspect of
quantum measurement. As an alternative strategy, formal methods are prone to
play a decisive role in the emerging field of quantum software. Recent works
initiate solutions for problems occurring at every stage of the development
process: high-level program design, implementation, compilation, etc. We review
the induced challenges for an efficient use of formal methods in quantum
computing and the current most promising research directions.

### Optimal Hadamard gate count for Clifford$+T$ synthesis of Pauli rotations sequences

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2302.07040v3)

**Date de publication :** 14/02/2023

**Auteur(s) :**
- Vivien Vandaele
- Simon Martiel
- Simon Perdrix
- Christophe Vuillot

**Résumé :**
The Clifford$+T$ gate set is commonly used to perform universal quantum
computation. In such setup the $T$ gate is typically much more expensive to
implement in a fault-tolerant way than Clifford gates. To improve the
feasibility of fault-tolerant quantum computing it is then crucial to minimize
the number of $T$ gates. Many algorithms, yielding effective results, have been
designed to address this problem. It has been demonstrated that performing a
pre-processing step consisting of reducing the number of Hadamard gates in the
circuit can help to exploit the full potential of these algorithms and thereby
lead to a substantial $T$-count reduction. Moreover, minimizing the number of
Hadamard gates also restrains the number of additional qubits and operations
resulting from the gadgetization of Hadamard gates, a procedure used by some
compilers to further reduce the number of $T$ gates. In this work we tackle the
Hadamard gate reduction problem, and propose an algorithm for synthesizing a
sequence of $\pi/4$ Pauli rotations with a minimal number of Hadamard gates.
Based on this result, we present an algorithm which optimally minimizes the
number of Hadamard gates lying between the first and the last $T$ gate of the
circuit.

### On the Hardness of Analyzing Quantum Programs Quantitatively

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2312.13657v1)

**Date de publication :** 21/12/2023

**Auteur(s) :**
- Martin Avanzini
- Georg Moser
- Romain Péchoux
- Simon Perdrix

**Résumé :**
In this paper, we study quantitative properties of quantum programs.
Properties of interest include (positive) almost-sure termination, expected
runtime or expected cost, that is, for example, the expected number of
applications of a given quantum gate, etc. After studying the completeness of
these problems in the arithmetical hierarchy over the Clifford+T fragment of
quantum mechanics, we express these problems using a variation of a quantum
pre-expectation transformer, a weakest precondition based technique that allows
to symbolically compute these quantitative properties. Under a smooth
restriction-a restriction to polynomials of bounded degree over a real closed
field-we show that the quantitative problem, which consists in finding an
upper-bound to the pre-expectation, can be decided in time double-exponential
in the size of a program, thus providing, despite its great complexity, one of
the first decidable results on the analysis and verification of quantum
programs. Finally, we sketch how the latter can be transformed into an
efficient synthesis method.

### Completeness of Sum-Over-Paths for Toffoli-Hadamard and the Dyadic Fragments of Quantum Computation

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2205.02600v2)

**Date de publication :** 05/05/2022

**Auteur(s) :**
- Renaud Vilmart

**Résumé :**
The "Sum-Over-Paths" formalism is a way to symbolically manipulate linear
maps that describe quantum systems, and is a tool that is used in formal
verification of such systems. We give here a new set of rewrite rules for the
formalism, and show that it is complete for "Toffoli-Hadamard", the simplest
approximately universal fragment of quantum mechanics. We show that the
rewriting is terminating, but not confluent (which is expected from the
universality of the fragment). We do so using the connection between
Sum-over-Paths and graphical language ZH-Calculus, and also show how the
axiomatisation translates into the latter. Finally, we show how to enrich the
rewrite system to reach completeness for the dyadic fragments of quantum
computation -- obtained by adding phase gates with dyadic multiples of $\pi$ to
the Toffoli-Hadamard gate-set -- used in particular in the Quantum Fourier
Transform.

### Rewriting and Completeness of Sum-Over-Paths in Dyadic Fragments of Quantum Computing

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2307.14223v4)

**Date de publication :** 26/07/2023

**Auteur(s) :**
- Renaud Vilmart

**Résumé :**
The "Sum-Over-Paths" formalism is a way to symbolically manipulate linear
maps that describe quantum systems, and is a tool that is used in formal
verification of such systems. We give here a new set of rewrite rules for the
formalism, and show that it is complete for "Toffoli-Hadamard", the simplest
approximately universal fragment of quantum mechanics. We show that the
rewriting is terminating, but not confluent (which is expected from the
universality of the fragment). We do so using the connection between
Sum-over-Paths and graphical language ZH-calculus, and also show how the
axiomatisation translates into the latter. We provide generalisations of the
presented rewrite rules, that can prove useful when trying to reduce terms in
practice, and we show how to graphically make sense of these new rules. We show
how to enrich the rewrite system to reach completeness for the dyadic fragments
of quantum computation, used in particular in the Quantum Fourier Transform,
and obtained by adding phase gates with dyadic multiples of $\pi$ to the
Toffoli-Hadamard gate-set. Finally, we show how to perform sums and
concatenation of arbitrary terms, something which is not native in a system
designed for analysing gate-based quantum computation, but necessary when
considering Hamiltonian-based quantum computation.

### A Complete Equational Theory for Quantum Circuits

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2206.10577v2)

**Date de publication :** 21/06/2022

**Auteur(s) :**
- Alexandre Clément
- Nicolas Heurtel
- Shane Mansfield
- Simon Perdrix
- Benoît Valiron

**Résumé :**
We introduce the first complete equational theory for quantum circuits. More
precisely, we introduce a set of circuit equations that we prove to be sound
and complete: two circuits represent the same unitary map if and only if they
can be transformed one into the other using the equations. The proof is based
on the properties of multi-controlled gates -- that are defined using
elementary gates -- together with an encoding of quantum circuits into linear
optical circuits, which have been proved to have a complete axiomatisation.

### Quantum Circuit Completeness: Extensions and Simplifications

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2303.03117v3)

**Date de publication :** 06/03/2023

**Auteur(s) :**
- Alexandre Clément
- Noé Delorme
- Simon Perdrix
- Renaud Vilmart

**Résumé :**
Although quantum circuits have been ubiquitous for decades in quantum
computing, the first complete equational theory for quantum circuits has only
recently been introduced. Completeness guarantees that any true equation on
quantum circuits can be derived from the equational theory. We improve this
completeness result in two ways: (i) We simplify the equational theory by
proving that several rules can be derived from the remaining ones. In
particular, two out of the three most intricate rules are removed, the third
one being slightly simplified. (ii) The complete equational theory can be
extended to quantum circuits with ancillae or qubit discarding, to represent
respectively quantum computations using an additional workspace, and hybrid
quantum computations. We show that the remaining intricate rule can be greatly
simplified in these more expressive settings, leading to equational theories
where all equations act on a bounded number of qubits. The development of
simple and complete equational theories for expressive quantum circuit models
opens new avenues for reasoning about quantum circuits. It provides strong
formal foundations for various compiling tasks such as circuit optimisation,
hardware constraint satisfaction and verification.

### A Curry-Howard Correspondence for Linear, Reversible Computation

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2302.11887v3)

**Date de publication :** 23/02/2023

**Auteur(s) :**
- Kostia Chardonnet
- Alexis Saurin
- Benoît Valiron

**Résumé :**
In this paper, we present a linear and reversible programming language with
inductives types and recursion. The semantics of the languages is based on
pattern-matching; we show how ensuring syntactical exhaustivity and
non-overlapping of clauses is enough to ensure reversibility. The language
allows to represent any Primitive Recursive Function. We then give a
Curry-Howard correspondence with the logic $\mu$MALL: linear logic extended
with least fixed points allowing inductive statements. The critical part of our
work is to show how primitive recursion yields circular proofs that satisfy
$\mu$MALL validity criterion and how the language simulates the cut-elimination
procedure of $\mu$MALL.

### Proceedings of the Twentieth International Conference on Quantum Physics and Logic

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2308.15489v2)

**Date de publication :** 23/08/2023

**Auteur(s) :**
- Shane Mansfield
- Benoît Valiron
- Vladimir Zamdzhiev

**Résumé :**
This volume contains the proceedings of the 20th International Conference on
Quantum Physics and Logic (QPL 2023). The aim of the QPL conference series is
to bring together academic and industry researchers working on mathematical
foundations of quantum computation, quantum physics, and related areas. The
main focus is on the use of algebraic and categorical structures, formal
languages, type systems, semantic methods, as well as other mathematical and
computer scientific techniques applicable to the study of physical systems,
physical processes, and their composition.

### Minimal Equational Theories for Quantum Circuits

**Lien de l'article :** [ArXiv](http://arxiv.org/abs/2311.07476v2)

**Date de publication :** 13/11/2023

**Auteur(s) :**
- Alexandre Clément
- Noé Delorme
- Simon Perdrix

**Résumé :**
We introduce the first minimal and complete equational theory for quantum
circuits. Hence, we show that any true equation on quantum circuits can be
derived from simple rules, all of them being standard except a novel but
intuitive one which states that a multi-control $2\pi$ rotation is nothing but
the identity. Our work improves on the recent complete equational theories for
quantum circuits, by getting rid of several rules including a fairly
impractical one. One of our main contributions is to prove the minimality of
the equational theory, i.e. none of the rules can be derived from the other
ones. More generally, we demonstrate that any complete equational theory on
quantum circuits (when all gates are unitary) requires rules acting on an
unbounded number of qubits. Finally, we also simplify the complete equational
theories for quantum circuits with ancillary qubits and/or qubit discarding.
