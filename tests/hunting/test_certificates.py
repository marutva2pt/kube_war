# flake8: noqa: E402
from kube_hunter.conf import Config, set_config

set_config(Config())

from kube_hunter.core.events.types import Event
from kube_hunter.modules.hunting.certificates import CertificateDiscovery, CertificateEmail
from kube_hunter.core.events.event_handler import handler


def test_CertificateDiscovery():
    cert = """
    -----BEGIN CERTIFICATE-----
MIIDZDCCAkwCCQCAzfCLqrJvuTANBgkqhkiG9w0BAQsFADB0MQswCQYDVQQGEwJV
UzELMAkGA1UECAwCQ0ExEDAOBgNVBAoMB05vZGUuanMxETAPBgNVBAsMCG5vZGUt
Z3lwMRIwEAYDVQQDDAlsb2NhbGhvc3QxHzAdBgkqhkiG9w0BCQEWEGJ1aWxkQG5v
ZGVqcy5vcmcwHhcNMTkwNjIyMDYyMjMzWhcNMjIwNDExMDYyMjMzWjB0MQswCQYD
VQQGEwJVUzELMAkGA1UECAwCQ0ExEDAOBgNVBAoMB05vZGUuanMxETAPBgNVBAsM
CG5vZGUtZ3lwMRIwEAYDVQQDDAlsb2NhbGhvc3QxHzAdBgkqhkiG9w0BCQEWEGJ1
aWxkQG5vZGVqcy5vcmcwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDS
CHjvtVW4HdbbUwZ/ZV9s6U4x0KSoyNQrsCZjB8kRpFPe50DS5mfmu2SNBGYKRgzk
4QEEwFB9N2o8YTWsCefSRl6ti4ToPZqulU4hhRKYrEGtMJcRzi3IN7s200JaO3UH
01Su8ruO0NESb5zEU1Ykfh8Lub8TGEAINmgI61d/5d5Aq3kDjUHQJt1Ekw03Ylnu
juQyCGZxLxnngu0mIvwzyL/UeeUgsfQLzvppUk6In7tC1zzMjSPWo0c8qu6KvrW4
bKYnkZkzdQifzbpO5ERMEsh5HWq0uHa6+dgcVHFvlhdqF4Uat87ygNplVf0txsZB
MNVqbz1k6xkZYMnzDoydAgMBAAEwDQYJKoZIhvcNAQELBQADggEBADspZGtKpWxy
J1W3FA1aeQhMvequQTcMRz4avkm4K4HfTdV1iVD4CbvdezBphouBlyLVLDFJP7RZ
m7dBJVgBwnxufoFLne8cR2MGqDRoySbFT1AtDJdxabE6Fg+QGUpgOQfeBJ6ANlSB
+qJ+HG4QA+Ouh5hxz9mgYwkIsMUABHiwENdZ/kT8Edw4xKgd3uH0YP4iiePMD66c
rzW3uXH5J1jnKgBlpxtog4P6dHCcoq+PZJ17W5bdXNyqC1LPzQqniZ2BNcEZ4ix3
slAZAOWD1zLLGJhBPMV1fa0sHNBWc6oicr3YK/IDb0cp9kiLvnUu1pHy+LWQGqtC
rceJuGsnJEQ=
-----END CERTIFICATE-----
"""
    c = CertificateDiscovery(Event())
    c.examine_certificate(cert)


@handler.subscribe(CertificateEmail)
class test_CertificateEmail:
    def __init__(self, event):
        assert event.email == b"build@nodejs.org0"
