# X2X Personal

Status: composition scaffold only. No production authorization or release claim.

X2X Personal is an independently deployable product composition that must consume the signed, qualified X2X Core release. It is not a kernel fork and may not independently authorize a consequence.

## Required dependency

Personal must pin:

- exact X2X Core release tag;
- exact implementation commit;
- canonical specification commit;
- capability-manifest digest;
- signed binding record;
- verified evidence artifact.

Until those values exist in a signed release binding, this repository remains non-production scaffolding.

## Product responsibilities

Personal may provide:

- device and account UX;
- user policy selection;
- gateway connector integration;
- privacy and accessibility controls;
- product telemetry that does not expand authority;
- forensic receipt presentation and export.

Personal may not:

- mint or broaden authority;
- convert UNKNOWN into approval;
- bypass the Core composition boundary;
- invoke a consequential adapter without a Core decision and bounded grant;
- substitute an unqualified kernel version.

## Planned contract

The implementation will consume the shared composition-root contract from X2X Core and will carry a versioned capability manifest. The first production vertical slice is adult Personal; age and jurisdiction behavior will be policy packages, not a second kernel.
