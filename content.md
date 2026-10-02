---
# Page settings. The article starts after the closing --- below.
title: |
  World Modeling through
  Spectral Alignment
description: We train world models to preserve relationships between observations. Read about SpecWM, its spectral alignment objective, and results on three visual manipulation environments.
subtitle: What information should a latent world model preserve?
authors:
- name: Holger Molin
  affiliation: 1,*
  equal: true
- name: William Peng
  affiliation: 1,*
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
author_note: '* Equal contribution. Order within braces is randomized.'
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
metrics:
- before: 52%
  after: 68%
  label: OGBench Cube
  change: +16 percentage points
- before: 49%
  after: 77%
  label: OGBench Scene
  change: +28 percentage points
- before: 29%
  after: 51%
  label: CALVIN
  change: +22 percentage points
figures:
  environments:
    image: assets/environments.png
    zoom: assets/environments.png
    fallback: assets/environments.png
    title: The three evaluation environments
    alt: OGBench Cube, OGBench Scene, and CALVIN.
    width: 2500
    height: 919
    loading: lazy
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
    alt: 'CEM success: random 13, 21, 17%; LeWM 52, 49, 29%; temporal SpecWM 68, 77, 51%; quasimetric SpecWM 71, 74, 47% on Cube, Scene and CALVIN respectively.'
    width: 2200
    height: 687
    loading: lazy
  final_probes:
    image: assets/final_probes.png
    zoom: assets/final_probes.svg
    fallback: assets/final_probes.pdf
    title: Linear recoverability of manipulated object position
    alt: 'Object-position probe R squared: LeWM versus temporal SpecWM is 0.98 versus 0.81 on Cube, 0.09 versus 0.78 on Scene, and 0.41 versus 0.47 on CALVIN.'
    width: 2200
    height: 687
    loading: lazy
  spectral_conversion:
    image: assets/spectral_conversion.png
    zoom: assets/spectral_conversion.svg
    fallback: assets/spectral_conversion.pdf
    title: Recovering kernel eigenvectors from learned embeddings
    alt: Kernel eigenvector probe curves for state, proprioception and depth teachers; fully specified teachers generally recover eigenvectors better than underspecified teachers or an untrained encoder.
    width: 2200
    height: 757
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
    title: Planning-cost ablation on Scene
    alt: LeWM planning success 50% with L2 and 51% with cosine; temporal SpecWM 77% with either cost.
    width: 2200
    height: 2144
    loading: lazy
  scene_normalization_ablation_rounded:
    image: assets/scene_normalization_ablation_rounded.png
    zoom: assets/scene_normalization_ablation_rounded.svg
    fallback: assets/scene_normalization_ablation_rounded.pdf
    title: Normalization ablation on Scene
    alt: LeWM success 53% with BatchNorm and 51% with LayerNorm; temporal SpecWM 77% with either normalization.
    width: 2200
    height: 2144
    loading: lazy
  abstract_fig:
    image: assets/abstract_fig.png
    zoom: assets/abstract_fig.svg
    fallback: assets/abstract_fig.pdf
    title: 'Spectral alignment: from pairwise distances to embeddings'
    alt: Pairwise distances define a teacher similarity matrix. The encoder learns student embeddings whose pairwise similarities match the teacher.
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
  metrics_aria: 'CEM planning success: LeWorldModel compared with temporal SpecWM'
  expanded_figure: Enlarged figure
  figure_close_hint: Press Escape or click to close.
explorer:
  title: Temporal kernel bandwidth
  tag: Interactive
  low: 0 · dissimilar
  high: 1 · similar
  label: Kernel bandwidth, σ
  formula: K_{ij}=e^{-|i-j|/\sigma}
  hint: Try changing σ. The plot shows the raw kernel, before centering and tempering.
  description: At 7 frames apart, similarity is {similarity}. {band}
  narrow: A narrow band emphasizes nearby observations.
  medium: A wider band preserves similarity across longer separations.
  wide: A wide band keeps distant observations more similar.
  aria: Temporal similarity matrix for 23 observations with bandwidth {sigma}. Similarity at a separation of 7 frames is {similarity}.
---

:::figure abstract_fig
**World modeling through spectral alignment.** We turn pairwise distances into teacher similarities, then train the encoder’s embedding similarities to match them.
:::

## What should a world model preserve? {#overview}

:::lead
A world model needs enough information to predict what happens when an agent acts. It doesn’t need every detail in the image. So what should it keep?
:::

:::note
A JEPA predicts future embeddings rather than pixels. It can leave out details, but its training objective has to guide which ones.
:::

Recent work has made JEPA training more stable by regularizing the embedding distribution. But avoiding collapse alone doesn’t ensure that the model keeps the information needed for control. An encoder may distinguish robot configurations while ignoring the objects the robot must manipulate.

We want a direct way to specify what the encoder should preserve. In **SpecWM**, we define a teacher kernel that says how similar pairs of observations should be, then train the encoder’s embedding similarities to match it. We also train an action-conditioned predictor to output future latents.

The teacher can use physical state, depth, or proprioception. When those aren’t available, the order of observations in a trajectory is enough to provide a training signal. We test how these choices affect what the model represents and how well it plans.

## Spectral alignment {#method}

:::figure pipeline
**Spectral alignment on a single trajectory.** We train the encoder’s pairwise similarities to match the temporal target. Top: observations from OGBench Scene. Bottom: the target kernel, the encoder’s Gram matrix, the kernel’s spectral embedding, and the encoder outputs. Matching pairwise similarities encourages the encoder to recover the target’s geometry.
:::

We start with a distance between observations. This might be a physical distance, or just the number of frames between two observations in a trajectory. We turn that distance into a similarity with a Laplacian kernel:

$$
K_{ij}=\exp\!\left(-\frac{d(x_i,x_j)}{\sigma}\right).
$$

:::note
For a single-scale kernel, we set **σ** to the median distance among the pairs used to build the teacher.
:::

Observations that are close according to this distance get similar embeddings; pairs more than a few σ apart get a target similarity near zero. We then center the kernel so the encoder learns the variation between pairs, rather than their shared positive baseline.

These pairwise similarities also define a set of coordinates for the observations: a *spectral embedding*. For a positive semidefinite kernel $K=U\Lambda U^\top$, we scale each eigenvector by the square root of its eigenvalue:

$$
H_{\mathrm{spec}}=U\Lambda^{1/2},\qquad H_{\mathrm{spec}}H_{\mathrm{spec}}^\top=K.
$$

Each row gives one observation’s coordinates. Their inner products reproduce the teacher similarities.

A few large eigenvalues could still dominate the loss, letting the encoder ignore the other directions. To reduce this imbalance, we take the square root of the retained eigenvalues (α = ½). We keep up to 128 positive directions.

:::steps
### 1. Center

Remove row and column means, then restore the grand mean. This removes the shared positive baseline.

### 2. Temper

Raise retained positive eigenvalues to α = ½, keeping up to 128 directions.

### 3. Align

Rescale embedding norms to match the target diagonal, then match the centered matrix of inner products to the target.
:::

$$
\mathcal L_{\mathrm{spec}}=\|\widetilde S-K^\alpha\|_F^2.
$$

Here $\widetilde S$ is the centered Gram matrix of the rescaled embeddings:

$$
\bar h_i=\sqrt{K^\alpha_{ii}}\frac{h_i}{\|h_i\|},\qquad S=\bar H\bar H^\top.
$$

This is the connection to spectral embeddings: in the fully specified setting, zero spectral loss makes the rescaled encoder outputs recover the spectral embedding of $K^\alpha$, up to a rotation or reflection. This assumes enough embedding dimensions and a positive target diagonal; [Theorem 1](#spectral-recovery) gives the precise statement. We can therefore inspect a teacher’s ideal representation through eigendecomposition, without training a model.

The encoder alone isn’t enough for planning. We also train a predictor to output the embedding of the next observation given the current one and an action. We maximize its cosine similarity with the target, letting gradients flow through both. RMS normalization fixes the scale of the embeddings used by the predictor and planner.

$$
\mathcal L=\mathcal L_{\mathrm{spec}}-\lambda\sum_i\cos(g_\phi(f_\theta(x_i),a_i),f_\theta(x_i^{\prime})).
$$

For planning, we use the Cross-Entropy Method (CEM). We sample action sequences, predict where they lead, and score those outcomes by their similarity to the goal embedding. We refit the sampling distribution on the best candidates, execute part of the selected sequence, then replan.

## Learning from temporal distance {#temporal}

Without state labels or other metadata, we can use time. For two observations in the same trajectory, we set the teacher distance to the number of indices between them: $d(x_i,x_j)=|i-j|$.

This requires only the order of observations. Nearby frames get higher target similarity, and frames farther apart get lower similarity.

:::explorer

:::

### Long-range pairs on CALVIN

In CALVIN, blocks move only when manipulated. They often stay still throughout a short clip, so the temporal kernel gets little signal about their positions. We add eight observations from farther away in the same episode and average two kernels with different bandwidths. These extra observations contribute only to the spectral loss and need no associated actions.

:::note
CALVIN uses bandwidths of 7 and 45 sampled observations. The extra frames come from 300–3,000 raw frames away. See Appendix C.2.
:::

We also try a quasimetric kernel. Its learned distance estimates the minimum number of steps needed to get between states, rather than the separation we happened to observe in a trajectory. This gives us another teacher to compare, though learning the distance can introduce errors.

## Planning with SpecWM {#results}

:::figure environments
**Evaluation environments.** OGBench Cube, OGBench Scene, and CALVIN.
:::

SpecWM improves planning success over LeWorldModel with both temporal and quasimetric kernels, by an average of 21 percentage points. The planner scores predicted outcomes by their similarity to the goal. Our objective trains that similarity to reflect temporal or quasimetric proximity.

:::figure fair_cem
**Figure 1. Planning success.** We evaluate 100 fixed tasks per environment and average the 20k, 24k, and 28k checkpoints over three seeds. Error bars show one standard deviation across seeds.
:::

:::note
We add failure trajectories to the training data for both models. Below, we check how much these extra trajectories help.
:::

:::table planning
| Environment | LeWM | SpecWM<br>Temporal | SpecWM<br>Quasimetric |
| :--- | ---: | ---: | ---: |
| OGBench Cube | 52 | 68 | 71 |
| OGBench Scene | 49 | 77 | 74 |
| CALVIN | 29 | 51 | 47 |
:::

The learned quasimetric kernel performs about as well as the temporal kernel overall. Which one works better depends on the environment.

## What do the representations preserve? {#representations}

To check what the embeddings contain, we fit linear probes to predict object positions. We use observations the encoder never saw during training, fitting ridge regressors and selecting their regularization by cross-validation.

:::figure final_probes
**Figure 2. Object-position probes.** We fit ridge regressors to recover the manipulated object’s position from final-checkpoint embeddings, splitting held-out episodes into probe training and test sets. Bars average three seeds; error bars show one standard deviation across seeds.
:::

**Better probing doesn’t always mean better planning.** On Cube, LeWM recovers object position more accurately than temporal SpecWM, but plans less successfully. On Scene, SpecWM does better at both.

### Kernel choice

We also compare state, depth, and proprioceptive teachers. With relationships specified across states, the state kernel gives the highest average R² on Scene (0.93). The temporal kernel, which only provides relationships within trajectories, reaches 0.84. Proprioceptive kernels preserve the robot’s configuration but largely omit object states.

:::table probes
| Scene probe R² | Temporal<sup>1</sup> | State<sup>2</sup> | Proprio<sup>2</sup> | Depth<sup>2</sup> |
| :--- | ---: | ---: | ---: | ---: |
| Scene average | 0.84 | **0.93** | 0.16 | 0.50 |
| Cube | 0.79 | 0.96 | 0.08 | 0.09 |
| Arm | 0.67 | 0.73 | 0.67 | 0.59 |
| Drawer | 0.91 | 0.99 | 0.01 | 0.87 |
| Window | 0.87 | 0.99 | 0.00 | 0.91 |
| Buttons | 0.96 | 0.99 | 0.02 | 0.04 |
:::

:::table-caption
Selected columns from the paper’s Table 1, a separate kernel ablation from the probe comparison above. <sup>1</sup>Relationships within trajectories only. <sup>2</sup>Relationships specified across states.
:::

:::figure spectral_conversion
**Figure 3. Recovering the teacher’s spectral directions.** Eigenvector probes compare fully specified and underspecified supervision against an untrained encoder.
:::

## Additional ablations {#ablations}

We check the effects of failure data, prediction gradients, planning cost, and normalization.

:::details open | Failure data helps both methods.
When trained only on expert data, predictors tend to generalize poorly to random actions. Adding failure trajectories improves planning for both models in every environment. SpecWM still outperforms LeWM without them, so the extra data doesn’t explain the gap.

:::figure data_ablation
**Figure 4. Data coverage.** Solid bars include failure rollouts and average three seeds; hatched bars use play data only and one seed, with matched updates and frames per update.
:::
:::

:::details | Gradients through the prediction target matter.
What happens if we stop gradients through the next-state target? The prediction loss still updates the encoder through the current observation, but planning success generally falls. The probe results change in both directions.

:::figure stopgrad_ablation
**Figure 5. Prediction target gradients.** Means over three seeds; whiskers show one cross-seed standard deviation.
:::
:::

:::details | The cost function and normalization do not explain the gap.
Our main experiments use L2 distance for LeWM and cosine similarity for SpecWM. Swapping the planning cost doesn’t explain the gains. We also try both BatchNorm and LayerNorm in the projection head; this makes little difference in the reported ablation.

:::paired
:::figure scene_cost_ablation_rounded
**Figure 6. Planning cost.** Three seeds, averaged over their final three checkpoints.
:::

:::figure scene_normalization_ablation_rounded
**Figure 7. Normalization.** One seed per run, averaged over the final three checkpoints.
:::
:::
:::

## Conclusion {#discussion}

Spectral alignment lets us specify which pairwise relationships a world model should preserve. The teacher changes what the representation keeps. Even a teacher that uses only trajectory ordering improves planning across all three environments.

We still don’t fully understand why some kernels give better planning without better probe scores. We’d like to understand that connection and test which kernels work best at larger scales. Language-based semantic distances are another teacher we’d like to explore.

:::actions code

:::

## Theoretical results {#theory}

Here are the main results. We leave the proofs to Section 5 and Appendix D of the paper.

:::theorem spectral-recovery | Theorem 1
### The spectral loss has a known optimum

Let $H_{\mathrm{spec}}$ be the spectral embedding of the centered, tempered target $K^\alpha$, padded to $d$ dimensions. If its rank is at most $d$ and its diagonal is strictly positive, the minimum spectral loss is zero, attained exactly at

$$
H^\star=\operatorname{diag}(c)\,H_{\mathrm{spec}}\,Q,\qquad c_i>0,\quad Q^\top Q=I.
$$

The objective recovers the teacher’s spectral embedding up to positive row scales and an orthogonal transform.
:::

:::theorem linear-recovery | Theorem 2
### Labels can be recovered from their relationships

Let $Y\in\mathbb R^{n\times p}$ have centered, unit-norm rows and rank at most $d$. With $K=YY^\top$, $\alpha=1$, and all positive directions retained, every global minimizer with row norm $\sqrt d$ allows exact linear recovery:

$$
\min_{W\in\mathbb R^{d\times p}}\|Y-H^\star W\|_F^2=0.
$$
:::

:::theorem nuisance-invariance | Theorem 3
### Matching the teacher can remove nuisance information

Write an observation as $x=(s,n)$, where the teacher depends on state $s$ but not nuisance $n$. Assume coverage: nuisance pairs possible under independent draws at two states are also possible together within a trajectory visiting those states. With fixed-norm outputs, target-diagonal rescaling, a strictly positive target diagonal, and zero expected spectral loss,

$$
f_\theta((s_i,n))=f_\theta((s_i,n'))
$$

for almost every clip, every frame $i$, and almost every pair of independent nuisance draws at $s_i$.
:::

:::theorem successor-measure | Theorem 4
### The temporal target contains the successor measure

Consider a finite, stationary, irreducible, aperiodic Markov chain under policy $\pi_\beta$, with stationary distribution $\mu$. For this result, omit centering, tempering, and truncation. Let $\gamma=e^{-1/\sigma}$ and $M^\beta(x,x')=\sum_{t\ge0}\gamma^t\Pr(x_t=x'\mid x_0=x,\pi_\beta)$ be the discounted successor measure. For uniformly sampled indices in a length-$T$ trajectory, define $R_T(x,x')=\mathbb E[\gamma^{|i-j|}\mid x_i=x,x_j=x']$. Then

$$
\begin{aligned}T R_T(x,x')\xrightarrow[T\to\infty]{}&\frac{M^\beta(x,x')}{\mu(x')}+\frac{M^\beta(x',x)}{\mu(x)}\\&-\frac{\mathbf1[x=x']}{\mu(x)}.\end{aligned}
$$

For a reversible chain, the two successor terms are equal.
:::

:::theorem kernel-dominance | Theorem 5 · Appendix
### When is one kernel better for every linear probe?

Take two centered, tempered targets of rank at most $d$ with positive diagonals, and global minimizers with row norm $\sqrt d$. Define their cosine Gram matrices by $K^{\mathrm{cos}}_{ik}=K^\alpha_{ik}/\sqrt{K^\alpha_{ii}K^\alpha_{kk}}$. The first kernel gives no greater optimal linear-probe error for every target $Y$ if and only if

$$
\operatorname{col}(K_2^{\mathrm{cos}})\subseteq\operatorname{col}(K_1^{\mathrm{cos}}).
$$

Dominance is strict if and only if the inclusion is strict.
:::
