# Automated Pre/Post-Cutover Network Verification Harness
Python network migration verifier with multi-vendor Netmiko collection boundary, normalized route/interface/MAC/BGP state comparison, diff generation and deterministic go/no-go logic. Includes Docker, CI and tests.

The diff behavior is verified locally. “Within seconds” is a benchmark claim and should only be used after timing collection + comparison against a defined device count and environment.
