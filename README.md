# Path Protocol Models

This repository contains a collection of models to consider multiparty message-forwarding protocols as part of a submission to a conference. These models are built inside the Tamarin prover tool using the framework established in our paper.

In most cases, analysis was performed on a 28-core Xeon server with a 2.6Ghz CPU and 64gb of RAM. Note that the models are still a work-in-progress: we are working on improving the level of detail, refining corruption to be more generic (as in the paper), and improving termination.

## Layout

The root folder contains ./pi-oracle.py, the Oracle file used to improve Tamarin's heuristic search. Other than this, the models are each split into separate folders. Each folder contains the following files:

- A `.spthy` file which contains the protocol's implementation into Tamarin
- `.pdf` and `.jpg` files containing a message sequence chart showing the protocol's intended execution
- A `README` file contains any additional notes about the protocol in question

The following protocols are modelled:

- `mctls/` models the record phase of the mcTLS protocol (citation [6] in our paper)
- `mbtls/` models the record phase of the mbTLS protocol (citation [23] in our paper)
- `matls/` models the record phase of the maTLS protocol (citation [25] in our paper)
- `Chaum/` models a primitive onion protocol using nested encryption, such as proposed by Chaum (citation [7] in our paper)
- `TOR-Establishment/` models the circuit establishment protocol of the TOR scheme (citation [8] in our paper)
- `TOR-Record/` models the data exchange protocol of the TOR scheme (citation [8] in our paper)
- `HORNET-Record/` models the record phase of the HORNET mixnet protocol (citation [40] in our paper)
- `Lightning/` models the Lightning payment protocol (citation [10] in our paper)
- `LightningSig/` models a extension of the Lightning payment protocol using a chained signature to ensure path symmetry (proposed in our paper)