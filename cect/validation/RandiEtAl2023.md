Functional connectivity data of _C. elegans_ from: Randi et al. 2023, Neural signal propagation atlas of _Caenorhabditis elegans_, [Nature 623, 406–414 (2023)](https://doi.org/10.1038/s41586-023-06683-4).

We used the [WormNeuroAtlas package](https://github.com/francescorandi/wormneuroatlas) as discussed in the paper to provide the signal propagation map values. 
The method _get_signal_propagation_map()_ specifying the wildtype data (strain="wt") was used to get the post-stimulus calcium response amplitude (⟨ΔF/F₀⟩ₜ) matrix, while 
_get_signal_propagation_q()_ was used to get the q-values (the false discovery rate, i.e. the probability that a neuron pair declared "functionally connected" is actually a false positive). We used a q_max = 0.05 and just added that to the adjacency matrix used in this example.

We obtained the validation values below by calling the above functions and printing the value in the signal propagation for specific connections, checking q < 0.05. 