# compsyling-tools

This repository contains tools for generating experimental materials and packaging complete tasks for psycholinguistic experiments.

It includes:
- pcibex template for categorical perception, self-paced reading, priming, web-based visual world paradigm;
- python code for converting text to audio material, generating images for the visual word paradigm

---

## What's Included

### Stimulus Generation (under `generation/`)
- **Audio**: Generate, segment, align, and clean auditory stimuli using gTTS, Praat, and MFA-compatible tools
- **Images**: Generate visual stimuli via DALL·E API
- **Text**: Create variations of sentence stimuli or structured prompt templates

---

### Ready-to-Use Task Bundles (under `tasks/`)

Each task is packaged as a `.zip` file and can be downloaded, customized, and run as-is:

- `demo-pci-intro.zip` — introduction to basic PCIbex controllers (using Ibex Farm syntax) 
- `demo-categorical-perception.zip` — b/p categorical perception task  
- `demo-gardenpath-selfpacedreading.zip` — garden path effect using self-paced reading  
- `demo-lexical-priming.zip` — semantic/phonological priming effect using lexical decision   
- `demo-visualwordparadigm.zip` — web-based visual world paradigm using WebGazer.js on PCIbex

These include PCIbex-compatible or HTML setups with instructions and demo data.

---

## License

MIT License for code. For image/audio tools, please review the usage terms of external APIs (e.g., DALL·E, Google TTS, MFA).
