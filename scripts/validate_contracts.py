import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(relative_path):
    with (ROOT / relative_path).open(encoding="utf-8") as handle:
        return json.load(handle)


def fail(message):
    raise SystemExit(f"CONTRACT_VALIDATION_FAILED: {message}")


manifest = load("manifests/capability-manifest.json")
if manifest["product_id"] != "x2x-personal":
    fail("manifest product_id is not x2x-personal")
constraints = manifest["authority_constraints"]
for key in (
    "independent_authority",
    "direct_consequence_adapter_invocation",
    "runtime_capability_expansion",
    "unknown_to_allow",
):
    if constraints.get(key) is not False:
        fail(f"authority constraint {key} must be false")

for required in ("DECISION", "EXECUTION_ATTEMPT", "VERIFICATION", "RECONCILIATION", "CLOSEOUT"):
    if required not in manifest["required_receipts"]:
        fail(f"missing required receipt {required}")

request_contract = load("contracts/core-request.schema.json")
decision_contract = load("contracts/core-decision-envelope.schema.json")
if request_contract["properties"]["schema_version"]["const"] != "x2x.personal.core-request.v1":
    fail("request contract version drift")
if decision_contract["properties"]["schema_version"]["const"] != "x2x.personal.core-decision.v1":
    fail("decision contract version drift")

vectors = load("tests/contract-vectors.json")["vectors"]
expected = {vector["id"]: vector["expected"] for vector in vectors}
if expected.get("product-side-authority") != "REJECT_COMPOSITION":
    fail("missing product-side authority negative vector")
if expected.get("unknown-authority") != "DEFER_OR_DENY":
    fail("missing unknown-authority fail-closed vector")
if expected.get("unqualified-kernel") != "REJECT_RELEASE":
    fail("missing unqualified-kernel release vector")

print("PERSONAL_CONTRACT_GATE_OK")
