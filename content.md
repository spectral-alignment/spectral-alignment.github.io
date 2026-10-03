---
# Page settings. The article starts after the closing --- below.
title: |
  World Modeling through
  Spectral Alignment
description: What information should a latent world model preserve? SpecWM explicitly specifies desired relationships between observations through a target similarity kernel.
subtitle: What information should a latent world model preserve?
authors:
- name: Holger Molin
  affiliation: '1'
  equal: true
- name: William Peng
  affiliation: '1'
  equal: true
- name: Marco Bagatella
  affiliation: '2'
- name: Randall Balestriero
  affiliation: '3'
affiliations:
- marker: '1'
  name: Stanford University
- marker: '2'
  name: ETH Zurich
- marker: '3'
  name: Brown University
author_note: 'Equal contribution. Order within braces is randomized.'
links:
  code:
    label: Code
    url: https://anonymous.4open.science/r/SpecWM/
navigation:
- link: code
- label: Results
  url: '#results'
- label: Theory
  url: '#theory'
contents:
- id: overview
  label: Introduction
  section_label: INTRODUCTION
- id: method
  label: Spectral alignment
  section_label: METHOD
- id: temporal
  label: Temporal kernels
  section_label: TEMPORAL KERNELS
- id: results
  label: Planning
  section_label: PLANNING
- id: representations
  label: Probing
  section_label: PROBING
- id: ablations
  label: Ablations
  section_label: ABLATIONS
- id: discussion
  label: Conclusion
  section_label: CONCLUSION
- id: theory
  label: Theory
  section_label: THEORY
metrics_image:
  image: assets/environments.png
  title: The three evaluation environments
  alt: OGBench Cube, OGBench Scene, and CALVIN, in the same order as the planning scores below.
  width: 2500
  height: 919
metrics:
- before: 52%
  after: 68%
  label: OGBench Cube
  change: +16 percentage points over LeWM baseline
- before: 49%
  after: 77%
  label: OGBench Scene
  change: +28 percentage points over LeWM baseline
- before: 29%
  after: 51%
  label: CALVIN
  change: +22 percentage points over LeWM baseline
figures:
  pipeline:
    image: assets/pipeline.png
    zoom: assets/pipeline.svg
    fallback: assets/pipeline.pdf
    title: Spectral alignment on a single trajectory
    alt: Eight robot observations along a trajectory, followed by the temporal target kernel, learned encoder Gram matrix, and their corresponding embedding geometries.
    width: 2200
    height: 943
  fair_cem:
    image: assets/fair_cem.png
    zoom: assets/fair_cem.svg
    fallback: assets/fair_cem.pdf
    title: CEM planning success across three environments
    alt: 'CEM success: random 13, 21, 17%; LeWM 52, 49, 29%; temporal SpecWM 68, 77, 51%; quasimetric SpecWM 71, 74, 47% on Cube, OGBench Scene and CALVIN respectively.'
    width: 2200
    height: 687
    loading: lazy
  final_probes:
    image: assets/final_probes.png
    zoom: assets/final_probes.svg
    fallback: assets/final_probes.pdf
    title: Linear recoverability of manipulated object position
    alt: 'Object-position probe R squared: LeWM versus temporal SpecWM is 0.98 versus 0.81 on Cube, 0.09 versus 0.78 on OGBench Scene, and 0.41 versus 0.47 on CALVIN.'
    width: 2200
    height: 687
    loading: lazy
  spectral_conversion:
    image: assets/spectral_conversion.png
    zoom: assets/spectral_conversion.png
    fallback: assets/spectral_conversion.png
    title: Recovering kernel eigenvectors from learned embeddings
    alt: Kernel eigenvector probe curves for state, proprioception and depth targets; fully specified targets generally recover eigenvectors better than underspecified targets or an untrained encoder.
    width: 809
    height: 278
    loading: lazy
  data_ablation:
    image: assets/data_ablation.png
    zoom: assets/data_ablation.svg
    fallback: assets/data_ablation.pdf
    title: Failure-data ablation
    alt: Failure-data ablation showing planning success and object-position probes with failure rollouts versus play data only on all three environments.
    width: 2200
    height: 1514
    loading: lazy
  stopgrad_ablation:
    image: assets/stopgrad_ablation.png
    zoom: assets/stopgrad_ablation.svg
    fallback: assets/stopgrad_ablation.pdf
    title: Stop-gradient ablation
    alt: Planning and probing comparisons with and without stop-gradient on the prediction target.
    width: 2200
    height: 1514
    loading: lazy
  scene_cost_ablation_rounded:
    image: assets/scene_cost_ablation_rounded.png
    zoom: assets/scene_cost_ablation_rounded.svg
    fallback: assets/scene_cost_ablation_rounded.pdf
    title: Planning-cost ablation on OGBench Scene
    alt: LeWM planning success 50% with L2 and 51% with cosine; temporal SpecWM 77% with either cost.
    width: 2200
    height: 2144
    loading: lazy
  scene_normalization_ablation_rounded:
    image: assets/scene_normalization_ablation_rounded.png
    zoom: assets/scene_normalization_ablation_rounded.svg
    fallback: assets/scene_normalization_ablation_rounded.pdf
    title: Normalization ablation on OGBench Scene
    alt: LeWM success 53% with BatchNorm and 51% with LayerNorm; temporal SpecWM 77% with either normalization.
    width: 2200
    height: 2144
    loading: lazy
  abstract_fig:
    image: assets/abstract_fig.png?v=2bf3c8bf
    zoom: assets/abstract_fig.svg?v=2bf3c8bf
    fallback: assets/abstract_fig.pdf?v=2bf3c8bf
    title: 'Spectral alignment: from pairwise distances to embeddings'
    alt: Pairwise distances define a target similarity matrix. The encoder learns embeddings whose pairwise similarities match the target.
    width: 2200
    height: 581
tables:
  planning:
    highlight: 2
    caption: CEM planning success (%)
  probes:
    highlight: 1
ui:
  skip: Skip to article
  back_to_top: Back to top
  resources: Resources
  contents: In this article
  contents_aria: Article contents
  metrics_aria: 'CEM planning success: LeWM baseline compared with temporal SpecWM'
  expanded_figure: Enlarged figure
  figure_close_hint: Press Escape or click to close.
explorer:
  title: Temporal kernel bandwidth
  tag: Interactive
  low: 0 · dissimilar
  high: 1 · similar
  label: Kernel bandwidth, σ
  formula: K_{ij}=e^{-|i-j|/\sigma}
  hint: The bandwidth σ sets the range of distances the target resolves. The plot shows the raw kernel, before centering.
  description: At 7 frames apart, similarity is {similarity}. {band}
  narrow: A narrow band emphasizes nearby observations.
  medium: A wider band preserves similarity across longer separations.
  wide: A wide band keeps distant observations more similar.
  aria: Temporal similarity matrix for 23 observations with bandwidth {sigma}. Similarity at a separation of 7 frames is {similarity}.
---

:::figure abstract_fig
**Spectral alignment framework.** Pairwise distances between samples define a target similarity kernel. We train the encoder to reconstruct this target through embedding similarities.
:::

## How do we tell a world model what to preserve? {#overview}

:::lead
The goal of a world model is to encode sufficient information to predict the consequences of an agent’s actions. At the same time, complex real-world observations contain large amounts of task-irrelevant information. Learning a compact representation therefore hinges on deciding which aspects of an observation to retain.
:::

Joint Embedding Predictive Architectures (JEPAs) predict outcomes in a latent space, rather than reconstructing high-dimensional observations in pixel space, allowing learned representations to abstract away details of the input. The training objective must guide which distinctions the model preserves without requiring it to reproduce every detail of an observation.

Recent work has made substantial progress toward stable JEPA training through regularizing the embedding distribution. However, avoiding collapse alone does not ensure that a representation preserves information needed for control. For instance, an encoder may distinguish robot configurations while ignoring the objects the robot must manipulate. We seek a direct method to specify the relationships we want to preserve and build them into a world model.

We approach this problem through the lens of spectral representation learning, which historically focuses on extracting representations from pairwise relationships between samples. Several contrastive and non-contrastive objectives admit spectral interpretations. Building on this perspective, we make the pairwise notion of similarity between two observations the center of a new training objective for latent dynamics modeling.

We introduce a **spectral alignment** framework for training world models to preserve a chosen similarity structure. We specify the pairwise relationships we want to preserve through a target similarity kernel, built from distances between observations. We then train an encoder to learn embeddings whose pairwise similarities match the target and an action-conditioned predictor to output future latents. We name the resulting world model SpecWM.

When some information about the underlying system is known, encoders can be trained based on physical distances, but the natural ordering of states within a trajectory is also sufficient to provide a training signal. Empirically, the choice of kernel strongly controls which physical quantities are recoverable from the representation. Temporal spectral alignment improves planning across OGBench Cube, OGBench Scene, and CALVIN.

## Spectral alignment {#method}

:::figure pipeline
**Spectral alignment on a single trajectory.** Top: sampled observations from OGBench Scene. Bottom: the temporal target kernel and encoder Gram matrix (before centering), the spectral embedding of $K$ (top three eigenvectors), and the encoder rows $h_i$ (top three principal components), colored by frame index. Matching pairwise similarities encourages the encoder to recover the target’s geometry.
:::

### Building a target

We start from a distance $d$ between pairs of observations, derived from ground-truth measurements or simply by counting the observations that separate them in the data. For $n$ observations, we adopt a Laplacian kernel to convert distances into similarities:

$$
K_{ij}=\exp\!\left(-\frac{d(x_i,x_j)}{\sigma}\right).
$$

Observations that are close according to $d$ remain distinguishable, while pairs more than a few $\sigma$ apart have similarity near zero. The bandwidth $\sigma$ therefore sets the range of distances the target resolves; we set it to the median target distance over the pairs the kernel is defined on.

Given a target kernel specifying the desired inner product between every pair of inputs, we can construct a coordinate vector for each input that realizes these pairwise relationships. Such a construction is called a *spectral embedding*. For a symmetric, positive semidefinite kernel $K=U\Lambda U^\top$, a spectral embedding is

$$
H_{\mathrm{spec}}=U\Lambda^{1/2},\qquad H_{\mathrm{spec}}H_{\mathrm{spec}}^\top=K.
$$

Each row provides the coordinates of one sample. Each eigenvalue determines the relative contribution of its corresponding eigenvector to the kernel, making eigenvalue rescaling a natural reweighting operation.

Without centering, the kernel would be dominated by a positive baseline, and regressing this target would favor matching that shared baseline rather than the variation around it. Still, if a few eigenvalues dominate, the encoder can achieve a small squared error by matching those directions while largely ignoring the others. We therefore *temper* the kernel by reshaping its spectrum before it is used as a target.

:::steps
### 1. Center

Remove row and column means, then restore the grand mean, to form the centered kernel $\widetilde K$.

### 2. Temper

Raise the leading positive eigenvalues to $\alpha=1/2$ and truncate the spectrum at $m=128$. Normalize the target to have trace $n$.

### 3. Align

Rescale each embedding to the length the target prescribes, then regress the centered matrix of embedding inner products onto the target.
:::

With $\widetilde K=U\Lambda U^\top$, the tempered target is $K^\alpha=nU\Lambda^\alpha U^\top/\operatorname{tr}(\Lambda^\alpha)$. The encoder $f_\theta$ maps each observation $x_i$ to an embedding $h_i\in\mathbb R^d$. We rescale these outputs and compute their Gram matrix:

$$
\bar h_i=\sqrt{K^\alpha_{ii}}\frac{h_i}{\|h_i\|},\qquad S=\bar H\bar H^\top.
$$

We double center $S$ and regress the target through a spectral loss:

$$
\mathcal L_{\mathrm{spec}}=\|\widetilde S-K^\alpha\|_F^2.
$$

In the fully specified setting, an embedding table that minimizes this loss recovers the row-normalized spectral embeddings of $K^\alpha$, up to an orthogonal transformation. [Theorem 1](#spectral-recovery) gives the conditions. We can thus evaluate the probing qualities of spectral embeddings derived from arbitrary kernels without ever having to train a model.

### Prediction and planning

While the spectral loss is sufficient for training an encoder, planning in latent space requires learning a predictor. We train it by a simple regression objective in latent space, which is also backpropagated through the encoder:

$$
\mathcal L=\mathcal L_{\mathrm{spec}}-\lambda\sum_i\cos(g_\phi(f_\theta(x_i),a_i),f_\theta(x_i^{\prime})).
$$

The predictor $g_\phi$ takes the current embedding and an action, and predicts the embedding of the next observation. For stability, we apply a parameter-free RMS normalization to the encoder output, so that every embedding has norm $\sqrt d$. This fixes the scale of the embeddings seen by the predictor and the planner.

We use the Cross-Entropy Method (CEM) to optimize action sequences. Candidate sequences are sampled from a Gaussian distribution, and the world model predicts the representation of observations $T$ steps ahead for each. Candidates are then scored according to similarity to the embedding of a goal observation. The action distribution is refit on the best candidates. We then execute a prefix of the selected sequence before replanning from the new observation.

## Learning from temporal distance {#temporal}

When metadata is not available, the ordering of observations in trajectories itself can form an *unsupervised* kernel. We use a temporal kernel, which relies on the absolute difference between indices for observations ordered in a trajectory: $d(x_i,x_j)=|i-j|$. Its only source of supervision is the order of observations in a trajectory.

:::explorer

:::

While supervised kernels can describe relationships between all pairs of inputs, the unsupervised kernels we use only express relationships for pairs of inputs in the same trajectory. In this *underspecified* setting, cross-trajectory similarities are excluded from the training objective. We omit tempering and target-diagonal rescaling; each clip’s squared error is normalized by the mean squared magnitude of its centered target before averaging across clips.

### Long-range pairs on CALVIN

In CALVIN, blocks move only when manipulated, so their positions often remain constant within a short clip. Within-clip temporal supervision therefore provides little signal to distinguish block positions. We augment each clip with eight observations from the same episode to capture changes over longer periods. These observations contribute only to the spectral loss, using their original time indices, and require no associated actions.

:::note
The extra observations are sampled 300–3,000 raw frames away. We average two centered, trace-normalized Laplacian kernels with bandwidths of 7 and 45 sampled observations. OGBench Scene and Cube retain a single-scale kernel.
:::

### A learned distance

We also evaluate a quasimetric kernel, which estimates temporal distances between observations according to the optimal goal-reaching policy. While this potentially introduces estimation errors, it labels state pairs by the minimum number of steps between states, instead of expressing the temporal separations observed in the data, and can thus compensate for poor data quality. We symmetrize this distance to match the symmetric Gram matrix of the embeddings.

## Planning with SpecWM {#results}

Our empirical evaluation revolves around three visual manipulation environments: OGBench Cube and OGBench Scene, and CALVIN. OGBench Scene and CALVIN introduce multiple objects and articulated fixtures whose states must be represented for control. These environments directly test whether the learned representation preserves information about the surrounding scene as well as the robot itself.

With temporal and quasimetric kernels, **SpecWM improves upon LeWM by an average of 21 percentage points in planning success rate**. The planner ranks predicted outcomes by their embedding similarity to the goal, which spectral alignment shapes to reflect temporal or quasimetric proximity.

:::figure fair_cem
**Figure 1. Planning success.** Average CEM planning success rate on 100 fixed tasks per environment. Bars report the mean over the 20k, 24k, and 28k checkpoints and three seeds, with whiskers showing one cross-seed standard deviation. SpecWM consistently outperforms LeWM.
:::

:::note
We generate failure data for each environment and append it to the canonical datasets for both models. We ablate this decision below.
:::

:::table planning
| Environment | LeWM | SpecWM<br>Temporal | SpecWM<br>Quasimetric |
| :--- | ---: | ---: | ---: |
| OGBench Cube | 52 | 68 | 71 |
| OGBench Scene | 49 | 77 | 74 |
| CALVIN | 29 | 51 | 47 |
:::

Overall, a learned quasimetric kernel is generally on par with a readily available temporal kernel, but either may be preferable depending on the environment.

## What do the representations preserve? {#representations}

To isolate representation quality from prediction accuracy, we evaluate linear probing performance for the position of objects across environments. We consider held-out observations that the encoder was never trained on. For each of five train-evaluation splits, we fit a ridge regressor for each state variable, choose regularization by cross-validation, and report $R^2$ on the evaluation set, averaged over variables and splits.

:::figure final_probes
**Figure 2. Object-position probes.** Linear probe $R^2$ of the manipulated object’s position from each model’s final-checkpoint embedding. Bars report the mean over three seeds, with whiskers showing one cross-seed standard deviation. Random is an untrained encoder of the same architecture.
:::

**SpecWM does not always beat LeWM on probing, and probe quality does not directly correlate with planning performance.** On Cube, LeWM recovers object position more accurately but plans less successfully. On OGBench Scene, SpecWM does better at both.

### Kernel choice

We extend the investigation to supervised kernels: state, depth, and proprioception. For each, we use the Euclidean distance between the corresponding feature vectors as the target distance. The state kernel uses the simulator state underlying each observation. Although this information is generally unavailable in real-world settings, it lets us evaluate a target with access to the full physical state.

The fully specified state kernel achieves the highest average $R^2$ (0.93). Under underspecified supervision, the temporal kernel nearly matches the state kernel (0.84 versus 0.85). **Proprioceptive kernels preserve the robot’s configuration but largely omit object states.**

:::table probes
| OGBench Scene probe R² | Temporal<sup>1</sup> | State<sup>2</sup> | Proprio<sup>2</sup> | Depth<sup>2</sup> |
| :--- | ---: | ---: | ---: | ---: |
| OGBench Scene average | 0.84 | **0.93** | 0.16 | 0.50 |
| Cube | 0.79 | 0.96 | 0.08 | 0.09 |
| Arm | 0.67 | 0.73 | 0.67 | 0.59 |
| Drawer | 0.91 | 0.99 | 0.01 | 0.87 |
| Window | 0.87 | 0.99 | 0.00 | 0.91 |
| Buttons | 0.96 | 0.99 | 0.02 | 0.04 |
:::

:::table-caption
Selected columns from the paper’s Table 1: linear probe $R^2$ on held-out OGBench Scene episodes. <sup>1</sup>Relationships within trajectories only. <sup>2</sup>Relationships specified across states.
:::

:::figure spectral_conversion
**Figure 3. Spectral recovery.** Linear probe $R^2$ between kernel eigenvectors and embeddings from encoders trained on fully specified state, proprioception, and depth. Underspecified variants and an untrained encoder are included for comparison.
:::

We evaluate the method's ability to recover spectral embeddings by by fitting linear probes to each eigenvector from the model embeddings. Recovery is strongest for eigenvectors associated with large eigenvalues and decreases as relative contribution decreases.

The state kernel's lower recovery scores at later indices is largely a function of its less even distribution of magnitude across eigenvalues. Weighting each eigenvector’s probe $R^2$ by its normalized eigenvalue gives mean scores of 0.965 for state, 0.987 for proprioception, and 0.992 for depth.

## Additional ablations {#ablations}

:::details open | Failure data
Predictors tend to generalize poorly to random actions when trained on expert-only data. We train LeWM and temporal SpecWM on the play data alone, at matched updates, frames per update, and schedule. Failure data raises planning success for both models in every environment, but does not explain the difference between them.

:::figure data_ablation
**Figure 4. Effect of the failure data.** CEM success (top) and object-position probe $R^2$ (bottom) for LeWM and temporal SpecWM, trained with failure rollouts (solid, three seeds) or on play data alone (hatched, one seed), at matched updates and frames per update. SpecWM outperforms LeWM in both cases.
:::
:::

:::details | Prediction gradients
We evaluate a variant of SpecWM which does not backpropagate the predictor regression objective through the target. The prediction loss still updates the encoder through the current observation, but no longer through the next observation used as its target. Planning success generally decreases, while probing results do not follow an obvious trend.

:::figure stopgrad_ablation
**Figure 5. Effect of a stop-gradient on the prediction target.** Bars report the mean over three seeds, with whiskers showing one cross-seed standard deviation. The stop-gradient generally lowers planning success and raises object recoverability in some cases while diminishing recoverability in others.
:::
:::

:::details | Planning cost and normalization
The two world models have different inherent distance metrics in their latent distributions. We use the one that fits each latent most naturally: L2 for LeWM and cosine similarity for SpecWM. The choice of measure is not the cause of the planning gains. The choice of normalization layer also does not have a substantial impact on planning performance.

:::paired
:::figure scene_cost_ablation_rounded
**Figure 6. Planning cost.** Cosine similarity and L2 distance are evaluated on both LeWM and SpecWM. Three training seeds are evaluated at their respective final three checkpoints for each setting.
:::

:::figure scene_normalization_ablation_rounded
**Figure 7. Normalization layer.** BatchNorm versus LayerNorm in the MLP producing the encoder embedding. One seed is used per run; CEM success is averaged over the final three checkpoints.
:::
:::
:::

## Conclusion {#discussion}

The core idea is to directly specify the pairwise relationships that representations should preserve through a target kernel. We find that readily available kernels result in strong planning performance, which is not entirely correlated with probing accuracy.

Pursuing a better understanding of the mechanisms enabling effective planning would be valuable. We view the study of which kernels are most conducive to large-scale self-supervised training as the next primary direction of work. Kernels involving language for semantic distances are another future direction.

:::actions code

:::

## Theoretical analysis {#theory}

The teacher kernel specifies which relationships the encoder should preserve. We now ask what matching those relationships implies: which representations minimize the loss, which quantities a linear probe can recover, when irrelevant information disappears, and why temporal similarity can help planning. The results below describe idealized optima under explicit assumptions; full proofs appear in the paper’s proofs appendix.

### The spectral loss has a known optimum

In the fully specified setting, the teacher defines relationships between every pair of inputs. Its centered, tempered target $K^\alpha$ can be decomposed into eigenvectors and eigenvalues. A spectral embedding uses the retained eigenvectors as coordinates, scaled by the square roots of the target’s eigenvalues. When the embedding dimension is large enough, these coordinates reproduce the target’s pairwise inner products exactly.

:::theorem spectral-recovery | Theorem 1
### Spectral recovery

Suppose $m\le d$ and $K^\alpha_{ii}>0$ for every input $i$. Then the minimum spectral loss is zero, attained exactly at

$$
H^\star=\operatorname{diag}(c)\,H_{\mathrm{spec}}\,Q,\qquad c_i>0,\quad Q^\top Q=I_d.
$$

Here $m$ is the number of retained positive spectral directions, $d$ is the encoder dimension, $H_{\mathrm{spec}}$ is the spectral embedding of $K^\alpha$ with square-root eigenvalue scaling, padded to $d$ dimensions, and $Q\in\mathbb R^{d\times d}$ is orthogonal.
:::

The optimum recovers the target’s geometry up to a rotation or reflection and positive scaling of each row. Row scaling remains free because the loss rescales each embedding to the length prescribed by the target diagonal. With fixed-norm encoder outputs, this becomes a row-normalized spectral embedding, up to an orthogonal transformation.

This gives a way to inspect a kernel before training a neural encoder: compute its spectral embedding and evaluate what its coordinates make accessible. The theorem characterizes the optimum of an embedding table; it does not guarantee that neural-network training reaches that optimum.

### Downstream probing guarantees

A linear probe can recover a quantity exactly when its values lie in the representation’s column space. The spectral characterization therefore connects kernel choice to the information accessible downstream. In particular, a kernel built from label relationships can make the labels themselves linearly recoverable, even though the encoder never directly regresses onto those labels.

:::theorem linear-recovery | Theorem 2
### Linear recoverability

Let $Y\in\mathbb R^{n\times p}$ be centered, with $\mathbf1^\top Y=0$, unit row norms $\|y_i\|=1$, and $\operatorname{rank}(Y)\le d$. Set $K=YY^\top$, use $\alpha=1$, and retain all positive spectral directions. Every global minimizer $H^\star$ of the spectral loss subject to $\|h_i\|=\sqrt d$ satisfies

$$
\min_{W\in\mathbb R^{d\times p}}\|Y-H^\star W\|_F^2=0.
$$
:::

Under these conditions, matching the labels’ pairwise inner products preserves enough information to reconstruct them with a linear map. This motivates teachers built from physical quantities. The exact guarantee applies to the stated label kernel and normalization; it does not imply perfect recovery for every distance-based kernel used in the experiments.

### Task-irrelevant information

Selective invariance means retaining relevant distinctions while dropping details the teacher ignores. Write each observation as $x_i=(s_i,n_i)$, where $s_i$ is task-relevant state and $n_i$ is nuisance information. For example, a manipulation teacher may depend on object positions while ignoring moving foliage in the background. We ask whether matching that teacher also makes the encoder ignore the foliage.

Let $\nu(\cdot\mid s_i)$ be the distribution of nuisance values at state $s_i$, and let $Z$ collect the task-relevant trajectory and teacher metadata. We need a coverage assumption: nuisance values that are individually possible at two states must also be possible together in a trajectory visiting those states.

:::note
**Coverage (A1).** For almost every $Z$, every pair of distinct indices $i,j$, and every measurable set $E$ of nuisance pairs, independent draws $n\sim\nu(\cdot\mid s_i)$ and $n'\sim\nu(\cdot\mid s_j)$ satisfy

$$
\Pr\big((n,n')\in E\mid s_i,s_j\big)>0
\quad\Longrightarrow\quad
\Pr\big((n_i,n_j)\in E\mid Z\big)>0.
$$

Conditioning on a trajectory may change the likelihood of nuisance pairs, but cannot rule out an otherwise possible set of pairs.
:::

Coverage includes independent sensor noise and correlated disturbances when all otherwise possible combinations remain possible. It excludes a background identity or lighting condition that varies across trajectories but stays fixed within each one. Such a shared attribute could select a rotation for every embedding in a clip without changing their pairwise similarities.

:::theorem nuisance-invariance | Theorem 3
### Abstraction of task-irrelevant information

Assume coverage, fixed-norm encoder outputs, and target-diagonal rescaling. If each trajectory’s centered, tempered target $K^\alpha$ has strictly positive diagonal entries almost surely and $\mathbb E[\mathcal L_{\mathrm{spec}}]=0$, then

$$
f_\theta((s_i,n))=f_\theta((s_i,n'))
$$

for almost every clip, every frame $i$, and almost every pair $(n,n')$ drawn independently from $\nu(\cdot\mid s_i)$.
:::

At zero expected loss, changing the nuisance component while holding the relevant state fixed leaves the representation unchanged. Coverage lets us vary nuisance draws while preserving the teacher’s inner products; centering forces the rescaled embeddings to sum to zero, preventing one such draw from changing its embedding independently. This result assumes target-diagonal rescaling, which is omitted in our practical underspecified training variant.

### Temporal kernels and the successor measure

Temporal supervision uses only how far apart observations occur in a trajectory. To understand its connection to planning, we move from a free embedding table to a state-conditioned encoder $h:\mathcal S\to\{z\in\mathbb R^d:\|z\|=1\}$. The behavioral successor measure counts discounted future visits under the data-collection policy:

$$
M^\beta(x,x')=\sum_{t=0}^{\infty}\gamma^t\Pr(x_t=x'\mid x_0=x,\pi_\beta),\qquad \gamma=e^{-1/\sigma}\in(0,1).
$$

Assume a finite state space and a stationary Markov policy $\pi_\beta$ whose induced chain $P$ is irreducible and aperiodic. Its stationary distribution is $\mu$, and trajectories start with $x_0\sim\mu$. Sample both indices uniformly from a length-$T$ trajectory. For this analysis, omit student and teacher centering, teacher tempering, and spectral truncation.

Writing $s(x,x')=h(x)^\top h(x')$, the population loss is

$$
\mathcal L_{\mathrm{spec}}^{\mathrm{pop}}(h)=\mathbb E_{\tau,i,j}\left[\big(s(x_i,x_j)-\gamma^{|i-j|}\big)^2\right].
$$

The same state pair can occur at different temporal separations. Define its expected teacher similarity as

$$
R_T(x,x')=\mathbb E\left[\gamma^{|i-j|}\mid x_i=x,\ x_j=x'\right].
$$

A conditional bias–variance decomposition separates the loss into regression onto $R_T$ and a term independent of the encoder. Minimizing the population loss is therefore equivalent to minimizing the expected squared error between embedding similarity and $R_T$. The next result identifies this target for long trajectories.

:::theorem successor-measure | Theorem 4
### Population target

Under the assumptions above, for every pair $x,x'\in\mathcal S$,

$$
\begin{aligned}
T R_T(x,x')\xrightarrow[T\to\infty]{}&\frac{M^\beta(x,x')}{\mu(x')}+\frac{M^\beta(x',x)}{\mu(x)}\\
&-\frac{\mathbf1[x=x']}{\mu(x)}.
\end{aligned}
$$

If the chain is reversible, with $\mu(x)P(x'\mid x)=\mu(x')P(x\mid x')$, this simplifies to

$$
T R_T(x,x')\xrightarrow[T\to\infty]{}\frac{2M^\beta(x,x')}{\mu(x')}-\frac{\mathbf1[x=x']}{\mu(x')}.
$$
:::

The temporal target thus contains a symmetrized successor measure, normalized by stationary state frequencies. It reflects discounted visitation in both temporal directions, relative to how common each state is in the data. This connects the similarity score used in planning to how readily states lead to one another under the behavior policy, within the idealized setting above.

### Comparing kernels for linear probing

The paper’s additional kernel-dominance result asks when one kernel is at least as useful as another for every linear probe target. At a zero-loss optimum with fixed row norms, the encoder’s column space is determined by the target’s cosine Gram matrix. Dominance therefore amounts to inclusion of the spaces of linearly recoverable targets.

:::theorem kernel-dominance | Theorem 5 · Appendix
### Kernel dominance

Take two centered, tempered targets of rank at most $d$ with positive diagonals, and global minimizers with row norm $\sqrt d$. Define their cosine Gram matrices by $K^{\mathrm{cos}}_{ik}=K^\alpha_{ik}/\sqrt{K^\alpha_{ii}K^\alpha_{kk}}$. The first kernel gives no greater optimal linear-probe error for every target $Y$ if and only if

$$
\operatorname{col}(K_2^{\mathrm{cos}})\subseteq\operatorname{col}(K_1^{\mathrm{cos}}).
$$

Dominance is strict if and only if this inclusion is strict.
:::
