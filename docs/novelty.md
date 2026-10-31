# Research position and prior art

Visual authentication is established: Seeing-Is-Believing used camera phones and
2D barcodes for device authentication in 2005. QR login deployment research exposes
workflow and authorization failures; pQRAuth explicitly adds a physical pose
factor. OpenAST supplies neither a new cryptographic primitive nor a replacement
for those physical-association mechanisms.

RATS separates evidence from appraisal and relying-party decisions. CaMeL and
Fides enforce policy around model control/data flows. OpenAST follows those
boundaries but does not implement their IFC mechanisms or reproduce their agent
benchmarks. Signed visual claims plus exact action grants are an engineering
reference; their combination alone is not established research novelty.

The prospective research problem is preserving scoped guarantees through visual,
voice and tactile handoffs while acquiring adequate evidence efficiently. The
current equally expressive typed-policy control can match the gateway in serial
cases. A future contribution must show a composition rule, a formal result or
measurable acquisition/autonomy improvement against strong controls.

Primary sources checked October 31, 2026:

- [Seeing-Is-Believing](https://scholars.duke.edu/publication/1493989)
- [QRLogin deployment study](https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-xin)
- [pQRAuth](https://www.usenix.org/conference/usenixsecurity24/presentation/wu-chuxiong)
- [RATS architecture](https://www.rfc-editor.org/rfc/rfc9334.html)
- [CaMeL](https://arxiv.org/abs/2503.18813)
- [Fides](https://arxiv.org/abs/2505.23643)
