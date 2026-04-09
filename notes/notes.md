## Microbial Physiology Data

### Cell
- Synechocystis PCC6803
- target wavelengths were measure light scattering and not absortion: e.g 730nm
- We can also target regions were cells absorb light to get and idea of pigment composition: e.g. 634 and 685 nm

### Synechocystis ploidy
- Number of complete (sets of) chromosomes in a cell

- 2011: Copy numbers ranging from ~200 copies to ~50 genome copies depending on strain and growth phase are reported
- 2016: Same group reports copy number ranging from ~20 to ~5 genome copies depending on strain and growth phase


### The experiment
2 conditions
- Low [Phosphate] – 0.0115 mM
- “Normal” [Phosphate] – 0.23 mM


### Data analysis

- Pigment composition -> OD measurements
- Growth rates -> Turbidostat OD data
- Ploidy level -> CASY-counter, qPCR (next-week)

### Dataset Summary
- design: match culture ID (channel) to experimental conditions
- spectrophotometer: OD measurements at different wavelengths from the
spectrophotometer
- turbidostat: automated OD720 measurements from Multi-cultivator
- casy: cell count data from CASY-counter
- qPCR: Ct values from quantitative PCR

### Casy Counter
#### Protocol
1. Dilute sample of interest (measurement range)
2. Pipette 10 μL dilution into CASY-vial with 10 mL of CASY-ton buffer
3. Insert CASY-vial into CASY-counter
4. Measure:
    - CASY-counter will perform 3 measurements of each sample
    - Each measurement will take 200 μL from CASY-vial
    - The machine will report for each measurement:
        - Total number of counts
        - Peak diameter
        - Average diameter

So, this means that:
- vial contains
    - 10 μL of diluted sample
    - into 10000 μL of CASY-ton buffer
- measurement volume is 200 μL

example calculation:
- measurement_volume = 200μL
- counts = 2212
- sample_volume = 10 μL  e.
- casyton_volume = 10000 μL
- sample_dilution = 2    e.g. sample is diluted to 1:2 with casyton volumee

```
 cells / μL = (counts / measurement_volume) * ((sample_volume + casyton_volume) / sample_volume) * sample_dilution

cells / μL = (2212 / 200) * ((10 + 10000) / 10) * 2
cells / μL = 11.06 * 1001 * 2
cells / μL = 22142.12

cells / mL = cells / μL * 1000
cells / mL = 22142.12 * 1000
cells / mL = 22,142,120
```
