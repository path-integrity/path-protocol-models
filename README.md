# Path Protocol Models

This repository contains a collection of models to consider multiparty message-forwarding protocols as part of a submission to a conference. These models are built inside the Tamarin prover tool using the framework established in our paper.

In most cases, analysis was performed on a 28-core Xeon server with a 2.6Ghz CPU and 64gb of RAM.

## Layout

The root folder contains ./pi-oracle.py, the Oracle file used to improve Tamarin's heuristic search. Other than this, the models are each split into separate folders. Each folder contains the following files:

- A `.spthy` file which contains the protocol's implementation into Tamarin
- A `.pdf` file containing a message sequence chart showing the protocol's intended execution
- A `README` file contains any additional notes about the protocol in question

The following protocols are modelled:

- `simpleOnion/` models a primitive onion protocol using nested encryption, such as proposed by Chaum (citation [7] in our paper)
- `mbtls/` models the record phase of the mbTLS protocol (citation [23] in our paper)
