# Route-Based Synthesizability Score

Scores how readily a compound can be made by running a retrosynthetic search against the ZINC catalogue of purchasable building blocks, so the result reflects commercial availability rather than structure alone. A directed message-passing network proposes disconnections, restricted to templates that split the target into smaller precursors, so protecting-group steps cannot be expressed. Returns a continuous score plus the step and precursor counts of the best route. The bundled checkpoint is the authors release retrained after the paper.

This model was incorporated on 2026-09-25.Last packaged on 2026-09-28.

## Information
### Identifiers
- **Ersilia Identifier:** `eos2srx`
- **Slug:** `synomega`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Synthetic accessibility`, `Chemical synthesis`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `10`
- **Output Consistency:** `Fixed`
- **Interpretation:** Higher scores indicate easier synthesis from purchasable building blocks; the remaining columns describe the best route found.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| synscore | float | high | SynOmega synthesizability score computed from the count of non-purchasable starting materials in the best route |
| bb_coverage | float | high | Fraction of the best route starting materials that are purchasable |
| solved | float | high | One if a route within the depth limit was found with every starting material purchasable and zero otherwise |
| u | float | high | Number of starting materials in the best route that are not purchasable |
| min_steps | float | high | Reactions in the shortest solved route and empty when no solved route was found |
| min_route_depth | float | high | Longest linear sequence of the shortest solved route and empty when no solved route was found |
| num_routes | float | high | Number of distinct solved routes found for the target |
| num_leaves | float | high | Starting materials in the best route found |
| num_purchasable_leaves | float | high | Starting materials in the best route that are purchasable |
| expansions | float | high | Node expansions the search used for this target |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos2srx](https://hub.docker.com/r/ersiliaos/eos2srx)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2srx.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2srx.zip)

### Resource Consumption
- **Model Size (Mb):** `224`
- **Environment Size (Mb):** `1478`
- **Image Size (Mb):** `1824.16`

**Computational Performance (seconds):**
- 10 inputs: `149.95`
- 100 inputs: `217.04`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/zbc0315/synomega](https://github.com/zbc0315/synomega)
- **Publication**: [https://doi.org/10.1021/acs.jcim.6c02529](https://doi.org/10.1021/acs.jcim.6c02529)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2026`
- **Ersilia Contributor:** [TiagoJanela](https://github.com/TiagoJanela)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos2srx
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos2srx
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
