# OPENAST: Open Agent Sight Trust

**Visual research scaffold.** Part of [OpenModalityTrust](https://github.com/ketanbj/open-modality-trust).

This repository will explore signed visual codes, camera/display challenges, scene/claim binding and audio/visual handoffs.

There is no implemented security protocol or runnable adapter yet. The current
repository contains design boundaries and the intended source/test/example
structure. A valid marker or fresh response does not prove scene truth, display location, or proximity; live relay and relocated tags must remain explicit.

The common contracts live in the umbrella's `spec/` directory. They are drafts,
not wire-level interoperability guarantees. The umbrella pins this repository
as a submodule under `modalities/openast`. Contribute here independently, publish
child commits, then update the umbrella pointer.

- [Design](docs/design.md)
- [Source scope](src/openast/README.md)
- [Test plan](tests/README.md)
- [Example plan](examples/README.md)
